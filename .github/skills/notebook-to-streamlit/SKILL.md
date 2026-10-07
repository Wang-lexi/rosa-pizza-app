---
name: notebook-to-streamlit
description: Convert the completed Jupyter Notebook logic for MMGMT 722 Assignment 1, Part 3, into a beginner-friendly Streamlit app when the user requests the conversion.
---

# Notebook to Streamlit

Use the completed notebook as the source of truth for the app's calculations.

- Reuse the notebook's logic, especially the `best_promise()` function. Preserve its decision rules and calculations when connecting it to Streamlit inputs.
- Keep the Python code beginner-friendly, with clear variable names, simple functions, and straightforward control flow.
- Avoid unnecessary advanced Python, abstractions, or complex patterns.
- Keep `delivery_times(..., seed=1)` so results are reproducible.
- Allow the user to select a zone and a time block using the options supported by the notebook.
- Allow the user to set the range of promise times to evaluate.
- Allow the user to adjust refund cost, churn per late order, and profit margin. Preserve the notebook's units and interpretation of these values.
- Provide a button that runs the recommendation using the selected inputs and displays the recommended promise returned by the notebook's logic.

Create the app only when the user requests implementation; creating this skill alone does not authorize creating `app.py` or other app files.
