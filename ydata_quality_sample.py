# pip install ydata-quality
    # Make sure your Python Version is 3.8 (as of July 2023)
from ydata_quality import DataQuality
import pandas as pd
import re 
import textwrap



# Load data
df = pd.read_csv('guerry_histdata.csv')


# Create Main Engine
ED_EXTENSIONS = ['a_custom_EDV', 999999999, '!', '', 'UNKNOWN']
SENSITIVE_FEATURES = ['Suicides', 'Crime_parents', 'Infanticide']

dq = DataQuality(df=df, label='Pop1831', ed_extensions=ED_EXTENSIONS, sensitive_features=SENSITIVE_FEATURES, random_state=42)


########################################################################################################################################################################

# # Run Data Quality Checks
#dq.run_all_checks()

# Full Evaluation
full_results = dq.evaluate()

# # Print Results
# dq.print_results()

# # Profile the data
# profile = dq.profile_data()

# # Print a summary of the findings
# print("Missing values:")
# print(profile["missing_values"])
# print("Duplicate values:")
# print(profile["duplicate_values"])
# print("Outliers:")
# print(profile["outliers"])

########################################################################################################################################################################

# # Impute missing values with the mean
# dq.impute_missing_values(method="mean")

# # Remove duplicate values
# dq.remove_duplicate_values()

# # Transform outliers with the median
# dq.transform_outliers(method="median")

# # Generate a report that summarizes the findings of the data cleaning
# report = dq.report()
# print(report)


########################################################################################################################################################################

# # Create histograms
# dq.plot_histograms()

# # Create box plots
# dq.plot_box_plots()

# # Create correlation matrices
# dq.plot_correlation_matrices()

# # Generate a report that summarizes the findings of the data visualization
# report = dq.report()
# print(report)


########################################################################################################################################################################

# Check the status
warnings = dq.get_warnings()

# With get_warnings you can also filter the warning list by specific conditions
duplicate_quality_warnings = dq.get_warnings(category='Duplicates')
priority_1_warnings = dq.get_warnings(priority=1)
priority_2_warnings = dq.get_warnings(priority=2)
priority_3_warnings = dq.get_warnings(priority=3)

print(type(priority_1_warnings))
print(type(priority_2_warnings))
# print(priority_3_warnings)

########################################################################################################################################################################

# # Create an HTML file using the ydata-quality library functions
# report = full_results.report()
# print(report.to_html())


# Create an HTML file manually

# # Helper function to strip ANSI escape codes from a warning message
# def strip_ansi_escape_codes(warning):
#     """Converts non-string elements to string and strips ANSI escape codes from a warning message."""
#     if not isinstance(warning, str):
#         warning = str(warning)
#     return re.sub(r"\033\[[0-9;]*m", "", warning)

# # Remove the ANSI escape codes
# warnings = [strip_ansi_escape_codes(warning) for warning in warnings]

# # Create an HTML file -- Format #1
# with open("warnings.html", "w") as f:
#     f.write("<html><body><ul>")

#     for warning in warnings:
#         # Search for the first occurrence of text within square brackets
#         match = re.search(r"\[.*?\]", warning)
#         if match:
#             # Extract the text within square brackets and bold it
#             bold_text = "<strong>" + match.group() + "</strong>"
#             # Replace the matched text with the bold version
#             warning = warning.replace(match.group(), bold_text)

#         f.write("<li>" + warning + "</li>")

#     f.write("</ul></body></html>")


# Helper function to convert non-string elements to string and strip ANSI escape codes from a warning message
def strip_ansi_escape_codes(warning):
    """Converts non-string elements to string and strips ANSI escape codes from a warning message."""
    if not isinstance(warning, str):
        warning = str(warning)
    return re.sub(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", "", warning)

# Helper function to apply bold formatting
def apply_bold(text):
    return "<strong>" + text + "</strong>"

# Helper function to wrap long lines to fit within 80 characters
def wrap_lines(text, width=80):
    lines = text.splitlines()
    wrapped_lines = []
    for line in lines:
        wrapped_line = textwrap.fill(line.strip(), width=width, initial_indent="  ", subsequent_indent="  ")
        wrapped_lines.append(wrapped_line)
    return "\n".join(wrapped_lines)

# Create an HTML file
with open("warnings.html", "w") as f:
    f.write("<html><body><pre>")

    # Warnings summary
    f.write(apply_bold("Warnings:\n"))
    f.write(f"    TOTAL: {len(warnings)} warning(s)\n")
    f.write(f"    {apply_bold('Priority 1')}: {len(priority_1_warnings)} warning(s)\n")
    f.write(f"    {apply_bold('Priority 2')}: {len(priority_2_warnings)} warning(s)\n\n")

    # Priority 1 warnings
    f.write(apply_bold("Priority 1 - heavy impact expected:\n"))
    for warning in priority_1_warnings:
        warning = strip_ansi_escape_codes(warning)
        indented_warning = wrap_lines(warning)
        f.write(f"{apply_bold('*')} {indented_warning}\n")
    f.write("\n")

    # Priority 2 warnings
    f.write(apply_bold("Priority 2 - usage allowed, limited human intelligibility:\n"))
    for warning in priority_2_warnings:
        warning = strip_ansi_escape_codes(warning)
        indented_warning = wrap_lines(warning)
        f.write(f"{apply_bold('*')} {indented_warning}\n")
    f.write("\n")

    f.write("</pre></body></html>")



# generate report for each warning type above
# duplicate_quality_warnings_report = dq.report(warnings=duplicate_quality_warnings)
# priority_1_warnings_report = dq.report(warnings=priority_1_warnings)
# priority_2_warnings_report = dq.report(warnings=priority_2_warnings)
# priority_3_warnings_report = dq.report(warnings=priority_3_warnings)

# Print Reports
# print(duplicate_quality_warnings_report)
# print(priority_1_warnings_report)

########################################################################################################################################################################

# # Check the results
# results = dq.get_results()

# # Save Results
# dq.save_results('guerry_histdata_results.csv')


