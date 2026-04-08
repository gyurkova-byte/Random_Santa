# Random Santa

**Description:**  
A console Python application for organizing Secret Santa gift assignments.

**Features:**
- Displays a list of available gifts
- Requests participant names from the user
- Randomly assigns givers and receivers, avoiding self-gifting
- Shows final results in a nice table using `rich` library

**Technologies Used:**
- Python
- rich (for console table visualization)

**Example Usage:**
```python
# Run the main script
python main.py
```

**Notes:**
- All user inputs are taken via the console
- Gift assignments are random but exclude self-gifting
