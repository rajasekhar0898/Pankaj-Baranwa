from flask import Flask, jsonify
from api_fetch import fetch_data_from_api
from citation_identifier import identify_citations

app = Flask(__name__)

@app.route('/')
def get_citations():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data_from_api(api_url)
    output = {"citations": []}

    if data:
        response_objects = data.get("response_objects", [])
        citations = identify_citations(response_objects)
        for citation in citations:
            citation_info = {"source": citation['context'], "link": citation.get('link', 'N/A')}
            output["citations"].append(citation_info)
    
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
