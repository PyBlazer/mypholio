import streamlit as st
import plotly.express as px
import requests as r
import pandas as pd
import random
import base64
from datetime import datetime

# ------------------ Настройки страницы ------------------
st.set_page_config(
    page_title="Maksim Androschuk | Pholio",
    page_icon="🇺🇦",
    layout="wide"
)
# ------------------ Скрываем лишнее ---------------------
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                .appview-container .main .block-container{padding-top: 1rem;}
                
                div[data-testid="stSidebarUserContent"] {
                    padding: 2rem 1.5rem !important;
                    with: 330px !important;
                }
                
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)


def skills(skill_name, skill_lvl):
    bar = st.progress(0, text=skill_name)

    for percent_complete in range(skill_lvl):
        bar.progress(percent_complete + 1, text=skill_name)


def cloud_tag(text):
    words = text.split()

    # Создаем случайный порядок слов
    random.shuffle(words)

    # Стилизация HTML с помощью CSS
    styled_text = ""
    for word in words:
        # Случайный размер и толщина текста для каждого слова
        font_size = random.randint(12, 24)
        font_thickness = random.randint(1, 5)
        line_height = random.uniform(1.0, 1.5)  # Рандомное значение для line-height

        styled_text += f'<span style="font-size: {font_size}px; font-weight: {font_thickness * 100}; margin: 5px; display: inline-block; line-height: {line_height};">{word}</span> '

    # Добавляем стили к облаку тегов
    st.markdown(
        f'<div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center;">{styled_text}</div>',
        unsafe_allow_html=True
    )


def copy():
    # Текст копирайта
    copyright_text = (
            "&copy; " + str(datetime.now().year) + " Maskim Androschuk."
    )

    # Вставка изображения и текста копирайта в боковую панель
    st.sidebar.markdown(
        f'<div style="display: flex; flex-direction: column; align-items: center;">'
        f'<p>{copyright_text}</p>'
        f'</div>',
        unsafe_allow_html=True
    )


def brand_logo(file, caption):
    st.markdown(
        '''
        <style>
            .carousel-container { display: flex; overflow-x: auto; }
            .brand-logo-container { position: relative; }
            .brand-logo { filter: grayscale(100%); transition: filter 0.3s, opacity 0.3s; cursor: pointer; opacity: 0.5;}
            .brand-logo:hover { filter: grayscale(0%); opacity: 1; }
            .caption { text-align: center; padding: 5px; background-color: rgba(255, 255, 255, 0.7); opacity: 0; transition: opacity 0.3s; }
            .brand-logo-container:hover .caption { opacity: 1; }
        </style>
        ''',
        unsafe_allow_html=True
    )

    with st.markdown('<div class="carousel-container">', unsafe_allow_html=True):
        st.markdown(
            f'''
            <div class="brand-logo-container">
                <img class="brand-logo" src="data:image/png;base64,{base64.b64encode(open(file, "rb").read()).decode()}">
                <p class="caption">{caption}</p>
            </div>
            ''',
            unsafe_allow_html=True
        )


def get_age():
    dob_str = "06-05-1981"
    dob = datetime.strptime(dob_str, "%d-%m-%Y")
    current_date = datetime.now()
    age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
    return age


def YesNo():
    data = r.get('https://yesno.wtf/api').json()
    return data


def BlockChain():
    data = r.get(
        'https://api.blockchain.info/charts/transactions-per-second?timespan=5weeks&rollingAverage=8hours&format=json').json()
    return data


def Exchange(date):
    data = r.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json").json()
    return data


