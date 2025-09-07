# Project: RBC Stock News Sentiment Analyzer

## Project Goal

The primary objective of this project is to determine if a correlation exists between the sentiment of news headlines concerning the Royal Bank of Canada and the performance of its stock price. This project serves as a practical, step-by-step introduction to the data analysis workflow.

## Chosen Company

- **Company:** Royal Bank of Canada
- **Stock Ticker:** RY.TO (Toronto Stock Exchange)

## Core Technologies

- **Language:** Python 3
- **Environment:** VS Code with a `venv` virtual environment.
- **Key Libraries:**
  - `requests` & `BeautifulSoup4` (for web scraping)
  - `yfinance` (for stock data)
  - `pandas` (for data manipulation)
  - `vaderSentiment` (for sentiment analysis)
  - `matplotlib` & `seaborn` (for visualization)

## User Goals

The primary goal of this project is to successfully navigate the entire lifecycle of a data science project. This will serve as a hands-on learning experience to build a mental map of the workflow, from raw idea to final visualization, and overcome the initial paralysis of starting a new data project.

## Project Approach: Apprentice Mode

**Goal:** To provide a structured, hands-on learning experience by building the project step-by-step.

- **Gemini's Role (Instructor/Project Lead):** Provide clear, single-step instructions, explain the purpose of each step, and supply code in small, digestible snippets.
- **User's Role (Apprentice/Developer):** Execute the provided commands, write the code as instructed, and confirm when each step is completed.

### Workflow

1. Gemini provides one instruction (a command or code snippet) and an explanation.
2. The user performs the action.
3. The user confirms completion.
4. Gemini provides the next instruction.

## Tooling Strategy

To ensure a smooth and efficient workflow, we will use the following tools for specific purposes:

### 1. Basic Memory

- **Purpose**: To maintain session-to-session continuity within the active `vault` memory project.
- **Structure**: To keep our work organized, we will create a new folder named `rbc-stock-news-sentiment-analyzer/` inside the `vault` project. All session notes and summaries for this project will be stored there.

### 2. Context7

- **Purpose**: To ensure the use of up-to-date libraries and to follow current conventions and best practices in our code.

### 3. mcp-server-time

- **Purpose**: To get accurate, localized timestamps for all notes and logs, ensuring proper chronological order.

### 4. Custom Commands

To streamline project management, we will use the following custom commands:

- **/update-memory**: Analyzes current progress by reviewing `GEMINI.md` and `analyzer.py`, then saves a summary note to the `rbc-stock-news-sentiment-analyzer/` memory folder to ensure session continuity.
- **/update-project-docs**: Audits all project documentation and source code (`GEMINI.md`, `analyzer.py`) to ensure they are synchronized and reflect the current project state.

## Project Documentation

This project uses the following documents to guide its development.

- `GEMINI.md`: The main project dashboard, tracking our progress and current tasks.
- `docs/TECHNICAL_SPEC.md`: The technical blueprint, outlining the script's architecture and data flow.
- `docs/DECISIONS.md`: A log of key technical choices and the reasoning behind them.

## Session Workflow

To ensure continuity, we will follow a strict session management protocol.

- **Ending a Session:** The user will run `/update-memory` to save a summary of the day's work. For major milestones, `/update-project-docs` will be used to update all project documentation.
- **Starting a Session:** The user will run `/resume-work` to bring Gemini up to speed on the project's current state and receive the next instruction.

---

## Phase 1: Environment Setup

**Goal:** To prepare the local development environment, install all necessary tools, and create the initial project script file.

**Status:** NOT STARTED
***Note: Instructions for each task will be provided one at a time.***

### Task List

- [ ] **Task 1: Setup Local Environment**
  - [ ] 1.1: Create a project folder on your local machine.
  - [ ] 1.2: Create a Python virtual environment named `venv` inside the project folder.
  - [ ] 1.3: Activate the virtual environment.

- [ ] **Task 2: Install Dependencies**
  - [ ] 2.1: Install all required Python libraries with a single `pip` command.

- [ ] **Task 3: Create Project Script**
  - [ ] 3.1: Create a main Python script file named `analyzer.py`.

---

## Phase 2: Data Extraction

**Goal:** To gather historical stock prices and relevant news headlines.

**Status:** NOT STARTED
***Note: Instructions for each task will be provided one at a time.***

### Task List

- [ ] **Task 1: Download Stock Data**
  - [ ] 1.1: Write a script using `yfinance` to download daily stock prices for RY.TO for a defined period (e.g., last year).
- [ ] **Task 2: Scrape News Headlines**
  - [ ] 2.1: Identify a suitable news source for scraping (e.g., Google News, Globe and Mail).
  - [ ] 2.2: Write a script using `requests` and `BeautifulSoup4` to collect headlines related to RBC for the same period.

---

## Phase 3: Sentiment Analysis & Transformation

**Goal:** To analyze the sentiment of each headline and transform the data for merging.

**Status:** NOT STARTED
***Note: Instructions for each task will be provided one at a time.***

### Task List

- [ ] **Task 1: Analyze Sentiment**
  - [ ] 1.1: For each collected headline, calculate a compound sentiment score using `vaderSentiment`.
- [ ] **Task 2: Aggregate Scores**
  - [ ] 2.1: Use `pandas` to group the sentiment scores by date.
  - [ ] 2.2: Calculate an average daily sentiment score.

---

## Phase 4: Loading & Combining Data

**Goal:** To merge the stock price and sentiment score datasets into a single master dataset.

**Status:** NOT STARTED
***Note: Instructions for each task will be provided one at a time.***

### Task List

- [ ] **Task 1: Load Datasets**
  - [ ] 1.1: Load the daily stock prices into a pandas DataFrame.
  - [ ] 1.2: Load the daily average sentiment scores into a pandas DataFrame.
- [ ] **Task 2: Merge Datasets**
  - [ ] 2.1: Merge the two DataFrames on the date column to create a unified dataset.

---

## Phase 5: Visualization & Analysis

**Goal:** To visualize the combined data to identify potential correlations between news sentiment and stock price.

**Status:** NOT STARTED
***Note: Instructions for each task will be provided one at a time.***

### Task List

- [ ] **Task 1: Create Visualization**
  - [ ] 1.1: Use `matplotlib` or `seaborn` to create a dual-axis line chart.
  - [ ] 1.2: Plot the stock price on the left Y-axis and the average sentiment score on the right Y-axis.
  - [ ] 1.3: Use the date for the shared X-axis.
- [ ] **Task 2: Analyze Results**
  - [ ] 2.1: Visually inspect the chart for correlations between sentiment shifts and stock price movements.

---

## Current Task for Apprentice

The current objective is to **verify the sentiment analysis script**.

**Instruction:** Run the `analyzer.py` script from your terminal.

'''bash
python3 analyzer.py
'''

You should see each headline followed by its sentiment scores (negative, neutral, positive, compound). Let me know the result.
