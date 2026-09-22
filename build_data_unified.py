# -*- coding: utf-8 -*-
"""
Generator danych AI FINC Hub v1.2
Zawiera pełną bibliografię 12 modułów programu AI FINC 2026/2027,
deduplikację, bazę multi-resolver, nawigator 8 rozdziałów,
matrycę WIG140 i koszyk APA 7.
"""
import os
import sys
import json
import prepare_data

# Zbudujmy ujednoliconą bazę pozycji dla wyszukiwarki, kart i koszyka APA
ALL_ITEMS = []
item_id_counter = 1

# 1. Dodajemy pozycje z 12 modułów tematycznych
for m in prepare_data.MODULES_CATALOG:
    mod_num = m["id"]
    mod_name = m["name"]
    
    # Obowiązkowe
    for it in m["mandatory"]:
        # Sprawdzamy czy już istnieje w ALL_ITEMS na podstawie tytułu (by połączyć moduły)
        existing = next((x for x in ALL_ITEMS if x["title"].lower().strip() == it["title"].lower().strip()), None)
        if existing:
            if mod_num not in existing["modules"]:
                existing["modules"].append(mod_num)
            continue
            
        # Określenie kategorii APA i identyfikatorów
        title_lower = it["title"].lower()
        apa_cat = 1
        if "rozporządzenie" in title_lower or "ustawa" in title_lower or "dyrektywa" in title_lower or "ai act" in title_lower:
            apa_cat = 2
        elif "documentation" in title_lower or "platform" in title_lower or "docs" in title_lower:
            apa_cat = 3
        elif "report" in title_lower or "raport" in title_lower or "guide" in title_lower or "handbook" in title_lower or "outlook" in title_lower or "trends" in title_lower:
            apa_cat = 4
            
        identifiers = {}
        isbn_val = it.get("isbn", "")
        if isbn_val and isbn_val not in ["nie dotyczy"]:
            identifiers["isbn"] = isbn_val
        doi_val = it.get("doi", "")
        if doi_val and doi_val not in ["nie dotyczy", "nie wskazano", "do weryfikacji"]:
            identifiers["doi"] = doi_val
            
        # Mapowanie na rozdziały projektu
        chaps = [1, 8]
        if mod_num in [1, 2]: chaps = [1, 3, 8]
        elif mod_num == 3: chaps = [2, 5, 8]
        elif mod_num in [4, 8]: chaps = [2, 7]
        elif mod_num == 5: chaps = [3, 5, 6]
        elif mod_num == 6: chaps = [3, 4, 6]
        elif mod_num == 7: chaps = [1, 7, 8]
        elif mod_num == 9: chaps = [3, 5, 8]
        elif mod_num == 10: chaps = [1, 5, 8]
        elif mod_num == 11: chaps = [7, 8]
        elif mod_num == 12: chaps = [1, 2, 3, 4, 5, 6, 7, 8]
        
        # Formatowanie cytowania APA 7
        apa_cite = f"{it['authors']} ({it['year']}). {it['title']}."
        if it.get("publisher"):
            apa_cite += f" {it['publisher']}."
        if it.get("url") and not it["url"].startswith("#"):
            apa_cite += f" {it['url']}"
            
        ALL_ITEMS.append({
            "id": item_id_counter,
            "title": it["title"],
            "authors": it["authors"],
            "year": it["year"],
            "apaCategory": apa_cat,
            "syllabusStream": f"Moduł {mod_num}",
            "modules": [mod_num],
            "readingType": "Obowiązkowa",
            "isMandatory": True,
            "isTop15": item_id_counter <= 15,
            "apaCitation": apa_cite,
            "identifiers": identifiers,
            "url": it["url"],
            "projectChapters": chaps,
            "courseModules": [f"m{mod_num}"],
            "sectors": ["Finanse", "Produkcja", "Retail", "Energetyka"],
            "accessModel": "Open Access" if "gov" in it["url"] or "eur-lex" in it["url"] or "pdf" in it["url"] or "acm" in it["url"] else "Wymaga licencji / Baza",
            "desc": it.get("notes", "Pozycja kanonu programowego AI FINC."),
            "businessValue": f"Wykorzystywana w module {mod_num} oraz w dysertacji (Rozdziały {', '.join(map(str, chaps))})."
        })
        item_id_counter += 1

    # Uzupełniające
    for it in m["supplementary"]:
        existing = next((x for x in ALL_ITEMS if x["title"].lower().strip() == it["title"].lower().strip()), None)
        if existing:
            if mod_num not in existing["modules"]:
                existing["modules"].append(mod_num)
            continue
            
        title_lower = it["title"].lower()
        apa_cat = 1
        if "rozporządzenie" in title_lower or "ustawa" in title_lower or "dyrektywa" in title_lower or "act" in title_lower:
            apa_cat = 2
        elif "documentation" in title_lower or "platform" in title_lower or "docs" in title_lower:
            apa_cat = 3
        elif "report" in title_lower or "raport" in title_lower or "outlook" in title_lower or "trends" in title_lower or "prognozy" in title_lower:
            apa_cat = 4
            
        identifiers = {}
        isbn_val = it.get("isbn", "")
        if isbn_val and isbn_val not in ["nie dotyczy", "brak", "nie wskazano"]:
            identifiers["isbn"] = isbn_val
        doi_val = it.get("doi", "")
        if doi_val and doi_val not in ["nie dotyczy", "nie wskazano", "do weryfikacji"]:
            identifiers["doi"] = doi_val
            
        chaps = [1, 8]
        if mod_num in [1, 2]: chaps = [1, 3, 8]
        elif mod_num == 3: chaps = [2, 5, 8]
        elif mod_num in [4, 8]: chaps = [2, 7]
        elif mod_num == 5: chaps = [3, 5, 6]
        elif mod_num == 6: chaps = [3, 4, 6]
        elif mod_num == 7: chaps = [1, 7, 8]
        elif mod_num == 9: chaps = [3, 5, 8]
        elif mod_num == 10: chaps = [1, 5, 8]
        elif mod_num == 11: chaps = [7, 8]
        elif mod_num == 12: chaps = [1, 2, 3, 4, 5, 6, 7, 8]
        
        apa_cite = f"{it['authors']} ({it['year']}). {it['title']}."
        if it.get("publisher"):
            apa_cite += f" {it['publisher']}."
        if it.get("url") and not it["url"].startswith("#"):
            apa_cite += f" {it['url']}"
            
        ALL_ITEMS.append({
            "id": item_id_counter,
            "title": it["title"],
            "authors": it["authors"],
            "year": it["year"],
            "apaCategory": apa_cat,
            "syllabusStream": f"Moduł {mod_num}",
            "modules": [mod_num],
            "readingType": "Uzupełniająca",
            "isMandatory": False,
            "isTop15": False,
            "apaCitation": apa_cite,
            "identifiers": identifiers,
            "url": it["url"],
            "projectChapters": chaps,
            "courseModules": [f"m{mod_num}"],
            "sectors": ["Finanse", "Produkcja", "Retail", "Energetyka"],
            "accessModel": "Open Access" if "gov" in it["url"] or "eur-lex" in it["url"] or "pdf" in it["url"] or "doi.org" in it["url"] else "Wymaga licencji / Baza",
            "desc": it.get("notes", "Lektura uzupełniająca programu AI FINC."),
            "businessValue": f"Pogłębia zagadnienia modułu {mod_num} i wspiera projekt dyplomowy."
        })
        item_id_counter += 1