# ------- PAGES ----------------------
def page1():

    st.subheader("Вступ")

    text_1 = '''
        Професійний та досвідчений **Python** розробник з успішним досвідом у створенні бекендів та управлінні базами даних.      
        Шукаю нові виклики та можливість приєднатися до команди, де можна внести значущий внесок у технічний розвиток та досягнення цілей проектів.
    '''
    st.markdown(text_1)
    st.subheader("Мій внесок")
    text_2 = '''   
        - Глибокі технічні знання та вміння вдосконалювати процеси розробки.   
        - Моє бажання приносити користь та впроваджувати інновації в проекти робить мене відмінним кандидатом для вакансії **Python** розробника.   
        - Готовий приєднатися до вашої команди та внести свої силу та експертизу для досягнення ваших цілей.
    '''
    st.markdown(text_2)

    st.divider()
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        brand_logo('img/mtm_logo.png', 'Концерн «Міські теплові мережі»')
    with col2:
        brand_logo('img/afarm_logo2.png', 'ТОВ "АЛЕКСФАРМ"')
    with col3:
        brand_logo('img/zva_logo2.png', 'Запорізький завод високовольтної апаратури')
    with col4:
        brand_logo('img/zpr_logo2.png', 'ПАТ "Запорізький завод "Перетворювач"')
    with col5:
        brand_logo('img/uz_logo2.png', 'Акціонерне товариство «Українська залізниця»')
    with col6:
        brand_logo('img/pfu_logo2.png', 'Пенсійний фонд України')
    st.divider()

    col_skils, col_lang, col_works = st.columns(3)
    with col_skils:
        st.subheader("Навички")
        skills('python', 60)
        skills('php', 40)
        skills('delphi', 10)
        skills('js', 10)
    with col_lang:
        st.subheader("Знання мов")
        skills('Українська', 100)
        skills('English', 10)
        skills('Русский', 100)
    with col_works:
        st.subheader("Hard & Soft skills")
        text = "ChatGPT REST API Joomla Wordpress Flask FastApi Django MSSQL MySql CSV Json Asterisk IZAR@NET2 Delphi JS HTML CSS Streamlit NodeRED GLPI pandas requests SNMP Dinstar CentOS Debian NGINX Apache Postman PuTTY"
        cloud_tag(text=text)
    st.divider()

    # Освіта
    st.subheader("Освіта")
    st.write("""- [**інженер-програміст**] Запорізька державна інженерна академія (ЗДІА), Системне програмування, Запоріжжя, з **2003**р. по **2009**р.""")
    st.write("""- [**технік-електронік**] Запорізький коледж радіоелектроніки (ЗКР), Обчислювальна техніка, Запоріжжя, з **1996**р. по **2000**р.""")


