from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def analyze_traffic_data(website_url):
    """
    Fetches and analyzes website traffic data from the provided URL.

    Args:
        website_url: The URL of the website to analyze.

    Returns:
        A base64-encoded image of the traffic pattern plot, or an error message.
    """

    try:
        # Fetch website data (replace with actual data fetching logic)
        response = requests.get(website_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract traffic data (replace with your actual extraction logic)
        # This is a placeholder; you'll need to adapt this to your specific needs
        # and the structure of the website you're fetching data from.
        hours = []
        visitors = []
        for i in range(24):
            hour_data = soup.find(id=f"hour-{i}") # Example ID, adjust as needed
            if hour_data:
                hours.append(i)
                visitors.append(int(hour_data.text))

        # Create DataFrame if data was found
        if hours and visitors:
            df = pd.DataFrame({'Hour': hours, 'Visitors': visitors})

            # Create the plot
            plt.figure(figsize=(10, 6))
            plt.plot(df['Hour'], df['Visitors'])
            plt.xlabel('Hour of the Day')
            plt.ylabel('Number of Visitors')
            plt.title('Website Traffic Pattern')
            plt.grid(True)

            # Save the plot to a BytesIO object
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)

            # Encode the image in base64
            plot_url = base64.b64encode(img.getvalue()).decode()

            return plot_url
        else:
            return "No traffic data found on the website."

    except requests.exceptions.RequestException as e:
        return f"Error fetching website data: {e}"
    except Exception as e:
        return f"An error occurred: {e}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        website_url = request.form['website_url']
        plot_url = analyze_traffic_data(website_url)
        return render_template('traffic_report.html', plot_url=plot_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
