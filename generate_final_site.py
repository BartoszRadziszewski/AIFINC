# -*- coding: utf-8 -*-
"""
Generator kompletnego portalu AI FINC Academic Research Hub v1.2
Akademia Leona Koźmińskiego / KDF Dialog / ACCA
"""
import os
import sys
import json
import prepare_data

# Pobieramy bazę ALL_ITEMS
with open("database_dump_v12.json", "r", encoding="utf-8") as f:
    DATABASE = json.load(f)

# 8 Rozdziałów projektu dyplomowego
CHAPTERS = [
    {
        "id": 1,
        "title": "Rozdział 1: Wstęp i zdefiniowanie problemu biznesowego",
        "reqBadge": "Waga: Fundament koncepcyjny",
        "desc": "Dokładna identyfikacja problemów biznesowych (błędy, czasochłonność, koszty), mierzalny cel projektu, granice rozwiązania i kryteria sukcesu audytu w wybranej spółce WIG140.",
        "items": [
            { "id": "ch1_1", "text": "1.1 Opis problemu biznesowego (efektywność operacyjna, ryzyko, predykcja cash flow, controlling marż w wybranej spółce WIG140)" },
            { "id": "ch1_2", "text": "1.2 Cel budowy rozwiązania (mierzalny, osiągalny, powiązany ze strategią organizacji i wskaźnikami KPI)" },
            { "id": "ch1_3", "text": "1.3 Zakres budowy (jasne zdefiniowanie funkcjonalności systemu AI i użytych zbiorów danych)" },
            { "id": "ch1_4", "text": "1.4 Wyłączenia i ograniczenia (co NIE wchodzi w zakres, warunki brzegowe, kiedy AI nie ma zastosowania)" },
            { "id": "ch1_5", "text": "1.5 Ocena i audytowalność (jak mierzona będzie efektywność, jakość przetwarzania oraz okresowa weryfikacja)" }
        ]
    },
    {
        "id": 2,
        "title": "Rozdział 2: Zgodność z regulacjami oraz aspekty etyczne",
        "reqBadge": "Waga: Wymóg patronatu ACCA",
        "desc": "Zapewnienie zgodności z EU AI Act 2024/1689, RODO art. 22 i Basel III, minimalizacja ryzyk regulacyjnych, zapobieganie stronniczości (bias) i zapewnienie wyjaśnialności (XAI).",
        "items": [
            { "id": "ch2_1", "text": "2.1 Regulacje (analiza zgodności z EU AI Act 2024/1689, RODO art. 22, wytycznymi EBA/KNF i Basel III)" },
            { "id": "ch2_2", "text": "2.2 Zarządzanie ryzykiem regulacyjnym (matryca ryzyk prawnych i plan ich mitygacji)" },
            { "id": "ch2_3", "text": "2.3 Bezstronność i sprawiedliwość (mechanizmy pomiaru i redukcji biasu w danych i algorytmach decyzyjnych)" },
            { "id": "ch2_4", "text": "2.4 Przejrzystość i wyjaśnialność (mechanizmy XAI – np. SHAP, LIME – w decyzjach finansowych)" }
        ]
    },
    {
        "id": 3,
        "title": "Rozdział 3: Projektowanie rozwiązania",
        "reqBadge": "Waga: Architektura systemowa",
        "desc": "Kompleksowa architektura systemu AI: diagramy BPMN 2.0, przepływy integracyjne ERP/EPM, wybór infrastruktury (chmura hybrydowa/on-premise) i model bezpieczeństwa.",
        "items": [
            { "id": "ch3_1", "text": "3.1 Architektura rozwiązania (diagram wysokopoziomowy, warstwa danych, silnik AI, interfejs użytkownika)" },
            { "id": "ch3_2", "text": "3.2 Integracja z istniejącymi procesami i systemami (ERP, CRM, hurtownie danych, Business Intelligence)" },
            { "id": "ch3_3", "text": "3.3 Uzasadnienie doboru technologii i modeli (kryteria wyboru algorytmów, narzędzi, bibliotek i chmury)" },
            { "id": "ch3_4", "text": "3.4 Skalowalność i utrzymanie (architektura chmurowa, konteneryzacja, mikroserwisy, procedury DR/BCP)" },
            { "id": "ch3_5", "text": "3.5 Bezpieczeństwo i prywatność danych (szyfrowanie end-to-end, kontrola dostępu RBAC, anonimizacja)" }
        ]
    },
    {
        "id": 4,
        "title": "Rozdział 4: Zarządzanie danymi",
        "reqBadge": "Waga: Jakość fundamentu danych",
        "desc": "Pozyskiwanie i inżynieria danych: pipeline ETL/ELT, walidacja jakości danych finansowych, etykietowanie, obsługa braków oraz przeciwdziałanie dryfowi danych (Data Drift).",
        "items": [
            { "id": "ch4_1", "text": "4.1 Źródła danych (identyfikacja danych wewnętrznych spółki oraz zewnętrznych – giełdowych, makro)" },
            { "id": "ch4_2", "text": "4.2 Przygotowanie i wstępne przetwarzanie (czyszczenie, obsługa braków, imputacja, standaryzacja)" },
            { "id": "ch4_3", "text": "4.3 Zapewnienie jakości danych (metodyki Data Quality, walidacja spójności finansowej)" },
            { "id": "ch4_4", "text": "4.4 Inżynieria cech (konstrukcja zmiennych objaśniających, wskaźników finansowych, lagów czasowych)" },
            { "id": "ch4_5", "text": "4.5 Bezpieczeństwo danych w procesie przetwarzania (retencja, izolacja środowisk treningowych)" }
        ]
    },
    {
        "id": 5,
        "title": "Rozdział 5: Wybór modeli, uczenie i ewaluacja",
        "reqBadge": "Waga: Silnik analityczny AI",
        "desc": "Dobór algorytmów (ML, Deep Learning, LLM, agenci autonomiczni), protokół walidacji krzyżowej (TimeSeriesSplit), metryki biznesowe i techniczne (RMSE, MAE, AUC, F1).",
        "items": [
            { "id": "ch5_1", "text": "5.1 Dobór algorytmów (uzasadnienie: modele regresyjne, drzewa decyzyjne XGBoost, sieci rekurencyjne, LLM)" },
            { "id": "ch5_2", "text": "5.2 Architektura i strojenie hiperparametrów (Optuna, GridSearch, walidacja krzyżowa TimeSeries)" },
            { "id": "ch5_3", "text": "5.3 Trening i walidacja modeli (podział train/val/test z uwzględnieniem chronologii danych)" },
            { "id": "ch5_4", "text": "5.4 Metryki ewaluacji (dokładność techniczna: RMSE, MAE, AUC vs metryki biznesowe controllingu)" },
            { "id": "ch5_5", "text": "5.5 Analiza błędów i ograniczenia modeli (badanie residuów, przypadki brzegowe, scenariusze stresowe)" }
        ]
    },
    {
        "id": 6,
        "title": "Rozdział 6: Implementacja i wdrożenie",
        "reqBadge": "Waga: Inżynieria MLOps",
        "desc": "Wdrożenie produkcyjne MLOps: konteneryzacja Docker/Kubernetes, CI/CD pipeline, monitoring dryfu modelu (Concept Drift) oraz procedury awaryjnego przełączania (failover).",
        "items": [
            { "id": "ch6_1", "text": "6.1 Architektura wdrożenia (środowisko produkcyjne, konteneryzacja Docker/K8s, API REST/gRPC)" },
            { "id": "ch6_2", "text": "6.2 Pipeline CI/CD/CT (automatyzacja testów, wdrażania kodu i ciągłego dotrenowywania modeli)" },
            { "id": "ch6_3", "text": "6.3 Monitoring produkcyjny (MLOps: śledzenie opóźnień, metryk predykcji, dryfu danych i modeli)" },
            { "id": "ch6_4", "text": "6.4 Plan testów akceptacyjnych (UAT z udziałem controllerów i dyrektorów finansowych)" },
            { "id": "ch6_5", "text": "6.5 Plan wycofania i procedury awaryjne (fallback do modeli heurystycznych w przypadku awarii)" }
        ]
    },
    {
        "id": 7,
        "title": "Rozdział 7: Zarządzanie zmianą i dokumentacja",
        "reqBadge": "Waga: Transformacja ludzi i procesów",
        "desc": "Zarządzanie zmianą organizacyjną (metodyka ADKAR / Kotter), program szkoleń dla departamentu finansowego, dokumentacja techniczna i użytkownika.",
        "items": [
            { "id": "ch7_1", "text": "7.1 Strategia zarządzania zmianą (analiza interesariuszy, mapa oporu, komunikacja korzyści)" },
            { "id": "ch7_2", "text": "7.2 Program szkoleń i upskillingu (warsztaty prompt engineeringu i interpretacji wyników AI dla finansistów)" },
            { "id": "ch7_3", "text": "7.3 Dokumentacja użytkownika końcowego (podręcznik operacyjny dla controllera, instrukcje 'krok po kroku')" },
            { "id": "ch7_4", "text": "7.4 Dokumentacja techniczna i architektoniczna (karty modeli Model Cards, schematy baz danych)" },
            { "id": "ch7_5", "text": "7.5 Plan komunikacji wewnętrznej (harmonogram wdrożenia, dyżury eksperckie, zbieranie feedbacku)" }
        ]
    },
    {
        "id": 8,
        "title": "Rozdział 8: Podsumowanie, ocena efektów i wnioski",
        "reqBadge": "Waga: Weryfikacja ROI & CVO",
        "desc": "Ocena efektywności biznesowej: kalkulacja ROI, NPV, TCO, redukcja czasu procesów finansowych, benchmarking dojrzałości oraz roadmapa rozwoju.",
        "items": [
            { "id": "ch8_1", "text": "8.1 Ocena efektywności: twarde porównanie wskaźników przed i po wdrożeniu AI" },
            { "id": "ch8_2", "text": "8.2 Zwrot z inwestycji (szacunkowe ROI, NPV, TCO, redukcja kosztów operacyjnych)" },
            { "id": "ch8_3", "text": "8.3 Wnioski strategiczne i implikacje dla modelu operacyjnego organizacji" },
            { "id": "ch8_4", "text": "8.4 Benchmarking rynkowy i pozycjonowanie dojrzałości AI spółki na tle konkurencji" },
            { "id": "ch8_5", "text": "8.5 Uczenie się organizacji i zarządzanie zmianą kulturową w zespole finansowym" },
            { "id": "ch8_6", "text": "8.6 Refleksja etyczna i identyfikacja ryzyk wtórnych (zgodnie z wytycznymi)" },
            { "id": "ch8_7", "text": "8.7 Rekomendowane kierunki dalszego rozwoju rozwiązania (roadmapa)" }
        ]
    }
]

