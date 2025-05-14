
# 📊 SWOT Analysis MCP Tool

A Python-based tool for performing SWOT (Strengths, Weaknesses, Opportunities, and Threats) analysis using a Flask API, integrated with [FastMCP](https://www.npmjs.com/package/@modelcontextprotocol/inspector) to enable tool execution via MCP-compatible environments.

![SWOT Banner](images/swot_banner.png)

---

## 🔍 Overview

This project allows users to perform a structured SWOT analysis on a given product or entity via a RESTful API. The backend is powered by Flask, while `main.py` uses FastMCP to expose the tool to LLM agents. This can be especially useful for automated reasoning and market analysis workflows.

---

## 🚀 Features

- 🧠 AI-assisted SWOT analysis from user input
- 🌐 Flask-based API with `/analyze` endpoint
- 🔧 FastMCP integration for tool invocation in agent environments
- 🧪 Automatic testing and endpoint validation using Python subprocess
- 📤 Modular file structure for scalability and debugging

---

## 📂 Project Structure

```
.
├── app.py              # Flask application exposing the /analyze endpoint
├── mcp_swot.py         # Script to launch Flask app and test the endpoint
├── main.py             # FastMCP integration file to run the swot_analysis tool
├── images/             # Folder for screenshots and architecture images
└── README.md
```

---

## 📸 Screenshots

### 1. Swagger Endpoint Test  
![API Test](images/swagger_test.png)

### 2. Console Output  
![Console Logs](images/console_output.png)

---

## 🧰 Installation & Usage

### Step 1: Clone the Repo
```bash
git clone https://github.com/your-username/swot-analysis-mcp.git
cd swot-analysis-mcp
```

### Step 2: Setup Virtual Environment
```bash
conda create -n swot_env python=3.9
conda activate swot_env
pip install -r requirements.txt
```

### Step 3: Run the Tool with FastMCP
```bash
npx @modelcontextprotocol/inspector python main.py
```

---

## 📬 API Endpoint

- **POST** `/analyze`  
    ```json
    {
      "product_name": "redmi note10"
    }
    ```

    **Response**
    ```json
    {
      "strengths": [...],
      "weaknesses": [...],
      "opportunities": [...],
      "threats": [...]
    }
    ```

---

## ⚙️ Error Handling

If you encounter this error:
```
'charmap' codec can't encode character '\u20b9'
```
Add this to the top of your Python file:
```python
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

---

## ✍️ Author

Tanujkumar Mangalapally  
*Data Scientist | MLOps Engineer | AI Enthusiast*

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
