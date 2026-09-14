# Taste Oracle

A helpful restaurant recommendation assistant.

## How to run the project locally

### 1. Clone this repository

`git clone https://github.com/tem-ctrl/taste-oracle.git`

### 2. Create and activate virtual environment running Python3.11

```sh
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```sh
pip install -r requirements.txt
```

### 3. Create a watsonx project and fill in environment variables

1. Signup/Signin to IBM watsonx AI account via [https://dataplatform.cloud.ibm.com/login?context=wx](https://dataplatform.cloud.ibm.com/login?context=wx)
2. Create a project
3. Create an API key for the project
4. Fill in environement variable: `WATSONX_PROJECT_ID`, `WATSONX_API_KEY` and `WATSONX_URL`
