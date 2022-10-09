# fastapi_simple_db
URL for this repo : https://github.com/pleabargain/fastapi_simple_db

# description
Super simple demo piece but it mostly kind of works.

# python 3.10.5

# test the app by running in the terminal
 ```uvicorn main:app --reload```   


# URLs in the project
I used these to check on status of the API while I was building it.
* http://127.0.0.1:8000/api/v1/users

* http://127.0.0.1:8000/docs
interactive documentation


* http://127.0.0.1:8000/redoc
Non interactive documentation

# IDE
I used VS Code.


## lots of problems with uuid!
Need to learn more about it.

# TODO  
* the put request doesn't work
* how to save changes to a real DB?
* currently post requests are not being saved
* use more dummy data from sites like mockaroo
* figure out how to document the various API commands! Ack! 

# why http?
You can comment all you like in the HTTP and that helps me in the debugging process.
I thought it important to be able to see the full structure of the request. Keep in mind POST requests  only get 'id' in the response! Not a bug!

# inspired by
https://www.youtube.com/watch?v=GN6ICac3OXY
Though he deleted the URL for this repo on his chat. 