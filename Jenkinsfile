pipeline {
    agent any
    parameters {
        choice(
            name: 'MODULE',
            choices: ['SQL', 'Python', 'Notebook', 'All'],
            description: 'Choose which module to execute'
        )
    }
    environment {
        SNOWSQL_PATH = '"C:\\Program Files\\Snowflake SnowSQL\\snowsql.exe"'  // Path to SnowSQL executable
        SNOWSQL_CONNECTION = 'demo'  // Connection name from SnowSQL configuration
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/manjunathbabur/snowflake-cicd-demo1.git'  // Replace with your Git repository URL
            }
        }
stage('Setup Environment') {
    steps {
        script {
            echo "Setting up Python environment..."
            bat """
                python -m pip install --upgrade pip setuptools wheel
                python -m pip install snowflake-connector-python
            """
        }
    }
}
stage('Install Snowflake Connector') {
    steps {
        script {
            echo "Installing precompiled Snowflake connector..."
            bat """
                pip install path\\to\\snowflake_connector_python-3.13.1-cp39-cp39-win_amd64.whl
            """
        }
    }
}


        stage('Run Selected Module') {
            steps {
                script {
                    if (params.MODULE == 'SQL' || params.MODULE == 'All') {
                        echo "Running SQL Module..."
                        def sqlFiles = [
                            'sql/create_table.sql',
                            'sql/insert_data.sql',
                            'sql/update_data.sql'
                        ]
                        for (file in sqlFiles) {
                            bat """
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake_demo1/${file.replace('\\', '/')}' @PROD_NOTEBOOK_STAGE;"
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "RUN 'file://@PROD_NOTEBOOK_STAGE/${file}';"
                            """
                        }
                    }

                    if (params.MODULE == 'Python' || params.MODULE == 'All') {
                        echo "Running Python Module..."
                        def pythonFiles = [
                            'scripts/process_data.py',
                            'scripts/generate_report.py'
                        ]
                        for (file in pythonFiles) {
                            bat """
                                python ${file}
                            """
                        }
                    }

                    if (params.MODULE == 'Notebook' || params.MODULE == 'All') {
                        echo "Running Notebook Module..."
                        def notebooks = [
                            'notebooks/analysis_notebook.ipynb',
                            'notebooks/summary_notebook.ipynb'
                        ]
                        for (notebook in notebooks) {
                            bat """
                                jupyter nbconvert --execute --to notebook --inplace ${notebook}
                            """
                        }
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo "Running Tests for Selected Module..."
                script {
                    if (params.MODULE == 'SQL' || params.MODULE == 'All') {
                        echo "Running SQL tests..."
                        bat """
                            sqlcmd -i tests/test_create_table.sql
                        
                        """
                    }

                    if (params.MODULE == 'Python' || params.MODULE == 'All') {
                        echo "Running Python tests..."
                        bat """
                            pytest tests/test_notebooks.py
                        """
                    }

                    if (params.MODULE == 'Notebook' || params.MODULE == 'All') {
                        echo "Running Notebook tests..."
                        bat """
                            jupyter nbconvert --execute --to notebook --inplace tests/test_notebooks.ipynb
                        """
                    }
                }
            }
        }
        stage('Debug') {
            steps {
                echo "Running Debugging for Selected Module..."
                script {
                    if (params.MODULE == 'Python' || params.MODULE == 'All') {
                        echo "Starting Python Debugger..."
                        bat """
                            python -m pdb scripts/process_data.py
                        """
                    }

                    if (params.MODULE == 'SQL' || params.MODULE == 'All') {
                        echo "Debugging SQL Scripts..."
                        bat """
                            ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "SELECT * FROM <your_debug_table>;"
                        """
                    }
                }
            }
        }
        stage('Update') {
            steps {
                echo "Running Update Operations for Selected Module..."
                script {
                    if (params.MODULE == 'SQL' || params.MODULE == 'All') {
                        echo "Updating SQL scripts..."
                        def sqlFiles = [
                            'sql/create_table.sql',
                            'sql/insert_data.sql',
                            'sql/update_data.sql'
                        ]
                        for (file in sqlFiles) {
                            bat """
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake_demo1/${file.replace('\\', '/')}' @PROD_NOTEBOOK_STAGE;"
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "RUN 'file://@PROD_NOTEBOOK_STAGE/${file}';"
                            """
                        }
                    }

                    if (params.MODULE == 'Python' || params.MODULE == 'All') {
                        echo "Updating Python scripts..."
                        bat """
                            python scripts/process_data.py
                            python scripts/generate_report.py
                        """
                    }

                    if (params.MODULE == 'Notebook' || params.MODULE == 'All') {
                        echo "Updating Notebooks..."
                        def notebooks = [
                            'notebooks/analysis_notebook.ipynb',
                            'notebooks/summary_notebook.ipynb'
                        ]
                        for (notebook in notebooks) {
                            bat """
                                jupyter nbconvert --execute --to notebook --inplace ${notebook}
                            """
                        }
                    }
                }
            }
        }
        stage('Clear') {
            steps {
                echo "Clearing Temporary Files and Cleanup..."
                script {
                    bat """
                        echo "Clearing workspace..."
                        del /q /s C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\snowflake_demo1\\*
                    """
                }
            }
        }
    }
    post {
        success {
            echo "Pipeline completed successfully for module: ${params.MODULE}."
        }
        failure {
            echo "Pipeline failed for module: ${params.MODULE}. Please check the logs."
        }
    }
}
