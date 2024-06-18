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

## Usage

- To add articles, log in as an admin and navigate to the admin panel (`http://127.0.0.1:8000/admin`). From there, you can create new articles and assign them to categories.

- To view the blog website, simply visit the homepage (`http://127.0.0.1:8000`) and browse through the articles.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
