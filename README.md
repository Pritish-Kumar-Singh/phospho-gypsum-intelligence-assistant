# Phospho-Gypsum Intelligence Assistant
### AI-Powered Knowledge & Recommendation System using RAG

The **Phospho-Gypsum Intelligence Assistant** is a domain-specific Generative AI platform designed to help engineers, researchers, sustainability teams, and industrial decision-makers at IFFCO PARADEEP analyze phospho-gypsum utilization opportunities. 

The system leverages **Retrieval-Augmented Generation (RAG)** to ingest technical reports, research papers, government guidelines, and internal plant documents, delivering evidence-based answers and structured recommendations alongside source references in seconds.

---

## 📌 Business Problem: Why Phospho-Gypsum is a Major Issue for IFFCO Paradeep

### What is Happening?
IFFCO Paradeep operates one of India's largest phosphatic fertilizer manufacturing facilities, producing phosphoric acid and DAP fertilizer at a massive scale. During phosphoric acid production, a persistent by-product called **phospho-gypsum (PG)** is generated. Currently, the generation rate vastly outpaces utilization demand.

### Why is this a Serious Business Problem?

1. **Massive Annual Generation** Historical data indicates the Paradeep plant generates approximately **40 lakh metric tonnes (4 million tonnes)** of phospho-gypsum per year.
   $$\text{Fertilizer Production} \longrightarrow \text{Phosphoric Acid} \longrightarrow \text{Phospho-Gypsum Generation} \longrightarrow \text{Growing Stockpiles}$$

2. **Land Consumption & Opportunity Cost** Long-term storage requires dedicated stacking facilities spanning hundreds of acres. This results in:
   * Occupation of valuable industrial land.
   * Restrained capacity for future plant expansion.
   * Escalating infrastructure construction and maintenance costs.

3. **Environmental Compliance & Liabilities** Phospho-gypsum stacks demand strict technical oversight, including leachate management, complex liner systems, continuous water monitoring, and groundwater protection measures. Improper handling risks regulatory non-compliance, heavy monitoring costs, and environmental liability.

4. **Compounding Waste Management Overhead** Treating PG purely as waste creates a costly operational cycle:
   $$\text{Generation} \longrightarrow \text{Transportation} \longrightarrow \text{Stacking} \longrightarrow \text{Monitoring} \longrightarrow \text{Maintenance}$$

5. **Missed Revenue Opportunities** Extensive research shows phospho-gypsum has high utility in cement manufacturing, road construction, agricultural soil conditioning, gypsum board production, and land reclamation. The operational challenge is not whether uses exist, but establishing a systematic pipeline to **Find $\rightarrow$ Evaluate $\rightarrow$ Match $\rightarrow$ Recommend $\rightarrow$ Scale** the right opportunities.

---

## 💡 Why This Project Matters

Most critical information is currently scattered across unstructured formats:
* Academic Research Papers & Technical Journals
* Government & CPCB (Central Pollution Control Board) Guidelines
* Internal IFFCO Operational & Planning Reports
* Industry Sustainability Studies

Engineers and decision-makers cannot manually parse thousands of document pages during active operations. This project collapses that workflow:

| Traditional Workflow | RAG-Enabled Workflow |
| :--- | :--- |
| ❌ Search through multiple scattered PDFs |  Query the unified system instantly |
| ❌ Manually read 200+ pages of dense jargon | ⚡ Receive structured, evidence-backed answers |
| ❌ Spend days cross-referencing findings |  Get concrete recommendations with exact source citations |

---

## 🚀 Getting Started

Follow these steps to run the Phospho-Gypsum Intelligence Assistant on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/phospho-gypsum-intelligence-assistant.git

cd phospho-gypsum-intelligence-assistant
```

---

### 2️⃣ Create a Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Gemini API Key

Create a `.env` file in the project root directory.

```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

You can generate a Gemini API key from Google AI Studio.

---

### 5️⃣ Add Knowledge Base Documents

Place all technical PDFs inside:

```text
data/raw_documents/
```

Examples:

* IFFCO Reports
* Research Papers
* Government Guidelines
* Sustainability Studies
* Technical Documentation

---

### 6️⃣ Build the Vector Database

Run the ingestion pipeline:

```bash
python src/ingestion/ingest.py
```

This process will:

```text
Load PDFs
     ↓
Extract Text
     ↓
Split into Chunks
     ↓
Generate Embeddings
     ↓
Create FAISS Vector Index
```

After successful execution, the following files will be generated:

```text
data/vector_store/
├── index.faiss
└── index.pkl
```

---

### 7️⃣ Launch the Application

Start the Streamlit application:

```bash
streamlit run src/ui/app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📖 Example Queries

Try asking:

```text
Can phospho-gypsum replace natural gypsum in cement manufacturing?
```

```text
How can IFFCO utilize phospho-gypsum more effectively?
```

```text
What are the environmental risks associated with phospho-gypsum stockpiles?
```

```text
Can phospho-gypsum be used in road construction?
```

```text
What industries should purchase phospho-gypsum from IFFCO?
```

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | `Streamlit` | Interactive, clean web dashboard interface |
| **Backend** | `Python` | Core logic and pipeline orchestration |
| **LLM** | `Gemini 2.5 Flash` | Advanced reasoning and contextual text generation |
| **GenAI Framework** | `LangChain` | RAG architecture workflow orchestration |
| **Vector Database** | `FAISS` | High-performance local vector similarity search |
| **Embedding Model** | `Sentence Transformers` | `all-MiniLM-L6-v2` for generating semantic text vectors |
| **Document Loader**| `PyPDFLoader` | Extracts text data cleanly from structured PDFs |
| **Text Chunking** | `SemanticChunker` | Smart contextual splitting of technical text blocks |
| **Environment Mgmt**| `python-dotenv` | Secure handling of API credentials via `.env` |

---

## Author

* Pritish Kumar Singh
* Electrical Engineering | Data Science | Machine Learning

##  Connect With Me

* Email: [pritishsinghprf@gmail.com](mailto:pritishsinghprf@gmail.com)
* LinkedIn: www.linkedin.com/in/pritish1298