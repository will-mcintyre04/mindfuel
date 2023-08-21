from app import create_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app instance using factory function
app = create_app('development')

if __name__ == '__main__':
    app.run()