def page2():

    st.subheader("Сценарії та Автоматизація")

    # Опис розділу
    st.write("""
        Цей розділ призначений для опису різноманітних проектів з написання скриптів та автоматизації,
        які розроблені для внутрішнього використання на підприємстві. Тут представлені рішення, які
        спрямовані на оптимізацію та полегшення рутинних завдань, що виникають у процесі роботи.

        Описані проекти включають в себе різні скрипти та програми, створені з метою підвищення
        ефективності внутрішніх процесів та забезпечення зручності користувачів. Ці інструменти можуть
        охоплювати автоматизацію рутинних завдань, створення звітів, аналіз даних, інтеграцію різних
        систем та багато іншого.

        Мета цього розділу - відобразити інноваційний підхід до внутрішнього управління та підтримки
        підприємства, використовуючи розроблені внутрішні інструменти для оптимізації робочих процесів
        та підвищення продуктивності.
    """)
    st.divider()
    st.subheader("АРМ адміністратора особистого кабінету")
    st.caption('Flask + Bootstrap')
    st.write("""
        Веб-додаток, розроблений за допомогою Flask та Bootstrap, який дозволяє адміністратору виконувати оновлення даних з MSSQL до MySQL в певний час, обраної користувачем.

        Користувач може вказати конкретну дату, з якої розпочнеться процес оновлення даних. Додаток надає можливість оновлення як всієї бази даних, так і частково, вибравши певні сегменти для оновлення.
        
        Окрім цього, в додатку реалізовано функціонал відображення логів процесу оновлення. Адміністратор може переглядати інформацію щодо успішно виконаних або помилкових кроків під час оновлення даних. Це допомагає забезпечити контроль над процесом та швидко реагувати на будь-які проблеми.
        
        Використання Bootstrap надає додатку сучасний та адаптивний інтерфейс, що полегшує взаємодію адміністратора з додатком на різних пристроях.
    """)
    st.subheader("Менеджер Синхронізації Даних")
    st.caption('Delphi + RestAPI')
    st.write("""
        Власно розроблений додаток з використанням Delphi та RestAPI для оптимізації і управління процесом синхронізації даних. Додаток спрямований на взаємодію зі стороннім програмним засобом, який опитує та зберігає дані приладів обліку.
    
        За допомогою API-запитів, програма отримує необхідні дані від стороннього додатка. Після отримання даних вони обробляються відповідно до потреб та порівнюються з інформацією в MS SQL. У випадку необхідності, програма може виконати додавання нових записів або внесення змін у БД стороннього додатка.
        
        Використання технології Delphi дозволяє створити ефективний та зручний інтерфейс для користувача. Додаток дозволяє з легкістю взаємодіяти з API та автоматизувати процеси синхронізації даних, забезпечуючи ефективний контроль та управління інформаційним обміном між різними системами.
    """)
    st.subheader("GLPI Аналітичні звіти")
    st.caption('Streamlit + RestAPI')
    st.write("""
        Представляє собою веб-додаток, розроблений за допомогою Streamlit та RestAPI, який надає користувачам можливість моніторингу та аналізу даних з системи управління ІТ-ресурсами GLPI. Додаток складається з набору дашбордів, які дозволяють ефективно відстежувати та аналізувати ключові показники продуктивності та стану обладнання.
    
        Один з дашбордів надає огляд кількості тікетів для кожного виконавця. Крім того, він автоматично розраховує KPI, використовуючи робочий час. Це дозволяє ефективно відслідковувати та оцінювати продуктивність кожного виконавця в контексті відповідальностей та обсягу роботи.
        
        Другий дашборд отримує інформацію про всі мережеві принтери, занесені в GLPI, і опитує їх лічильники за допомогою протоколу SNMP. Це дозволяє забезпечити швидкий та зручний доступ до актуальної інформації про використання принтерів, їх стан та ефективність в мережі.
        
        Використання Streamlit надає зручний та інтерактивний інтерфейс для користувачів, що спрощує взаємодію з аналітичними даними та дозволяє швидко приймати відповідальні рішення на основі зібраної інформації.
    """)
    st.subheader("Інше")
    st.caption("Python, PHP")
    st.write("""
        Окрім  розробки веб-додатків, маю досвід в написанні коротких скриптів на мовах програмування Python та PHP. Здійснював створення і оптимізацію скриптів для вирішення різноманітних задач, таких як отримання статусу SIP номерів, робота з API GSM шлюза, парсинг SMS повідомлень та опитування SIM-карт через GSM шлюз. Також займався обробкою CSV та XML файлів, що дозволяло ефективно взаємодіяти з різними джерелами даних. Маю досвід у впровадженні та вдосконаленні функціональності за допомогою автоматизованих скриптів, що сприяє підвищенню ефективності та автоматизації рутинних завдань.
    """)


