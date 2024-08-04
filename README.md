# Flask Weather Application

This Flask application provides weather information for a specified city using the OpenWeatherMap API. The application includes basic error handling and renders the results on a web page.

## Features

- **Index Page**: Displays a form to input the city name.
- **Weather Endpoint**: Processes POST requests to fetch and display weather information for the specified city.
- **Error Handling**: Handles cases where the city is not found or other errors occur.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/shekoder/your-repo.git
    cd your-repo
    ```

2. Install the required Python libraries:

    ```sh
    pip install Flask requests
    ```

3. Set up your OpenWeatherMap API key:

    Replace `2aecf04cb5f79b16e630804d7dee4490` in the `app.py` file with your actual OpenWeatherMap API key.

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter the name of a city in the form and submit it to get the weather information.

## Application Structure

- `app.py`: The main Python script for the Flask application.
- `templates/index.html`: The HTML form for city input.
- `templates/weather.html`: The HTML page displaying the weather information.
- `templates/error.html`: The HTML page for displaying error messages.

## Example

- **Request Example**:
    - City: `London`

- **Response**:
    - Displays weather information for London or an error message if the city is not found.
