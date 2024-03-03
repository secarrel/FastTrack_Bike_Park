# FastTrack Bike Park

[MOCKUP](mockup.link)

link to deployed site: [LINK]()

## Introduction

FastTrack Bike Park is a fictional mountain biking park. This project is a website for this park, allowing users to book an uplift, pedal pass, coaching courses, or hire equipment. 



- test purchase details
- admin access details

## Table of Contents


## Project Planning (5 Planes)

### Strategy Plane
#### Goals
I have set goals for the project alongside the user stories, which are based on these. These provide useful guidance at the first stages of planning through to the final UX decisions.

##### User Goals
- Navigate site
- Search, filter, and sort products
- Add products to the shopping basket
- CRUD functionality within the shopping basket
- Checkout securely with Stripe
- See purchases in 'User Profile'
- Sign-in, Sign-up, Sign-out
- Update account settings
- Contact the site admin

##### Business Goals
- Provide important information about the bike park to allow users to make informed decisions and purchase products.
- Provide a variety of products to appeal to a mountain biking audience of varying experiences.
- CRUD functionality on all products.
- Track activity purchases in a calendar.
- Reply to customer queries.
- Amend bookings and purchases as required. 
- Increase footfall on-site through marketing and good UX.

#### User Stories

|  | I would like... | so that I can ... |
| ---- | ---- | ---- |
| As a First Time User | to see a navbar with clear and intuitive navigation links | easily move around the site to find relevant products and information. |
|  | to see a clear explanation of what the site is and it's purpose | understand how I can use it for my needs. |
|  | to be able to add items to my basket without having an account | decide whether to sign up or not based on the suitability of the product offering for me. |
|  | to be able to create an account | see my order history and bookings |
|  | to be able to sort, filter and search products | find the most suitable products easily and quickly. |
|  | to see items added to my basket, edit them, and remove them individually | checkout with exactly the products I would like to buy, without having to create a whole new basket. |
|  | to see the current conditions of the bike park | decide whether to book a ticket for the day. |
|  | to know what ability level I need to be to visit | decide whether to book and what to book. |
|  | to know details about the park that could affect my visit (eg. contact, hours, trails, location) . | be prepared and book the appropriate product. |
| As a Registered User | Easily navigate to the product I would like to book | quickly book without looking through all products when I know what I need already. |
|  | to see my previous purchases | order the same product again or find out the details of a booking. |
|  | to edit my account details | keep using my account with the correct personal information. |
|  | to sign into an account I have previously created | keep track of purchases and continue to purchase products. |
|  | to be able to contact the site admin about an order | resolve any issues with the purchase. |
|  | to be able to see promotional information | buy products at a lower price, encouraging me to visit the site more frequently. |
| As a site admin | to be able to use CRUD functionality on all products | keep them up to date easily. |
|  | to be able to see all sales | analyse sales and review marketing practices. |
|  | to see a calendar with all activity bookings | keep track of what has been purchased and assign instructors. |
|  | to be able to provide refunds or reschedules for accidental bookings | retain customers through positive experiences. |

**WORK IN PROGRESS**

#### Marketing
- Social media 

    Users can sign up for the newsletter to get updates on promotions, events and other news about the park. Using Django AllAuth, users are also able to sign in using social media, encouraging them to sign up and share their experience which will promote the site.

- Promotions

    The site should have a promotions section, potentially as a carousel just below the header. Promotions can also be sent out to users who have signed up for the newsletter.

- Company Values

    Including a section about company values will help people connect with the park and site. I have strong environmental values and would like to promote conservation and sustainable practices. This is something I intend to mention on the site. Many mountain bikers share these values as they love to spend time in nature and therefore want to protect it. So I think these values are well-aligned to the target audience.

        WORK IN PROGRESS
    - Meta tags
    - Look into sitemap.xml and robots.txt
    - Further research into marketing techniques is required.


