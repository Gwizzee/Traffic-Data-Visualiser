# Traffic Data Visualiser
A Python web app that visualises website traffic data to identify peak hours.

Features:

*   Allows the user to enter a website URL.
*   Fetches website data and extracts website traffic information.
*   Displays a line chart of website traffic over a 24-hour period.
*   Identifies peak hours based on the traffic data.

Requirements:

*   Python 3.7 or higher
*   Flask
*   pandas
*   matplotlib
*   requests
*   beautifulsoup4

Installation:

1.  Clone the repository: `git clone https://github.com/your-username/traffic-analyser.git`
2.  Install the required packages: `pip install -r requirements.txt`

Usage:

1.  Run the app: `python app.py`
2.  Open your web browser and go to `http://127.0.0.1:5000/`
3.  Enter the URL of the website you want to analyze and click "Analyse".
4.  The app will attempt to fetch data from the website, extract traffic information and display a chart.

Notes:

*   Error Handling: The app includes error handling for network issues and data processing errors.
  
Contributing:

Contributions are welcome! Feel free to add features or pull requests.

License:

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3.0 - see the [LICENSE](LICENSE) file for details.
