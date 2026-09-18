# Patient Narrative Text Collection

A Python web-scraping and text-processing prototype developed to collect patient narratives from online sources for potential downstream sentiment analysis.

## Project Overview

This project was created as an early proof of concept for exploring how publicly available patient narratives might be collected and prepared for sentiment analysis.

The broader idea was to investigate whether unstructured online discussions could provide useful insight into patient experiences and perspectives. The prototype focuses on non-Hodgkin lymphoma and uses a patient story published by the Leukemia & Lymphoma Society as its initial source.

The code currently represents the **data-collection and text-preparation stage** of that concept. It does not itself perform sentiment analysis.

## What the Script Does

The Python script:

* Sends an HTTP request to a specified web page using `requests`
* Parses the returned HTML using BeautifulSoup
* Identifies and extracts the main article text
* Separately extracts text from the page's comments section
* Removes blank entries and selected HTML/Unicode artifacts
* Combines individual paragraphs into continuous text
* Filters non-printable characters
* Saves the cleaned article and comment text to a local text file for potential further analysis

The resulting text was intended to provide input for a later natural-language-processing or sentiment-analysis workflow.

## Technologies Used

* **Python**
* **requests** — retrieving web content
* **BeautifulSoup** — parsing HTML and extracting text
* **Python string utilities** — basic text cleaning and character filtering

## Repository Contents

`nHLsentiment1.py`
Python script containing the web-scraping and text-cleaning workflow.

`README.md`
Project documentation.

`requirements.txt`
External Python packages required by the script.

Running the script also creates:

`nHLsentiment1.txt`
A text file containing the source URL followed by the cleaned article and comment text.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/EnragedSpark596/SentimentAnalysis.git
cd SentimentAnalysis
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python nHLsentiment1.py
```

If the source webpage remains available and its HTML structure is compatible with the original scraper, the script will create `nHLsentiment1.txt` in the project directory.

## Project Context

This is an earlier Python project and is preserved substantially in its original form as part of my development portfolio.

The project originated as a proof of concept for exploring how online patient narratives could potentially be gathered and analyzed to better understand patient experiences. The broader concept was relevant to work exploring how patient-generated information might provide useful insights for healthcare and pharmaceutical organizations.

The current code demonstrates the first part of that workflow: retrieving unstructured web content, identifying relevant sections of a page, cleaning the resulting text and preparing it for subsequent analysis.

The planned sentiment-analysis stage was not implemented in the version currently contained in this repository.

## Limitations

This is a prototype rather than a production web-scraping application.

In particular:

* The scraper was written for the HTML structure of a specific webpage at the time the project was developed.
* Changes to that webpage may cause the selectors used by the script to fail.
* The script does not currently include error handling for failed requests or changed page structures.
* It processes a single source rather than a collection of websites.
* It prepares text for analysis but does not itself perform sentiment classification or other NLP analysis.

These limitations reflect the exploratory nature and original scope of the project.

## Ethical Considerations

Patient narratives can contain sensitive personal information even when they are published publicly. Any extension of this prototype into a larger research or commercial system would need to consider privacy, source terms of use, appropriate data handling, consent and the limitations of drawing conclusions from self-selected online narratives.

## Author

**Ian Jones**

Former chemical and process safety engineer developing Python skills in data analysis, automation, machine learning and practical problem-solving.
