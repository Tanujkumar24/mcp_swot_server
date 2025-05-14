
# Google Search API Setup & UV MCP Environment Configuration

This guide walks you through setting up the Google Search API and configuring a project using the UV package installer and MCP tools.

---

## 🔍 Google Search API Creation Steps

### 1. Get Your Google API Key

**Step 1:** Go to [Google Cloud Console](https://console.cloud.google.com/)

**Step 2:** Create a New Project
- Click the dropdown near the top left → “New Project”
- Give it a name like `EcommerceSWOTProject` and click **Create**

**Step 3:** Enable Programmable Search API
- In your project, search for: `"Programmable Search Engine API"`
- Click it → then click **Enable**

**Step 4:** Generate API Key
- Go to: [API Credentials](https://console.cloud.google.com/apis/credentials)
- Click **+ Create Credentials** → **API Key**
- Copy the key (you’ll use this in your Python script as `GOOGLE_API_KEY`)

---

### 2. Get the Search Engine ID (CX)

**Step 1:** Go to [Programmable Search Engine](https://programmablesearchengine.google.com/about/)

**Step 2:** Click “Get Started” or “New Search Engine”
- Under **Sites to Search**, enter any relevant site
- Name your search engine
- Click **Create**

**Step 3:** Find Your CX ID
- Go to: [Search Engine Dashboard](https://programmablesearchengine.google.com/cse/)
- Click the name of your search engine
- Under **Search Engine ID**, copy the CX ID

---

## 🧪 UV Package Installer & Configuration

### UV Installation

- **Windows PowerShell Command:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- **Official UV Installation Guide (Mac/Linux):**  
[UV Docs](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)

---

### 🐍 Conda Environment Setup

```bash
conda create -n env_name python=3.10 -y
conda activate env_name
pip install -r requirements.txt
```

---

## 🚀 MCP Setup with UV

### Project Initialization (UV-managed):

```bash
uv init mcp-server-demo
cd mcp-server-demo
uv add "mcp[cli]"
```

### Alternatively (pip install):

```bash
pip install "mcp[cli]"
```

### Running MCP Tools:

To run the `mcp` command with UV:

```bash
uv run mcp
```

Install the server in Claude Desktop and run it:

[Download Claude](https://claude.ai/download)

```bash
mcp install main.py
```

Test it with MCP Inspector:

```bash
mcp dev main.py
```

**Alternate Inspector Command (used during recording):**

```bash
npx @modelcontextprotocol/inspector python main.py
```

---
