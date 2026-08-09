from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "pdf"

FONT_DIR = Path("/System/Library/Fonts/Supplemental")
FONT_FILES = {
    "CVSerif": FONT_DIR / "Georgia.ttf",
    "CVSerif-Bold": FONT_DIR / "Georgia Bold.ttf",
    "CVSerif-Italic": FONT_DIR / "Georgia Italic.ttf",
    "CVSerif-BoldItalic": FONT_DIR / "Georgia Bold Italic.ttf",
}

LINK = colors.HexColor("#000088")
TEXT = colors.black
MUTED = colors.HexColor("#555555")


CV_DATA = {
    "en": {
        "filename": "alexander-anisimov-cv-en.pdf",
        "name": "Alexander Anisimov",
        "headline": "Data Analysis | Product Analytics | Statistics",
        "contacts": [
            ("alananisimov@gmail.com", "mailto:alananisimov@gmail.com"),
            ("GitHub", "https://github.com/alananisimov"),
            ("Telegram", "https://t.me/hollz69"),
            ("+7 923 709-01-58", "tel:+79237090158"),
        ],
        "availability": "Moscow | Available up to 20 hours/week | Remote preferred, hybrid in Moscow possible",
        "profile": (
            "High school student at CPM School and a final-stage DANO prize winner. Analyzed T-Bank "
            "business data and public road-safety data using Python, statistical methods, and data "
            "visualization. Seeking a data or product analytics internship."
        ),
        "education_title": "Education",
        "education": {
            "title": "CPM School",
            "location": "Computer Science track | Moscow",
            "date": "2025 - 2027 (expected)",
            "bullets": [
                "GPA: 5.0/5.0 across all subjects; coursework in olympiad mathematics and competitive programming",
                "Independent study: Harvard STAT 110 (Probability), ISLP (Statistical Learning with Python), and econometrics",
            ],
        },
        "data_title": "Data Analysis & Competitions",
        "data_entries": [
            {
                "title": "2nd Place, DANO Hackathon at ITMO University",
                "location": "T-Bank Gorod case",
                "date": "April 2026",
                "bullets": [
                    "Analyzed 102,351 grocery orders from T-Bank Gorod to study how markup was associated with order composition and volume",
                    "Segmented results by product category and cashback level, prepared GMV comparisons and visualizations, and formulated a behavioral explanation for lower price sensitivity in ready meals and bakery products",
                    "In the final analysis, a 1 pp markup increase was associated with a 1.13% GMV decline for fruit, vegetable, and sweets categories, while ready meals, bakery, and drinks were nearly unchanged (+0.08%); the difference was significant (p &lt; 0.001)",
                    "Prepared materials for the final presentation; the 6-person team placed 2nd among more than 40 teams",
                ],
            },
            {
                "title": "Prize Winner, DANO Data Analysis Olympiad - Final Stage",
                "location": "road safety research",
                "date": "Nov - Dec 2025",
                "bullets": [
                    "Cleaned anomalies and outliers in a public road-accident dataset and conducted EDA across violation types and injury rates",
                    "Developed and visualized the research logic linking intoxication-related violations to a higher share of injury-causing accidents",
                    "Translated the findings into policy recommendations on alcohol interlocks, novice-driver limits, and transport alternatives, and prepared final presentation materials",
                ],
            },
        ],
        "projects_title": "Selected Projects",
        "projects": [
            {
                "title": "AD-Platform",
                "url": "https://github.com/alananisimov/ad-platform",
                "location": "solo project | PROD 2025 individual final",
                "date": "February 2025",
                "bullets": [
                    "Built four Go microservices for campaigns, ad delivery, statistics, and users, connected through gRPC and RabbitMQ",
                    "Implemented campaign ranking using expected profit, externally supplied ML relevance scores, delivery progress, and freshness",
                    "Added PostgreSQL, MongoDB, Redis caching, OpenTelemetry tracing, Prometheus/Grafana monitoring, and Testcontainers-based tests",
                ],
            },
            {
                "title": "NFT Marketplace",
                "url": "https://github.com/alananisimov/nft-marketplace",
                "location": "solo paid freelance MVP",
                "date": "Nov 2024 - Feb 2025",
                "bullets": [
                    "Developed a Telegram Mini App and bots for issuing, browsing, purchasing, holding, and staking Stellar-based NFTs",
                    "Built a TypeScript monorepo with Next.js, tRPC, PostgreSQL/Drizzle, Redis, MinIO/S3, authentication, and the Stellar SDK",
                    "Reduced repeated blockchain and storage requests through Redis and image caching, substantially improving catalog response time",
                ],
            },
            {
                "title": "Olcbox",
                "url": "https://github.com/alananisimov/olcbox",
                "location": "open-source maintainer",
                "date": "2026 - Present",
                "bullets": [
                    "Developing a cross-platform networking client with Kotlin Multiplatform and Compose for Android, iOS, macOS, Windows, and Linux",
                    "Project adoption: 420+ GitHub stars, 40+ forks, and external contributions",
                ],
            },
            {
                "title": "PROD Olympiad Team Final",
                "location": "frontend lead | 5-person team",
                "date": "Feb - Mar 2025",
                "summary": (
                    "Designed the complete UI in Figma, created the frontend architecture, implemented "
                    "the React/Next.js application, and coordinated frontend work for a coworking-management "
                    "MVP. Finalist among approximately 60 teams."
                ),
            },
        ],
        "skills_title": "Technical Skills",
        "skills": [
            (
                "Data & ML",
                "Python, Pandas, NumPy, SciPy, scikit-learn, Statsmodels, Matplotlib, Seaborn, Plotly; "
                "EDA, hypothesis testing, regression, tree-based models, PCA, feature engineering, "
                "cross-validation, and model evaluation",
            ),
            (
                "Mathematics",
                "Probability, mathematical statistics, linear algebra (MIT 18.06), Calculus II, and introductory econometrics",
            ),
            (
                "Engineering",
                "Go, TypeScript, C++, Git, Docker, Linux, gRPC, RabbitMQ, PostgreSQL, MongoDB, Redis",
            ),
            ("SQL", "SELECT, JOIN, GROUP BY, and aggregate functions"),
        ],
        "languages_title": "Languages & Additional Honors",
        "languages": (
            "<b>Russian:</b> Native | <b>English:</b> C1 proficiency | "
            "<b>German:</b> B2, Goethe-Zertifikat (2025)"
        ),
        "honor": (
            "Prize winner, regional stage of the All-Russian School Olympiad in German; "
            "qualified for the national final. Winner, DANO Data Analysis Hackathon (2025)."
        ),
    },
    "ru": {
        "filename": "alexander-anisimov-cv-ru.pdf",
        "name": "Александр Анисимов",
        "headline": "Анализ данных | Продуктовая аналитика | Статистика",
        "contacts": [
            ("alananisimov@gmail.com", "mailto:alananisimov@gmail.com"),
            ("GitHub", "https://github.com/alananisimov"),
            ("Telegram", "https://t.me/hollz69"),
            ("+7 923 709-01-58", "tel:+79237090158"),
        ],
        "availability": "Москва | До 20 часов в неделю | Удалённо или гибридно в Москве",
        "profile": (
            "Ученик Школы ЦПМ и призёр заключительного этапа DANO. Анализировал бизнес-данные "
            "Т-Банка и открытые данные ГИБДД с помощью Python, статистических методов и визуализации. "
            "Ищу стажировку аналитика данных или продуктового аналитика."
        ),
        "education_title": "Образование",
        "education": {
            "title": "Школа ЦПМ",
            "location": "информатический профиль | Москва",
            "date": "2025 - 2027 (ожидается)",
            "bullets": [
                "Средний балл: 5.0/5.0 по всем предметам; олимпиадная математика и спортивное программирование",
                "Самостоятельное обучение: Harvard STAT 110 (теория вероятностей), ISLP (статистическое обучение на Python), эконометрика",
            ],
        },
        "data_title": "Анализ данных и соревнования",
        "data_entries": [
            {
                "title": "2-е место на хакатоне DANO в Университете ИТМО",
                "location": "кейс Т-Банка «Город»",
                "date": "Апрель 2026",
                "bullets": [
                    "Исследовал 102 351 заказ сервиса Т-Банка «Город», чтобы оценить связь наценки с составом и объёмом корзины",
                    "Сегментировал результаты по категориям и уровню кешбэка, подготовил сравнения GMV и визуализации и сформулировал поведенческое объяснение более низкой ценовой чувствительности готовой еды и выпечки",
                    "В итоговом анализе рост наценки на 1 п.п. был связан со снижением GMV фруктов, овощей и сладостей на 1,13%, тогда как готовая еда, выпечка и напитки почти не изменились (+0,08%); разница значима (p &lt; 0,001)",
                    "Подготовил материалы для итоговой презентации; команда из 6 человек заняла 2-е место среди более чем 40 команд",
                ],
            },
            {
                "title": "Призёр заключительного этапа олимпиады DANO",
                "location": "исследование безопасности дорожного движения",
                "date": "Ноябрь - декабрь 2025",
                "bullets": [
                    "Очистил открытые данные ГИБДД от аномалий и выбросов и провёл EDA по видам нарушений и доле ДТП с пострадавшими",
                    "Выстроил и визуализировал логику исследования, связывающую нарушения в состоянии опьянения с более высокой долей ДТП с пострадавшими",
                    "Сформулировал практические рекомендации: алкозамки для рецидивистов, ограничения для начинающих водителей и развитие транспортных альтернатив; подготовил материалы для итоговой презентации",
                ],
            },
        ],
        "projects_title": "Проекты",
        "projects": [
            {
                "title": "AD-Platform",
                "url": "https://github.com/alananisimov/ad-platform",
                "location": "индивидуальный проект | финал PROD 2025",
                "date": "Февраль 2025",
                "bullets": [
                    "Разработал четыре микросервиса на Go для управления кампаниями, показа рекламы, статистики и пользователей, связав их через gRPC и RabbitMQ",
                    "Реализовал ранжирование кампаний по ожидаемой прибыли, внешним ML-оценкам релевантности, выполнению плана и свежести",
                    "Добавил PostgreSQL, MongoDB, кэширование в Redis, трассировку OpenTelemetry, мониторинг Prometheus/Grafana и тесты на Testcontainers",
                ],
            },
            {
                "title": "NFT Marketplace",
                "url": "https://github.com/alananisimov/nft-marketplace",
                "location": "индивидуальный оплаченный фриланс-MVP",
                "date": "Ноябрь 2024 - февраль 2025",
                "bullets": [
                    "Разработал Telegram Mini App и ботов для выпуска, просмотра, покупки, хранения и стейкинга NFT в сети Stellar",
                    "Построил TypeScript-монорепозиторий на Next.js, tRPC, PostgreSQL/Drizzle, Redis, MinIO/S3, с авторизацией и Stellar SDK",
                    "Сократил повторные запросы к блокчейну и хранилищу с помощью Redis и кэширования изображений, заметно ускорив каталог",
                ],
            },
            {
                "title": "Olcbox",
                "url": "https://github.com/alananisimov/olcbox",
                "location": "мейнтейнер open-source проекта",
                "date": "2026 - н. в.",
                "bullets": [
                    "Разрабатываю кроссплатформенный сетевой клиент на Kotlin Multiplatform и Compose для Android, iOS, macOS, Windows и Linux",
                    "Проект получил более 420 звёзд и 40 форков на GitHub и внешние контрибуции",
                ],
            },
            {
                "title": "Командный финал олимпиады PROD",
                "location": "лид фронтенда | команда из 5 человек",
                "date": "Февраль - март 2025",
                "summary": (
                    "Спроектировал весь UI в Figma, разработал frontend-архитектуру и приложение "
                    "на React/Next.js, координировал работу фронтенда над MVP управления коворкингом. "
                    "Финалист среди примерно 60 команд."
                ),
            },
        ],
        "skills_title": "Технические навыки",
        "skills": [
            (
                "Анализ данных и ML",
                "Python, Pandas, NumPy, SciPy, scikit-learn, Statsmodels, Matplotlib, Seaborn, Plotly; "
                "EDA, проверка гипотез, регрессии, деревья решений и ансамбли, PCA, feature engineering, "
                "кросс-валидация и оценка моделей",
            ),
            (
                "Математика",
                "Теория вероятностей, математическая статистика, линейная алгебра (MIT 18.06), "
                "математический анализ уровня Calculus II, основы эконометрики",
            ),
            (
                "Разработка",
                "Go, TypeScript, C++, Git, Docker, Linux, gRPC, RabbitMQ, PostgreSQL, MongoDB, Redis",
            ),
            ("SQL", "SELECT, JOIN, GROUP BY и агрегатные функции"),
        ],
        "languages_title": "Языки и дополнительные достижения",
        "languages": (
            "<b>Русский:</b> родной | <b>Английский:</b> C1 | "
            "<b>Немецкий:</b> B2, Goethe-Zertifikat (2025)"
        ),
        "honor": (
            "Призёр регионального этапа ВсОШ по немецкому языку; участник заключительного этапа. "
            "Победитель хакатона DANO по анализу данных (2025)."
        ),
    },
}


