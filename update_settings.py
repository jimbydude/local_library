import os
from datetime import datetime
import pytz

def update_settings(project_dir):
    """
    Updates the settings.py file of a Django project to include the current TIME_ZONE.

    Args:
        project_dir (str): The path to the Django project directory (where settings.py is located).
    """
    settings_file = os.path.join(project_dir, "settings.py")

    if not os.path.exists(settings_file):
        print(f"Error: settings.py not found in {project_dir}")
        return

    # Get the current timezone
    current_time_zone = datetime.now(pytz.timezone('UTC')).astimezone().tzinfo.zone

    # Placeholder for additional settings
    additional_settings = """
# Placeholder for additional settings
# Example:
# LANGUAGE_CODE = 'en-us'
"""

    try:
        with open(settings_file, "r") as file:
            settings_content = file.readlines()

        # Update TIME_ZONE and add placeholders
        with open(settings_file, "w") as file:
            for line in settings_content:
                if line.strip().startswith("TIME_ZONE"):
                    file.write(f"TIME_ZONE = '{current_time_zone}'\n")
                else:
                    file.write(line)
            file.write("\n")
            file.write(additional_settings)

        print(f"Updated TIME_ZONE to '{current_time_zone}' in {settings_file}")
    except Exception as e:
        print(f"Error updating settings.py: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with the path to your Django project directory
    project_directory = "local_library"
    update_settings(project_directory)
