pipeline {
    agent any
    environment {
        SNOWSQL_PATH = '"C:\\Program Files\\Snowflake SnowSQL\\snowsql.exe"'  // Path to SnowSQL executable
        SNOWSQL_CONNECTION = 'demo'  // Connection name from SnowSQL configuration
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/snowflake-ci-cd-demo1.git'  // Replace with your Git repository URL
            }
        }
        stage('Test Files') {
            steps {
                script {
                    def testFiles = [
                        'tests/test_create_table.sql',
                        'tests/test_insert_data.py',
                        'tests/test_notebooks.py'
                    ]
                    for (testFile in testFiles) {
                        echo "Running test: ${testFile}"
                        if (testFile.endsWith('.sql')) {
                            bat """
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake-ci-cd-demo/${testFile}' @PROD_NOTEBOOK_STAGE;"
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "RUN 'file://@PROD_NOTEBOOK_STAGE/${testFile}';"
                            """
                        } else if (testFile.endsWith('.py')) {
                            bat "python ${testFile}"
                        }
                    }
                }
            }
        }
        stage('Update Files to Snowflake Stage') {
            steps {
                script {
                    def files = [
                        'sql/create_table.sql',
                        'scripts/process_data.py',
                        'notebooks/analysis_notebook.ipynb'
                    ]
                    for (file in files) {
                        bat """
                            ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "PUT 'file://C:/ProgramData/Jenkins/.jenkins/workspace/snowflake-ci-cd-demo/${file.replace('\\', '/')}' @PROD_NOTEBOOK_STAGE;"
                        """
                    }
                }
            }
        }
        stage('Run SQL and Python Files') {
            steps {
                script {
                    def filesToRun = [
                        'sql/create_table.sql',
                        'scripts/process_data.py'
                    ]
                    for (file in filesToRun) {
                        if (file.endsWith('.sql')) {
                            bat """
                                ${env.SNOWSQL_PATH} -c ${env.SNOWSQL_CONNECTION} -q "RUN 'file://@PROD_NOTEBOOK_STAGE/${file}';"
                            """
                        } else if (file.endsWith('.py')) {
                            bat "python ${file}"
                        }
                    }
                }
            }
        }
    }
    post {
        success {
            mail to: 'team@example.com',
                 subject: 'Pipeline Success: Snowflake CI/CD Demo',
                 body: 'All stages completed successfully. Files have been uploaded and executed in Snowflake.'
        }
        failure {
            mail to: 'team@example.com',
                 subject: 'Pipeline Failure: Snowflake CI/CD Demo',
                 body: 'One or more stages failed. Please check the Jenkins logs for more details.'
        }
    }
}
