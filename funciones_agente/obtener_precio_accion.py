# Módulo para consultar precios de acciones en tiempo real usando yfinance
import yfinance as yf
from utils.sanitizar import sanitizar

# Diccionario para mapear nombres comunes de empresas a sus Tickers de bolsa correspondientes
COMPANY_TICKERS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "apple inc": "AAPL",
    "microsoft corp": "MSFT",
    "tesla motors": "TSLA"
}

def obtener_precio_accion(driver, user_input):
    """
    Busca y retorna el precio actual de una acción utilizando la librería yfinance.
    
    Argumentos:
        driver: Instancia de Selenium WebDriver (opcional).
        user_input: Input del usuario que contiene el nombre de la empresa.
    
    Retorna:
        El precio formateado como cadena o un mensaje explicativo si no se encuentra.
    """
    # Sanitizar el input para extraer únicamente el nombre de la empresa o el ticker
    company_name = sanitizar(user_input)
    
    # Buscar si el nombre está en nuestro mapeo interno de tickers
    ticker = COMPANY_TICKERS.get(company_name)
    
    # Si no está en el mapa, asumimos que el usuario pudo haber ingresado el Ticker directamente
    if not ticker:
        ticker = company_name.upper()

    try:
        # Inicializar el objeto Ticker de yfinance
        stock = yf.Ticker(ticker)

        #obtener info del ticker
        info = stock.info
        ticker_symbol = info.get("symbol", ticker)
        currency = info.get("currency", "N/A")
        
        # Obtener el historial del último día para extraer el precio de cierre más reciente
        data = stock.history(period="1d")
        
        if not data.empty:
            # Extraer el valor de la columna 'Close' de la última fila disponible
            price = data['Close'].iloc[-1]
            return (
                f"Ticker: {ticker_symbol}\n"
                f"Divisa: {currency}\n"
                f"Precio: {price:.2f}"
            )
        else:
            return "No se encontraron datos de cotización (puede que el símbolo sea incorrecto o esté deslistado)."
            
    except Exception as e:
        # Capturar errores de la API o problemas de red
        return f"Error al consultar el precio de la acción: {e}"
