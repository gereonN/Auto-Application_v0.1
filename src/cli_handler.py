import json

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

def collect_user_input():
    """ Guides the user through all questions regarding job search preferences. """
    
    print("\n🚀 Welcome to your Personal Job Application Agent!\n")
    
    user_input = {
        "location": ask_question("Where would you like to work?", {1: "Germany", 2: "USA", 3: "Remote"}),
        "work_mode": ask_question("What work mode do you prefer?", {1: "On-Site", 2: "Hybrid", 3: "Remote"}),
        "salary_min": ask_question("What is your minimum salary expectation?", 
                                   {1: "Show all", 2: "25k+", 3: "50k+", 4: "75k+", 5: "100k+"}),
        "job_type": ask_question("What type of job are you looking for?", {1: "Full-Time", 2: "Part-Time"}),
        "experience_level": ask_question("What is your experience level?", 
                                         {1: "Entry", 2: "Mid", 3: "Senior"}, multi_select=True),
        "keywords": ask_question("Enter job-related keywords (comma-separated):", free_text=True),
        "analyze_resume": ask_question("Would you like to analyze your resume?", {1: "Yes", 0: "No"})
    }

    # Resume analysis input (if selected)
    if user_input["analyze_resume"] == 1:
        user_input["resume_text"] = ask_question("Copy and paste your resume text below:", free_text=True)
        user_input["linkedin_profile"] = ask_question("Enter your LinkedIn profile URL:", free_text=True)

    return user_input
