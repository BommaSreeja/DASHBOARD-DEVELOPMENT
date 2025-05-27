# DASHBOARD-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: BOMMA SREEJA

*INTERN ID*: CT04DL352

*DOMAIN*: DATA ANALYSIS

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

This Python program is a web-based interactive data visualization dashboard for crop recommendation analysis, built using the Dash framework developed by Plotly. Dash combines the capabilities of Flask, Plotly, and React.js to create data-driven web applications entirely in Python, making it ideal for data analysts and scientists who want to build dashboards without needing extensive front-end development knowledge.
The application begins by importing essential libraries. Pandas is used to load and manipulate the crop dataset, while Plotly is employed for generating rich interactive visualizations. The Dash library provides the framework for building and structuring the web interface. Additionally, modules like webbrowser and threading are used to automatically launch the dashboard in a browser when the script is executed.
The dataset, loaded from a local CSV file, contains agricultural features such as nitrogen (N), phosphorus (P), potassium (K), temperature, humidity, pH, rainfall, and the target label, which is the recommended crop. This data forms the basis for the visual insights generated in the dashboard.
The dashboard layout includes a header title, a dropdown selector for choosing a specific crop, and two visual output sections:
A correlation heatmap
A scatter plot of rainfall vs temperature
The dropdown is dynamically populated with all unique crop names found in the dataset, allowing users to interactively select any crop and view its corresponding analytics. When a crop is selected, Dash callbacks are triggered to update the visualizations in real time.
The first visualization, a correlation heatmap, displays the relationship between various environmental and nutrient features for the selected crop. The program uses Plotly Graph Objects to generate a heatmap using the correlation matrix derived from the numeric columns (excluding the crop label). This allows users to understand how closely different parameters (e.g., temperature and humidity) are associated, helping researchers and agronomists identify interdependencies.
The second visualization is a scatter plot created using Plotly Express, which shows the relationship between rainfall and temperature for the selected crop. It provides a visual sense of the range and clustering of environmental conditions in which the crop is typically recommended or observed. These insights can support better agricultural planning and region-specific crop suitability analysis.
One notable feature of the program is the use of the webbrowser and threading libraries to automatically open the local dashboard URL (http://127.0.0.1:8050/) in the user's default browser when the script runs. This enhances usability, making the dashboard easily accessible without requiring manual navigation.
This dashboard is highly suitable for applications in precision agriculture, academic research, and AgriTech solutions, where stakeholders need to interpret agricultural data interactively. It is designed to run locally in a standard Python environment with the necessary libraries installed (Dash, Pandas, Plotly). The tool empowers users to explore complex relationships within agricultural datasets through an intuitive and interactive interface, helping them make data-informed decisions about crop selection and environmental suitability.

*OUTPUT*:

![Image](https://github.com/user-attachments/assets/afb597b9-0ec6-42b0-b13f-2eb8f7372446)

![Image](https://github.com/user-attachments/assets/8aee4b41-1829-49af-aa6c-9877d2a0153d)
