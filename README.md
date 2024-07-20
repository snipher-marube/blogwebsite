# Blog Website

This is a blog website built with Django and Tailwind CSS. It allows the admin to add articles and group them into categories.

## Prerequisites

Before getting started, make sure you have the following installed:

- Python 3.x
- Django
- Tailwind CSS

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/snipher-marube/blogwebsite.git
    ```

2. Navigate to the project directory:

    ```bash
    cd blogwebsite
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your web browser and visit `http://127.0.0.1:8000` to see the blog website.

## Elasticsearch Integration
To integrate Elasticsearch with the blog website, follow these steps:

1. Install Docker and Docker Compose if you haven't already.

2. Start the Elasticsearch container using Docker Compose:

    ```bash
    docker-compose up -d elasticsearch
    ```

3. Rebuild the search index by running the following command:

    ```bash
    python manage.py search_index --rebuild
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Open your web browser and visit `http://127.0.0.1:8000` to see the blog website with Elasticsearch integration.

## Usage

After integrating Elasticsearch, you can use the search functionality on the blog website. Simply enter a search query in the search bar and press Enter. The website will display the articles that match the search query.


## Contributingg

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


## License

This project is licensed under the [MIT License](LICENSE).
