# 7-10 Home Split - Backend

This is the backend API for the 7-10 Home Split web app. The API allows the frontend to manage users, user profiles, home listings and favorited homes.

Frontend repository: https://github.com/estein1988/710-home-fe

### Built With
Frontend: React 17.0.1, Google Maps API, Semantic UI, Material UI<br>
Backend: Python 3.7.9, Django v3.1.2, Django Rest Framework v3.12.1, Django Rest Framework Simple JWT 4.4.0, PostgreSQL v13.0

### API Sources
- Realtor.com API for Real Estate Listings: [Realtor API](https://rapidapi.com/apidojo/api/realtor/endpoints)
- Google Maps API for map interface: [Google Maps API](https://developers.google.com/maps/documentation)

### Demo Video
[Demo Video](https://www.youtube.com/watch?v=qRIJAES9l9E&feature=youtu.be)

## App Features

### Home Listings

This API endpoint contains a model which stores live real estate listings from the fixtures file in the repo. Each listing has location information, price links, IDs and other attributes regarding each home.

### Users

This API endpoint extends the abstract user model, and contains certain user information behind username and password such as, budget, hobbies, and lease end date.

### Favorites

This API endpoint joins users with their favorited home listings, through each model's ID fields.

## Challenges

This is my first project coding in Python and working with Django. Coming from Rails, it was a steep learning curve as I learned the hard-way how much Rails provides with out-of-the-box functionality. With Django, it was more difficult to connect model relationships, but I overcame this by developing object serializers to reference as variables in the model serializers.

Extending the user model and implementing authentication was also a challenge as there are a few ways to handle it (deciding between the Simple-JWT package and alternatively, Rest Framework-JWT). I decided to use the Simple-JWT package with the Django User model, so I could use some of the model fields given with Django but still use JWT verification. It was beneficial to wait for the first migration until the User model was properly setup and identified. 

## Future Implementation

- Add an end-point for home listings that facilities real-time data updates. Currently, the database can be seeded through real home listings in the fixtures folder of the repo, but I couldn't find free sources of data which would permit the end-point to update with every fetch.
- Add an endpoint which updates the user profile based on his/her mortgage calculations on the frontend.

## Collaboration

1. Fork and/or clone this repo & the backend repo: [Frontend Repo](https://github.com/estein1988/710-home-fe)
2. Create PostgreSQL database: `createdb homesplit`
3. Migrate database tables in backend: `python3 manage.py migrate` and `python3 manage.py loaddata home`
4. Run backend server: `python3 manage.py runserver`
5. Install dependencies on frontend: `npm install`
6. Run frontend server: `npm start`
7. Checkout new branch
   
If you'd like to collaborate on this project, please feel free to email me at: [estein1988@gmail.com](estein1988@gmail.com), or at or at https://www.linkedin.com/in/steinelliott/ 
