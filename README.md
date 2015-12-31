# Steam Market Lookup #

A Python-Flask server for getting prices of items on the Steam market.
Deployable to Heroku.

## Resources ##
`/listings/<int:app_id>/<item:string>`

GET - Gets the 10 most recent item prices from the steam market

```JSON
{
  "success": ...
  "app_name": ...,
  "items": [
    {
      "id": ...,
      "price": ...
    }
  ]
}
```
