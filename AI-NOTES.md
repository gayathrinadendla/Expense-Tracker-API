# AI_NOTES.md

# AI Usage Report

## 1. AI-generated vs. My Work

I used ChatGPT as a learning assistant to understand Flask, REST APIs, JSON handling, and project structure. The overall implementation, debugging, testing, and integration were completed by me.

AI helped with:
- Understanding Flask routing
- Designing the REST API structure
- Learning Postman for API testing
- Explaining JSON handling
- Understanding request.get_json() and jsonify()
- Creating the README documentation

I implemented, tested, and modified the code during development.

---

## 2. Validation and Changes

I manually tested every API endpoint using Postman.

The following endpoints were verified:

- POST /expenses
- GET /expenses
- GET /expenses?category=Food
- GET /expenses/total
- DELETE /expenses/<id>

During testing I corrected several issues including:

- HTTP method mismatches (GET vs POST)
- Flask routing errors
- Duplicate route definitions
- Session and JSON handling mistakes
- Data persistence in data.json

All APIs were re-tested after fixing the issues.

---

## 3. AI Suggestions Not Used

Some initial AI suggestions were simplified and modified to improve readability and make the code easier to understand.

Instead of directly copying generated code, I tested each function, understood its purpose, and adjusted the implementation wherever necessary.

The final project reflects my understanding of Flask REST APIs, JSON file handling, and API testing using Postman.