def register_fonts() -> None:
    for name, path in FONT_FILES.items():
        if not path.exists():
            raise FileNotFoundError(f"Required font not found: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))

    pdfmetrics.registerFontFamily(
        "CVSerif",
        normal="CVSerif",
        bold="CVSerif-Bold",
        italic="CVSerif-Italic",
        boldItalic="CVSerif-BoldItalic",
    )


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=16.5,
            leading=18,
            textColor=TEXT,
            alignment=TA_CENTER,
            spaceAfter=0.8 * mm,
        ),
        "headline": ParagraphStyle(
            "Headline",
            parent=base["Normal"],
            fontName="CVSerif-Italic",
            fontSize=8.6,
            leading=9.8,
            textColor=TEXT,
            alignment=TA_CENTER,
            spaceAfter=1 * mm,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=8.3,
            leading=9.5,
            textColor=TEXT,
            alignment=TA_CENTER,
            spaceAfter=0.8 * mm,
        ),
        "availability": ParagraphStyle(
            "Availability",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=7.8,
            leading=9,
            textColor=TEXT,
            alignment=TA_CENTER,
            spaceAfter=2.2 * mm,
        ),
        "profile": ParagraphStyle(
            "Profile",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=8.4,
            leading=9.8,
            textColor=TEXT,
            borderPadding=0,
            leftIndent=0,
            spaceAfter=2.3 * mm,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=10.7,
            leading=12,
            textColor=TEXT,
            spaceBefore=1.7 * mm,
            spaceAfter=1.1 * mm,
            borderColor=TEXT,
            borderWidth=0,
            borderPadding=(0, 0, 0.8 * mm, 0),
        ),
        "entry": ParagraphStyle(
            "Entry",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=8.35,
            leading=9.7,
            textColor=TEXT,
        ),
        "entry_right": ParagraphStyle(
            "EntryRight",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=8,
            leading=9.3,
            textColor=TEXT,
            alignment=TA_RIGHT,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=8.15,
            leading=9.55,
            textColor=TEXT,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="CVSerif",
            fontSize=8.15,
            leading=9.55,
            textColor=TEXT,
            leftIndent=0,
            firstLineIndent=0,
        ),
    }


