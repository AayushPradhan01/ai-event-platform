# Import FastAPI dependency tools
from fastapi import Depends, HTTPException, status

# Import OAuth2 handler (used for authentication)
from fastapi.security import OAuth2PasswordBearer

# Import JWT decoding tools
from jose import jwt, JWTError

# Import secret key and algorithm
from app.services.user_service import SECRET_KEY, ALGORITHM


# Define OAuth2 scheme
# This tells FastAPI how to extract token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


# Function to get current user from token
def get_current_user(token: str = Depends(oauth2_scheme)):
    print("\n🔐 Authenticating user using OAuth2...")

    try:
        # Decode JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Extract email from token
        email = payload.get("sub")

        # If email missing → invalid token
        if email is None:
            print("❌ Token missing user info")

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        print(f"✅ User authenticated: {email}")

        return email

    except JWTError:
        print("❌ Token invalid or expired")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )