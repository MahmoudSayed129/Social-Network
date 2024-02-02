# Social Network

## Demonstration
Watch the [YouTube video](https://youtu.be/vzFbNDSxei4) to see the application in action.

## Project Overview
Design a Twitter-like social network website for making posts and following users. The application allows users to create posts, follow other users, view posts from followed users, and interact with posts by liking and editing them.

### Features
- **New Post**: Users can create new text-based posts.
- **All Posts**: View all posts from all users, sorted by most recent.
- **Profile Page**: Visit a user's profile page to see their posts, followers, and following status.
- **Following**: View posts from users that the current user follows.
- **Pagination**: Display posts with pagination, 10 posts per page with next and previous buttons.
- **Edit Post**: Users can edit their own posts.
- **Like and Unlike**: Like or unlike posts with asynchronous updates.

## Getting Started

### Prerequisites
- Python 3.x
- Django 2.x or 3.x

### Installation
1. Clone the project.
2. Open a terminal and navigate to the `project4` directory.
3. Run the following commands to set up the application:
   ```sh
   python manage.py makemigrations network
   python manage.py migrate
   ```
4. Start the Django development server:
   ```sh
   python manage.py runserver
   ```
5. Open a web browser and go to `http://127.0.0.1:8000` to access the application.

## Usage
- **New Post**: Write and submit a new post using the provided form.
- **All Posts**: Navigate to see all posts from all users, with the most recent posts first.
- **Profile Page**: Click on a username to view their profile page, including posts, followers, and following status.
- **Following**: View posts from users that you follow.
- **Pagination**: Navigate through posts with next and previous buttons.
- **Edit Post**: Click on the "Edit" button to edit your own posts.
- **Like and Unlike**: Like or unlike posts by clicking on the respective buttons.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
- Harvard University's CS50 course for the project idea and initial guidelines.
- Django and JavaScript communities for their support and resources.
