# AI Cold Email Generator for Professors

This Python script utilizes OpenAI's GPT-4 to generate professional cold emails tailored for professors based on their research interests and your background. It also includes functionality to send the emails via Gmail.

## Features
- Uses AI to generate personalized cold emails.
- Sends emails via SMTP (Gmail integration).
- Customizable inputs for professor details, sender information, and email content.

## Requirements
- Python 3.x
- `openai` Python package
- SMTP access (Gmail)

## Installation
1. Clone the repository or download the script.
2. Install required dependencies:
   ```sh
   pip install openai
   ```

## Usage
1. Set your OpenAI API key in the script.
2. Provide professor details and your own information.
3. Configure your Gmail credentials (Note: You may need to enable "Less Secure Apps" or use an app password).
4. Run the script:
   ```sh
   python ai_cold_email_professors.py
   ```

## Notes
- Ensure you replace placeholders with your actual credentials before running the script.
- Use responsibly and avoid spam-like behavior when reaching out to professors.

## License
MIT License
