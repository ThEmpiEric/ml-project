import sys 
from src.logger import logging

def error_message_detail(message:str, message_detail:sys):
    """
    Extracts detailed error message including file name and line number."""
    exc_tb = message_detail.exc_info()[2] 
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error en el archivo [ {file_name} ] - linea numero {line_number} - error message: {str(message)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, message_detail:sys): 
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, message_detail=message_detail) 

    def __str__(self):
        return self.error_message
    
#Testing 
if __name__ == "__main__":
    try: 
        a = 1 / 0
    except Exception as e:
        logging.info("Division by zero error")
        raise CustomException(e,sys)