(function(){
	if (is_server === true) {
		console.log('init.js is_server');
		window.DJANGO_JS_CSRF = false;
		window.DJANGO_JS_INIT = true;
	}

	window.DJANGO_JS_URLS = {{ urls|safe }};
	window.DJANGO_JS_CONTEXT = {{ context|safe }};
}());