# 6 sektorów WIG140
WIG_SECTORS = [
    {
        "sector": "Bankowość, Ubezpieczenia & Fintech",
        "tickers": "PKO, PEKAO, SPL, ING, ALR, KRU, PZU",
        "problem": "Wysoki koszt manualnego uzgadniania rozrachunków, opóźnienia w ocenie ryzyka płynności, podatność na fraudy i wymogi raportowania EBA/KNF.",
        "useCases": "• Predykcja niewypłacalności kontrahentów (ML scoring)\n• Ciągły monitoring transakcji i detekcja anomalii AML\n• Asystent LLM w audycie sprawozdawczości ostrożnościowej",
        "dataSources": "Sprawozdania finansowe (ESEF), bazy NBP API, wskaźniki BIK/KRD, publiczne komunikaty ESPI/EBI.",
        "pythonCode": "import yfinance as yf\nbank = yf.Ticker('PKO.WA')\ndf = bank.history(period='2y')\nprint(df.head())"
    },
    {
        "sector": "Przemysł, Produkcja & Górnictwo",
        "tickers": "KGHM, PKN, KTY, ENA, CAR, APR, ALM",
        "problem": "Wahania cen energii i surowców w rachunku kosztów ciągłych, trudności w predykcji dynamicznego BOM oraz optymalizacji zapasów (working capital).",
        "useCases": "• Predykcyjne planowanie kosztów energii i materiałów\n• Dynamiczny budżet kosztów wydziałowych w czasie rzeczywistym\n• Automatyczne uzgadnianie faktur surowcowych w SAP ERP",
        "dataSources": "Ceny surowców LME/TGE, sprawozdania jednostkowe i skonsolidowane ESEF, dane Stooq CSV.",
        "pythonCode": "import pandas as pd\nurl = 'https://stooq.pl/q/d/l/?s=kgh&i=d'\ndf = pd.read_csv(url)\nprint(df.tail())"
    },
    {
        "sector": "Handel, E-Commerce & Logistyka",
        "tickers": "LPP, DNP, CCC, ALE, EOP, ABS",
        "problem": "Presja marżowa, koszty zwrotów, zmienność popytu sezonowego oraz trudności w cash flow forecasting w cyklu krótkoterminowym.",
        "useCases": "• Predykcja cash flow i należności z użyciem XGBoost/Prophet\n• Dynamiczne zarządzanie rabatami i marżą w retailu\n• Automatyzacja uzgadniania płatności wielokanałowych (Omnichannel)",
        "dataSources": "Raporty kwartalne, wskaźniki sprzedaży LFL, stopa inflacji z GUS BDL API, kursy walut NBP.",
        "pythonCode": "import requests\nnbp = requests.get('https://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json').json()\nprint('Kurs EUR:', nbp['rates'][0]['mid'])"
    },
    {
        "sector": "Energetyka, Media & Utilities",
        "tickers": "PGE, TPE, ENA, ZEPAK, KGN",
        "problem": "Koszty uprawnień do emisji CO2 (EU ETS), zmienność cen na TGE, zarządzanie CAPEX projektów transformacji energetycznej i raportowanie ESG.",
        "useCases": "• Prognozowanie przepływów pieniężnych z wieloletnich inwestycji OZE\n• Automatyczna ekstrakcja wskaźników CSRD/ESG z raportów niefinansowych\n• Ocena ryzyka kredytowego portfela klientów biznesowych",
        "dataSources": "Komunikaty ESPI o cenach energii, sprawozdania niefinansowe ESEF, notowania uprawnień EUA.",
        "pythonCode": "import yfinance as yf\npge = yf.Ticker('PGE.WA')\nprint(pge.financials)"
    },
    {
        "sector": "Technologie, TMT & IT",
        "tickers": "ACP, CMR, OPL, CPS, 11B, TEN",
        "problem": "Rozliczanie kosztów projektów R&D, alokacja czasu pracy zespołów deweloperskich, rozpoznawanie przychodów z umów długoterminowych (MSSF 15).",
        "useCases": "• Predykcja rentowności kontraktów IT na bazie historycznych wdrożeń\n• Automatyzacja monitorowania SLA i kosztów infrastruktury chmurowej\n• Agentowe wsparcie audytu wewnętrznego i wyceny IP",
        "dataSources": "Portfel kontraktów z ESPI, sprawozdania roczne ESEF, dane branżowe KDF Dialog.",
        "pythonCode": "import yfinance as yf\nasseco = yf.Ticker('ACP.WA')\nprint(asseco.info['operatingMargins'])"
    },
    {
        "sector": "Budownictwo & Infrastruktura",
        "tickers": "BDX, TOR, ERB, DOM, ATAL",
        "problem": "Ryzyko przekroczenia budżetu inwestycji (cost overrun), indeksacja cen materiałów w kontraktach, wahania kapitału obrotowego i gwarancje bankowe.",
        "useCases": "• Predykcja rentowności kontraktu budowlanego w całym cyklu życia\n• Wczesne wykrywanie anomalii w kosztorysach podwykonawców\n• Modelowanie rezerw na ryzyka kontraktowe",
        "dataSources": "Komunikaty o wygranych przetargach ESPI, wskaźniki cen produkcji budowlanej GUS, sprawozdania GPW.",
        "pythonCode": "import yfinance as yf\nbdx = yf.Ticker('BDX.WA')\nprint(bdx.balance_sheet)"
    }
]

print("Generowanie szablonu strony HTML...")

