import aiohttp
from config import WEATHER_API_KEY

async def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ua"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    temp = data["main"]["temp"]
                    desc = data["weather"][0]["description"]
                    return f"Погода у місті {city.capitalize()}:\nТемпература: {temp}°C\nОпис: {desc.capitalize()}"
                elif response.status == 404:
                    return "Місто не знайдено. Перевір правильність назви."
                else:
                    return "Помилка сервісу погоди. Спробуй пізніше."
    except Exception as e:
        return "Зовнішній сервіс погоди наразі недоступний. Перевір підключення до мережі."