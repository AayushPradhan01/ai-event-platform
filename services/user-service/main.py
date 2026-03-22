# Import FastAPI class (used to create the application)
from fastapi import FastAPI

# Import router from user_routes file
from app.routes.user_routes import router as user_router

# Create FastAPI app instance
# This is the main application object
app = FastAPI()

# Include all routes from user_router into this app
# This connects our routes to the application
app.include_router(user_router)

# Define a simple root endpoint (homepage)
@app.get("/")
def root():
    # This function runs when user hits "/"
    print("📥 Root endpoint called")

    # Return simple JSON response
    return {"message": "User Service is running"}