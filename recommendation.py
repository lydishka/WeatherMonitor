def get_clothing_advice(temperature, condition, wind_speed, humidity):
    condition = condition.lower()
    base_advice = ""
    items = []
    additional_recommendations = []
    if temperature > 28:
        base_advice = "ЖАРКО: Легкая светлая одежда из натуральных тканей"
        items = ["хлопковая футболка или майка", "шорты или легкие брюки", "открытая обувь"]
        if humidity > 70:
            additional_recommendations.append("Выбирайте влагопроводящие ткани для лучшей вентиляции")
    elif 23 <= temperature <= 28:
        base_advice = "ТЕПЛО: Легкая комфортная одежда"
        items = ["футболка или блузка", "джинсы или брюки", "легкая обувь"]
        if wind_speed > 5:
            items.append("ветровка на случай усиления ветра")
    elif 17 <= temperature < 23:
        base_advice = "КОМФОРТНО: Многослойная одежда"
        items = ["лонгслив или рубашка", "джинсы", "легкая куртка или кардиган"]
        if "дождь" in condition:
            items.append("дождевик или зонт")
    elif 10 <= temperature < 17:
        base_advice = "ПРОХЛАДНО: Теплая одежда"
        items = ["свитер или толстовка", "утепленные брюки", "куртка", "закрытая обувь"]
        if wind_speed > 7:
            additional_recommendations.append("Ветрозащитная куртка обязательна")
    elif 0 <= temperature < 10:
        base_advice = "ХОЛОДНО: Зимняя одежда"
        items = ["термобелье", "шерстяной свитер", "зимняя куртка", "шапка", "перчатки"]
        if temperature < 5:
            items.append("шарф для защиты горла")
    else:
        base_advice = "МОРОЗ: Экстремально теплая одежда"
        items = ["термобелье", "пуховик", "шерстяные носки", "зимние ботинки", "шарф"]
        additional_recommendations.append("Ограничьте пребывание на улице")

    if "дождь" in condition or "ливень" in condition:
        additional_recommendations.append("Водонепроницаемая куртка и обувь обязательны")
        if temperature < 15:
            additional_recommendations.append("Не забудьте зонт")

    if "снег" in condition or "мокрый снег" in condition:
        items.append("непромокаемые ботинки")
        additional_recommendations.append("Обувь с противоскользящей подошвой")

    if "гроза" in condition:
        additional_recommendations.append("Избегайте металлических аксессуаров")

    if wind_speed > 10:
        additional_recommendations.append("Плотно застегивающаяся ветрозащитная одежда")
    elif wind_speed > 15:
        additional_recommendations.append("Капюшон или плотно сидящая шапка обязательны")

    full_advice = f"{base_advice}\nОсновной гардероб: {', '.join(items)}"

    if additional_recommendations:
        full_advice += f"\nДополнительные рекомендации: {'; '.join(additional_recommendations)}"

    return full_advice


