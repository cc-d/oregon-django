# Django Full Stack Demo of Art
Demonstration of art project for Django Full Stack Engineer candidates. We believe the scope outlined below is likely more than the 4 hours we have asked you to commit to this. Please complete as much of the assignment as you can in the allotted time, adjusting the README as you go. You should prioritize your work and focus on the most important parts first.

We would like you to create a simple Restaurant Menu CRUD application using a React frontend and Django REST backend.

## Needs Statements
- A customer needs a way to see a restaurant's menu. For each menu item, they need to see the item name, item cost, and item description.
- A restaurant owner needs a way to update their menu. They should be able to add new items, remove old items, and update cost and description of existing items.

## Prerequisites
- Install python 3 (apt-get install python-3 on ubuntu 20)
- Install pip 3 (apt-get install python3-pip on ubuntu 20)
- Install python requirements (pip3 install -r requirements.txt on ubuntu 20)
- Apply migrations (python3 manage.py migrate on ubuntu 20)

- The react section of this was going to be over 8 steps long, but just installing and configuring it (and resolving CORS errors) ended up taking up too much time so I just completed the frontend in django. I had to upgrade my dev server from 512mb to 2048mb ram just to even compile the npm packages 

## Usage
```zsh
git clone https://gitlab.com/wwdofa/django-assignments/CaryCarter-Django-demo-of-art.git
cd cd CaryCarter-Django-demo-of-art
Run the server: python3 manage.py runserver 0.0.0.0:8000
Navigatie to server ip/port Example: http://168.235.89.157:8000/
Add/Remove items Example: http://168.235.89.157:8000/
```

## Contributing
```zsh
git clone https://gitlab.com/wwdofa/django-assignments/CaryCarter-Django-demo-of-art.git
cd cd CaryCarter-Django-demo-of-art
TODO: Provide instructions for contributors
```
