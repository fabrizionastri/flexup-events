# FlexUp Events - Django HTMX Coding Challenge  
*Fabrizio Nastri, Jan 2024*

## Table of Contents
- [FlexUp Events - Django HTMX Coding Challenge](#flexup-events---django-htmx-coding-challenge)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Objective](#objective)
  - [What We’re Looking For](#what-were-looking-for)
  - [Challenge Requirements](#challenge-requirements)
  - [Development Guidelines](#development-guidelines)
  - [User Stories \& Features](#user-stories--features)
  - [Submission Instructions](#submission-instructions)



## Introduction
Welcome to the FlexUp Events Django + HTMX coding challenge! This repository contains starter code that simulates a minimal event management app. The purpose of this challenge is to assess your skills in:

- **Django** (views, models, ORM, etc.)  
- **Django templating**  
- **HTMX** (dynamic partials, inline editing, etc.)  
- **Reading and understanding legacy code**  
- **Debugging and improving an existing codebase**  

You’ll find references to an existing architecture that aims to minimize front-end overhead by leveraging Django templating and HTMX for dynamic interactions.  

This project serves as:
- A standalone proof of concept for features that may be integrated into the FlexUp application in the future.
- A technical challenge for candidates evaluating how to work with Django and HTMX.



## Objective
By completing the tasks described here, you will demonstrate your ability to:

- Implement new features or fix bugs according to given specifications.  
- Ensure the code you write is clean, maintainable, and follows the existing project’s style (see [`_documents/guidelines.md`](../_documentation/guidelines.md) for specifics).  
- Handle typical “legacy” issues or partial code that may require extra care to integrate properly.  



## What We’re Looking For
1. **Technical Competence**  
   - Understanding Django views, models, URLs, and templating.
   - Proper usage of HTMX to update parts of a page.
2. **Code Clarity and Maintainability**  
   - Readable, well-structured, and documented code.
   - Clear and concise commit messages.
3. **Ability to Read and Extend Existing Code**  
   - Familiarity with typical Django project structures.
   - Willingness to follow established patterns and guidelines.
4. **Attention to Specifications**  
   - Closely follow the instructions in this file.
   - Check [`_documents/guidelines.md`](../_documentation/guidelines.md) for style/format requirements.
5. **Troubleshooting**  
   - Identify and fix bugs or performance issues.
   - Use best practices for debugging Django apps.


## Challenge Requirements
1. **Review Existing Code**  
   - Familiarize yourself with the project layout and code style.
2. **Implement the Assigned Features or Tickets**  
   - Review & update the app to meet the Complete any tasks specified in [challenge_instructions.md](/_documentation/challenge_instructions.md) or related files.
3. **Improve or Refactor Where Needed**  
   - If you see obvious inefficiencies or code smells, feel free to address them—just explain your changes clearly.
4. **Adhere to Guidelines**  
   - Maintain consistent coding style and comply with the guidelines in [`_documents/guidelines.md`](/_documentation/guidelines.md).


## Development Guidelines
- Use **Git** for version control:
  - **Commit Often**: Commit changes in logical increments.
  - **Feature Branches**: Work in separate branches for each major feature or ticket.
- Follow the existing **Django** patterns:
  - Keep models, views, and templates organized.
  - Use the existing URL patterns.
- **HTMX** usage:
  - Keep your partial templates clear and well-commented.
  - Use snippet-based updates for forms and in-page content changes.
- Make sure your code is **well-documented** and includes:
  - Docstrings for significant functions or classes.
  - Comments where needed to explain non-obvious logic.

Below is a suggested **User Stories & Features** section to include in the challenge instructions. You can place it wherever fits best in your existing file (for example, after **Challenge Requirements** or before **Development Guidelines**). No need to rewrite the entire file—just insert this new section as appropriate.

## User Stories & Features

The application you will be working on should allow both organizers and guests to participate in event management according to these core user stories:

1. **Create Event**  
   - An **organizer** clicks the “New event” button in the navbar.  
   - Fills out the event form (date, title, etc.).  
   - Clicks “Create event” to submit.  
   - Receives **two links**:  
     - A **registration link** (`/event/<event_id>/register`) to share with guests.  
     - An **admin link** (`/event/<event_id>/admin/<event_admin_code>`) for editing event details and managing participant responses.
   - The organizer is advised to store these links for future use.

2. **Share Links**  
   - The **organizer** can share the registration link with any guests (via email, messaging, social platforms, etc.).  
   - The **admin** link should remain private (or shared only with co-organizers) to maintain event editing permissions.  

3. **Guest RSVP**  
   - **Guests** open the registration link (`/event/<event_id>/register`).  
   - They see:
     1. **Event Details** in read-only mode.  
     2. **Responses**: A list of all participants who have responded (each in read-only mode).  
     3. A **New response** form at the bottom of the table or in a popup (in edit mode) with “Submit” and “Cancel” buttons.  
   - Guests can set their response status to **Confirmed**, **Maybe**, or **Declined**.  
   - After submitting, a unique **edit link** is provided to the guest for updating their RSVP later.  They are advised to store this link for future use.

4. **Admin Management**  
   - **Organizers** (using the admin link) see:
     1. **Event Details** at the top of the page (in edit mode, but with an “Edit” button toggle).  
     2. **Responses**: A list of current participants with their statuses (each in edit mode).  
     3. A **New response** form at the bottom of the table (in edit mode) with “Submit” and “Cancel.”  
   - Organizers can set participant status to **Confirmed**, **Maybe**, **Declined**, **Invited** or **Waiting List**.  

5. **Security & Editing**  
   - **Unique links** ensure only the organizer or authorized individuals can modify event details.  
   - **Guest links** allow participants to modify only their own responses.  


## Submission Instructions
1. **Fork** this repository into your own GitHub account.  
2. Work on your tasks in a **feature branch**.  
3. When you’re satisfied with your solution:
   - Push your changes to your fork on GitHub.
   - Provide a link to your repository OR open a **Pull Request** to the original repository (if instructed).
4. **Remove These Instructions**  
   - This file (`challenge_instructions.md`) should be removed or cleared of any references to the challenge itself.
   - The final version of the README should be updated according to your changes but must not include these instruction notes.



**IMPORTANT**: These instructions are for your eyes only and must be deleted before you finalize and submit your challenge solution.  

Good luck, and thanks for participating in the FlexUp Events coding challenge!
