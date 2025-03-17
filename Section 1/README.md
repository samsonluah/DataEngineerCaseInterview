### Section 1: Data Pipelines

### Airflow

For this section, I opted to use airflow as I have familiarity with it in my past 2 internships as well as school projects. To avoid the hassle of needing to install airflow locally, I ran the `DSAD_DE_Case_Interview_LuahJunYang_section_1.ipynb` notebook in Google Colab, using ngrok to access the Airflow Web UI.

The notebook contains the necessary code to install the packages, write the DAG to the /dags/ folder, initializing airflow db and starting the webserver and scheduler. You will also be able to access the Airflow Web UI using your own free ngrok authtoken after creating an account.

### DAG
#### Scheduling
For the scheduling of the DAG, I set it in the `default_args` of the DAG as `"10 1 * * * "` which implies 0110hrs every day, which would account for the new data files coming in at 1am everyday.

#### Data Processing
I defined a singular `process_data()` function that takes in the file location of the target input csv. Using pandas, the function performs the required data transformations as stated in the case interview file.

It drops the rows with empty name columns, and subsequently splits the column up into 2 new columns first_name and last_name.

Then it converts the price column to string to remove the prepended zeros, then converting them back to numeric type to check for and create the boolean above_100 column.

#### Airflow Tasks

Upon defining the function and the DAG object, I created 2 tasks using PythonOperator, one task instance for processing of each of the input CSV files.

![alt text](image.png)