def section_heading(text: str, styles: dict[str, ParagraphStyle]):
    heading = Paragraph(text, styles["section"])
    table = Table([[heading]], colWidths=[None])
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.65, TEXT),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.8 * mm),
            ]
        )
    )
    return table


def entry_header(entry: dict, styles: dict[str, ParagraphStyle]):
    title = entry["title"]
    if entry.get("url"):
        title = f'<link href="{entry["url"]}" color="#000088"><b>{title}</b></link>'
    else:
        title = f"<b>{title}</b>"

    location = entry.get("location")
    if location:
        title += f", <i>{location}</i>"

    left = Paragraph(title, styles["entry"])
    right = Paragraph(entry["date"], styles["entry_right"])
    table = Table([[left, right]], colWidths=[157 * mm, 32 * mm])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.4 * mm),
            ]
        )
    )
    return table


def bullet_list(items: list[str], styles: dict[str, ParagraphStyle]):
    flowables = [
        ListItem(Paragraph(item, styles["bullet"]), leftIndent=2.3 * mm)
        for item in items
    ]
    return ListFlowable(
        flowables,
        bulletType="bullet",
        start="circle",
        leftIndent=4.6 * mm,
        bulletFontName="CVSerif",
        bulletFontSize=6,
        bulletOffsetY=1.2,
        spaceAfter=1.3 * mm,
    )


