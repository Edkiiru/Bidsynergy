# Project Overview
Colaberry is developing a recommendation system to identify federal contract-winning companies that may need data contracting services, aiming to foster partnerships and create job opportunities. Using collaborative filtering and NLP, the system will analyze contract data, including award information and descriptions, to recommend companies for outreach.

The primary users are Colaberry's business development team, who will leverage these insights to expand business opportunities. In the long term, the system could also forecast emerging contracting trends relevant to Colaberry’s offerings, driving strategic growth and innovation.

![Zoom Image](DALL·E_2024-10-22_18.21.04.webp)

---

## Executive Summary
Colaberry's initiative focuses on leveraging advanced analytics to unlock new business opportunities by identifying federal contract awardees in need of data services. This system uses collaborative filtering and NLP to match contract winners with Colaberry’s offerings, empowering the business development team to engage in targeted outreach. Beyond immediate gains, the solution will provide strategic insights into future federal contracting trends, ensuring Colaberry remains proactive and aligned with market demands, fostering sustainable growth and innovation.

---

## Background
To navigate the complexity of contract data, the project will develop a recommendation system utilizing collaborative filtering and NLP to pinpoint high-potential partners. This solution will streamline outreach efforts, foster strategic partnerships, and generate new job opportunities.

The project also serves as a professional development initiative, offering Colaberry interns hands-on experience with real-world data challenges. Successful interns will have the opportunity for full-time roles, creating a seamless talent pipeline that supports Colaberry’s growth. Beyond identifying immediate prospects, the system will forecast trends in federal contracting, ensuring Colaberry stays proactive and aligned with future market demands.

---

## Problem Statement
Colaberry aims to identify federal contract-winning companies likely to need data services, enabling targeted outreach and partnership opportunities. The challenge lies in analyzing complex contract data efficiently to unlock business potential while fostering job creation and talent development within Colaberry.

---

## Project Objective
The objective of this project is to develop a data-driven recommendation system that identifies federal contract-winning companies likely to need data contracting services. This solution will streamline outreach efforts, foster strategic partnerships, create job opportunities, and provide hands-on experience for Colaberry interns, supporting both immediate business growth and long-term talent development.

---

## Data Overview
The project will leverage federal contract data to identify companies that are potential candidates for Colaberry’s data contracting services. The dataset will include key details about awarded contracts, enabling the recommendation system to analyze patterns, detect relevant opportunities, and recommend companies likely to require Colaberry’s services. Collaborative filtering and NLP will be applied to enhance the accuracy and relevance of these recommendations.

### Data Sources
- **SAM.gov (System for Award Management):** Offers profiles of federal contractors, including their NAICS codes and business capabilities.
- **Colaberry Internal Data:** Existing partnerships, services provided, and business development insights that inform the model's recommendations.

### Key Data Fields (Independent Variables)
- **Award Number:** Unique identifier for each contract.
- **Awardee:** Name of the company receiving the contract.
- **Department/Agency:** Federal entity awarding the contract.
- **NAICS Code:** Industry classification to determine service relevance.
- **Award Date:** Contract issue date, used to identify recent opportunities.
- **Contract Description:** Text data analyzed using NLP to assess the need for data services.

---

## Key Performance Indicators (KPIs)
- **Accuracy of Recommendations:** The percentage of recommended companies that express interest or engage with Colaberry.
- **Conversion Rate:** Number of identified companies that result in successful partnerships or contracts.
- **Job Opportunities Created:** The number of new jobs generated through successful partnerships.
- **Internship-to-Full-Time Conversion Rate:** Percentage of interns involved in the project who transition to full-time roles.
- **Outreach Efficiency:** Time saved in identifying and reaching out to potential partners compared to manual methods.
- **Trend Forecasting Accuracy:** The ability to predict future federal contract trends relevant to Colaberry’s services.

---

## System Architecture
The recommendation system will integrate collaborative filtering and NLP models, processing federal contract data to identify relevant partners. It will leverage cloud-based infrastructure for data ingestion, model training, and deployment, ensuring scalability and seamless access for Colaberry’s business development team.

### Pipeline Steps:
1. **SAM.gov to Lakehouse:** Copies data from the SAM.gov API connection to a staging table in the BidSynergy Lakehouse.
2. **Updating Auto-refresh Notebook:** Adds a refresh timestamp column and updates the data.
3. **1-Month Filter Notebook:** Filters the staging table to meet specific criteria.
4. **3-Year Filter Notebook:** Filters records over three years with an award amount greater than or equal to $2 million.
5. **Merged Notebook:** Merges records from the 3-year and 1-month filters.
6. **BidSynergy to Basecamp Notebook:** Automates the updated CSV file in the BidSynergy Lakehouse to consulting project docs in Basecamp.
7. **Pipeline Fail Notice:** Sends an email alert message in case the pipeline execution fails on schedule.

---

## Methodology
1. **Data Collection:** Federal contract data sourced from SAM.gov, alongside Colaberry’s internal data.
2. **Data Cleaning and Preprocessing:** Handling missing values, standardizing fields, and tokenizing contract descriptions.
3. **Exploratory Data Analysis (EDA):** Identifying patterns in awards by year and industry.
4. **Model Development:**
   - Collaborative Filtering: To recommend companies based on award patterns.
   - NLP Analysis: To assess contract descriptions.
5. **Model Training and Validation:** Splitting data into training and test sets.
6. **Evaluation Metrics:** Measuring performance using KPIs.
7. **Deployment:** Integrating the system into Colaberry’s workflow.

---

## Results
- **Case 1: Awards per Year:** Analysis of annual federal awards to identify active sectors.
- **Case 2: Proposals by Month:** Seasonal trends in contracting to optimize outreach timing.

---

## Impact
1. **Business Growth:** New partnerships will expand Colaberry’s client base.
2. **Job Creation:** Opportunities for Colaberry interns and full-time staff.
3. **Operational Efficiency:** Automating partner identification saves time and effort.
4. **Strategic Alignment:** Forecasting trends ensure proactive service alignment.

---

## Lessons Learned and Future Work
### Lessons Learned
- Addressing data quality issues is critical for model accuracy.
- Combining collaborative filtering with NLP improves recommendation relevance.

### Future Work
- Expanding to include grant and non-federal contract data.
- Exploring advanced machine learning techniques for better forecasting accuracy.
- Refining model recommendations based on actual outcomes.

---

## Deployment
The recommendation system will be deployed using cloud-based infrastructure, enabling seamless integration into Colaberry’s operations. A web-based dashboard will provide real-time insights, while automated workflows ensure continuous data analysis and up-to-date recommendations. User training will ensure effective utilization of the system.

[Power BI Service Deployment](https://app.fabric.microsoft.com/view?r=eyJrIjoiYTBjMTNkNzctOTA0Ny00OGIxLTk2MmYtNmY0MGUzNzMyMjVmIiwidCI6ImYxYWQ2ODFmLTZmNjItNDNhOS04MjQxLTA3MDMxNjBlMTM0OCIsImMiOjN9)
