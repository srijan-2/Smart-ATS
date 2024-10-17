# Smart Application Tracking System: Leveraging Generative AI and LangChain

### Group Members
- Shivendra Singh (2029197)
- Srijan Kumar (2029202)
- Sneha Singh (2029203)
- Jyoti Kumar (2029204)

**Project Supervisor**: Prof. Amiya Kumar Dash  
**Institution**: KIIT University | 2024  

## Project Overview

The **Smart Application Tracking System (Smart ATS)** aims to revolutionize traditional applicant tracking systems by leveraging **Google Gemini** for semantic matching and **LangChain** for modular, flexible AI interactions. Traditional ATS platforms rely heavily on rigid keyword matching, which can overlook qualified candidates who phrase their experiences differently. Our system overcomes these limitations by understanding deeper contextual relevance, providing a more accurate and personalized experience.

## Key Features

- **Semantic Resume Matching**: Uses Google Gemini to evaluate resumes based on context, not just keywords. This ensures a more nuanced match between job descriptions and candidates' resumes.
- **Personalized Project and Certification Recommendations**: Suggests relevant projects and certifications to job seekers to help enhance their resumes based on current market demands.
- **Tailored Cover Letter Generation**: Streamlines the application process by drafting personalized cover letters aligned with job descriptions.
- **AI-Powered Parsing**: Leverages large language models (LLMs) to parse resumes and generate matching scores, making the application process more efficient and tailored.

## Technologies Used

- **Google Gemini**: For semantic matching and contextual understanding of resumes and job descriptions.
- **LangChain**: For orchestrating sequential tasks such as project recommendations, cover letter generation, and resume parsing.
- **Generative AI**: Used for resume parsing, generating match percentages, and crafting outputs like cover letters and project suggestions.

## How It Works

1. **Parsing & Cleaning**: The system begins by parsing the resume and job description to extract relevant content. Basic cleaning operations are performed to remove unnecessary characters or formatting.
2. **LangChain-Powered Workflow**: The cleaned text is passed through LangChain's Sequential Chain, which interacts with Google Gemini to generate specific outputs:
   - **Project Suggestions**: Based on job descriptions, the system recommends projects that enhance the candidate's profile.
   - **Cover Letters**: Automatically generates personalized cover letters.
   - **Certification Suggestions**: Recommends certifications aligned with job market trends.
3. **Output Generation**: Based on the analysis, users receive a tailored match percentage and the generated suggestions.

## Setup & Installation

To set up the Smart ATS on your local machine, follow these steps:

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/smart-ats.git
    cd smart-ats
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your API keys for Google Gemini (or equivalent LLM):
    - Add your API keys in the `.env` file.
4. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Upload a resume and job description through the application interface.
2. The system will analyze both files, parse relevant information, and generate:
   - A matching score.
   - Personalized project and certification suggestions.
   - A tailored cover letter draft.
3. Review the suggestions and export them for further use.

## Example

Here’s a quick example of how the system works:

**Input**:  
- Resume (uploaded as a PDF or text file).
- Job description (uploaded as a text file).

**Output**:  
- Matching Score: `85%`
- Recommended Projects: "Develop a Machine Learning Model for HR Analytics"
- Suggested Certifications: "AI in HR - Professional Certification"
- Generated Cover Letter: "Dear Hiring Manager, I am excited to apply..."

## Future Scope

Our Smart ATS has potential for further enhancement, including:
- Improved resume parsing with more detailed feedback.
- Integration with major job search platforms like LinkedIn or Indeed.
- Providing explanations alongside matching scores for better transparency.
  
## Contributing

We welcome contributions! If you’d like to contribute, please:
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add some feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---
