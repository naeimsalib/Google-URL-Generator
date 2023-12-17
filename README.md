# Google URL Generator

## Overview

Google URL Generator is a Flask-based web application designed to create Google search URLs based on user queries. It simplifies the process of generating Google search links, allowing users to directly enter search queries and receive ready-to-use Google search URLs.

## How It Works

The web application takes a user's search query input and uses the "Google URL Generator" API to generate a URL that directs to Google's search results for that query. This makes it incredibly easy to programmatically create URLs for Google searches.

## Features

- **User-Friendly Interface**: A simple and intuitive interface for entering search queries.
- **Instant URL Generation**: Quick generation of Google search URLs from user input.
- **Responsive Design**: The application is built using Bootstrap, ensuring a responsive design that works well on both desktop and mobile devices.

## API Used

The application uses the "Google URL Generator" API, which is a custom API hosted on RapidAPI. This API accepts search queries and returns a Google search URL specific to that query. The API is designed to be simple yet effective, providing a straightforward way to generate Google search links programmatically.

Check out the API on RapidAPI: [Google URL Generator API](https://rapidapi.com/naeimsalib/api/google-url-generator)

## Live Application

The web application is hosted on Heroku and can be accessed at the following URL: [Google URL Generator Web App](https://google-url-generator-app-22a0aa44cdad.herokuapp.com/)

## Getting Started

To run the application locally:

1. Clone the repository:
   git clone https://github.com/naeimsalib/Google-URL-Generator.git
2. Navigate to the cloned directory:
    cd Google-URL-Generator
3. Install the required dependencies:
    pip install -r requirements.txt
4. Run the Flask app:
    flask run


The application will be accessible at `http://localhost:5000`.

## Contributing

Contributions to improve Google URL Generator are welcome. Feel free to fork the repository and submit pull requests.
