# Django HTMX Event Organizer

> Note to the candidate:
>
> - This README file was taken from another project and partially updated. 
> - Please update the README with the correct information (including any changes made to the technical details and usage) once you have completed the challenge and remove this note.
> - Read the instruction for this challenge here : `_documentation\challenge_instructions.md`

### Description

This repo is a starting point for a simple Django app that allows users to securely manage events without requiring emails or logins.
- Organiser can create events and share the event link with the guests.
- Guests can RSVP to the event by providing their name and response.
- Organiser receive a unique link to edit the event and participant's response.
- Participants receive a unique link to edit their response.

An event managment app will in the future be added to the FlexUp app, but for the time being, this is a standalone project, used as a test for the candidates and as a "proof of concept" for the some of the features that will be implemented in the FlexUp app.


### Installation

- Install [uv](https://docs.astral.sh/uv/), [python](https://www.python.org/downloads/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your machine
- `git clone https://github.com/fabrizionastri/flexup-events` clone the repository to your local machine
- `uv sync` to install the required dependencies and create the virtual environment
- `python manage.py runserver` to start the server

### Access the App

- Open browser on http://localhost:8000/ to see the app

### Technical Details

- This app is designed to be used without requiring any login or email.
  - the app does not have a user database, so it does not store any user information.
  - the app does not have a email service, so it does not send any email.
- A single form is used to create, view and edit an object (event or participant).
  - the style and read-only status of the form is based on the `data-readonly` variable, which is toggled by the `Edit` button, and is stored in memory (handled in JavaScript only in the browser).
  - only the users with the correct link can edit the object. 
  - edit authorisation is handle both at the front-end and back-end level.
    - the `Edit` button is hidden if the user does not have the correct link.
    - the back-end checks the link and the object id to authorise the edit.

### Usage
- Organiser can create an event by clicking on the "New event" button in the navbar, then filling the form and clicking on the "Create event" button.
- Organiser is provided with 2 links and advised to store them in a safe place:
  - **registration** link: `events.flexup.org/event/\<event_id\>/register` to share with the guests
  - **admin** link: `events.flexup.org/event/\<event_id\>/admin/<event_admin_code\>` to manage the event and manage the participants' responses
- Organiser can send the links by any means they prefer (email, WhatsApp, facebook, etc, etc.):
  - the invitation link to the guests
  - the edit link to any other event organizer/admin
- When guests clicks on the invitation link, they are sent to the event registration page which contains the following:
  1. `Event Details`: the event details at the top of the page (the event form, in read only mode)
  2. `Responses` the list of current participants with their respective status (each row contains the response form, in read only mode, with the data of that participant)
  3. `New response:` blank response form in edit mode at the bottom of the table, with the "Submit" and "Cancel" buttons
  - available status for the guest are: `Confirmed`, `Maybe`, `Declined`
- After submitting the response, the guest is provided with a unique link to edit their response and advised to store it in a safe place (this link is the only way for them to edit their response)
- When the organiser clicks on the admin link, they are sent to the event admin page which contains the following:
  1. `Event Details`: the event details at the top of the page (the event form, in edit mode, but with the `Edit` button visible)
  2. `Responses` the list of current participants with their respective status (each row contains the response form, in edit mode, with the data of that participant) and an edit button for each participant
  3. `New response:` blank response form in edit mode at the bottom of the table, with the "Submit" and "Cancel" buttons
  - available status for the organiser are: `Confirmed`, `Maybe`, `Declined`, `Not responded`


### Technologies Used

- Django: The backend framework for developing the web application.
- Django Templating Engine: For generating dynamic HTML content.
- Bootstrap: For styling the web pages.
- JavaScript: For client-side scripting.
- SQLite (or other databases): Default database for Django.
  
### Contribution

If you'd like to contribute to this project:

- Fork the repository
- Create a new branch (git checkout -b feature-branch)
- Make your changes
- Commit your changes (git commit -m 'Add new feature')
- Push to the branch (git push origin feature-branch)
- Create a new Pull Request