# Generujemy kod HTML
HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI FINC – Academic Research Hub | Akademia Leona Koźmińskiego</title>
    <meta name="description" content="Autonomiczny pulpit badawczo-dydaktyczny wspierający słuchaczy studiów podyplomowych AI w finansach i controllingu przedsiębiorstw. Kanon literatury badawczo-dydaktycznej 12 modułów tematycznych 2026/2027.">
    <meta name="author" content="Bartosz Radziszewski">
    
    <style>
        :root {{
            --bg-color: #f4f7fa;
            --text-color: #1e293b;
            --card-bg: #ffffff;
            --primary-color: #0b2545; /* ALK Navy */
            --primary-hover: #133a6b;
            --secondary-color: #b4865e; /* ALK Gold */
            --secondary-hover: #966f4c;
            --accent-blue: #464feb;
            --border-color: #e2e8f0;
            --tag-bg: #f1f5f9;
            --tag-text: #334155;
            --callout-bg: #f8fafc;
            --hover-shadow: 0 10px 25px -5px rgba(11, 37, 69, 0.08), 0 8px 10px -6px rgba(11, 37, 69, 0.04);
            --id-badge-bg: #e0f2fe;
            --id-badge-text: #0369a1;
            --id-badge-border: #bae6fd;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --table-border: #e6e6e6;
            --table-header-bg: #f5f5f5;
        }}

        [data-theme="dark"] {{
            --bg-color: #0b1120;
            --text-color: #f8fafc;
            --card-bg: #1e293b;
            --primary-color: #38bdf8;
            --primary-hover: #7dd3fc;
            --secondary-color: #e2b17a;
            --secondary-hover: #f3cda2;
            --accent-blue: #818cf8;
            --border-color: #334155;
            --tag-bg: #334155;
            --tag-text: #e2e8f0;
            --callout-bg: #131d31;
            --hover-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
            --id-badge-bg: #1e3a5f;
            --id-badge-text: #7dd3fc;
            --id-badge-border: #0369a1;
            --success-color: #34d399;
            --warning-color: #fbbf24;
            --table-border: #334155;
            --table-header-bg: #1e293b;
        }}

        /* Wymogi stylistyczne użytkownika */
        a {{ text-decoration: none; color: #464feb; }}
        a:hover {{ text-decoration: underline; }}
        tr th, tr td {{ border: 1px solid #e6e6e6; }}
        tr th {{ background-color: #f5f5f5; }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            transition: background-color 0.25s, color 0.25s;
        }}

        /* Stylistyka tabel */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            font-size: 0.88rem;
            background: var(--card-bg);
            border-radius: 8px;
            overflow: hidden;
        }}
        tr th, tr td {{
            padding: 0.75rem 1rem;
            text-align: left;
            vertical-align: top;
        }}
        tr th {{
            font-weight: 700;
            color: var(--text-color);
        }}

        /* Header */
        header {{
            background-color: var(--card-bg);
            border-bottom: 2px solid var(--border-color);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 4px rgba(0,0,0,0.03);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }}
        .header-brand {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        .header-logo {{
            background: linear-gradient(135deg, #0b2545 0%, #133a6b 100%);
            color: #ffffff;
            font-weight: 900;
            font-size: 1.25rem;
            padding: 0.5rem 0.85rem;
            border-radius: 8px;
            letter-spacing: 1px;
            border: 1px solid var(--secondary-color);
        }}
        .header-title h1 {{
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--text-color);
            line-height: 1.2;
        }}
        .header-title p {{
            font-size: 0.82rem;
            color: #64748b;
        }}
        .header-controls {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .btn-theme, .btn-basket-indicator {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            padding: 0.5rem 0.9rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.88rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.2s;
        }}
        .btn-theme:hover, .btn-basket-indicator:hover {{
            background: var(--tag-bg);
            border-color: var(--accent-blue);
        }}
        .basket-badge {{
            background-color: var(--accent-blue);
            color: white;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.15rem 0.45rem;
            border-radius: 10px;
        }}

        /* Navigation Bar Tabs */
        .nav-tabs {{
            display: flex;
            background: var(--card-bg);
            border-bottom: 1px solid var(--border-color);
            padding: 0 2rem;
            overflow-x: auto;
            gap: 0.5rem;
        }}
        .tab-btn {{
            padding: 0.85rem 1.25rem;
            font-size: 0.92rem;
            font-weight: 600;
            color: #64748b;
            border: none;
            background: none;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            white-space: nowrap;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .tab-btn:hover {{
            color: var(--text-color);
        }}
        .tab-btn.active {{
            color: var(--accent-blue);
            border-bottom-color: var(--accent-blue);
            font-weight: 700;
        }}

        /* Main Container */
        .main-container {{
            max-width: 1440px;
            margin: 0 auto;
            padding: 1.5rem 2rem 3rem 2rem;
        }}
        .tab-pane {{
            display: none;
        }}
        .tab-pane.active {{
            display: block;
        }}

        /* Multi-Resolver */
        .resolver-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }}
        .resolver-header h2 {{
            font-size: 1.15rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .resolver-header p {{
            font-size: 0.85rem;
            color: #64748b;
            margin-top: 0.2rem;
        }}
        .search-box-row {{
            display: flex;
            gap: 0.5rem;
            margin: 1rem 0 0.75rem 0;
            flex-wrap: wrap;
        }}
        .resolver-input {{
            flex: 1;
            min-width: 280px;
            padding: 0.75rem 1rem;
            font-size: 0.95rem;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            background: var(--bg-color);
            color: var(--text-color);
            outline: none;
            transition: border 0.2s;
        }}
        .resolver-input:focus {{
            border-color: var(--accent-blue);
        }}
        .btn-resolver {{
            background: var(--primary-color);
            color: #ffffff;
            border: none;
            padding: 0.75rem 1.25rem;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            transition: background 0.2s;
        }}
        .btn-resolver:hover {{
            background: var(--primary-hover);
        }}
        .resolver-quick-chips {{
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
            align-items: center;
            margin-top: 0.5rem;
        }}
        .chip-label {{
            font-size: 0.78rem;
            font-weight: 600;
            color: #64748b;
        }}
        .chip-btn {{
            background: var(--tag-bg);
            color: var(--tag-text);
            border: 1px solid var(--border-color);
            padding: 0.25rem 0.6rem;
            border-radius: 12px;
            font-size: 0.75rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .chip-btn:hover {{
            background: var(--accent-blue);
            color: #ffffff;
            border-color: var(--accent-blue);
        }}

        /* Explorer Layout */
        .explorer-layout {{
            display: grid;
            grid-template-columns: 290px 1fr;
            gap: 1.5rem;
            align-items: start;
        }}
        @media (max-width: 960px) {{
            .explorer-layout {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Filters Sidebar */
        .filters-panel {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.25rem;
            position: sticky;
            top: 5rem;
        }}
        .filters-panel h3 {{
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem;
        }}
        .btn-reset-filters {{
            background: none;
            border: none;
            color: var(--accent-blue);
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
        }}
        .filter-group {{
            margin-bottom: 1rem;
        }}
        .filter-title {{
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #64748b;
            margin-bottom: 0.4rem;
        }}
        .filter-select {{
            width: 100%;
            padding: 0.55rem 0.75rem;
            font-size: 0.85rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: var(--bg-color);
            color: var(--text-color);
            outline: none;
        }}

        /* Cards Grid */
        .cards-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            font-size: 0.9rem;
            color: #64748b;
        }}
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 1.25rem;
        }}
        .item-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.25rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
        }}
        .item-card:hover {{
            transform: translateY(-2px);
            box-shadow: var(--hover-shadow);
            border-color: #cbd5e1;
        }}
        .card-top {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }}
        .card-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
        }}
        .badge {{
            font-size: 0.7rem;
            font-weight: 700;
            padding: 0.2rem 0.5rem;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }}
        .badge-mandatory {{
            background-color: #dcfce7;
            color: #166534;
            border: 1px solid #bbf7d0;
        }}
        .badge-supplementary {{
            background-color: #f1f5f9;
            color: #475569;
            border: 1px solid #e2e8f0;
        }}
        .badge-research {{
            background-color: #fef3c7;
            color: #92400e;
            border: 1px solid #fde68a;
        }}
        .badge-module {{
            background-color: #e0e7ff;
            color: #3730a3;
            border: 1px solid #c7d2fe;
        }}

        .card-title {{
            font-size: 1.05rem;
            font-weight: 700;
            line-height: 1.35;
            margin-bottom: 0.4rem;
        }}
        .card-authors {{
            font-size: 0.85rem;
            color: #64748b;
            margin-bottom: 0.75rem;
            font-weight: 500;
        }}
        .card-desc {{
            font-size: 0.85rem;
            color: var(--text-color);
            margin-bottom: 0.85rem;
            line-height: 1.45;
        }}
        .card-meta-box {{
            background: var(--callout-bg);
            border-left: 3px solid var(--secondary-color);
            padding: 0.6rem 0.8rem;
            border-radius: 0 6px 6px 0;
            font-size: 0.8rem;
            margin-bottom: 1rem;
        }}
        .card-identifiers {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 1rem;
        }}
        .id-badge {{
            font-size: 0.75rem;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            background: var(--id-badge-bg);
            color: var(--id-badge-text);
            border: 1px solid var(--id-badge-border);
            padding: 0.2rem 0.45rem;
            border-radius: 4px;
        }}
        .card-footer {{
            border-top: 1px solid var(--border-color);
            padding-top: 0.85rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.5rem;
        }}
        .btn-card-action {{
            padding: 0.45rem 0.75rem;
            font-size: 0.8rem;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
            border: 1px solid var(--border-color);
            background: var(--card-bg);
            color: var(--text-color);
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }}
        .btn-card-action:hover {{
            background: var(--tag-bg);
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }}
        .btn-card-action.active {{
            background: #dcfce7;
            color: #166534;
            border-color: #86efac;
        }}

        /* Syllabus View Styles */
        .syllabus-hero {{
            background: linear-gradient(135deg, #0b2545 0%, #1e3a5f 100%);
            color: #ffffff;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        .syllabus-hero h2 {{
            font-size: 1.6rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }}
        .syllabus-hero p {{
            font-size: 0.95rem;
            opacity: 0.9;
            max-width: 900px;
            line-height: 1.5;
        }}
        .syllabus-jump-bar {{
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
            margin-top: 1.25rem;
        }}
        .btn-jump {{
            background: rgba(255,255,255,0.15);
            color: #ffffff;
            border: 1px solid rgba(255,255,255,0.25);
            padding: 0.35rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.2s;
        }}
        .btn-jump:hover {{
            background: #ffffff;
            color: #0b2545;
            text-decoration: none;
        }}

        .module-block {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.75rem;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }}
        .module-header {{
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 0.85rem;
            margin-bottom: 1.25rem;
        }}
        .module-header h3 {{
            font-size: 1.3rem;
            font-weight: 800;
            color: var(--text-color);
        }}
        .module-desc {{
            font-size: 0.9rem;
            color: #64748b;
            margin-top: 0.35rem;
        }}
        .reading-section-title {{
            font-size: 1rem;
            font-weight: 700;
            margin: 1.25rem 0 0.5rem 0;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .status-pill {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
            text-transform: uppercase;
        }}
        .status-pill.mandatory {{
            background: #dcfce7;
            color: #166534;
        }}
        .status-pill.supplementary {{
            background: #f1f5f9;
            color: #475569;
        }}

        /* Navigator styles */
        .navigator-progress-banner {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }}
        .progress-bar-bg {{
            height: 10px;
            background: var(--border-color);
            border-radius: 5px;
            overflow: hidden;
            margin-top: 0.5rem;
        }}
        .progress-bar-fill {{
            height: 100%;
            background: linear-gradient(90deg, #464feb, #10b981);
            width: 0%;
            transition: width 0.3s;
        }}
        .chapters-list {{
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }}
        .chapter-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
        }}
        .chapter-card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 0.75rem;
        }}
        .chapter-items-checklist {{
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
            margin-top: 1rem;
        }}
        .checklist-item {{
            display: flex;
            align-items: flex-start;
            gap: 0.6rem;
            font-size: 0.88rem;
        }}
        .checklist-item input[type="checkbox"] {{
            margin-top: 0.25rem;
            cursor: pointer;
        }}

        /* WIG140 Matrix */
        .sectors-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
            gap: 1.5rem;
        }}
        .sector-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
        }}
        .code-block {{
            background: #0f172a;
            color: #f8fafc;
            padding: 0.85rem 1rem;
            border-radius: 8px;
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 0.82rem;
            overflow-x: auto;
            margin-top: 0.75rem;
        }}

        /* Bibliography Tab */
        .basket-toolbar {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.25rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}
        .btn-toolbar {{
            padding: 0.6rem 1rem;
            font-size: 0.85rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            border: 1px solid var(--border-color);
            background: var(--card-bg);
            color: var(--text-color);
            transition: all 0.2s;
        }}
        .btn-toolbar.primary {{
            background: var(--accent-blue);
            color: white;
            border-color: var(--accent-blue);
        }}
        .btn-toolbar:hover {{
            background: var(--tag-bg);
            border-color: var(--accent-blue);
        }}
        .btn-toolbar.primary:hover {{
            background: #3b42c4;
        }}
        .apa-group-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }}
        .apa-group-card h3 {{
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 1rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem;
        }}
        .apa-citation-entry {{
            padding: 0.75rem 0;
            border-bottom: 1px dashed var(--border-color);
            font-size: 0.9rem;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
        }}
        .apa-citation-entry:last-child {{
            border-bottom: none;
        }}

        /* Toast Notifications */
        #toast {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #1e293b;
            color: #ffffff;
            padding: 0.85rem 1.25rem;
            border-radius: 8px;
            font-size: 0.88rem;
            font-weight: 600;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);
            display: none;
            z-index: 1000;
        }}
    </style>
