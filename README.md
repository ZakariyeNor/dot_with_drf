# DOT-DRF (Django OAuth Toolkit with DRF + Next.js Frontend)

A full-stack project demonstrating **OAuth2 authentication** using **Django REST Framework** and **django-oauth-toolkit**, with a **Next.js + TypeScript frontend** for managing notes.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Folder Structure](#folder-structure)
- [License](#license)

---

## Project Overview

This project demonstrates:

- **Django REST Framework** backend with `notes_api` app  
- OAuth2 authentication using **django-oauth-toolkit**  
- **Next.js + TypeScript** frontend consuming the API  
- Users can log in, create notes, and view notes securely  

---

## Features

- User login via OAuth2 password grant  
- Protected API endpoints (scoped access)  
- Create, read, and list notes  
- Next.js frontend with login and notes UI  
- Axios integration for API calls  
- CORS handling between frontend and backend  

---

## Tech Stack

- **Backend:** Django, Django REST Framework, django-oauth-toolkit  
- **Frontend:** Next.js (App Router), TypeScript, Axios, Tailwind CSS  
- **Authentication:** OAuth2 (Password Grant)  
- **Database:** SQLite (default, can use Postgres/MySQL)  

---

## Prerequisites

- Python 3.10+  
- Node.js 18+  
- npm or yarn  
- Git  

---

## Setup

### Backend

1. Navigate to backend folder:

```bash
cd DOT-DRF/dot_with_drf/notes_api
