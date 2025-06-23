# backend service
cd backend
# setting up virtual env
python3 -m venv support
source ./support/bin/activate

# Intall packages
python3 -m pip install -r requirements.txt

# Check .env is setup
GEMINI_API_KEY

# Run the server
uvicorn main:app --reload

# Swagger doc