### Scope Plane
I have decided to approach this project with [agile methodology](https://asana.com/resources/agile-methodology) as I am aware it has a large scope relative to my previous projects and, despite careful planning, I'm not certain of how long it will take to create the MVP and additional features. At least by working in this way, I know I will have a functional product to submit at any stage of development. 

I have broken the project into sprints with soft deadlines to guide me through development. You can see these sprints and a timeline below. The intention is that at the end of a sprint, I will review the work I have completed and test it for bugs and any poor UX. I would like to fully complete each sprint in full before moving on to the next. 

I will also be using [GITHUB PROJECTS]() to set smaller tasks for myself as I think this will help with motivation and direction. I think this will be an effective way to organize myself to ensure I don't miss any important features I was hoping to include. 

##### Sprints & Time management 
| Order | Description | Timeframe | 
| ---- | ---- | ---- | 
| 1 | Planning | 19/02/24 - 24/02/24|
| 2 | Project Setup | 24/02/24 - 26/02/24 |
| 3 | Authentication Setup, Sign-in and Sign-up page | 26/02/24 - 28/02/24 |
| 4 | Base Template and Landing Page | 28/02/24 - 01/03/24 |
| 5 | Basic Navigation Setup | 01/03/24 |
| 6 | Deploy | 02/03/24 |
| 7 | Product Setup and Product Pages | 04/03/24 - 07/03/24 |
| 8 | Product Filtering, Searching and Sorting | 08/03/24 - 09/03/24 |
| 9 | Booking System Setup | 11/03/24 - 15/03/24 |
| 10 | Shopping Bag Setup and CRUD | 16/03/24 - 20/03/24 |
| 11 | Checkout & Stripe | 21/03/24 - 25/03/24 |
| 12 | User Profile | 26/03/24 - 29/03/24 |
| 13 | Admin Page Setup | 01/04/24 - 05/04/24 |
| 14 | Email Setup | 05/04/24 - 07/04/24 |
| 15 | Testing and Readme | 07/04/24 - 15/04/24 |

##### Prioritization
The Kanban board in GitHub Projects will help with feature prioritization as well as with efficiency and motivation. I will label each feature using the [MoSCoW](https://www.techtarget.com/searchsoftwarequality/definition/MoSCoW-method) method. 
- **M**ust have
This will outline the MVP for this project. Anything in the category with be the priority and developed before anything in other MoSCoW categories. 
- **S**hould have
Anything in this category would be beneficial to the project but without it, I would still have a functional site that meets the pass criteria.
- **C**ould have
This category will include the features that I would like to include in the site but have a smaller impact and generally aren't that important. These features will be added at the end of the project if there is enough time. Anything in the category will be noted as a future feature.
- **W**ill not have
I'm including this category so that I can control scope creep. It will help to set the boundaries of the project. 

| Item | Feature | MoSCoW Category | 
| ---- | ---- | ---- | 
| 1 | User Authentication with Django AllAuth| **M** |
| 2 | Product (uplift and pedal pass) display with Search, filter & sort| **M** |
| 3 | Product Details Page | **M** |
| 4 | Shopping Basket with CRUD | **M** |
| 5 | Secure Checkout with Stripe | **M** |
| 6 | Responsive Design | **M** |
| 7 | Toasts | **M** |
|  | ... |  |

    WORK IN PROGRESS

### Structure Plane
#### How features fit together.
#### Navigation
#### Categorization 
#### Flow chart

### Skeleton Plane
    #### Wireframes 
    #### Database Schema

### Surface Plane
    #### UX/UI

        ##### Design inspiration
        ##### Colour Scheme

        - Show colour pallet
        - Explain colour scheme intentions
        - Accessibility checks ?
        - Contrast checks ?
        - Learn about root variables

        ##### Typography 

        - Show fonts & pairing
        - Explain typography intentions

    #### Defensive Design 
        - Django AllAuth
        - Form Validation and error messages
        - Toasts
        - Redirection to accessible urls. 
        - Deletion confirmation required.
        - Error pages with navigation to the home page. 
        - Complete testing and validation of features. 
        - CSRF tokens????

## Features

### Feature access
- Which features are visible to who?

| Feature | Guest | Registered account holder | Admin | Staff |
|---------|--------|------|--------|--------|
| Feature | Access? | Access? | Access? | Access? | 
| Feature | Access? | Access? | Access? | Access? | 
| Feature | Access? | Access? | Access? | Access? | 
| Feature | Access? | Access? | Access? | Access? | 


### CRUD functionality 

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Feature | Create | Read | Update | Delete |
| Feature | Create | Read | Update | Delete |
| Feature | Create | Read | Update | Delete |
| Feature | Create | Read | Update | Delete |

### Feature Showcase

### Future Features

## Technologies
### Languages
### Frameworks
### Libraries
### Tools

## Testing

## Deployment 
### Connecting to GitHub
### Django Project Setup
#### Elephant SQL
### Heroku Deployment
### Google mail?
### Aws Config
### Stripe Config
### Clone Project
### Fork Project

## Credits
### Code
### Support materials
### Media
### Acknowledgements









