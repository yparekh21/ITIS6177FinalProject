from flask import Flask, render_template, request, jsonify
from azure.ai.textanalytics import ExtractiveSummaryAction, TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

# Azure Text Analytics configuration
key = "dc18f5e27339479db330dcfd68312d07"
endpoint = "https://finalprojectyash.cognitiveservices.azure.com"
credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    documents = data.get('documents', [])

    results = []
    for doc in documents:
        document = [doc['text']]
        poller = text_analytics_client.begin_analyze_actions(
            document,
            actions=[ExtractiveSummaryAction(max_sentence_count=4)],
        )

        document_results = poller.result()
        for result in document_results:
            extract_summary_result = result[0]  # first document, first result
            if extract_summary_result.is_error:
                return jsonify({'error': f"Error with code '{extract_summary_result.code}' and message '{extract_summary_result.message}'"})
            else:
                summary = " ".join([sentence.text for sentence in extract_summary_result.sentences])
                results.append({'id': doc['id'], 'summary': summary})

    return jsonify({'results': results})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