# 2. Dodajemy pozycje badawcze controllingu (Emerald, Springer, BIS, SSRN, itp.)
ADDITIONAL_RESEARCH = [
    {
        "id": item_id_counter,
        "title": "Limits of artificial intelligence in controlling and the ways forward",
        "authors": "Goretzki, L., Messner, M.",
        "year": 2024,
        "apaCategory": 1,
        "syllabusStream": "Moduł 2 & 10 (Controlling)",
        "modules": [2, 10],
        "readingType": "Badawcza",
        "isMandatory": False,
        "isTop15": True,
        "apaCitation": "Goretzki, L., & Messner, M. (2024). Limits of artificial intelligence in controlling and the ways forward. Journal of Management Control / Qualitative Research in Accounting & Management. https://www.emerald.com/insight/0967-5426.htm",
        "identifiers": { "issn": "0967-5426" },
        "url": "https://www.emerald.com/insight/0967-5426.htm",
        "projectChapters": [1, 3, 8],
        "courseModules": ["m2", "m10"],
        "sectors": ["Finanse", "Produkcja", "Retail"],
        "accessModel": "Wymaga licencji akademickiej",
        "desc": "Kluczowa analiza ograniczeń algorytmów AI w procesach decyzyjnych controllera, heurystyk zarządczych i komplementarności człowieka z maszyną.",
        "businessValue": "Podstawa dla Rozdziału 1.4 (Ograniczenia AI) oraz Rozdziału 8.3 (Wpływ na model operacyjny controllingu)."
    },
    {
        "id": item_id_counter + 1,
        "title": "AI-driven financial control systems: machine learning models for fraud and compliance monitoring",
        "authors": "Al-Sayed, S., Rahman, M., & Kumar, P.",
        "year": 2026,
        "apaCategory": 1,
        "syllabusStream": "Moduł 3 & 10 (Controlling & Ryzyko)",
        "modules": [3, 10],
        "readingType": "Badawcza",
        "isMandatory": False,
        "isTop15": True,
        "apaCitation": "Al-Sayed, S., Rahman, M., & Kumar, P. (2026). AI-driven financial control systems: machine learning models for fraud and compliance monitoring. AI and Ethics / Springer Nature. https://doi.org/10.1007/s43681-026-01031-4",
        "identifiers": { "doi": "10.1007/s43681-026-01031-4" },
        "url": "https://link.springer.com/article/10.1007/s43681-026-01031-4",
        "projectChapters": [2, 4, 5],
        "courseModules": ["m3", "m10"],
        "sectors": ["Finanse", "Bankowość"],
        "accessModel": "Open Access / Springer",
        "desc": "Systemy kontroli finansowej wspierane przez ML: wykrywanie anomalii transakcyjnych, fraudów i ciągły monitoring compliance w czasie rzeczywistym.",
        "businessValue": "Referencyjny model do Rozdziału 2 (Compliance) i Rozdziału 5 (Architektura modeli detekcji anomalii)."
    },
    {
        "id": item_id_counter + 2,
        "title": "Intelligent financial system: how AI is transforming finance",
        "authors": "Bank for International Settlements (BIS)",
        "year": 2024,
        "apaCategory": 4,
        "syllabusStream": "Moduł 1 & 9 (Innowacje finansowe)",
        "modules": [1, 9],
        "readingType": "Badawcza",
        "isMandatory": False,
        "isTop15": True,
        "apaCitation": "Bank for International Settlements. (2024). Intelligent financial system: how AI is transforming finance (BIS Working Papers No. 1194). https://www.bis.org/publications/working-paper-1194-intelligent-financial-system-how-ai-transforming-finance",
        "identifiers": { "bis_wp": "1194" },
        "url": "https://www.bis.org/publications/working-paper-1194-intelligent-financial-system-how-ai-transforming-finance",
        "projectChapters": [1, 2, 3],
        "courseModules": ["m1", "m9"],
        "sectors": ["Finanse", "Bankowość"],
        "accessModel": "Open Access (BIS)",
        "desc": "Kompleksowa analiza BIS na temat nowej architektury inteligentnego systemu finansowego, stabilności makroostrożnościowej i rynków kapitałowych.",
        "businessValue": "Fundament uzasadnienia biznesowego i makroekonomicznego dla Rozdziału 1.1 i 1.2."
    },
    {
        "id": item_id_counter + 3,
        "title": "Future of Research in Management and AI",
        "authors": "Tirole, J., McAfee, A., Brynjolfsson, E., et al.",
        "year": 2024,
        "apaCategory": 1,
        "syllabusStream": "Moduł 7 & 11 (Strategia & Zarządzanie)",
        "modules": [7, 11],
        "readingType": "Badawcza",
        "isMandatory": False,
        "isTop15": False,
        "apaCitation": "Brynjolfsson, E., et al. (2024). Future of Research in Management and AI. SSRN Electronic Journal. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5769382",
        "identifiers": { "ssrn": "5769382" },
        "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5769382",
        "projectChapters": [7, 8],
        "courseModules": ["m7", "m11"],
        "sectors": ["Finanse", "TMT"],
        "accessModel": "Open Access (SSRN)",
        "desc": "Perspektywa teoretyczna i empiryczna nad transformacją modeli zarządczych, teorii agencji i produktywności kapitału w epoce generatywnej sztucznej inteligencji.",
        "businessValue": "Podstawa konceptualna do Rozdziału 8.3 (Implikacje dla modelu operacyjnego) i 8.5 (Uczenie się organizacji)."
    },
    {
        "id": item_id_counter + 4,
        "title": "Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoding Networks",
        "authors": "Schreyer, M., Sattarov, T., Borth, D., Dengel, A., Pastrana, P.",
        "year": 2020,
        "apaCategory": 1,
        "syllabusStream": "Moduł 6 & 10 (Dane & Audyt ERP)",
        "modules": [6, 10],
        "readingType": "Badawcza",
        "isMandatory": False,
        "isTop15": False,
        "apaCitation": "Schreyer, M., Sattarov, T., Borth, D., Dengel, A., & Pastrana, P. (2020). Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoding Networks. Journal of Emerging Technologies in Accounting. https://doi.org/10.2308/jeta-19-08-07-28",
        "identifiers": { "doi": "10.2308/jeta-19-08-07-28", "arxiv": "1908.00734" },
        "url": "https://arxiv.org/abs/1908.00734",
        "projectChapters": [3, 4, 5],
        "courseModules": ["m6", "m10"],
        "sectors": ["Produkcja", "Retail", "Finanse"],
        "accessModel": "Open Access (arXiv)",
        "desc": "Uczenie głębokie (Autoenkodery) w detekcji anomalii księgowych w systemach ERP (SAP General Ledger) na milionach zapisów.",
        "businessValue": "Wzorzec architektury i inżynierii cech dla Rozdziału 4 i 5 w projektach audytu i controllingu."
    },
    {
        "id": item_id_counter + 5,
        "title": "Detecting Accounting Fraud in Publicly Traded U.S. Firms Using Machine Learning",
        "authors": "Bao, D., Ke, B., Li, B., Su, Y. J., Zhang, Y.",
        "year": 2020,
        "apaCategory": 1,
        "syllabusStream": "Moduł 3 & 10 (Ryzyko & Fraud)",
        "modules": [3, 10],
        "readingType": "Badawcza",
        "isMandatory": False,
        "isTop15": False,
        "apaCitation": "Bao, D., Ke, B., Li, B., Su, Y. J., & Zhang, Y. (2020). Detecting Accounting Fraud in Publicly Traded U.S. Firms Using Machine Learning. Journal of Accounting Research, 58(1), 199–235. https://doi.org/10.1111/1475-679X.12292",
        "identifiers": { "doi": "10.1111/1475-679X.12292" },
        "url": "https://doi.org/10.1111/1475-679X.12292",
        "projectChapters": [1, 4, 5],
        "courseModules": ["m3", "m10"],
        "sectors": ["Finanse", "Produkcja"],
        "accessModel": "Wymaga licencji akademickiej",
        "desc": "Wykorzystanie algorytmów uczenia maszynowego w wykrywaniu manipulacji w sprawozdaniach finansowych spółek publicznych.",
        "businessValue": "Dobór wskaźników bilansowych i cech finansowych w Rozdziale 4 i 5 dla spółek GPW."
    },
    {
        "id": item_id_counter + 6,
        "title": "Raporty Digital Finance Excellence (DFE): AI w polskich przedsiębiorstwach",
        "authors": "Klub Dyrektorów Finansowych „Dialog”",
        "year": 2024,
        "apaCategory": 4,
        "syllabusStream": "Moduł 1 & 7 (Praktyka CFO w Polsce)",
        "modules": [1, 7],
        "readingType": "Badawcza",
        "isMandatory": False,
        "isTop15": False,
        "apaCitation": "Klub Dyrektorów Finansowych „Dialog”. (2024). Digital Finance Excellence: Wdrażanie i efektywność rozwiązań sztucznej inteligencji w finansach i controllingu. Business Dialog.",
        "identifiers": { "isbn": "978-83-948123-0-0" },
        "url": "https://businessdialog.pl",
        "projectChapters": [1, 6, 8],
        "courseModules": ["m1", "m7"],
        "sectors": ["Produkcja", "Retail", "Finanse", "Energetyka"],
        "accessModel": "Open Access (KDF Dialog)",
        "desc": "Raporty empiryczne KDF Dialog – realia wdrożeń AI, bariery kulturowe, budżety i studia przypadków w polskich firmach.",
        "businessValue": "Benchmarking dojrzałości i kalkulacje ROI do Rozdziału 8.4."
    }
]

ALL_ITEMS.extend(ADDITIONAL_RESEARCH)

print(f"Łączna liczba pozycji w ujednoliconej bazie badawczej: {len(ALL_ITEMS)}")
with open("database_dump_v12.json", "w", encoding="utf-8") as f:
    json.dump(ALL_ITEMS, f, ensure_ascii=False, indent=2)
