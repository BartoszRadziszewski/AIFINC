# -*- coding: utf-8 -*-
"""
Moduł danych dla AI FINC 2026/2027
Kanon literatury 12 modułów tematycznych programu studiów AI w finansach i controllingu przedsiębiorstw
Akademia Leona Koźmińskiego / KDF Dialog / ACCA
"""

MODULES_CATALOG = [
    {
        "id": 1,
        "name": "1. Podstawy AI dla menedżerów finansowych",
        "desc": "Fundamenty sztucznej inteligencji, transformacja roli dyrektora finansowego w Chief Value Officera (CVO), trendy rynkowe oraz adaptacja zwinnych modeli operacyjnych w finansach.",
        "mandatory": [
            {
                "authors": "ACCA",
                "title": "Chief Value Officer: The Important Evolution of the CFO",
                "year": 2023,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.accaglobal.com/content/dam/ACCA_Global/professional-insights/ChiefValueOfficer/PI-CHIEF-VALUE-OFFICER%20v6.pdf",
                "linkText": "Oficjalny raport ACCA",
                "notes": "Kluczowa koncepcja CVO dla Rozdziału 1 i 8 projektu dyplomowego."
            },
            {
                "authors": "IBM",
                "title": "The CEO’s Guide to Generative AI",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.ibm.com/downloads/documents/us-en/107a02e9bec8fbd9",
                "linkText": "Oficjalna publikacja IBM",
                "notes": "Wytyczne wdrażania GenAI z perspektywy kadry zarządzającej."
            },
            {
                "authors": "CFA Institute Research Foundation",
                "title": "Handbook of Artificial Intelligence and Big Data Applications in Investments",
                "year": 2023,
                "isbn": "nie dotyczy (raport)",
                "doi": "nie dotyczy",
                "url": "https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/rf-brief/ai-and-big-data-in-investments.pdf",
                "linkText": "Oficjalna publikacja CFA Institute",
                "notes": "Standard analiz ilościowych i uczenia maszynowego w inwestycjach."
            },
            {
                "authors": "ACCA",
                "title": "Transformational Journeys: Finance and the Agile Organisation",
                "year": 2021,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.accaglobal.com/content/dam/ACCA_Global/professional-insights/TransformationalJourneys/PI-TRANSFORMATIONAL-JOURNEYS-v5.pdf",
                "linkText": "Oficjalny raport ACCA",
                "notes": "Podstawowa publikacja z zakresu transformacji zwinnej organizacji finansowej."
            },
            {
                "authors": "Stanford Institute for Human-Centered AI (HAI)",
                "title": "Artificial Intelligence Index Report 2024",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://aiindex.stanford.edu/wp-content/uploads/2024/04/HAI_2024_AI-Index-Report.pdf",
                "linkText": "Oficjalny raport Stanford HAI",
                "notes": "Najbardziej wszechstronny roczny raport dojrzałości AI na świecie."
            }
        ],
        "supplementary": [
            {
                "authors": "World Economic Forum (WEF)",
                "title": "AI in Action: Beyond Experimentation to Transform Industry",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://reports.weforum.org/docs/WEF_AI_in_Action_Beyond_Experimentation_to_Transform_Industry_2025.pdf",
                "linkText": "Oficjalny raport WEF",
                "notes": "Skalowanie wdrożeń AI z fazy PoC do produkcji przemysłowej."
            },
            {
                "authors": "ACCA",
                "title": "AI: Artificial Intelligence in the Finance Profession",
                "year": 2023,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.accaglobal.com/content/dam/ACCA_Global/professional-insights/PI-AI-ACCA-POSITION%20v2.pdf",
                "linkText": "Oficjalna publikacja ACCA",
                "notes": "Stanowisko ACCA w sprawie kompetencji, etyki i szans AI w finansach."
            },
            {
                "authors": "Deloitte",
                "title": "State of Generative AI in the Enterprise",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www2.deloitte.com/content/dam/Deloitte/us/Documents/consulting/us-state-of-gen-ai-q4.pdf",
                "linkText": "Raport Deloitte",
                "notes": "Globalne badanie barier i zwrotu z inwestycji (ROI) w GenAI."
            },
            {
                "authors": "World Bank Group",
                "title": "Global Trends in AI Governance: Evolving Country Approaches",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie wskazano",
                "url": "https://documents1.worldbank.org/curated/en/099120224205026271/pdf/P1786161ad76ca0ae1ba3b1558ca4ff88ba.pdf",
                "linkText": "Oficjalna publikacja World Bank",
                "notes": "Porównanie podejść jurysdykcyjnych do zarządzania i nadzoru nad sztuczną inteligencją."
            }
        ]
    },
    {
        "id": 2,
        "name": "2. Zastosowanie AI w finansach i controllingu",
        "desc": "Praktyczne zastosowanie modeli analitycznych, algorytmów predykcyjnych i uczenia maszynowego w prognozowaniu finansowym, controllingu operacyjnym i zarządzaniu kapitałem.",
        "mandatory": [
            {
                "authors": "CFA Institute Research Foundation",
                "title": "Handbook of Artificial Intelligence and Big Data Applications in Investments",
                "year": 2023,
                "isbn": "nie dotyczy (raport)",
                "doi": "nie dotyczy",
                "url": "https://rpc.cfainstitute.org/sites/default/files/-/media/documents/article/rf-brief/ai-and-big-data-in-investments.pdf",
                "linkText": "Oficjalna publikacja CFA Institute",
                "notes": "Metody ML w wycenie aktywów, modelowaniu portfelowym i analizie sentymentu."
            }
        ],
        "supplementary": []
    },
    {
        "id": 3,
        "name": "3. Zarządzanie ryzykiem wdrażania AI w finansach",
        "desc": "Identyfikacja, pomiar i mitygacja ryzyk modelowych, operacyjnych i systemowych wynikających z wdrożeń AI; frameworki agentowe i odporność finansowa.",
        "mandatory": [
            {
                "authors": "Jajuga, K. (red.)",
                "title": "Zarządzanie ryzykiem",
                "publisher": "Wydawnictwo Naukowe PWN",
                "year": 2018,
                "isbn": "978-83-01-20054-1",
                "doi": "nie dotyczy",
                "url": "https://ksiegarnia.pwn.pl/Zarzadzanie-ryzykiem,756551008,p.html",
                "linkText": "Oficjalna księgarnia PWN",
                "notes": "Fundament polskiej literatury akademickiej w zakresie teorii i metod zarządzania ryzykiem finansowym."
            },
            {
                "authors": "Joshi, S.",
                "title": "Gen AI Agentic Framework for Financial Risk Management",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "do weryfikacji",
                "url": "https://www.researchgate.net/publication/388717177_Gen_AI_for_Market_Risk_and_Credit_Risk_Learn_Agentically_powered_Gen_AI_Gen_AI_Agentic_Framework_for_Financial_Risk_Management",
                "linkText": "Rekord publikacji ResearchGate",
                "notes": "Agentowe architektury AI w zarządzaniu ryzykiem rynkowym i kredytowym."
            }
        ],
        "supplementary": [
            {
                "authors": "Ranjan, P., Pandey, B.K., Avacharmal, R.",
                "title": "Artificial Intelligence and Financial Security",
                "publisher": "BPB Publications",
                "year": 2024,
                "isbn": "do weryfikacji według formatu wydania",
                "doi": "nie dotyczy",
                "url": "https://bpbonline.com",
                "linkText": "Oficjalny wydawca BPB Publications",
                "notes": "Bezpieczeństwo systemów finansowych, cyber-odporność i AI."
            },
            {
                "authors": "Galety, M.G., Claver, J.H., Sriharsha, A.V., Vajjhala, N.R., Natarajan, A.K.",
                "title": "Data Analytics and AI for Quantitative Risk Assessment and Financial Computation",
                "publisher": "IGI Global",
                "year": 2024,
                "isbn": "do weryfikacji (wersja drukowana / elektroniczna)",
                "doi": "do weryfikacji",
                "url": "https://www.igi-global.com",
                "linkText": "Oficjalny portal IGI Global",
                "notes": "Ilościowa ocena ryzyka, modelowanie stochastyczne i algorytmy obliczeniowe."
            },
            {
                "authors": "Financial Stability Board (FSB)",
                "title": "The Financial Stability Implications of Artificial Intelligence",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.fsb.org/uploads/P14112024.pdf",
                "linkText": "Oficjalny raport FSB",
                "notes": "Implikacje AI dla stabilności globalnego systemu finansowego i ryzyka zarażania."
            },
            {
                "authors": "World Economic Forum (WEF), Accenture",
                "title": "Artificial Intelligence in Financial Services",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://reports.weforum.org/docs/WEF_Artificial_Intelligence_in_Financial_Services_2025.pdf",
                "linkText": "Oficjalny raport WEF",
                "notes": "Zastosowanie AI i frameworki nadzoru w sektorze bankowym i ubezpieczeniowym."
            }
        ]
    },
    {
        "id": 4,
        "name": "4. Regulacje UE w zakresie AI oraz aspekty etyczne",
        "desc": "Zgodność z unijnym AI Act (Rozporządzenie 2024/1689), wytycznymi etycznymi KE, prawami podstawowymi, ochroną godności ludzkiej i zarządzaniem ryzykiem prawnym.",
        "mandatory": [
            {
                "authors": "Nowakowski, M.",
                "title": "Sztuczna inteligencja. Praktyczny przewodnik dla sektora innowacji finansowych",
                "year": 2023,
                "isbn": "do weryfikacji w rekordzie bibliotecznym",
                "doi": "nie dotyczy",
                "url": "https://www.ibuk.pl/fiszka/299675/sztuczna-inteligencja-praktyczny-przewodnik-dla-sektora-innowacji-finansowych.html?srsltid=AfmBOorBLgjaueEddglJDJFIi4aYAUas--yt_8j0CJnPbKxvCG-rw6BY",
                "linkText": "Oficjalny rekord IBUK",
                "notes": "Praktyczny przewodnik po prawnych aspektach innowacji finansowych i FinTech."
            },
            {
                "authors": "Masood, A., Dawe, H., Price, E. i in.",
                "title": "Responsible AI in the Enterprise: Practical AI Risk Management for Explainable, Auditable, and Safe Models with Hyperscalers and Azure OpenAI",
                "publisher": "Helion / Packt",
                "year": 2023,
                "isbn": "do weryfikacji według formatu",
                "doi": "nie dotyczy",
                "url": "https://helion.pl/ksiazki/responsible-ai-in-the-enterprise-practical-ai-risk-management-for-explainable-auditable-and-safe-adnan-masood-heather-dawe-ed-price-dr-ehsan-ad,e_3mp6.htm",
                "linkText": "Rekord książki w księgarni Helion",
                "notes": "Wyjaśnialność modeli (XAI), audytowalność i frameworki bezpiecznego wdrażania chmurowego."
            },
            {
                "authors": "Parlament Europejski i Rada UE",
                "title": "Rozporządzenie (UE) 2024/1689 z 13 czerwca 2024 r. w sprawie sztucznej inteligencji (EU AI Act)",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://eur-lex.europa.eu/legal-content/PL/TXT/PDF/?uri=OJ:L_202401689",
                "linkText": "Oficjalny tekst AI Act w EUR-Lex",
                "notes": "Unijny akt prawny o kluczowym znaczeniu (Rozdział 2 dysertacji)."
            },
            {
                "authors": "Niezależna Grupa Ekspertów Wysokiego Szczebla ds. AI (KE)",
                "title": "Wytyczne w zakresie etyki dotyczącej godnej zaufania sztucznej inteligencji",
                "publisher": "Komisja Europejska",
                "year": 2019,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.europarl.europa.eu/meetdocs/2014_2019/plmrep/COMMITTEES/JURI/DV/2019/11-06/Ethics-guidelines-AI_PL.pdf",
                "linkText": "Oficjalny dokument Komisji Europejskiej",
                "notes": "7 kluczowych wymagań etycznych dla godnej zaufania AI (Trustworthy AI)."
            },
            {
                "authors": "Komisja Europejska",
                "title": "Europejska deklaracja praw i zasad cyfrowych w cyfrowej dekadzie",
                "year": 2023,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://eur-lex.europa.eu/legal-content/PL/TXT/PDF/?uri=CELEX:32023C0123%2801%29",
                "linkText": "EUR-Lex CELEX:32023C0123(01)",
                "notes": "Zasady poszanowania prywatności i praw obywateli w społeczeństwie cyfrowym."
            }
        ],
        "supplementary": [
            {
                "authors": "Salvi del Pero, A., Wyckoff, P., Vourc’h, A.",
                "title": "Using Artificial Intelligence in the Workplace: What Are the Main Ethical Risks?",
                "publisher": "OECD",
                "year": 2022,
                "isbn": "nie dotyczy",
                "doi": "do weryfikacji",
                "url": "https://www.oecd-ilibrary.org",
                "linkText": "Baza OECD iLibrary",
                "notes": "Etyczne ryzyka automatyzacji miejsc pracy i relacji pracowniczych."
            },
            {
                "authors": "Office of the United Nations High Commissioner for Human Rights (OHCHR)",
                "title": "Addressing Business Model Related Human Rights Risks: A B-Tech Foundational Paper",
                "year": 2020,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.ohchr.org/en/business/b-tech-project",
                "linkText": "Oficjalna baza projektu B-Tech ONZ",
                "notes": "Prawa człowieka a modele biznesowe spółek technologicznych."
            }
        ]
    },
    {
        "id": 5,
        "name": "5. Warsztaty: Prowadzenie projektów AI w praktyce",
        "desc": "Inżynieria promptów, budowa aplikacji LLM, frameworki orkiestracji (LangChain, LangFlow), narzędzia deweloperskie i zwinne prowadzenie projektów AI w controllingu.",
        "mandatory": [
            {
                "authors": "Bomba, R. i in.",
                "title": "Large Language Models in Finance: Applications, Challenges and Opportunities",
                "year": 2023,
                "isbn": "nie dotyczy",
                "doi": "do weryfikacji",
                "url": "https://dl.acm.org/doi/fullHtml/10.1145/3604237.3626869",
                "linkText": "Rekord publikacji ACM (DOI: 10.1145/3604237.3626869)",
                "notes": "Zastosowanie modeli LLM w analizie rynkowej, sprawozdawczości i finansach."
            },
            {
                "authors": "Ketterer, H., Himmelreich, H.",
                "title": "The AI-First Company: How to Compete and Win with Artificial Intelligence",
                "publisher": "Portfolio / Penguin Random House",
                "year": 2021,
                "isbn": "978-0-593-33031-9",
                "doi": "nie dotyczy",
                "url": "https://www.penguinrandomhouse.com/books/669098/the-ai-first-company-by-ash-fontana/",
                "linkText": "Oficjalna publikacja wydawcy",
                "notes": "Budowa kultury i strategii AI-First w przedsiębiorstwie."
            },
            {
                "authors": "LangChain / LangFlow",
                "title": "LangChain and LangFlow Documentation",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://docs.langchain.com",
                "linkText": "Dokumentacja LangChain & LangFlow",
                "notes": "Orkiestracja agentowa, RAG (Retrieval-Augmented Generation) i łączenie modeli z bazami wektorowymi."
            },
            {
                "authors": "OpenAI",
                "title": "OpenAI Documentation & API Reference",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://platform.openai.com/docs",
                "linkText": "Oficjalna dokumentacja OpenAI",
                "notes": "Referencyjna dokumentacja modeli OpenAI, function calling, Structured Outputs i Embeddings."
            }
        ],
        "supplementary": [
            {
                "authors": "Anthropic",
                "title": "Anthropic Claude Documentation & Prompt Engineering Guide",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://docs.anthropic.com",
                "linkText": "Dokumentacja Anthropic",
                "notes": "Zaawansowane techniki promptingu i modele Claude dla systemów korporacyjnych."
            },
            {
                "authors": "Google Cloud",
                "title": "AI and Machine Learning Products Documentation (Vertex AI)",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://cloud.google.com/docs/ai-ml",
                "linkText": "Dokumentacja Google Cloud AI",
                "notes": "Architektura chmurowa, modele Gemini i skalowanie enterprise AI."
            },
            {
                "authors": "Singh, S.",
                "title": "Building LLM Powered Applications",
                "publisher": "O’Reilly Media",
                "year": 2024,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://www.oreilly.com",
                "linkText": "Oficjalna platforma O’Reilly",
                "notes": "Praktyczny podręcznik inżynierii aplikacji opartych na modelach językowych."
            },
            {
                "authors": "Warden, P.",
                "title": "Practical Deep Learning for Financial Applications",
                "publisher": "Manning Publications",
                "year": 2024,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://www.manning.com",
                "linkText": "Katalog Manning Publications",
                "notes": "Praktyczne zastosowanie uczenia głębokiego w aplikacjach finansowych."
            },
            {
                "authors": "Capgemini",
                "title": "TechnoVision: Top 5 Tech Trends to Watch in 2025",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.capgemini.com/wp-content/uploads/2025/01/Top-Tech-Trends-2025_Report.pdf",
                "linkText": "Oficjalny raport Capgemini",
                "notes": "Wiodące trendy technologiczne i architektoniczne na 2025 r."
            },
            {
                "authors": "IBM",
                "title": "5 trendów AI na 2025 rok",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://crn.pl/aktualnosci/5-trendow-ai-na-2025-rok/",
                "linkText": "Artykuł w portalu CRN Polska",
                "notes": "Prognozy IBM dotyczące rozwoju generatywnej AI i agentów autonomicznych."
            },
            {
                "authors": "McKinsey & Company",
                "title": "The Economic Potential of Generative AI: The Next Productivity Frontier",
                "year": 2023,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier",
                "linkText": "Oficjalna publikacja McKinsey",
                "notes": "Kwantyfikacja wartości dodanej GenAI w przekroju funkcji korporacyjnych."
            },
            {
                "authors": "Stanford Institute for Human-Centered AI (HAI)",
                "title": "Artificial Intelligence Index Report 2024",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://aiindex.stanford.edu/wp-content/uploads/2024/04/HAI_2024_AI-Index-Report.pdf",
                "linkText": "Oficjalny raport Stanford HAI",
                "notes": "Doroczny raport wskaźników rozwoju sztucznej inteligencji na świecie."
            },
            {
                "authors": "EY",
                "title": "Top 10 Opportunities for Technology Companies in 2025",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.ey.com/en_gl/insights/tech-sector/top-10-opportunities-for-technology-companies-in-2025",
                "linkText": "Oficjalna publikacja EY",
                "notes": "Szanse rynkowe i alokacja kapitału w spółkach technologicznych."
            },
            {
                "authors": "Gartner",
                "title": "AI and Emerging Technologies in 2025",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.gartner.com",
                "linkText": "Baza raportów Gartner",
                "notes": "Analiza wschodzących technologii sztucznej inteligencji na 2025 rok."
            },
            {
                "authors": "Deloitte",
                "title": "2025 Global Technology Outlook",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.deloitte.com",
                "linkText": "Portal Deloitte Global",
                "notes": "Globalne trendy i perspektywy technologiczne dla przedsiębiorstw."
            },
            {
                "authors": "Accenture",
                "title": "AI in Business 2025",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.accenture.com",
                "linkText": "Portal Accenture Insights",
                "notes": "Zastosowanie sztucznej inteligencji w operacjach biznesowych."
            },
            {
                "authors": "PwC Polska",
                "title": "Prognozy dotyczące sztucznej inteligencji w biznesie w 2025 r.",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.pwc.pl/pl/artykuly/prognozy-dotyczace-sztucznej-inteligencji-w-biznesie-w-2025-roku.html",
                "linkText": "Oficjalna publikacja PwC Polska",
                "notes": "Polski kontekst biznesowy i perspektywy adopcji technologii AI."
            },
            {
                "authors": "MIT Technology Review",
                "title": "The State of AI in 2025",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.technologyreview.com",
                "linkText": "Serwis MIT Technology Review",
                "notes": "Globalny stan i kierunki rozwoju systemów sztucznej inteligencji."
            }
        ]
    },
    {
        "id": 6,
        "name": "6. Elementy zarządzania procesami biznesowymi i danymi",
        "desc": "Zarządzanie procesowe (BPM), modelowanie BPMN 2.0, architektury Data Mesh, Data Fabric, inżynieria danych i hiperautomatyzacja na potrzeby wdrożeń AI.",
        "mandatory": [
            {
                "authors": "Dumas, M., La Rosa, M., Mendling, J., Reijers, H.",
                "title": "Business Process Management",
                "publisher": "PWN",
                "year": 2022,
                "isbn": "do weryfikacji względem wydania",
                "doi": "nie dotyczy",
                "url": "https://ksiegarnia.pwn.pl",
                "linkText": "Oficjalna księgarnia PWN",
                "notes": "Światowy podręcznik akademicki zarządzania procesami biznesowymi."
            },
            {
                "authors": "Szelągowski, M.",
                "title": "Zarządzanie procesowe w gospodarce wiedzy: tworzenie wartości z kapitału intelektualnego",
                "publisher": "Wydawnictwo Linia",
                "year": 2018,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://www.wydawnictwolinia.pl",
                "linkText": "Oficjalny wydawca Linia",
                "notes": "Koncepcja dynamicznego zarządzania procesami w organizacjach opartych na wiedzy."
            },
            {
                "authors": "Misiak, Z.",
                "title": "Modelowanie procesów biznesowych. BPMN 2.0 od podstaw",
                "publisher": "Onepress",
                "year": 2023,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://onepress.pl",
                "linkText": "Księgarnia Onepress",
                "notes": "Praktyczny przewodnik po notacji BPMN 2.0 dla controllingu i analityków."
            },
            {
                "authors": "Brzychczy, E., Rostek, K.",
                "title": "Cyfrowa analiza danych i procesów",
                "publisher": "PWE",
                "year": 2024,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://www.pwe.com.pl",
                "linkText": "Polskie Wydawnictwo Ekonomiczne (PWE)",
                "notes": "Nowoczesne metody cyfrowej analizy procesowej i Process Mining."
            }
        ],
        "supplementary": [
            {
                "authors": "Badakhshan, P., Scholta, H., Schmiedel, T., vom Brocke, J.",
                "title": "A Measurement Instrument for the Ten Principles of Good BPM",
                "publisher": "Business Process Management Journal, 29(6), 1762–1790",
                "year": 2023,
                "isbn": "nie dotyczy",
                "doi": "10.1108/BPMJ-08-2021-0549",
                "url": "https://doi.org/10.1108/BPMJ-08-2021-0549",
                "linkText": "Oficjalny rekord DOI",
                "notes": "Narzędzie pomiarowe dla 10 zasad efektywnego zarządzania procesowego."
            },
            {
                "authors": "Berniak-Woźny, J., Szelągowski, M.",
                "title": "Business Processes Nature Assessment Matrix",
                "publisher": "Aslib Journal of Information Management, 74(2), 244–264",
                "year": 2022,
                "isbn": "nie dotyczy",
                "doi": "10.1108/AJIM-04-2021-0110",
                "url": "https://doi.org/10.1108/AJIM-04-2021-0110",
                "linkText": "Oficjalny rekord DOI",
                "notes": "Matryca oceny natury procesów biznesowych i podatności na automatyzację."
            },
            {
                "authors": "Gartner",
                "title": "Predicts 2021: Accelerate Results Beyond RPA to Hyperautomation",
                "year": 2020,
                "isbn": "G00736497",
                "doi": "nie dotyczy",
                "url": "https://www.gartner.com",
                "linkText": "Raport Gartner (Research ID: G00736497)",
                "notes": "Przejście od prostego RPA do hiperautomatyzacji z udziałem modeli AI."
            },
            {
                "authors": "Helbin, T., Van Looy, A.",
                "title": "Business Process Ambidexterity and Its Impact on Business-IT Alignment",
                "publisher": "RCIS 2019",
                "year": 2019,
                "isbn": "nie dotyczy",
                "doi": "10.1109/RCIS.2019.8877073",
                "url": "https://doi.org/10.1109/RCIS.2019.8877073",
                "linkText": "Oficjalny rekord DOI (IEEE)",
                "notes": "Oburęczność procesowa i dopasowanie biznesowo-technologiczne."
            },
            {
                "authors": "Mendling, J., Pentland, B.T., Recker, J.",
                "title": "Building a Complementary Agenda for Business Process Management and Digital Innovation",
                "publisher": "European Journal of Information Systems, 29(3), 208–219",
                "year": 2020,
                "isbn": "nie dotyczy",
                "doi": "10.1080/0960085X.2020.1755207",
                "url": "https://doi.org/10.1080/0960085X.2020.1755207",
                "linkText": "Oficjalny rekord DOI (Taylor & Francis)",
                "notes": "Integracja zarządzania procesami z innowacjami cyfrowymi."
            },
            {
                "authors": "Szelągowski, M. i in.",
                "title": "Exploring the Diversity of Business Process Nature in Organizations Industry 4.0/5.0",
                "publisher": "Future Business Journal, 10, 118",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "10.1186/s43093-024-00395-5",
                "url": "https://doi.org/10.1186/s43093-024-00395-5",
                "linkText": "Oficjalny rekord DOI (Springer Open)",
                "notes": "Zróżnicowanie procesów w erze Przemysłu 4.0 i 5.0."
            },
            {
                "authors": "Zelt, S., Schmiedel, T., vom Brocke, J.",
                "title": "Understanding the Nature of Processes: An Information Processing Perspective",
                "publisher": "Business Process Management Journal, 24(1), 67–88",
                "year": 2018,
                "isbn": "nie dotyczy",
                "doi": "10.1108/BPMJ-05-2016-0102",
                "url": "https://doi.org/10.1108/BPMJ-05-2016-0102",
                "linkText": "Oficjalny rekord DOI",
                "notes": "Perspektywa przetwarzania informacji w badaniu natury procesów biznesowych."
            },
            {
                "authors": "Gontar, B.",
                "title": "Cyfryzacja zarządzania danymi w organizacji",
                "publisher": "SIW Znak",
                "year": 2019,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://www.znak.com.pl/p/cyfryzacja-zarzadzanie-danymi-w-organizacji-120334",
                "linkText": "Rekord książki w księgarni Znak",
                "notes": "Architektura ładu danych (Data Governance) w polskich realiach."
            },
            {
                "authors": "Plich, P.",
                "title": "Zarządzanie zbiorami danych o dużej skali. Nowoczesna architektura z siatką danych i technologią Data Fabric",
                "publisher": "Helion",
                "year": 2024,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://helion.pl",
                "linkText": "Oficjalna księgarnia Helion",
                "notes": "Nowoczesne paradygmaty Data Mesh i Data Fabric dla analityki korporacyjnej."
            },
            {
                "authors": "Reis, J., Housley, M.",
                "title": "Inżynieria danych w praktyce. Kluczowe koncepcje i najlepsze technologie",
                "publisher": "Helion",
                "year": 2023,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://www.empik.com/inzynieria-danych-w-praktyce-kluczowe-koncepcje-i-najlepsze-technologie-joe-reis-matt-housley,p1379632762,ksiazka-p",
                "linkText": "Księgarnia Empik / Helion",
                "notes": "Fundament inżynierii danych, cykl życia danych (Data Engineering Lifecycle)."
            }
        ]
    },
    {
        "id": 7,
        "name": "7. Strategia transformacji cyfrowej oparta na AI",
        "desc": "Budowa strategii AI w przedsiębiorstwie, rekonfiguracja modelu operacyjnego, przezwyciężanie silosów organizacyjnych i generowanie mierzalnej wartości biznesowej.",
        "mandatory": [
            {
                "authors": "McKinsey & Company",
                "title": "The State of AI: How Organizations Are Rewiring to Capture Value",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.mckinsey.com/~/media/mckinsey/business%20functions/mckinsey%20digital/our%20insights/a%20generative%20ai%20reset%20rewiring%20to%20turn%20potential%20into%20value%20in%202024/a-generative-ai-reset-rewiring-to-turn-potential-into-value-in-2024.pdf?shouldIndex=false",
                "linkText": "Oficjalny raport McKinsey",
                "notes": "Przebudowa architektury procesów i kompetencji w celu monetyzacji potencjału AI."
            },
            {
                "authors": "Deloitte",
                "title": "State of Generative AI in the Enterprise",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/campaigns/2025/us-state-of-gen-ai-2024-q4.pdf",
                "linkText": "Oficjalny raport Deloitte",
                "notes": "Analiza dojrzałości, zwrotu z inwestycji (ROI) i skalowania generatywnej AI."
            }
        ],
        "supplementary": []
    },
    {
        "id": 8,
        "name": "8. Warsztaty: Profesjonalny dobór oraz umowa z doradcą AI",
        "desc": "Prawne i biznesowe aspekty kontraktowania usług doradczych, umów wdrożeniowych AI, klauzul SLA, praw autorskich (IP), odpowiedzialności za błędy modeli i ochrony poufności.",
        "mandatory": [
            {
                "authors": "Parlament Europejski",
                "title": "EU AI Act, tekst przyjęty 13 marca 2024 r.",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.europarl.europa.eu/doceo/document/TA-9-2024-0138_EN.html",
                "linkText": "Dokument Parlamentu Europejskiego",
                "notes": "Podstawa prawna formułowania wymogów zgodności w kontraktach z dostawcami AI."
            },
            {
                "authors": "Sejm RP",
                "title": "Ustawa z 10 maja 2018 r. o ochronie danych osobowych",
                "year": 2018,
                "isbn": "nie dotyczy",
                "doi": "Dz.U. 2018 poz. 1000",
                "url": "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20180001000",
                "linkText": "Oficjalny tekst ISAP",
                "notes": "Przepisy krajowe o ochronie danych osobowych i nadzorze UODO."
            },
            {
                "authors": "Parlament Europejski i Rada UE",
                "title": "Rozporządzenie (UE) 2016/679, RODO",
                "year": 2016,
                "isbn": "nie dotyczy",
                "doi": "CELEX: 32016R0679",
                "url": "https://eur-lex.europa.eu/legal-content/PL/ALL/?uri=CELEX%3A32016R0679",
                "linkText": "Oficjalny tekst EUR-Lex",
                "notes": "Art. 22 RODO (zautomatyzowane podejmowanie decyzji i profilowanie), umowy powierzenia danych (DPA)."
            },
            {
                "authors": "Sejm RP",
                "title": "Ustawa z 23 kwietnia 1964 r. – Kodeks cywilny, z późniejszymi zmianami",
                "year": 1964,
                "isbn": "nie dotyczy",
                "doi": "Dz.U. 1964 nr 16 poz. 93",
                "url": "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU19640160093",
                "linkText": "Oficjalny tekst ISAP",
                "notes": "Umowa o dzieło, zlecenie, klauzule należytej staranności, odpowiedzialność kontraktowa i kary umowne."
            }
        ],
        "supplementary": [
            {
                "authors": "Parlament Europejski i Rada UE",
                "title": "Dyrektywa (UE) 2022/2555, NIS2",
                "year": 2022,
                "isbn": "nie dotyczy",
                "doi": "ELI: dir/2022/2555",
                "url": "https://eur-lex.europa.eu/eli/dir/2022/2555",
                "linkText": "Oficjalny tekst EUR-Lex",
                "notes": "Wymogi cyberbezpieczeństwa dla podmiotów kluczowych i łańcucha dostaw IT/AI."
            },
            {
                "authors": "Parlament Europejski i Rada UE",
                "title": "Rozporządzenie (UE) 2023/2854, Data Act",
                "year": 2023,
                "isbn": "nie dotyczy",
                "doi": "CELEX: 32023R2854",
                "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32023R2854&qid=1704709568425",
                "linkText": "Oficjalny tekst EUR-Lex",
                "notes": "Dostęp do danych przemysłowych, przenoszalność usług chmurowych i ochrona przed nieuczciwymi klauzulami."
            }
        ]
    },
    {
        "id": 9,
        "name": "9. Wschodzące technologie i ich wpływ na finanse",
        "desc": "Technologie przełomowe: blockchain, rozproszone rejestry (DLT), kryptografia postkwantowa (Post-Quantum Cryptography) oraz technologie immersyjne.",
        "mandatory": [
            {
                "authors": "Tapscott, D., Tapscott, A.",
                "title": "Blockchain Revolution: How the Technology Behind Bitcoin and Other Cryptocurrencies Is Changing the World",
                "publisher": "Portfolio / Penguin Random House",
                "year": 2018,
                "isbn": "zależny od wydania",
                "doi": "nie dotyczy",
                "url": "https://www.penguinrandomhouse.com",
                "linkText": "Oficjalny katalog Penguin Random House",
                "notes": "Klasyczne opracowanie transformacji transakcji, zaufania i transferu wartości przez DLT."
            },
            {
                "authors": "IBM",
                "title": "Secure the Post-Quantum Future",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.ibm.com/quantum/quantum-safe",
                "linkText": "Oficjalna baza IBM Quantum Safe",
                "notes": "Ochrona infrastruktury finansowej i szyfrowania przed atakami z użyciem komputerów kwantowych."
            }
        ],
        "supplementary": [
            {
                "authors": "Ball, M.",
                "title": "The Metaverse: And How It Will Revolutionize Everything",
                "publisher": "Liveright / W.W. Norton",
                "year": 2022,
                "isbn": "do weryfikacji według wydania",
                "doi": "nie dotyczy",
                "url": "https://wwnorton.com",
                "linkText": "Oficjalny wydawca W.W. Norton",
                "notes": "Gospodarka wirtualna, infrastruktura cyfrowa i nowe modele monetyzacji."
            }
        ]
    },
    {
        "id": 10,
        "name": "10. Wdrażanie rozwiązań AI w finansach i controllingu: analiza przypadków",
        "desc": "Szczegółowa analiza wdrożeń case studies w instytucjach finansowych i przedsiębiorstwach: scoring kredytowy, analityka predykcyjna, automatyczne raportowanie zarządcze.",
        "mandatory": [
            {
                "authors": "Sriram, H.K.",
                "title": "Leveraging Artificial Intelligence and Machine Learning for Next-Generation Credit Risk Assessment Models",
                "publisher": "East Asian Journal of STEM",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie wskazano",
                "url": "https://esa-research.com/index.php/eajse/article/view/4",
                "linkText": "Oficjalny rekord artykułu (EAJSE)",
                "notes": "Nowoczesne modele ML w ocenie ryzyka kredytowego i predykcji defaultu."
            },
            {
                "authors": "World Economic Forum (WEF), Accenture",
                "title": "Artificial Intelligence in Financial Services",
                "year": 2025,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://reports.weforum.org/docs/WEF_Artificial_Intelligence_in_Financial_Services_2025.pdf",
                "linkText": "Oficjalny raport WEF",
                "notes": "Przegląd przypadków użycia AI w bankowości i zarządzaniu aktywami."
            }
        ],
        "supplementary": [
            {
                "authors": "Pavlović, M., Gligorić, C., Zdravković, F.",
                "title": "Revolutionizing Management Accounting: The Role of Artificial Intelligence in Predictive Analytics, Automated Reporting, and Decision-Making",
                "publisher": "Business & Management Compass",
                "year": 2024,
                "isbn": "nie dotyczy",
                "doi": "nie wskazano",
                "url": "https://bi.ue-varna.bg/ojs/index.php/bmc/article/view/77/19",
                "linkText": "Oficjalny rekord artykułu (BMC)",
                "notes": "Rachunkowość zarządcza wspierana AI, automatyzacja sprawozdawczości i systemy wspomagania decyzji."
            }
        ]
    },
    {
        "id": 11,
        "name": "11. Komunikacja AI i kultura start-upowa",
        "desc": "Zarządzanie zmianą technologiczną, kultura eksperymentowania i innowacji, zwinne metodyki (Agile), przezwyciężanie oporu personelu oraz budowa organizacji 'AI First'.",
        "mandatory": [
            {
                "authors": "Rubin, J., Grabowski, W., Naumiuk, M.",
                "title": "Zwinnologia 2.0: Agile w zarządzaniu zmianą",
                "publisher": "MT Biznes",
                "year": 2025,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://mtbiznes.pl",
                "linkText": "Oficjalna księgarnia MT Biznes",
                "notes": "Zwinne zarządzanie projektami i transformacją w polskich przedsiębiorstwach."
            },
            {
                "authors": "Brotman, A., Sack, A.",
                "title": "AI First: The Playbook for a Future-Proof Business and Brand",
                "publisher": "Harvard Business Review Press",
                "year": 2025,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://store.hbr.org",
                "linkText": "Oficjalna księgarnia HBR",
                "notes": "Praktyczny podręcznik budowy przewagi rynkowej opartej na sztucznej inteligencji."
            },
            {
                "authors": "Czopek, A. (red.)",
                "title": "Zarządzanie – komunikacja – nowoczesność",
                "publisher": "Wydawnictwo FNCE",
                "year": 2023,
                "isbn": "do weryfikacji",
                "doi": "nie dotyczy",
                "url": "https://fnce.pl",
                "linkText": "Oficjalny wydawca FNCE",
                "notes": "Komunikacja wewnętrzna, nowoczesne struktury organizacyjne i przywództwo cyfrowe."
            }
        ],
        "supplementary": []
    },
    {
        "id": 12,
        "name": "12. Projekt końcowy: opracowanie i wdrożenie rozwiązania AI",
        "desc": "Zwieńczenie programu studiów podyplomowych – kompleksowe opracowanie koncepcji i wdrożenia rozwiązania AI dla wybranej spółki z indeksu WIG140 GPW (lub macierzystej).",
        "mandatory": [
            {
                "authors": "Akademia Leona Koźmińskiego / KDF Dialog / ACCA",
                "title": "Standardy i wytyczne merytoryczne projektu końcowego AI FINC (8 Rozdziałów)",
                "year": 2026,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "#tab-navigator",
                "linkText": "Nawigator 8 Rozdziałów Dysertacji w Hubie",
                "notes": "Projekt dyplomowy integruje literaturę z Modułów 1–11 w strukturze 8 rozdziałów."
            }
        ],
        "supplementary": [
            {
                "authors": "Giełda Papierów Wartościowych w Warszawie",
                "title": "Baza spółek giełdowych WIG140 & GPW Benchmark",
                "year": 2026,
                "isbn": "nie dotyczy",
                "doi": "nie dotyczy",
                "url": "https://www.gpw.pl",
                "linkText": "Oficjalny portal GPW",
                "notes": "Dane sektorowe, studia przypadków, wskaźniki i kody pobierania danych finansowych API."
            }
        ]
    }
]

