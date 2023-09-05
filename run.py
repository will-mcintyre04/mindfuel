from app import create_app

# Create Flask app instance using factory function
app = create_app('production')

if __name__ == '__main__':
    app.run()