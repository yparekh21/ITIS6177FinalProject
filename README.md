# Document Summarization API

## Overview
The Document Summarization API provides a simple interface to summarize text documents using Azure Text Analytics. The API supports extracting key sentences from input text.

## Prerequisites


## Base URL
The base URL for the API is https://your-api-domain.com.

## Authentication
The API requires an API key for authentication. Include the API key in the headers of your requests using the Ocp-Apim-Subscription-Key header.

## Endpoints
Summarize Text

## Error Handling
The API returns appropriate HTTP status codes and error messages. If an error occurs, refer to the error field in the response for details.

### Status Codes
200 OK: Successful response.
400 Bad Request: Malformed request or invalid parameters.
401 Unauthorized: Missing or invalid API key.
429 Too Many Requests: Exceeded rate limit.
