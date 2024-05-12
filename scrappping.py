import requests
from bs4 import BeautifulSoup

def scrape_website(url, output_file):
    # Set a custom User-Agent header to mimic a web browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        # Send a GET request to the URL with custom headers
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the response
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the div with class "entry-content"
            entry_content_div = soup.find('div', class_='entry-content')
            
            # Find all <p> tags within the "entry-content" div
            paragraphs = entry_content_div.find_all('p')
            
            # Open the output file in write mode
            with open(output_file, 'w') as f:
                # Extract and write the text from each <p> tag that meets the criteria
                for p in paragraphs:
                    text = p.get_text().strip()
                    if text.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.')) or text.startswith(('a)', 'b)', 'c)', 'd)')):
                        f.write(text + '\n')
            
            # Find the div with class "collapseomatic_content"
            collapseomatic_content_div = soup.find('div', class_='collapseomatic_content')
            
            # If the "collapseomatic_content" div exists, write its text to the output file
            if collapseomatic_content_div:
                f.write(collapseomatic_content_div.get_text() + '\n')
                
            print("Data scraped successfully and saved to", output_file)
        else:
            print(f"Failed to retrieve data from the website. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# URL of the website you want to scrape
url = 'https://www.sanfoundry.com/operating-system-questions-answers/'

# Output file path
output_file = 'scraped_data.txt'

# Call the function with the URL and output file path
scrape_website(url, output_file)
