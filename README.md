## Sentiment Analysis and Text Translation API

This API lets you translate any text of any language to spanish as well as detecting the original language automatically and also analyze its sentiment to see if it's a positive, negative or neutral message.

## Usage

You can use our API in your app calling the Vercel deployment at https://ml-fast-api.vercel.app/ and using this API Key: key123

Additionally, the API hosts a Swagger documentation at https://ml-fast-api.vercel.app/docs# that will let you know each endpoint and how to use them with examples and also try them out (also using the API key)

Optionally you can clone the repository, locate yourself in the root directory, activate the python virtual environment by running

```python
venv\Scripts\activate
```

And run this command

```python
uvicorn main:app
```

This will run a local server that you can reach at 127.0.0.1:8000