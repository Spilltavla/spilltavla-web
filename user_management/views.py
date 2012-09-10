from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from social_auth.utils import setting, backend_setting
from user_management.forms import UserRegistrationForm


def login_page(request):
    context = {}
    return render_to_response('user_management/login.html',
                              RequestContext(request,context))
def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')

def login_error(request):
    context = {}
    return render_to_response('user_management/login_error.html',
                              RequestContext(request,context))

def redirect_to_user_registration(*args, **kwargs):
    if not kwargs['request'].session.get('saved_username') and \
       kwargs.get('user') is None:
        return HttpResponseRedirect('/user_registration/')

def user_registration(request):
    session_key = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
    backend = request.session[session_key]['backend']

    if request.method == 'POST' and request.POST.get('username'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            request.session['saved_username'] = form.cleaned_data['username']
            request.session['saved_first_name'] = form.cleaned_data[
                                                  'first_name']
            request.session['saved_last_name'] = form.cleaned_data['last_name']
            request.session['saved_gender'] = form.cleaned_data['gender']
            request.session['saved_birthday'] = form.cleaned_data['birthday']
            request.session['saved_invitation_code'] = form.cleaned_data[
                                                   'invitation_code']

            #Picture should be done smoother
            if 'picture' in request.session[session_key]['kwargs']['response']:
                request.session['saved_picture'] = request.session[session_key][
                                               'kwargs']['response']['picture']
            else:
                request.session['saved_picture'] = 'http://graduateland.com/' \
                                                   'media/gl/dummy_profile_picture.jpg'
            if 'link' in request.session[session_key]['kwargs']['response']:
                request.session['saved_profile_url'] = request.session[
                                                   session_key]['kwargs'][
                                                   'response']['link']
            return redirect('socialauth_complete', backend=backend)
    else:

        form_data = {}
        form_data['username'] = request.session[session_key]['kwargs'][
                              'details']['username']
        form_data['first_name'] = request.session[session_key]['kwargs'][
                              'details']['first_name']
        form_data['last_name'] = request.session[session_key]['kwargs'][
                              'details']['last_name']
        #Note! Some information might not be present in respone dict
        if 'gender' in request.session[session_key]['kwargs']['response']:
            gender = request.session[session_key]['kwargs'][
                                  'response']['gender'].capitalize()
            if gender.lower() == 'male':
                form_data['gender'] = 'M'
            elif gender.lower() == 'female':
                form_data['gender'] = 'F'
        if 'birthday' in request.session[session_key]['kwargs']['response']:
            form_data['birthday'] = request.session[session_key]['kwargs'][
                                    'response']['birthday']
        form_data['invitation_code'] = ""
        form = UserRegistrationForm(initial=form_data)
        form.from_oauth_provider = True

    context = {}
    context['backend'] = backend

    #TODO: Should try to get gravatar if no picture from oauth
    if 'picture' in request.session[session_key]['kwargs']['response']:
        context['picture'] = request.session[session_key]['kwargs'][
                             'response']['picture']
    else:
        context['picture'] = 'http://graduateland' \
                             '.com/media/gl/dummy_profile_picture.jpg'
    if 'birthday' in request.session[session_key]['kwargs']['response']:
        context['profile_url'] = request.session[session_key]['kwargs'][
                          'response']['link']
    context['form'] = form
    return render_to_response('user_management/user_registration.html',
                              context, RequestContext(request))

def get_user_data(request, *args, **kwargs):
    return_value = {}
    if kwargs.get('user'):
        return_value['username'] = kwargs['user'].username
    else:
        return_value['username'] = request.session.get('saved_username')
        return_value['first_name'] = request.session.get('saved_first_name')
        return_value['last_name'] = request.session.get('saved_last_name')
        return_value['gender'] = request.session.get('saved_gender')
        return_value['birthday'] = request.session.get('saved_birthday')
        return_value['picture'] = request.session.get('saved_picture')
        return_value['profile_url'] = request.session.get('saved_profile_url')

    return return_value

def save_registered_user_data(*args, **kwargs):
    #Here we save picture, birthday, gender, profile_url etc.
    #Should also create user profile to store this
    pass