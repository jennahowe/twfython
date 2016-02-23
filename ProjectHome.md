A python binding for the [TheyWorkForYou](http://www.theyworkforyou.com/) [API](http://www.theyworkforyou.com/api/).

This API is still not fully tested, so please report any bugs on the [Issues](http://code.google.com/p/twfython/issues/list) page.

# Usage #
twfy = TWFY.TWFY(APIKEY)

twfy.api.METHOD(PARAMS)

  * APIKEY = You [TheyWorkForYou API Key](http://www.theyworkforyou.com/api/key)
  * METHOD = The name of a [TheyWorkForYou API Function](http://www.theyworkforyou.com/api/), for example 'getMP'
  * PARAMS = The parameters supplied to the different [TheyWorkForYou API](http://www.theyworkforyou.com/api/) functions. See the [API docs](http://www.theyworkforyou.com/api/) for more info. The 'output' parameter is required by all methods and sets the output format you want the results in, must be one of: 'xml','php','js','rabx'

An example of how to use the API is included in the SVN repository, you can checkout the source [here](http://code.google.com/p/twfython/source/checkout)