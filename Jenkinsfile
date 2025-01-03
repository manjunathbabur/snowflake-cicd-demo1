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
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake-cicd-demo1/${file.replace('\\', '/')}' @PROD_NOTEBOOK_STAGE;"
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
