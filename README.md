# Customer Review to Support Ticket Pipeline

## Project Overview

This project converts customer reviews into structured complaint data and generates a professional support ticket summary using a two-step LangChain pipeline.

## Objectives

- Extract the main complaint from a customer review.
- Identify the related product or feature.
- Classify customer sentiment.
- Generate a concise support ticket summary with a recommended next action.

## Workflow

**Step 1: Complaint Analysis**

- Uses `PromptTemplate` to analyze the customer review.
- Uses `PydanticOutputParser` to return structured data containing the complaint, product or feature, and sentiment.

**Step 2: Support Ticket Generation**

- Uses `ChatPromptTemplate` with a support ticket writer persona.
- Uses `StrOutputParser` to generate the final ticket summary.
- Uses only the structured output from Step 1, not the original review.

## Technologies Used

- Python
- LangChain
- Pydantic
- NVIDIA AI Endpoints
- python-dotenv

## Setup Instructions

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your NVIDIA API key:

   ```text
   NVIDIA_API_KEY=your_nvidia_api_key
   ```

   Replace the placeholder with your own API key. Do not upload the `.env` file to GitHub.

5. Run the project:

   ```bash
   jupyter notebook main.ipynb
   ```

## Example Input

```text
The mobile app crashes every time I try to make a payment. I am very frustrated.
```

## Expected Output

The pipeline extracts the complaint, product or feature, and sentiment, then generates a professional support ticket summary with a recommended next action.

## Project Structure

```text
customer_review_support_ticket/
├── main.ipynb
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

The `.env` file and `.venv` directory should remain local and must not be committed to GitHub.
