# Question 1: String Cleaning and Normalization
raw_feedback = " The speaker was great, but the room was cold. "
step1_cleaned = raw_feedback.strip().lower()
step2_replaced = step1_cleaned.replace("speaker", "presenter")
step2_normalized = " ".join(step2_replaced.split())
final_feedback = step2_normalized.title()
print(f"Cleaned Feedback: {final_feedback}")

# Question 2: Writing, Reading, and Appending to Files
feedback_list = [
    "The Presenter Was Great, But The Room Was Cold.",
    "Great Explanation Of Python File Operations.",
    "The Session Was Interactive And Very Helpful."
]

with open("feedback.txt", "w", encoding="utf-8") as file:
    for entry in feedback_list:
        file.write(entry + "\n")

print("=== Initial Contents of feedback.txt ===")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

new_entry = "Overall Great Workshop Experience."
with open("feedback.txt", "a", encoding="utf-8") as file:
    file.write(new_entry + "\n")

print("\n=== Updated Contents of feedback.txt ===")
with open("feedback.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Question 3: Exception Handling for File Operations
try:
    with open("feedback.txt", "r", encoding="utf-8") as file:
        file_contents = file.readlines()
        print("\nSuccessfully accessed and read feedback.txt.")
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
except PermissionError:
    print("Permission denied. Close the file and try again.")
finally:
    print("Operation completed")

# Question 4: Analysis and Summary File Generation
total_feedback_count = 0
great_keyword_count = 0

try:
    with open("feedback.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        total_feedback_count = len(lines)
        for line in lines:
            if "great" in line.lower():
                great_keyword_count += 1
except FileNotFoundError:
    print("Error: feedback.txt could not be located.")

summary_content = (
    "=== Workshop Feedback Summary ===\n"
    f"Total Feedback: {total_feedback_count}\n"
    f"Mentioned 'great': {great_keyword_count}\n"
)

with open("summary.txt", "w", encoding="utf-8") as summary_file:
    summary_file.write(summary_content)

print("\n=== Workshop Feedback Summary ===")
print(f"Total Feedback: {total_feedback_count}")
print(f"Mentioned 'great': {great_keyword_count}")
