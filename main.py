"""
Coord Convertr
Author: Akshat Chhajer (akshat.c2k@gmail.com)
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8888, reload=True)
