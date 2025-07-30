# SafeRent Miami

**SafeRent Miami** is a data-driven web application that helps users compare and evaluate neighborhoods in Miami-Dade County based on affordability, safety, and livability using open public datasets.

---

## Project Overview

Many renters, especially first-time movers or low-income families, lack access to localized data when choosing where to live. SafeRent Miami centralizes critical public data — including affordable housing availability, crime reports, and 311 service complaints — into an intuitive tool that supports better housing decisions.

---

## Target Audience

- Renters looking for affordable and safe housing
- Students and young professionals new to Miami-Dade
- Local real estate agents
- Nonprofits and housing justice advocates

---

## Features (Planned)

- Interactive map of neighborhoods with safety and livability scores
- Search/filter by income, crime rate, or housing program
- Crime trend visualization by ZIP code or district
- Data-driven housing recommendations
- User-friendly, mobile-first UI

---

## Data Sources

| Dataset | Source |
|--------|--------|
| Affordable Housing Inventory | [Miami-Dade Open Data](https://opendata.miamidade.gov/Housing-and-Development/Affordable-Housing-Inventory/qa9c-jh3z) |
| Crime Data | [Miami-Dade Open Data](https://opendata.miamidade.gov/Public-Safety/Crime-Data/yi5j-kuha) |
| 311 Service Requests | [Miami-Dade Open Data](https://opendata.miamidade.gov/Public-Safety/311-Service-Requests/yi9x-zf4f) |

---

## Data Analysis Plan

I plan to:
- Clean and filter data for the last 2–3 years
- Generate livability and safety scores based on weighted metrics
- Use visualizations and simple predictive modeling to aid decision-making

---

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | React (fenago/fenago21) |
| Backend | FastAPI (Python) |
| Data Analysis | Python, Pandas, Scikit-learn |
| Visualization | Recharts, Chart.js |
| Deployment | Vercel (frontend), Render (backend) |

---

## Project Structure (Starter)
/saferent-miami
├── frontend/ # React app (customized from fenago21)
├── backend/ # FastAPI backend + data model
├── data/ # Raw + cleaned datasets
├── README.md
└── .gitignore