def get_activity_advice(temperature, condition, wind_speed, humidity, pressure):

    condition = condition.lower()
    activities = []
    precautions = []
    indoor_activities = []

    if temperature > 25:
        activities.extend([
            "Плавание в бассейне или открытом водоеме",
            "Прогулка в парке в тени деревьев",
            "Велосипедная прогулка утром или вечером"
        ])
        if humidity < 60:
            activities.append("Пляжные виды спорта")
        else:
            precautions.append("Высокая влажность - избегайте интенсивных нагрузок")

    elif 18 <= temperature <= 25:
        activities.extend([
            "Длительные пешие прогулки",
            "Бег трусцой в парке",
            "Йога на свежем воздухе",
            "Катание на роликах или скейте",
            "Пикник на природе"
        ])

    elif 10 <= temperature < 18:
        activities.extend([
            "Быстрая ходьба для поддержания тепла",
            "Поход в лес за грибами или ягодами",
            "Посещение уличных кафе с террасами"
        ])
        indoor_activities.extend([
            "Шоппинг в торговых центрах",
            "Посещение музеев"
        ])

    elif 0 <= temperature < 10:
        activities.extend([
            "Зимние виды спорта при наличии снега",
            "Бодрящая утренняя прогулка"
        ])
        indoor_activities.extend([
            "Посещение выставок",
            "Обед в уютном ресторане",
            "Боулинг или бильярд"
        ])
    else:
        indoor_activities.extend([
            "Катание на коньках (крытый каток)",
            "Поход в кинотеатр",
            "Чтение книг в библиотеке",
            "Домашние игры с семьей"
        ])

    if "ясно" in condition or "солнечно" in condition:
        activities.extend([
            "Фотографирование пейзажей",
            "Наблюдение за восходом или закатом"
        ])
        if temperature > 20:
            activities.append("Пикник на открытой местности")

    elif "дождь" in condition or "морось" in condition:
        precautions.append("Скользкие поверхности - будьте осторожны")
        indoor_activities.extend([
            "Посещение театра или концерта",
            "Настольные игры дома",
            "Приготовление нового блюда"
        ])
    elif "снег" in condition:
        activities.extend([
            "Лепка снеговика",
            "Катание на лыжах или сноуборде",
            "Катание на санках"
        ])
        precautions.append("Теплая одежда и нескользящая обувь обязательны")
    elif "гроза" in condition:
        precautions.append("Избегайте открытых пространств и воды")
        indoor_activities.extend([
            "Чтение книг",
            "Просмотр фильмов",
            "Творческие занятия"
        ])
    elif "туман" in condition:
        precautions.append("Ограниченная видимость - будьте внимательны")
        activities.append("Неспешная прогулка в знакомой местности")

    if wind_speed > 10:
        precautions.append("Сильный ветер - избегайте открытых пространств")
        indoor_activities.extend([
            "Тренировка в спортзале",
            "Йога или пилатес в помещении"
        ])
    elif wind_speed > 15:
        precautions.append("Очень сильный ветер - оставайтесь в помещении")

    if pressure < 980:
        precautions.append("Низкое атмосферное давление - возможны головные боли")
    elif pressure > 1020:
        precautions.append("Высокое атмосферное давление - осторожность гипертоникам")

    if humidity > 80:
        precautions.append("Высокая влажность - тяжело дышать, избегайте нагрузок")
    elif humidity < 30:
        precautions.append("Низкая влажность - пейте больше воды")
    result = ""

    if activities:
        result += "Рекомендуемые активности на улице:\n• " + "\n• ".join(activities)

    if indoor_activities:
        if result: result += "\n\n"
        result += "Активности в помещении:\n• " + "\n• ".join(indoor_activities)

    if precautions:
        if result: result += "\n\n"
        result += "Меры предосторожности:\n• " + "\n• ".join(precautions)

    return result if result else "Комфортная погода для любых занятий на свежем воздухе"


def get_health_recommendations(temperature, humidity, pressure, condition):
    condition = condition.lower()
    recommendations = []
    warnings = []

    if temperature > 30:
        warnings.append("Экстремальная жара - риск теплового удара")
        recommendations.extend([
            "Пейте 2-3 литра воды в день",
            "Избегайте нахождения на солнце с 12:00 до 16:00",
            "Носите светлую свободную одежду"
        ])
    elif temperature > 25:
        recommendations.append("Увеличьте потребление жидкости")
    elif temperature < -10:
        warnings.append("Сильный мороз - риск обморожения")
        recommendations.extend([
            "Ограничьте пребывание на улице",
            "Прикрывайте открытые участки кожи",
            "Дышите через шарф"
        ])
    elif temperature < 0:
        recommendations.append("Тепло одевайтесь, особенно защищайте руки и голову")
    if humidity > 85:
        warnings.append("Очень высокая влажность - тяжело дышать")
        recommendations.extend([
            "Осторожность астматикам и сердечникам",
            "Избегайте интенсивных физических нагрузок"
        ])
    elif humidity < 25:
        warnings.append("Очень сухой воздух - раздражение слизистых")
        recommendations.extend([
            "Используйте увлажнитель воздуха",
            "Закапывайте солевые растворы в нос"
        ])

    if pressure < 980:
        recommendations.append("Низкое давление - возможны головные боли у метеочувствительных")
    elif pressure > 1020:
        recommendations.append("Высокое давление - контроль давления у гипертоников")

    if "гроза" in condition:
        recommendations.append("Во время грозы оставайтесь в помещении")

    if "туман" in condition:
        recommendations.append("При тумане осторожность людям с respiratory проблемами")

    result = ""
    if warnings:
        result += "Внимание:\n• " + "\n• ".join(warnings)

    if recommendations:
        if result: result += "\n\n"
        result += "Рекомендации:\n• " + "\n• ".join(recommendations)

    return result