def entry_flowables(entry: dict, styles: dict[str, ParagraphStyle]):
    parts = [entry_header(entry, styles)]
    if entry.get("bullets"):
        parts.append(bullet_list(entry["bullets"], styles))
    elif entry.get("summary"):
        summary = Paragraph(entry["summary"], styles["body"])
        parts.extend([summary, Spacer(1, 1.4 * mm)])
    return KeepTogether(parts)


def build_pdf(language: str) -> Path:
    data = CV_DATA[language]
    styles = make_styles()
    output_path = OUTPUT_DIR / data["filename"]

    page_width, page_height = A4
    left_margin = 10.5 * mm
    right_margin = 10.5 * mm
    top_margin = 6.5 * mm
    bottom_margin = 6.5 * mm

    doc = BaseDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin,
        title=f'{data["name"]} - CV',
        author=data["name"],
        subject="Curriculum Vitae",
    )
    frame = Frame(
        left_margin,
        bottom_margin,
        page_width - left_margin - right_margin,
        page_height - top_margin - bottom_margin,
        id="main",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="cv", frames=[frame])
        ]
    )

    contacts = " | ".join(
        f'<link href="{href}" color="#000088">{label}</link>'
        for label, href in data["contacts"]
    )

    story = [
        Paragraph(data["name"], styles["name"]),
        Paragraph(data["headline"], styles["headline"]),
        Paragraph(contacts, styles["contact"]),
        Paragraph(data["availability"], styles["availability"]),
        Paragraph(data["profile"], styles["profile"]),
        section_heading(data["education_title"], styles),
        Spacer(1, 0.8 * mm),
        entry_flowables(data["education"], styles),
        section_heading(data["data_title"], styles),
        Spacer(1, 0.8 * mm),
    ]

    for entry in data["data_entries"]:
        story.append(entry_flowables(entry, styles))

    story.extend(
        [
            section_heading(data["projects_title"], styles),
            Spacer(1, 0.8 * mm),
        ]
    )

    for entry in data["projects"]:
        story.append(entry_flowables(entry, styles))

    story.extend(
        [
            section_heading(data["skills_title"], styles),
            Spacer(1, 0.8 * mm),
        ]
    )
    for label, value in data["skills"]:
        story.append(Paragraph(f"<b>{label}:</b> {value}", styles["body"]))
        story.append(Spacer(1, 0.5 * mm))

    story.extend(
        [
            section_heading(data["languages_title"], styles),
            Spacer(1, 0.8 * mm),
            Paragraph(data["languages"], styles["body"]),
            Spacer(1, 0.6 * mm),
            Paragraph(data["honor"], styles["body"]),
        ]
    )

    doc.build(story)
    return output_path


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    register_fonts()
    for language in ("en", "ru"):
        output_path = build_pdf(language)
        print(output_path)


if __name__ == "__main__":
    main()
