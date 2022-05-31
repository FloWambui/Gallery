# Gallery
### By Florence Wambui

### Description

Picasso gallery is an application that showcases beautiful images of Picasso's paintworks. Users get to view photos updated by the site admin and see photos based on the location. They can also copy the link to a photo to paste at their discretion. The search function will search photos based on the categories.


### Behavior Driven Development (BDD)
- A user can look at a variety of paintings that they are interested in.
- A user can click on the view moreand study the information of a single photo.
- A user may look for photographs in many categories.
- A user can copy the photo's link and send it to their pals.

### Setup Installation

- Copy the github repository url
- Clone to your computer
- Open terminal and navigate to the directory of the project you just cloned to your computer
- Run the following command to start the server using virtual environment

```
python3 -m venv --without-pip virtual
```

- To activate the virtual environment

```
source virtual/bin/activate
```

```
curl https://bootstrap.pypa.io/get-pip.py | python
```

```
pip install -r requirements.txt
```

- To copy .env.example to .env

```
cp .env.example .env
```

- Edit the .env file and replace the values with your own Cloudinary credentials and database credentials

- To run the server

```
python manage.py runserver

```


- Open the browser and navigate to http://127.0.0.1:8000/ to see the application in action

### Technologies Used
- HTML
- CSS
- Bootstrap
- Python
- Django
- PostgreSQL

### Apperance.
Homepage:
![HomePage](/static/photos/picasso.png)

View More:
![HomePage](/static/photos/deets.png)


- Live link to view the project <a target="_blank" href="https://picassogallery.herokuapp.com/">Picasso</a>

### Authors Info
Email Address- gflorencewambui@gmail.com.

Copyright (c) [2022] Florence Wambui.