class Recommendation:
    def get_clothing_advice(temperature, weather_condition):
        temp = temperature

        if temp > 25:
            return "👕 Легкая одежда: футболка, шорты, сандалии. Не забудьте солнцезащитные очки!"
        elif 18 <= temp <= 25:
            return "👚 Комфортная температура: футболка, джинсы, легкая куртка"
        elif 10 <= temp < 18:
            return "🧥 Прохладно: свитер, джинсы, ветровка. Возможно, понадобится зонт"
        elif 0 <= temp < 10:
            return "🧣 Холодно: теплая куртка, шапка, перчатки. Одевайтесь теплее!"
        else:
            return "🧤 Очень холодно: зимняя куртка, теплая обувь, шапка, шарф"


    def get_activity_advice(temperature, weather_condition, wind_speed):
        advice = []
        condition = weather_condition.lower()

        if "rain" in condition or "drizzle" in condition:
            advice.append("☔ Сегодня лучше остаться дома или взять зонт")
        elif "snow" in condition:
            advice.append("⛄ Отличный день для зимних прогулок и игр в снежки!")
        elif temperature > 20 and "clear" in condition:
            advice.append("🌞 Идеальная погода для пикника, велопрогулки или похода в парк")
        elif temperature > 25:
            advice.append("🏊 Жаркий день! Отличное время для купания или посещения бассейна")
        elif 15 <= temperature <= 22:
            advice.append("🚶 Комфортная температура для прогулок, бега или занятий спортом на улице")

        if wind_speed > 10:
            advice.append("💨 Сильный ветер! Будьте осторожны на открытых пространствах")

        if not advice:
            advice.append("📚 Хороший день для чтения книг или домашних дел")

        return advice


    def get_health_warnings(temperature, humidity, uv_index=None):
        warnings = []

        if temperature > 30:
            warnings.append("🥵 Осторожно! Высокая температура. Пейте больше воды")
        elif temperature < -10:
            warnings.append("🥶 Сильный мороз! Ограничьте время на улице")

        if humidity > 80:
            warnings.append("💨 Высокая влажность! Может быть душно, осторожнее астматикам")
        elif humidity < 30:
            warnings.append("🏜️ Низкая влажность! Используйте увлажняющий крем")

        if uv_index and uv_index > 6:
            warnings.append("⚠️ Высокий УФ-индекс! Используйте солнцезащитный крем")

        return warnings


    def get_all_recommendations(weather_data):
        temp = weather_data.get('main', {}).get('temp', 0)
        condition = weather_data.get('weather', [{}])[0].get('description', '')
        humidity = weather_data.get('main', {}).get('humidity', 0)
        wind_speed = weather_data.get('wind', {}).get('speed', 0)

        return {
            'clothing': Recommendation.get_clothing_advice(temp, condition),
            'activities': Recommendation.get_activity_advice(temp, condition, wind_speed),
            'warnings': Recommendation.get_health_warnings(temp, humidity)
        }