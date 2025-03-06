import json
from webhook_handler import send_request_to_validate_linkedin

def ask_question(question, options=None, multi_select=False, free_text=False):
    """ Ask the user a question, display options, and handle input validation. """
    print("\n" + question)

    if options:
        for key, value in options.items():
            print(f" {key}: {value}")

    if free_text:
        answer = input("\nEnter your response: ").strip()
    elif multi_select:
        answer = input("\nEnter your choices (comma-separated numbers): ").strip()
        answer = [int(x.strip()) for x in answer.split(",") if x.strip().isdigit()]
    else:
        answer = input("\nEnter your choice: ").strip()
        answer = int(answer) if answer.isdigit() else None

    print("✔️ Response recorded.")
    return answer

def multi_line_input(prompt):
    """ Function to take multi-line input (e.g., resume text). """
    print(prompt + " (Press Enter twice to finish)")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def collect_user_input():
    """ Guides the user through the job search or manual job entry process. """
    print("\n🚀 Welcome to your Personal Job Application Agent!\n")

    # Step 1: Ask the user if they want to enter a job link or perform a job search
    search_type = ask_question("Would you like to enter a job link manually or perform a job search?",
                               {1: "Enter Job Link", 2: "Perform Job Search"})

    user_input = {"search_type": search_type}

    if search_type == 1:
        # If the user selects to enter a job link
        user_input["job_link"] = ask_question("Enter the job posting link:", free_text=True)
    else:
        # If the user selects to perform a job search
        user_input.update({
            "location": ask_question("Where would you like to work?", {1: "Germany", 2: "USA", 3: "Remote"}),
            "work_mode": ask_question("What work mode do you prefer?", {1: "On-Site", 2: "Hybrid", 3: "Remote"}),
            "salary_min": ask_question("What is your minimum salary expectation?",
                                       {1: "Show all", 2: "25k+", 3: "50k+", 4: "75k+", 5: "100k+"}),
            "job_type": ask_question("What type of job are you looking for?", {1: "Full-Time", 2: "Part-Time"}),
            "experience_level": ask_question("What is your experience level?",
                                             {1: "Entry", 2: "Mid", 3: "Senior"}, multi_select=True),
            "keywords": ask_question("Enter job-related keywords (comma-separated):", free_text=True),
        })

    # Get LinkedIn Profile URL and validate it
    linkedin_profile = ask_question("Enter your LinkedIn profile URL:", free_text=True)
    # Validate LinkedIn URL and add it to the user input dictionary
    validation_response = send_request_to_validate_linkedin(linkedin_profile)
    user_input["linkedin_profile"] = linkedin_profile
    user_input["linkedin_validation"] = validation_response

    # Get the resume text
    user_input["resume_text"] = multi_line_input("Copy and paste your resume text below:")

    return user_input