def page3():
    st.subheader("Live demo")
    # Опис розділу
    st.write("""
            У цьому розділі ви зможете переконатися в ефективності та потужності використання **Python** та відкритих **API**.  
            Живі демонстрації включають в себе інтерактивні скрипти та віджети, розроблені з використанням **Streamlit**.
        """)
    st.divider()
    col1, col2, col_null = st.columns(3)
    with col1:
        st.subheader("Магічний шар долі ))")
        st.write("Необхідно поставити питання, і натиснути на кнопку.")
        btn_ask = st.button("Так, чи Ні?")
        if btn_ask:
            data = YesNo()
            answer = data.get('answer')
            st.write(f'Відповідь долі:  :red[**{answer}**]')
            st.image(data.get('image'), width=150)
    with col2:
        st.subheader("WebCam")
        st.write("Перевірка Web камери, якщо вона є )).")
        webcam = st.empty()
        cam_btn1, cam_btn2 = st.columns(2)
        with cam_btn1:
            cam_on = st.button("Увімкнути камеру")
        with cam_btn2:
            cam_off = st.button("Вимкнути камеру")
        if cam_on:
            pic = webcam.camera_input("Take a picture", label_visibility="hidden")
            if pic:
                st.image(pic)

        if cam_off:
            webcam.camera_input("Take a picture", disabled=True)
            webcam.empty()

    st.divider()
    block = BlockChain()
    df = pd.DataFrame(block["values"], columns=["x", "y"])

    # Преобразование timestamp в удобочитаемый формат
    df["x"] = pd.to_datetime(df["x"], unit="s").dt.strftime('%d-%m-%Y %H:%M:%S')

    # Отображение информации

    st.subheader("Швидкість транзакцій")
    st.write("Кількість транзакцій Bitcoin, які додаються до пулу на секунду")

    # Построение графика
    fig = px.line(df, x="x", y="y", labels={"x": "Часова мітка", "y": "Транзакцій у сек."})
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

    st.subheader("Офіційний курс гривні до іноземних валют та облікова ціна банківських металів")
    ex_col1, ex_col2, ex_calc_col = st.columns([1, 2, 2])
    with ex_col1:
        d = st.date_input("За яку дату переглянути курс?", format="DD.MM.YYYY")
        current_date = datetime.now().date()
        if d > current_date:
            st.warning("Обрана дата в майбутньому. Встановлено поточну дату.")
            d = current_date
        formatted_date = d.strftime("%Y%m%d")
        data = Exchange(formatted_date)
    with ex_col2:
        df_ex = pd.DataFrame(data)
        # Убираем последнюю колонку
        df_ex = df_ex.iloc[:, :-1]
        df_ex = df_ex.iloc[:, [0, 3, 1, 2]]
        # Переименовываем колонки
        df_ex.columns = ["Код", "alfa-3", "Назва", "Курс, грн."]
        st.dataframe(df_ex, hide_index=True, use_container_width=True, height=460)
    with ex_calc_col:
        with st.form('calc'):
            st.subheader("Конвертор валют", divider='rainbow')
            frm_col1, frm_col2 = st.columns(2)
            with frm_col1:
                order = st.number_input('Сума')
                cc_2 = st.selectbox('В яку валюту конверуємо?', df_ex['alfa-3'])
            with frm_col2:
                cc_1 = st.selectbox('Валюта', df_ex['alfa-3'])

            # Используем метод loc для получения значения "Курс, грн." по выбранному "alfa-3"
            selected_row = df_ex.loc[df_ex['alfa-3'] == cc_1]
            kurs_value = selected_row.iloc[0]['Курс, грн.']
            selected_row2 = df_ex.loc[df_ex['alfa-3'] == cc_2]
            kurs_value2 = selected_row2.iloc[0]['Курс, грн.']

            submitted = st.form_submit_button("Розрахувати")
            if submitted:
                res = order * kurs_value
                result = res * (1 / kurs_value2)
                st.divider()
                st.write(f"{order} {cc_1} = **{res:.2f}** UAH.")
                st.write(f"{order} {cc_1} = **{result:.2f}** {cc_2} через UAH.")

    st.divider()


def main():
    # --------- SIDEBAR --------------------------
    sidebar = st.sidebar
    sidebar.title("Андрощук Максим Володимирович")
    sidebar.markdown(
        f'''*"У світі творчості немає недосяжних задач, але часто зустрічаються неповні технічні завдання чи відсутність ресурсів"*''')
    sidebar.divider()
    sidebar.markdown(f''':gray[*вік:*] **{get_age()}**  
            :gray[*локація:*] **Україна, Запоріжжя**  
            :gray[*моб.тел.:*] **+38(068)0844808**    
            :gray[*е-пошта:*] **m.androschuk@gmail.com**          
            ''')

    link_col1, link_col2 = sidebar.columns(2)
    with link_col1:
        st.markdown(
            """<a href="https://www.work.ua/resumes/5553022/">
            <img src="data:image/png;base64,{}" width="100">
            </a>""".format(
                base64.b64encode(open("img/work-ua.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )

    with link_col2:
        st.markdown(
            """<a href="https://ua.linkedin.com/in/maksim-androschuk-29a42885">
            <img src="data:image/png;base64,{}" width="100">
            </a>""".format(
                base64.b64encode(open("img/linkedIn.png", "rb").read()).decode()
            ),
            unsafe_allow_html=True,
        )
    sidebar.divider()

    pages = {
        'Профіль': page1,
        'Сценарії та Автоматизація': page2,
        'Live demo': page3
    }
    sidebar.subheader("Розділи")
    page = sidebar.radio(".", list(pages.keys()),index=0,label_visibility="collapsed")

    if page in pages:
        pages[page]()
    else:
        st.write(f"Сторінки {page} не існує.")

    sidebar.divider()
    copy()

if __name__ == "__main__":
    main()
