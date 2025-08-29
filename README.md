# CampusFlight – Student Travel Platform 

CampusFlight is a website platform designed for **college students who travel by flight**.  
It helps students plan trips more efficiently, save money, and connect with peers traveling the same routes.  

- - -

## Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Setup](#-setup)
- [Usage](#-usage)
- [Team Roles](#-team-roles)
- [Next Steps](#-next-steps)

---

## Features
- **Airport Navigation** : Guidance from campus - airport (bus, shuttle, FlixBus).
- **Carpool Matching** : Find students from your university on the same flight.
- **Flight Statistics** : Track how many students use a specific flight.
- **Calendar Sync** : Connect to university calendars for cost effecive planning.
- **Friend Locator** : Find the cheapest time to visit your friends at other universities.
- **Flight Reliability** : Predict delays/cancellations from historical data/real time data.
- **DM System?** : 

---

## Tech Stack
- **Backend** : Flask (Python)
- **APIs** : Amadeus (flight data), Google Maps (routes/search)
- **Testing Tools**: curl, Postman
- **Database (planned)** : PostgreSQL with SQLAlchemy

---

## Setup
1. **Clone repo**
   (IDK what to put here)

---

## Usage
### API Route: `flights`

**Query Parameters**
- `origin`: (SJC, OAK, SFO only for now)  
- `destination`: IATA code (e.g, LAS, LAX)  
- `departure_date`: Format `MM-DD-YYYY`  
- `adults`: Number of travelers

---

## Next Steps 
- [ ] Add Google Maps API integration for shuttle/bus navigation  
- [ ] Implement FlixBus linking for intercity travel  
- [ ] Build carpool matching system for students on the same flight  
- [ ] Show flight popularity by university (analytics dashboard)  
- [ ] Sync with university calendars to recommend cheapest travel dates  
- [ ] Add flight delay prediction using historical data  
- [ ] Deploy Flask app to cloud (Heroku, AWS, or Render)  
- [ ] Write unit tests for all routes and helpers  
- [ ] Improve frontend UI for student friendly experience
  