REPEATED_ITEMS = [
    {
        "authors": "CFA Institute Research Foundation",
        "title": "Handbook of Artificial Intelligence and Big Data Applications in Investments (2023)",
        "modules": "Moduł 1 oraz Moduł 2",
        "status": "Lektura bazowa w obu modułach",
        "note": "W M1 stanowi ogólny przegląd innowacji inwestycyjnych, w M2 techniczne metody ilościowe w controllingu."
    },
    {
        "authors": "ACCA",
        "title": "Transformational Journeys: Finance and the Agile Organisation (2021)",
        "modules": "Moduł 1",
        "status": "Lektura obowiązkowa",
        "note": "Kluczowa publikacja z zakresu zwinności zespołów finansowych i controllingu."
    },
    {
        "authors": "Stanford Institute for Human-Centered AI (HAI)",
        "title": "Artificial Intelligence Index Report 2024",
        "modules": "Moduł 1 oraz Moduł 5",
        "status": "Lektura podstawowa i warsztatowa",
        "note": "Syntetyczny raport makro o trendach AI wykorzystywany w fundamentach (M1) i warsztatach narzędziowych (M5)."
    },
    {
        "authors": "Deloitte",
        "title": "State of Generative AI in the Enterprise (2025)",
        "modules": "Moduł 1 oraz Moduł 7",
        "status": "Lektura strategiczna",
        "note": "Badanie dojrzałości GenAI, kluczowe dla formułowania strategii transformacji cyfrowej (Rozdział 8)."
    },
    {
        "authors": "World Economic Forum (WEF), Accenture",
        "title": "Artificial Intelligence in Financial Services (2025)",
        "modules": "Moduł 3 oraz Moduł 10",
        "status": "Lektura analityczna i wdrożeniowa",
        "note": "W M3 omawia ryzyka stabilności i odporności, w M10 stanowi materiał do analizy przypadków wdrożeniowych."
    },
    {
        "authors": "Parlament Europejski i Rada UE",
        "title": "EU AI Act (Rozporządzenie UE 2024/1689)",
        "modules": "Moduł 4 oraz Moduł 8",
        "status": "Lektura prawna i regulacyjna",
        "note": "W M4 występuje jako ramy prawne i etyczne AI; w M8 jako norma kwalifikacji systemów w umowach z doradcą."
    },
    {
        "authors": "The AI-First Company",
        "title": "The AI-First Company: How to Compete and Win with Artificial Intelligence",
        "modules": "Moduł 5",
        "status": "Lektura obowiązkowa w M5",
        "note": "Budowa przewagi konkurencyjnej organizacji w oparciu o architekturę AI-First."
    }
]
