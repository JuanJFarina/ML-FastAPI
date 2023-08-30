## Sentiment Analysis and Text Translation API

This API lets you translate any text of any language to spanish as well as detecting the original language automatically and also analyze its sentiment to see if it's a positive, negative or neutral message.

## Features

- Python FastAPI project with 3 different endpoints using three different libraries with ML process: textblob, deep_translator and langdetect
- The API exposes a Swagger documentation carefully explained
- Both prior features are publicly accessible at a Vercel Domain
- The project uses a CI/CD pipeline with Github Actions that run Formatting and Linter with Black and Pylint, Unit tests with Pytest, and also Type Checking with MyPy
- The API endpoints are protected using API Key Authentication
- Text Language Detection using LangDetect library.
- Text translation from any language to Spanish using the Deep Translator library.
- Sentiment analysis of text to determine if it's positive, negative, or neutral using the TextBlob library.
- A frontend client use case demo of the API functionality that allows users to leave comments and see sentiment-based responses.

## Demo

A use case demonstration is hosted at https://ml-fast-api-c7ef.vercel.app/ where you can see a simple feedback message so users can leave a comment about the service/app, etc., the message can be in any language and the response will vary according to the message's sentiment.

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