</head>
<body>

    <!-- NAGŁÓWEK GŁÓWNY -->
    <header>
        <div class="header-brand">
            <div class="header-logo">AI FINC</div>
            <div class="header-title">
                <h1>AI FINC – Academic Research Hub</h1>
                <p>Akademia Leona Koźmińskiego • KDF Dialog • Patronat Merytoryczny ACCA • WIG140</p>
            </div>
        </div>
        <div class="header-controls">
            <button class="btn-theme" onclick="toggleTheme()" id="themeToggleBtn">🌓 Tryb ciemny</button>
            <button class="btn-basket-indicator" onclick="switchTab('tab-bibliography')">
                📋 Koszyk APA 7 <span class="basket-badge" id="basketCountBadge">0</span>
            </button>
            <a href="https://github.com/BartoszRadziszewski/AIFINC" target="_blank" class="btn-theme" style="text-decoration: none;">
                <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
                GitHub
            </a>
        </div>
    </header>

    <!-- ZAKŁADKI NAWIGACYJNE -->
    <nav class="nav-tabs">
        <button class="tab-btn active" id="tabBtn-explorer" onclick="switchTab('tab-explorer')">
            🔍 Global Explorer & Multi-Resolver
        </button>
        <button class="tab-btn" id="tabBtn-syllabus" onclick="switchTab('tab-syllabus')">
            📖 Kanon Literatury (12 Modułów AI FINC)
        </button>
        <button class="tab-btn" id="tabBtn-navigator" onclick="switchTab('tab-navigator')">
            🧭 Nawigator 8 Rozdziałów Projektu
        </button>
        <button class="tab-btn" id="tabBtn-wig140" onclick="switchTab('tab-wig140')">
            🏢 Laboratorium Spółek WIG140 & GPW
        </button>
        <button class="tab-btn" id="tabBtn-bibliography" onclick="switchTab('tab-bibliography')">
            📋 Koszyk Cytowań APA 7 & Generator
        </button>
    </nav>

    <!-- GŁÓWNA ZAWARTOŚĆ -->
    <main class="main-container">

        <!-- TAB 1: GLOBAL EXPLORER & MULTI-RESOLVER -->
        <section id="tab-explorer" class="tab-pane active">
            <!-- Multi-Resolver Bar -->
            <div class="resolver-card">
                <div class="resolver-header">
                    <h2>🔎 Multi-Resolver Identyfikatorów Naukowych & Prawnych</h2>
                    <p>Wprowadź DOI, SSRN ID, arXiv, ISBN, numer aktu prawnego CELEX (np. 32024R1689 dla AI Act) lub słowa kluczowe.</p>
                </div>
                <div class="search-box-row">
                    <input type="text" id="multiQueryInput" class="resolver-input" placeholder="Wklej identyfikator (np. 10.1145/3604237.3626869, SSRN: 5769382, ISBN: 978-83-01-20054-1, CELEX: 32024R1689) lub frazę..." oninput="handleSearch()">
                    <button class="btn-resolver" onclick="resolveDirectInput()">Rozpoznaj & Otwórz</button>
                </div>
                <div class="resolver-quick-chips">
                    <span class="chip-label">Szybkie filtry:</span>
                    <button class="chip-btn" onclick="setQuickSearch('EU AI Act')">EU AI Act 2024/1689</button>
                    <button class="chip-btn" onclick="setQuickSearch('Chief Value Officer')">ACCA CVO</button>
                    <button class="chip-btn" onclick="setQuickSearch('10.1145/3604237.3626869')">LLMs in Finance (ACM)</button>
                    <button class="chip-btn" onclick="setQuickSearch('Zarządzanie ryzykiem')">Jajuga (PWN)</button>
                    <button class="chip-btn" onclick="setQuickSearch('BPMN')">BPMN 2.0 (Onepress)</button>
                    <button class="chip-btn" onclick="setQuickSearch('Autoencoding')">Schreyer (Autoencoders)</button>
                    <button class="chip-btn" onclick="setQuickSearch('SSRN: 5769382')">SSRN: 5769382</button>
                </div>
            </div>

            <!-- Explorer Layout: Filters + Cards -->
            <div class="explorer-layout">
                <aside class="filters-panel">
                    <h3>
                        <span>Filtry Zasobów</span>
                        <button class="btn-reset-filters" onclick="resetFilters()">Wyczyść</button>
                    </h3>

                    <div class="filter-group">
                        <div class="filter-title">Moduł Tematyczny (1–12)</div>
                        <select id="filterModule" class="filter-select" onchange="renderCards()">
                            <option value="all">Wszystkie moduły (1–12)</option>
                            <option value="1">Moduł 1: Podstawy AI dla menedżerów finansowych</option>
                            <option value="2">Moduł 2: Zastosowanie AI w finansach i controllingu</option>
                            <option value="3">Moduł 3: Zarządzanie ryzykiem wdrażania AI w finansach</option>
                            <option value="4">Moduł 4: Regulacje UE w zakresie AI oraz aspekty etyczne</option>
                            <option value="5">Moduł 5: Warsztaty: Prowadzenie projektów AI w praktyce</option>
                            <option value="6">Moduł 6: Zarządzanie procesami biznesowymi i danymi</option>
                            <option value="7">Moduł 7: Strategia transformacji cyfrowej oparta na AI</option>
                            <option value="8">Moduł 8: Profesjonalny dobór oraz umowa z doradcą AI</option>
                            <option value="9">Moduł 9: Wschodzące technologie i ich wpływ na finanse</option>
                            <option value="10">Moduł 10: Wdrażanie AI w finansach i controllingu: case studies</option>
                            <option value="11">Moduł 11: Komunikacja AI i kultura start-upowa</option>
                            <option value="12">Moduł 12: Projekt końcowy</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title">Status / Typ Lektury</div>
                        <select id="filterReadingType" class="filter-select" onchange="renderCards()">
                            <option value="all">Wszystkie typy publikacji</option>
                            <option value="Obowiązkowa">⭐ Tylko Lektury Obowiązkowe</option>
                            <option value="Uzupełniająca">📖 Tylko Lektury Uzupełniające</option>
                            <option value="Badawcza">🔬 Publikacje Badawcze Controllingu (Emerald, Springer, BIS, SSRN)</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title">Rozdział Projektu ALK (1–8)</div>
                        <select id="filterChapter" class="filter-select" onchange="renderCards()">
                            <option value="all">Wszystkie rozdziały (1–8)</option>
                            <option value="1">Rozdział 1: Wstęp & Problem biznesowy</option>
                            <option value="2">Rozdział 2: Regulacje, etyka & AI Act</option>
                            <option value="3">Rozdział 3: Projektowanie & Architektura</option>
                            <option value="4">Rozdział 4: Zarządzanie danymi</option>
                            <option value="5">Rozdział 5: Modele AI & Algorytmy</option>
                            <option value="6">Rozdział 6: Implementacja & MLOps</option>
                            <option value="7">Rozdział 7: Dokumentacja & Zmiana</option>
                            <option value="8">Rozdział 8: ROI & Wartość biznesowa</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title">Kategoria APA 7 (4 grupy ALK)</div>
                        <select id="filterCategory" class="filter-select" onchange="renderCards()">
                            <option value="all">Wszystkie kategorie</option>
                            <option value="1">1. Artykuły i książki naukowe</option>
                            <option value="2">2. Akty prawne i normatywne</option>
                            <option value="3">3. Źródła internetowe i bazy</option>
                            <option value="4">4. Raporty eksperckie i instytucjonalne</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title">Sektor WIG140</div>
                        <select id="filterSector" class="filter-select" onchange="renderCards()">
                            <option value="all">Wszystkie sektory giełdowe</option>
                            <option value="Finanse">Bankowość & Usługi Finansowe</option>
                            <option value="Produkcja">Przemysł & Produkcja</option>
                            <option value="Energetyka">Energetyka & Surowce</option>
                            <option value="Retail">Handel & E-commerce</option>
                            <option value="TMT">TMT, Technologie & Media</option>
                            <option value="Budownictwo">Budownictwo & Infrastruktura</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title">Model Dostępu</div>
                        <select id="filterAccess" class="filter-select" onchange="renderCards()">
                            <option value="all">Wszystkie modele dostępu</option>
                            <option value="Open Access">Open Access / Wolny dostęp</option>
                            <option value="Wymaga licencji / Baza">Wymaga licencji / Baza wydawcy</option>
                        </select>
                    </div>
                </aside>

                <main>
                    <div class="cards-header">
                        <div>Znaleziono: <strong id="resultCount">0</strong> pozycji</div>
                        <div style="font-size: 0.8rem;">Kliknij <em>Kopiuj APA</em> lub <em>Dodaj do koszyka</em></div>
                    </div>
                    <div class="cards-grid" id="cardsContainer">
                        <!-- Karty renderowane w JS -->
                    </div>
                </main>
            </div>
        </section>

        <!-- TAB 2: KANON LITERATURY (12 MODUŁÓW AI FINC) -->
        <section id="tab-syllabus" class="tab-pane">
            <div class="syllabus-hero">
                <h2>Definitywny Kanon Literatury AI FINC 2026/2027</h2>
                <p>Kanon literatury badawczo-dydaktycznej obejmujący 12 modułów tematycznych studiów podyplomowych <em>AI w finansach i controllingu przedsiębiorstw</em>. Zawiera podział na lektury podstawowe i uzupełniające, zweryfikowane identyfikatory naukowe (ISBN, DOI, CELEX), oficjalne odnośniki do publikacji otwartych oraz analizę interdyscyplinarnych powiązań między modułami.</p>
                
                <div class="syllabus-jump-bar">
                    <span style="font-weight: 700; align-self: center; font-size: 0.85rem;">Skocz do modułu:</span>
                    <a href="#mod-1" class="btn-jump">Moduł 1</a>
                    <a href="#mod-2" class="btn-jump">Moduł 2</a>
                    <a href="#mod-3" class="btn-jump">Moduł 3</a>
                    <a href="#mod-4" class="btn-jump">Moduł 4</a>
                    <a href="#mod-5" class="btn-jump">Moduł 5</a>
                    <a href="#mod-6" class="btn-jump">Moduł 6</a>
                    <a href="#mod-7" class="btn-jump">Moduł 7</a>
                    <a href="#mod-8" class="btn-jump">Moduł 8</a>
                    <a href="#mod-9" class="btn-jump">Moduł 9</a>
                    <a href="#mod-10" class="btn-jump">Moduł 10</a>
                    <a href="#mod-11" class="btn-jump">Moduł 11</a>
                    <a href="#mod-12" class="btn-jump">Moduł 12</a>
                    <a href="#sec-dedup" class="btn-jump" style="background: rgba(245,158,11,0.3);">Deduplikacja</a>
                    <a href="#sec-top15" class="btn-jump" style="background: rgba(16,185,129,0.3);">⭐ TOP 15 Kanonu</a>
                </div>
            </div>

            <!-- RENDEROWANIE 12 MODUŁÓW -->
            <div id="modulesContainer">
                <!-- Generowane dynamicznie przez JS lub statycznie -->
            </div>

            <!-- SEKCJA: DEDUPLIKACJA I POWTÓRZENIA MIĘDZY MODUŁAMI -->
            <div class="module-block" id="sec-dedup">
                <div class="module-header">
                    <h3>🔄 Pozycje powtarzające się między modułami (Analiza deduplikacyjna)</h3>
                    <div class="module-desc">Szczegółowe zestawienie pozycji występujących w programie wielokrotnie w powiązaniu z ich kontekstem dydaktycznym.</div>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Autor / Publikacja</th>
                            <th style="width: 25%;">Występowanie w modułach</th>
                            <th style="width: 20%;">Status w programie</th>
                            <th style="width: 30%;">Uzasadnienie & Wyjaśnienie deduplikacji</th>
                        </tr>
                    </thead>
                    <tbody id="dedupTableBody">
                        <!-- Wypełniane z prepare_data.REPEATED_ITEMS -->
                    </tbody>
                </table>
            </div>

            <!-- SEKCJA: ⭐ TOP 15 KANONU -->
            <div class="module-block" id="sec-top15">
                <div class="module-header">
                    <h3>⭐ TOP 15 Lektur Kanonicznych dla Projektu Dyplomowego AI FINC</h3>
                    <div class="module-desc">Wyselekcjonowane, kluczowe dzieła łączące prawo (AI Act), finanse strategiczne (CVO), zarządzanie ryzykiem, inżynierię danych i controlling procesowy.</div>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 5%;">#</th>
                            <th style="width: 25%;">Instytucja / Autor</th>
                            <th style="width: 45%;">Tytuł publikacji</th>
                            <th style="width: 25%;">Obszar tematyczny & Moduły</th>
                        </tr>
                    </thead>
                    <tbody id="top15TableBody">
                        <!-- Wypełniane dynamicznie -->
                    </tbody>
                </table>
            </div>
        </section>

        <!-- TAB 3: NAWIGATOR 8 ROZDZIAŁÓW PROJEKTU KOŃCOWEGO -->
        <section id="tab-navigator" class="tab-pane">
            <div class="navigator-progress-banner">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
                    <div>
                        <h2 style="font-size: 1.25rem; font-weight: 800;">Nawigator 8 Rozdziałów Projektu Dyplomowego AI FINC</h2>
                        <p style="font-size: 0.88rem; color: #64748b;">Struktura zgodna ze standardem dysertacji podyplomowej ALK, patronatu ACCA i wymogami analizy spółki z WIG140.</p>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-size: 1.25rem; font-weight: 800; color: var(--accent-blue);" id="progressText">0 / 41 (0%)</span>
                        <div style="font-size: 0.75rem; color: #64748b;">Zrealizowane elementy wymogów</div>
                    </div>
                </div>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" id="progressBar"></div>
                </div>
            </div>

            <div class="chapters-list" id="chaptersContainer">
                <!-- Renderowane dynamicznie -->
            </div>
        </section>

        <!-- TAB 4: LABORATORIUM SPÓŁEK WIG140 & GPW -->
        <section id="tab-wig140" class="tab-pane">
            <div class="syllabus-hero" style="background: linear-gradient(135deg, #064e3b 0%, #0b2545 100%);">
                <h2>🏢 Laboratorium Analityczne Spółek WIG140 & GPW</h2>
                <p>Środowisko referencyjne dla projektów wdrożeniowych realizowanych na danych polskich spółek giełdowych. Zawiera charakterystykę 6 kluczowych sektorów, mapę problemów controllingu, wzorcowe use-case'y AI oraz gotowe skrypty Python do pobierania danych finansowych i giełdowych.</p>
            </div>

            <div class="sectors-grid" id="wigSectorsContainer">
                <!-- Renderowane dynamicznie -->
            </div>
        </section>

        <!-- TAB 5: KOSZYK CYTOWAŃ APA 7 & GENERATOR -->
        <section id="tab-bibliography" class="tab-pane">
            <div class="basket-toolbar">
                <div>
                    <h2 style="font-size: 1.25rem; font-weight: 800;">Twój Koszyk Cytowań APA 7 dla Dysertacji ALK</h2>
                    <p style="font-size: 0.85rem; color: #64748b;">Pozycje są automatycznie kategoryzowane według wymogów seminarium dyplomowego Akademii Leona Koźmińskiego (4 grupy).</p>
                </div>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <button class="btn-toolbar primary" onclick="copyAllCitations()">📋 Kopiuj całą bibliografię</button>
                    <button class="btn-toolbar" onclick="exportToTxt()">💾 Eksportuj do .TXT</button>
                    <button class="btn-toolbar" onclick="exportToBibtex()">📑 Eksportuj do BibTeX</button>
                    <button class="btn-toolbar" onclick="clearBasket()" style="color: #ef4444;">🗑️ Wyczyść</button>
                </div>
            </div>

            <div id="bibliographyContent">
                <!-- Grupy APA 7 renderowane dynamicznie -->
            </div>
        </section>

    </main>

    <!-- TOAST NOTIFICATION -->
    <div id="toast">Komunikat powiadomienia</div>

    <!-- DANE I SKRYPTY JAVASCRIPT -->
    <script>
        const DATABASE = __DATABASE_JSON__;
        const MODULES_DATA = __MODULES_DATA_JSON__;
        const REPEATED_ITEMS = __REPEATED_ITEMS_JSON__;
        const CHAPTERS = __CHAPTERS_JSON__;
        const WIG_SECTORS = __WIG_SECTORS_JSON__;

        let userBasket = JSON.parse(localStorage.getItem('aifinc_basket') || '[]');
        let userChecklist = JSON.parse(localStorage.getItem('aifinc_checklist') || '{{}}');

        document.addEventListener('DOMContentLoaded', () => {{
            initTheme();
            renderCards();
            renderSyllabusModules();
            renderDedupTable();
            renderTop15Table();
            renderNavigator();
            renderWigGrid();
            renderBibliography();
            updateProgress();
            updateBasketCount();
        }});

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

            const targetPane = document.getElementById(tabId);
            if (targetPane) targetPane.classList.add('active');

            const btnMap = {{
                'tab-explorer': 'tabBtn-explorer',
                'tab-syllabus': 'tabBtn-syllabus',
                'tab-navigator': 'tabBtn-navigator',
                'tab-wig140': 'tabBtn-wig140',
                'tab-bibliography': 'tabBtn-bibliography'
            }};
            const activeBtn = document.getElementById(btnMap[tabId]);
            if (activeBtn) activeBtn.classList.add('active');

            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function initTheme() {{
            const saved = localStorage.getItem('aifinc_theme') || 'light';
            document.documentElement.setAttribute('data-theme', saved);
            updateThemeButtonText(saved);
        }}

        function toggleTheme() {{
            const current = document.documentElement.getAttribute('data-theme') || 'light';
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('aifinc_theme', next);
            updateThemeButtonText(next);
        }}

        function updateThemeButtonText(theme) {{
            const btn = document.getElementById('themeToggleBtn');
            if (btn) {{
                btn.innerHTML = theme === 'dark' ? '☀️ Tryb jasny' : '🌓 Tryb ciemny';
            }}
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            toast.textContent = msg;
            toast.style.display = 'block';
            setTimeout(() => {{
                toast.style.display = 'none';
            }}, 2800);
        }}

        /* RENDEROWANIE MODUŁÓW W TAB 2 */
        function renderSyllabusModules() {{
            const container = document.getElementById('modulesContainer');
            if (!container) return;

            container.innerHTML = MODULES_DATA.map(mod => {{
                let mandHtml = '';
                if (mod.mandatory && mod.mandatory.length > 0) {{
                    mandHtml = `
                        <div class="reading-section-title">
                            <span class="status-pill mandatory">Lektury Obowiązkowe (${{mod.mandatory.length}})</span>
                        </div>
                        <table>
                            <thead>
                                <tr>
                                    <th style="width: 5%;">#</th>
                                    <th style="width: 25%;">Autor / Instytucja</th>
                                    <th style="width: 35%;">Tytuł publikacji & Rok</th>
                                    <th style="width: 15%;">Identyfikator</th>
                                    <th style="width: 20%;">Oficjalne źródło / Notatki</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${{mod.mandatory.map((it, idx) => `
                                    <tr>
                                        <td><strong>${{idx + 1}}</strong></td>
                                        <td><strong>${{it.authors}}</strong></td>
                                        <td>
                                            <a href="${{it.url}}" target="_blank" style="font-weight: 600;">${{it.title}}</a> (${{it.year}})
                                            ${{it.notes ? `<div style="font-size: 0.78rem; color: #64748b; margin-top: 0.25rem;">${{it.notes}}</div>` : ''}}
                                        </td>
                                        <td>
                                            ${{it.isbn && it.isbn !== 'nie dotyczy' ? `<span class="id-badge">ISBN: ${{it.isbn}}</span> ` : ''}}
                                            ${{it.doi && it.doi !== 'nie dotyczy' ? `<span class="id-badge">DOI: ${{it.doi}}</span> ` : ''}}
                                            ${{(!it.isbn || it.isbn === 'nie dotyczy') && (!it.doi || it.doi === 'nie dotyczy') ? `<span style="font-size: 0.78rem; color: #94a3b8;">nie dotyczy</span>` : ''}}
                                        </td>
                                        <td>
                                            <a href="${{it.url}}" target="_blank">${{it.linkText || 'Oficjalne źródło'}} &rarr;</a>
                                        </td>
                                    </tr>
                                `).join('')}}
                            </tbody>
                        </table>
                    `;
                }} else {{
                    mandHtml = `<p style="font-size: 0.85rem; color: #64748b; margin: 0.5rem 0;">W programie tego modułu lektury powiązane są bezpośrednio z warsztatem praktycznym i studiami przypadków.</p>`;
                }}

                let suppHtml = '';
                if (mod.supplementary && mod.supplementary.length > 0) {{
                    suppHtml = `
                        <div class="reading-section-title" style="margin-top: 1.5rem;">
                            <span class="status-pill supplementary">Lektury Uzupełniające (${{mod.supplementary.length}})</span>
                        </div>
                        <table>
                            <thead>
                                <tr>
                                    <th style="width: 5%;">#</th>
                                    <th style="width: 25%;">Autor / Instytucja</th>
                                    <th style="width: 35%;">Tytuł publikacji & Rok</th>
                                    <th style="width: 15%;">Identyfikator</th>
                                    <th style="width: 20%;">Oficjalne źródło / Notatki</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${{mod.supplementary.map((it, idx) => `
                                    <tr>
                                        <td>${{idx + 1}}</td>
                                        <td>${{it.authors}}</td>
                                        <td>
                                            <a href="${{it.url}}" target="_blank">${{it.title}}</a> (${{it.year}})
                                            ${{it.notes ? `<div style="font-size: 0.78rem; color: #64748b; margin-top: 0.25rem;">${{it.notes}}</div>` : ''}}
                                        </td>
                                        <td>
                                            ${{it.isbn && it.isbn !== 'nie dotyczy' ? `<span class="id-badge">ISBN: ${{it.isbn}}</span> ` : ''}}
                                            ${{it.doi && it.doi !== 'nie dotyczy' ? `<span class="id-badge">DOI: ${{it.doi}}</span> ` : ''}}
                                            ${{(!it.isbn || it.isbn === 'nie dotyczy') && (!it.doi || it.doi === 'nie dotyczy') ? `<span style="font-size: 0.78rem; color: #94a3b8;">nie dotyczy</span>` : ''}}
                                        </td>
                                        <td>
                                            <a href="${{it.url}}" target="_blank">${{it.linkText || 'Źródło'}} &rarr;</a>
                                        </td>
                                    </tr>
                                `).join('')}}
                            </tbody>
                        </table>
                    `;
                }} else {{
                    suppHtml = `<p style="font-size: 0.85rem; color: #64748b; margin: 0.5rem 0;">Brak odrębnych lektur uzupełniających w wykazie modułu.</p>`;
                }}

                return `
                    <div class="module-block" id="mod-${{mod.id}}">
                        <div class="module-header">
                            <h3>${{mod.name}}</h3>
                            <div class="module-desc">${{mod.desc}}</div>
                        </div>
                        ${{mandHtml}}
                        ${{suppHtml}}
                    </div>
                `;
            }}).join('');
        }}

        /* TABELA DEDUPLIKACJI */
        function renderDedupTable() {{
            const tbody = document.getElementById('dedupTableBody');
            if (!tbody) return;

            tbody.innerHTML = REPEATED_ITEMS.map(it => `
                <tr>
                    <td><strong>${{it.authors}}</strong><br><span style="font-size: 0.85rem; color: #64748b;">${{it.title}}</span></td>
                    <td><span class="badge badge-module">${{it.modules}}</span></td>
                    <td><strong>${{it.status}}</strong></td>
                    <td style="font-size: 0.85rem;">${{it.note}}</td>
                </tr>
            `).join('');
        }}

        /* TABELA TOP 15 */
        function renderTop15Table() {{
            const tbody = document.getElementById('top15TableBody');
            if (!tbody) return;

            const top15 = DATABASE.filter(d => d.isTop15);
            tbody.innerHTML = top15.map((it, idx) => `
                <tr>
                    <td><strong>${{idx + 1}}</strong></td>
                    <td>${{it.authors}}</td>
                    <td><strong><a href="${{it.url}}" target="_blank">${{it.title}}</a></strong></td>
                    <td><span class="badge badge-module">${{it.syllabusStream}}</span></td>
                </tr>
            `).join('');
        }}

        /* TAB 1: RENDEROWANIE KART EXPLORERA */
        function renderCards() {{
            const container = document.getElementById('cardsContainer');
            const searchVal = (document.getElementById('multiQueryInput').value || '').trim().toLowerCase();
            const modFilter = document.getElementById('filterModule').value;
            const readTypeFilter = document.getElementById('filterReadingType').value;
            const chapterFilter = document.getElementById('filterChapter').value;
            const categoryFilter = document.getElementById('filterCategory').value;
            const sectorFilter = document.getElementById('filterSector').value;
            const accessFilter = document.getElementById('filterAccess').value;

            const filtered = DATABASE.filter(item => {{
                if (searchVal) {{
                    const fullText = (item.title + ' ' + item.authors + ' ' + item.desc + ' ' + item.businessValue + ' ' + JSON.stringify(item.identifiers || {{}})).toLowerCase();
                    if (!fullText.includes(searchVal)) return false;
                }}
                if (modFilter !== 'all' && !(item.modules || []).includes(parseInt(modFilter))) return false;
                
                if (readTypeFilter === 'Obowiązkowa' && !item.isMandatory) return false;
                if (readTypeFilter === 'Uzupełniająca' && (item.isMandatory || item.readingType !== 'Uzupełniająca')) return false;
                if (readTypeFilter === 'Badawcza' && item.readingType !== 'Badawcza') return false;

                if (chapterFilter !== 'all' && !item.projectChapters.includes(parseInt(chapterFilter))) return false;
                if (categoryFilter !== 'all' && item.apaCategory !== parseInt(categoryFilter)) return false;
                if (sectorFilter !== 'all' && !(item.sectors || []).includes(sectorFilter)) return false;
                if (accessFilter !== 'all' && item.accessModel !== accessFilter) return false;

                return true;
            }});

            document.getElementById('resultCount').textContent = filtered.length;

            if (filtered.length === 0) {{
                container.innerHTML = `<div style="grid-column: 1/-1; padding: 3rem; text-align: center; color: #64748b; background: var(--card-bg); border-radius: 12px; border: 1px dashed var(--border-color);">
                    <h3>Brak pozycji spełniających podane kryteria</h3>
                    <p style="margin-top: 0.5rem;">Zmień parametry filtrów w lewym panelu lub skorzystaj z wyszukiwarki Multi-Resolver.</p>
                </div>`;
                return;
            }}

            container.innerHTML = filtered.map(item => {{
                const inBasket = userBasket.some(b => b.id === item.id);
                const categoryNames = {{
                    1: '1. Artykuł / Książka',
                    2: '2. Akt prawny',
                    3: '3. Źródło internetowe',
                    4: '4. Raport ekspercki'
                }};

                let idBadges = '';
                if (item.identifiers) {{
                    if (item.identifiers.doi) idBadges += `<a href="https://doi.org/${{item.identifiers.doi}}" target="_blank" class="id-badge">DOI: ${{item.identifiers.doi}}</a>`;
                    if (item.identifiers.ssrn) idBadges += `<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=${{item.identifiers.ssrn}}" target="_blank" class="id-badge">SSRN: ${{item.identifiers.ssrn}}</a>`;
                    if (item.identifiers.arxiv) idBadges += `<a href="https://arxiv.org/abs/${{item.identifiers.arxiv}}" target="_blank" class="id-badge">arXiv: ${{item.identifiers.arxiv}}</a>`;
                    if (item.identifiers.isbn) idBadges += `<span class="id-badge">ISBN: ${{item.identifiers.isbn}}</span>`;
                    if (item.identifiers.issn) idBadges += `<span class="id-badge">ISSN: ${{item.identifiers.issn}}</span>`;
                    if (item.identifiers.bis_wp) idBadges += `<span class="id-badge">BIS WP #${{item.identifiers.bis_wp}}</span>`;
                }}

                let typeBadge = '';
                if (item.isMandatory) {{
                    typeBadge = `<span class="badge badge-mandatory">Obowiązkowa</span>`;
                }} else if (item.readingType === 'Badawcza') {{
                    typeBadge = `<span class="badge badge-research">Badawcza</span>`;
                }} else {{
                    typeBadge = `<span class="badge badge-supplementary">Uzupełniająca</span>`;
                }}

                let moduleBadges = (item.modules || []).map(m => `<span class="badge badge-module">Moduł ${{m}}</span>`).join(' ');

                return `
                    <div class="item-card">
                        <div>
                            <div class="card-top">
                                <div class="card-badges">
                                    <span class="badge" style="background: var(--tag-bg); color: var(--tag-text);">${{categoryNames[item.apaCategory]}}</span>
                                    ${{typeBadge}}
                                    ${{moduleBadges}}
                                </div>
                                <span style="font-size: 0.75rem; color: #94a3b8; font-weight: 700;">#${{item.id}}</span>
                            </div>

                            <div class="card-title">
                                <a href="${{item.url}}" target="_blank">${{item.title}}</a>
                            </div>
                            <div class="card-authors">${{item.authors}} (${{item.year}})</div>

                            <div class="card-desc">${{item.desc}}</div>

                            <div class="card-meta-box">
                                <strong>Zastosowanie w dysertacji (Rozdziały: ${{item.projectChapters.join(', ')}}):</strong><br>
                                ${{item.businessValue}}
                            </div>

                            <div class="card-identifiers">
                                ${{idBadges || '<span style="font-size: 0.75rem; color: #94a3b8;">Brak zewnętrznych identyfikatorów numerycznych</span>'}}
                            </div>
                        </div>

                        <div class="card-footer">
                            <button class="btn-card-action" onclick="copyApaCitation(${{item.id}})">
                                📄 Kopiuj APA 7
                            </button>
                            <button class="btn-card-action ${{inBasket ? 'active' : ''}}" onclick="toggleBasket(${{item.id}})">
                                ${{inBasket ? '✓ W koszyku' : '+ Dodaj do pracy'}}
                            </button>
                        </div>
                    </div>
                `;
            }}).join('');
        }}

        function handleSearch() {{
            renderCards();
        }}

        function setQuickSearch(val) {{
            document.getElementById('multiQueryInput').value = val;
            renderCards();
        }}

        function resetFilters() {{
            document.getElementById('multiQueryInput').value = '';
            document.getElementById('filterModule').value = 'all';
            document.getElementById('filterReadingType').value = 'all';
            document.getElementById('filterChapter').value = 'all';
            document.getElementById('filterCategory').value = 'all';
            document.getElementById('filterSector').value = 'all';
            document.getElementById('filterAccess').value = 'all';
            renderCards();
            showToast('Zresetowano wszystkie filtry wyszukiwania');
        }}

        function resolveDirectInput() {{
            const val = (document.getElementById('multiQueryInput').value || '').trim();
            if (!val) return;

            if (val.startsWith('10.')) {{
                window.open('https://doi.org/' + val, '_blank');
                return;
            }}
            if (val.toLowerCase().includes('ssrn')) {{
                const id = val.replace(/[^0-9]/g, '');
                if (id) window.open('https://papers.ssrn.com/sol3/papers.cfm?abstract_id=' + id, '_blank');
                return;
            }}
            if (val.toLowerCase().includes('celex')) {{
                const id = val.replace(/.*celex:?/i, '').trim();
                window.open('https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:' + id, '_blank');
                return;
            }}
            if (val.startsWith('320')) {{
                window.open('https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:' + val, '_blank');
                return;
            }}
            renderCards();
        }}

        /* KOSZYK CYTOWAŃ APA 7 */
        function toggleBasket(id) {{
            const item = DATABASE.find(d => d.id === id);
            if (!item) return;

            const idx = userBasket.findIndex(b => b.id === id);
            if (idx >= 0) {{
                userBasket.splice(idx, 1);
                showToast('Usunięto pozycję z koszyka cytowań');
            }} else {{
                userBasket.push(item);
                showToast('Dodano pozycję do koszyka cytowań APA 7');
            }}

            localStorage.setItem('aifinc_basket', JSON.stringify(userBasket));
            updateBasketCount();
            renderCards();
            renderBibliography();
        }}

        function updateBasketCount() {{
            const badge = document.getElementById('basketCountBadge');
            if (badge) badge.textContent = userBasket.length;
        }}

        function copyApaCitation(id) {{
            const item = DATABASE.find(d => d.id === id);
            if (!item) return;
            navigator.clipboard.writeText(item.apaCitation).then(() => {{
                showToast('Skopiowano cytowanie APA 7 do schowka!');
            }});
        }}

        function renderBibliography() {{
            const container = document.getElementById('bibliographyContent');
            if (!container) return;

            if (userBasket.length === 0) {{
                container.innerHTML = `<div style="padding: 3rem; text-align: center; color: #64748b; background: var(--card-bg); border-radius: 12px; border: 1px dashed var(--border-color);">
                    <h3>Twój koszyk bibliograficzny jest pusty</h3>
                    <p style="margin-top: 0.5rem;">Przejdź do zakładki <strong>Global Explorer</strong> lub <strong>Kanon Literatury</strong> i kliknij <em>+ Dodaj do pracy</em> przy wybranych publikacjach.</p>
                </div>`;
                return;
            }}

            const groups = {{
                1: {{ title: '1. Artykuły i książki naukowe', items: [] }},
                2: {{ title: '2. Akty prawne i normatywne', items: [] }},
                3: {{ title: '3. Źródła internetowe i bazy danych', items: [] }},
                4: {{ title: '4. Raporty instytucjonalne i eksperckie', items: [] }}
            }};

            userBasket.forEach(b => {{
                if (groups[b.apaCategory]) groups[b.apaCategory].items.push(b);
            }});

            let html = '';
            for (const catId in groups) {{
                const grp = groups[catId];
                if (grp.items.length === 0) continue;

                html += `
                    <div class="apa-group-card">
                        <h3>${{grp.title}} (${{grp.items.length}})</h3>
                        <div>
                            ${{grp.items.map(item => `
                                <div class="apa-citation-entry">
                                    <div style="flex: 1;">
                                        ${{item.apaCitation}}
                                    </div>
                                    <div style="display: flex; gap: 0.35rem;">
                                        <button class="btn-card-action" onclick="copyApaCitation(${{item.id}})">Kopiuj</button>
                                        <button class="btn-card-action" style="color: #ef4444;" onclick="toggleBasket(${{item.id}})">Usuń</button>
                                    </div>
                                </div>
                            `).join('')}}
                        </div>
                    </div>
                `;
            }}

            container.innerHTML = html;
        }}

        function copyAllCitations() {{
            if (userBasket.length === 0) {{
                showToast('Koszyk jest pusty!');
                return;
            }}
            const groups = {{
                1: '1. Artykuły i książki naukowe',
                2: '2. Akty prawne i normatywne',
                3: '3. Źródła internetowe i bazy danych',
                4: '4. Raporty instytucjonalne i eksperckie'
            }};

            let text = 'BIBLIOGRAFIA PROJEKTU KOŃCOWEGO AI FINC (APA 7th edition)\\n\\n';
            for (let c = 1; c <= 4; c++) {{
                const items = userBasket.filter(b => b.apaCategory === c);
                if (items.length > 0) {{
                    text += groups[c] + '\\n' + '='.repeat(groups[c].length) + '\\n';
                    items.forEach(it => {{
                        text += it.apaCitation + '\\n\\n';
                    }});
                }}
            }}

            navigator.clipboard.writeText(text).then(() => {{
                showToast('Skopiowano całą bibliografię w formacie ALK do schowka!');
            }});
        }}

        function exportToTxt() {{
            if (userBasket.length === 0) return showToast('Brak pozycji do eksportu');
            let content = 'BIBLIOGRAFIA PROJEKTU KOŃCOWEGO AI FINC\\n\\n';
            userBasket.forEach(it => {{
                content += it.apaCitation + '\\n\\n';
            }});
            const blob = new Blob([content], {{ type: 'text/plain;charset=utf-8' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Bibliografia_AIFINC_ALK.txt';
            a.click();
        }}

        function exportToBibtex() {{
            if (userBasket.length === 0) return showToast('Brak pozycji do eksportu');
            let bib = '';
            userBasket.forEach((it, idx) => {{
                const key = (it.authors.split(' ')[0].replace(/[^a-zA-Z]/g, '') || 'Ref') + it.year + '_' + idx;
                bib += `@misc{{${{key}},\\n  author = {{${{it.authors}}}},\\n  title = {{${{it.title}}}},\\n  year = {{${{it.year}}}},\\n  url = {{${{it.url}}}}\\n}}\\n\\n`;
            }});
            const blob = new Blob([bib], {{ type: 'text/plain;charset=utf-8' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Bibliografia_AIFINC.bib';
            a.click();
        }}

        function clearBasket() {{
            if (confirm('Czy na pewno chcesz opróżnić koszyk cytowań?')) {{
                userBasket = [];
                localStorage.setItem('aifinc_basket', '[]');
                updateBasketCount();
                renderCards();
                renderBibliography();
                showToast('Opróżniono koszyk bibliograficzny');
            }}
        }}

        /* NAWIGATOR 8 ROZDZIAŁÓW */
        function renderNavigator() {{
            const container = document.getElementById('chaptersContainer');
            if (!container) return;

            container.innerHTML = CHAPTERS.map(chap => {{
                return `
                    <div class="chapter-card">
                        <div class="chapter-card-header">
                            <div>
                                <h3 style="font-size: 1.15rem; font-weight: 800;">${{chap.title}}</h3>
                                <p style="font-size: 0.85rem; color: #64748b; margin-top: 0.2rem;">${{chap.desc}}</p>
                            </div>
                            <span class="badge badge-mandatory">${{chap.reqBadge}}</span>
                        </div>

                        <div class="chapter-items-checklist">
                            ${{chap.items.map(it => `
                                <label class="checklist-item">
                                    <input type="checkbox" id="${{it.id}}" ${{userChecklist[it.id] ? 'checked' : ''}} onchange="toggleChecklistItem('${{it.id}}')">
                                    <span>${{it.text}}</span>
                                </label>
                            `).join('')}}
                        </div>

                        <div style="margin-top: 1rem; border-top: 1px solid var(--border-color); padding-top: 0.75rem; display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.78rem; color: #64748b;">Powiązane lektury z bazy:</span>
                            <button class="btn-card-action" onclick="filterByChapter(${{chap.id}})">
                                🔍 Zobacz lektury dla Rozdziału ${{chap.id}} &rarr;
                            </button>
                        </div>
                    </div>
                `;
            }}).join('');
        }}

        function toggleChecklistItem(id) {{
            userChecklist[id] = !userChecklist[id];
            localStorage.setItem('aifinc_checklist', JSON.stringify(userChecklist));
            updateProgress();
        }}

        function updateProgress() {{
            const total = 41; // 5 + 4 + 5 + 5 + 5 + 5 + 5 + 7
            let done = 0;
            for (const k in userChecklist) {{
                if (userChecklist[k]) done++;
            }}
            const pct = Math.round((done / total) * 100);
            const textEl = document.getElementById('progressText');
            const barEl = document.getElementById('progressBar');
            if (textEl) textEl.textContent = `${{done}} / ${{total}} (${{pct}}%)`;
            if (barEl) barEl.style.width = pct + '%';
        }}

        function filterByChapter(chapId) {{
            switchTab('tab-explorer');
            document.getElementById('filterChapter').value = chapId;
            renderCards();
        }}

        /* WIG140 MATRIX */
        function renderWigGrid() {{
            const container = document.getElementById('wigSectorsContainer');
            if (!container) return;

            container.innerHTML = WIG_SECTORS.map(sec => `
                <div class="sector-card">
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: var(--text-color);">${{sec.sector}}</h3>
                    <div style="font-size: 0.8rem; color: var(--secondary-color); font-weight: 700; margin: 0.25rem 0 0.75rem 0;">
                        Przykładowe spółki GPW: ${{sec.tickers}}
                    </div>
                    
                    <div style="font-size: 0.85rem; margin-bottom: 0.6rem;">
                        <strong>Problem biznesowy controllingu:</strong><br>
                        ${{sec.problem}}
                    </div>

                    <div style="font-size: 0.85rem; margin-bottom: 0.6rem; white-space: pre-line;">
                        <strong>Rekomendowane use-case'y AI:</strong><br>
                        ${{sec.useCases}}
                    </div>

                    <div style="font-size: 0.82rem; color: #64748b; margin-bottom: 0.6rem;">
                        <strong>Źródła danych:</strong> ${{sec.dataSources}}
                    </div>

                    <div style="font-size: 0.78rem; font-weight: 700; text-transform: uppercase; color: #64748b; margin-top: 0.5rem;">
                        Przykładowy skrypt pozyskiwania danych (Python):
                    </div>
                    <pre class="code-block"><code>${{sec.pythonCode}}</code></pre>
                </div>
            `).join('');
        }}
    </script>
</body>
</html>
"""

# Zastąpienie placeholderów JSON
print("Injektowanie struktur danych do szablonu...")
HTML_FINAL = HTML_CONTENT.replace("__DATABASE_JSON__", json.dumps(DATABASE, ensure_ascii=False))
HTML_FINAL = HTML_FINAL.replace("__MODULES_DATA_JSON__", json.dumps(prepare_data.MODULES_CATALOG, ensure_ascii=False))
HTML_FINAL = HTML_FINAL.replace("__REPEATED_ITEMS_JSON__", json.dumps(prepare_data.REPEATED_ITEMS, ensure_ascii=False))
HTML_FINAL = HTML_FINAL.replace("__CHAPTERS_JSON__", json.dumps(CHAPTERS, ensure_ascii=False))
HTML_FINAL = HTML_FINAL.replace("__WIG_SECTORS_JSON__", json.dumps(WIG_SECTORS, ensure_ascii=False))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML_FINAL)

print(f"Pomyślnie wygenerowano index.html! Rozmiar pliku: {os.path.getsize('index.html')} bajtów.")
