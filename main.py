/* HERE IS THE MAIN FUNCTION */
    
from database import create_db
from gui import main as start_gui

if __name__ == "__main__":
    create_db()  
    start_gui() 
