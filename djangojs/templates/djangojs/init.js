(function(){
    if (typeof is_server !== undefined) {
        window.DJANGO_JS_CSRF = false;
    }
    else {
        window.DJANGO_JS_CSRF = true;
    }

    window.DJANGO_JS_URLS = {{ urls|safe }};
    window.DJANGO_JS_CONTEXT = {{ context|safe }};

    window.DJANGO_JS_INIT = true;
}());
