All the links i.e to view the drinks, create, delete or to update the drinks are in the views.py file in the api in the form of dictionary.
To add a new drink write in this format for eg.
{
  "name" : "coke",
  "category" : "soda",
  "amount" : "60"
}

To update a drink go the link described in the api_urls for ex- http://127.0.0.1:8000/api/update-drink/3 and proceed to write the drink in the formate specified above.

