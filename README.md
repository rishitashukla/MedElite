INFINITE — Facility Assessment Report Generator
Managed by Medelite | Internal Tool for Directors
Live Site
https://rishitashukla.github.io/MedElite/
Overview
Enter any nursing facility CCN to instantly pull live CMS data and generate a polished Facility Assessment Snapshot. Combines public CMS data with manual operational inputs and exports to PDF or Word doc in one click.
How to Use

Enter a CCN (e.g. 686123) and click Look up
Fill in operational fields — EMR, census, patient type, medical coverage
Optionally type a custom facility name to override the CMS name
Click Download PDF or Download Word Doc

Features

Live CMS API lookup by CCN
Facility name manual override (INFINITE branding always stays fixed)
All 12 hospitalization and ED metrics with state and national benchmarks
One-click PDF export matching reference layout
One-click Word (.docx) export
Fully responsive UI

Tech Stack

Vanilla HTML, CSS, JavaScript — no framework
jsPDF + jsPDF-AutoTable — PDF export
docx.js — Word document export
Cloudflare Worker — CORS proxy for CMS API

CMS Endpoints
EndpointData4pq5-n9pyProvider info, star ratingstbry-pc3dClaims-based quality measureswse2-w6ygState and national averages
Assumptions

CMS API blocks browser requests from static sites (no CORS headers) — resolved by deploying a personal Cloudflare Worker proxy
Census Capacity auto-populated from CMS "Number of Certified Beds" field
State/national benchmarks fetched from a separate averages endpoint and joined by state code
CCNs automatically zero-padded to 6 digits before querying

Test Case
CCN: 686123 — Kendall Lakes Healthcare and Rehab Center, Miami FL

Reference: https://www.medicare.gov/care-compare/details/nursing-home/686123/view-all?state=FL
