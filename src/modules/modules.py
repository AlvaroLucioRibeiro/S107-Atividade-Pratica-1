import json

# Path to your JSON file
json_file_path = "data/dados.json"


def load_json_data(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: Data loaded from the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_professor_name(name):
    """
    Validate if the given professor name is valid and return it.

    Args:
        name (str): Name of the professor.

    Returns:
        str: The validated professor name.

    Raises:
        ValueError: If the name is not a valid string.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Invalid name: The name must be a non-empty string.")

    if any(char.isdigit() for char in name):
        raise ValueError("Invalid name: The name cannot contain numbers.")

    # Additional logic could be added here for further validation if needed
    return name


def process_professor_data(professor_data):
    """
    Process professor data, assign the building based on the room, and print the information.

    Args:
        professor_data (dict): A dictionary containing professor information.

    Raises:
        ValueError: If data is empty or period is not a string.
        TypeError: If 'predio' is not a list.
    """
    if not professor_data:
        raise ValueError("Professor data cannot be empty.")

    for professor, data in professor_data.items():
        if not isinstance(data["periodo"], str):
            raise ValueError(f"Invalid period: {data['periodo']}. Must be a string.")

        if not isinstance(data["predio"], list):
            raise TypeError(f"Invalid 'predio' type: {data['predio']}. Must be a list.")

        room = int(data["sala"])

        print(f"Professor: {data['nomeDoProfessor']}")
        print(f"Office Hours: {data['horarioDeAtendimento']}")
        print(f"Period: {data['periodo']}")
        print(f"Room: {room}")
        print(f"Available Buildings: {', '.join(data['predio'])}")
        print("-" * 40)


if __name__ == "__main__":
    # Load data from the JSON file and process professor information.
    professor_data = load_json_data(json_file_path)
    process_professor_data(professor_data)