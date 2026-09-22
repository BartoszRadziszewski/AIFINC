# -*- coding: utf-8 -*-
import os
import json

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI FINC – Academic Research Hub | Akademia Leona Koźmińskiego</title>
    <meta name="description" content="Autonomiczny dashboard badawczo-dydaktyczny wspierający słuchaczy studiów podyplomowych AI w finansach i controllingu przedsiębiorstw na Akademii Leona Koźmińskiego w przygotowaniu projektu końcowego dla spółek WIG140.">
    <meta name="author" content="Bartosz Radziszewski">
    
    <style>
        :root {
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
        }

        [data-theme="dark"] {
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
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            transition: background-color 0.25s, color 0.25s;
        }

        a { text-decoration: none; color: var(--accent-blue); }
        a:hover { text-decoration: underline; }

        /* Stylistyka tabel */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            font-size: 0.88rem;
            background: var(--card-bg);
            border-radius: 8px;
            overflow: hidden;
        }
        tr th, tr td {
            border: 1px solid var(--table-border);
            padding: 0.75rem 1rem;
            text-align: left;
        }
        tr th {
            background-color: var(--table-header-bg);
            font-weight: 700;
            color: var(--text-color);
        }

        /* Header */
        header {
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
        }
        .header-brand {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .logo-badge {
            background: linear-gradient(135deg, #0b2545 0%, #1e3a8a 100%);
            color: #fff;
            padding: 0.5rem 0.85rem;
            border-radius: 8px;
            font-weight: 800;
            font-size: 1.1rem;
            letter-spacing: 0.05em;
            border-bottom: 3px solid #b4865e;
        }
        .header-title h1 {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-color);
            line-height: 1.2;
        }
        .header-title p {
            font-size: 0.82rem;
            color: #64748b;
        }
        .header-actions {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        .btn-theme, .btn-basket-toggle, .btn-gh {
            background: var(--tag-bg);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            padding: 0.45rem 0.85rem;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            text-decoration: none;
        }
        .btn-theme:hover, .btn-basket-toggle:hover, .btn-gh:hover {
            border-color: var(--secondary-color);
            transform: translateY(-1px);
        }
        .badge-counter {
            background-color: var(--secondary-color);
            color: #fff;
            font-size: 0.75rem;
            padding: 0.15rem 0.45rem;
            border-radius: 10px;
            font-weight: 700;
        }

        /* Nav Tabs */
        .nav-tabs {
            background-color: var(--card-bg);
            border-bottom: 1px solid var(--border-color);
            display: flex;
            gap: 0.5rem;
            padding: 0 2rem;
            overflow-x: auto;
        }
        .tab-btn {
            background: transparent;
            border: none;
            border-bottom: 3px solid transparent;
            padding: 0.9rem 1.2rem;
            font-size: 0.92rem;
            font-weight: 600;
            color: #64748b;
            cursor: pointer;
            transition: all 0.2s;
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .tab-btn:hover {
            color: var(--text-color);
        }
        .tab-btn.active {
            color: var(--secondary-color);
            border-bottom-color: var(--secondary-color);
        }

        /* Main Container */
        .app-container {
            max-width: 1440px;
            margin: 0 auto;
            padding: 1.5rem 2rem;
        }

        .tab-pane {
            display: none;
        }
        .tab-pane.active {
            display: block;
        }

        /* Multi-Resolver */
        .resolver-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        .resolver-header h2 {
            font-size: 1.15rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .resolver-header p {
            font-size: 0.85rem;
            color: #64748b;
            margin-top: 0.2rem;
        }
        .search-box-row {
            display: flex;
            gap: 0.5rem;
            margin: 1rem 0 0.75rem 0;
            flex-wrap: wrap;
        }
        .resolver-input {
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
        }
        .resolver-input:focus {
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 3px rgba(70, 79, 235, 0.15);
        }
        .btn-resolve {
            background-color: var(--primary-color);
            color: #fff;
            border: none;
            padding: 0.75rem 1.4rem;
            font-size: 0.95rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.2s;
        }
        .btn-resolve:hover {
            background-color: var(--primary-hover);
        }
        .engine-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            align-items: center;
        }
        .engine-label {
            font-size: 0.78rem;
            font-weight: 700;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-right: 0.25rem;
        }
        .pill-btn {
            background: var(--tag-bg);
            color: var(--tag-text);
            border: 1px solid var(--border-color);
            padding: 0.35rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            text-decoration: none;
        }
        .pill-btn:hover {
            background-color: var(--secondary-color);
            color: #fff;
            border-color: var(--secondary-color);
        }
        .resolver-feedback {
            font-size: 0.82rem;
            margin-top: 0.6rem;
            font-weight: 500;
            min-height: 1.2rem;
        }

        /* Explorer Layout */
        .explorer-layout {
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 1.5rem;
            align-items: start;
        }
        @media (max-width: 960px) {
            .explorer-layout { grid-template-columns: 1fr; }
        }

        /* Filters Panel */
        .filters-panel {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.25rem;
            position: sticky;
            top: 5rem;
        }
        .filters-panel h3 {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .btn-reset-filters {
            font-size: 0.75rem;
            background: transparent;
            color: var(--secondary-color);
            border: none;
            cursor: pointer;
            font-weight: 600;
        }
        .filter-group {
            margin-bottom: 1.25rem;
        }
        .filter-title {
            font-size: 0.82rem;
            font-weight: 700;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 0.5rem;
        }
        .filter-select {
            width: 100%;
            padding: 0.5rem 0.75rem;
            font-size: 0.85rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: var(--bg-color);
            color: var(--text-color);
            outline: none;
        }

        /* Cards Grid */
        .cards-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            font-size: 0.9rem;
            color: #64748b;
        }
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 1.25rem;
        }
        .card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.25rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
            transform: translateY(-2px);
            box-shadow: var(--hover-shadow);
            border-color: #cbd5e1;
        }
        .card-meta-badges {
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
            margin-bottom: 0.65rem;
        }
        .badge {
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            letter-spacing: 0.02em;
        }
        .badge-top15 { background-color: #fef08a; color: #854d0e; border: 1px solid #facc15; font-weight: 800; }
        .badge-stream { background-color: #e2e8f0; color: #1e293b; }
        .badge-chapter { background-color: #e0e7ff; color: #3730a3; }
        .badge-apa-1 { background-color: #fef3c7; color: #92400e; }
        .badge-apa-2 { background-color: #fee2e2; color: #991b1b; }
        .badge-apa-3 { background-color: #ecfdf5; color: #065f46; }
        .badge-apa-4 { background-color: #f3e8ff; color: #6b21a8; }
        .badge-access { background-color: var(--tag-bg); color: var(--tag-text); }

        .card-title {
            font-size: 1.05rem;
            font-weight: 700;
            line-height: 1.35;
            margin-bottom: 0.4rem;
        }
        .card-authors {
            font-size: 0.83rem;
            color: #64748b;
            margin-bottom: 0.65rem;
            font-style: italic;
        }
        .card-desc {
            font-size: 0.85rem;
            color: var(--text-color);
            margin-bottom: 0.85rem;
            line-height: 1.5;
        }
        .card-callout {
            background-color: var(--callout-bg);
            border-left: 3px solid var(--secondary-color);
            padding: 0.6rem 0.75rem;
            border-radius: 0 6px 6px 0;
            font-size: 0.8rem;
            margin-bottom: 0.85rem;
        }
        .card-callout strong {
            color: var(--secondary-color);
            display: block;
            margin-bottom: 0.2rem;
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .card-identifiers {
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
            margin-bottom: 1rem;
        }
        .id-badge {
            font-size: 0.72rem;
            padding: 0.15rem 0.45rem;
            background-color: var(--id-badge-bg);
            color: var(--id-badge-text);
            border: 1px solid var(--id-badge-border);
            border-radius: 4px;
            text-decoration: none;
            font-family: monospace;
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
        }
        .card-footer {
            border-top: 1px solid var(--border-color);
            padding-top: 0.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.5rem;
        }
        .btn-card-action {
            background: var(--tag-bg);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            padding: 0.35rem 0.65rem;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s;
        }
        .btn-card-action:hover {
            background-color: var(--secondary-color);
            color: #fff;
            border-color: var(--secondary-color);
        }
        .btn-add-basket.in-basket {
            background-color: var(--success-color);
            color: #fff;
            border-color: var(--success-color);
        }

        /* Syllabus Section */
        .syllabus-section {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        .syllabus-section h3 {
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        [data-theme="dark"] .syllabus-section h3 {
            color: var(--primary-color);
        }
        .syllabus-subhead {
            font-size: 0.88rem;
            color: #64748b;
            margin-bottom: 1rem;
        }
        .top15-banner {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            border: 2px solid #f59e0b;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            color: #78350f;
        }
        [data-theme="dark"] .top15-banner {
            background: linear-gradient(135deg, #451a03 0%, #78350f 100%);
            border-color: #d97706;
            color: #fef3c7;
        }
        .top15-banner h2 {
            font-size: 1.25rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Toast */
        .toast {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #0f172a;
            color: #fff;
            padding: 0.75rem 1.25rem;
            border-radius: 8px;
            font-size: 0.88rem;
            font-weight: 600;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);
            z-index: 1000;
            display: none;
            border-left: 4px solid var(--secondary-color);
        }

        /* Footer */
        footer {
            background-color: var(--card-bg);
            border-top: 1px solid var(--border-color);
            padding: 2rem;
            margin-top: 3rem;
            text-align: center;
            font-size: 0.85rem;
            color: #64748b;
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-brand">
            <div class="logo-badge">AI FINC</div>
            <div class="header-title">
                <h1>AI FINC – Academic Research Hub</h1>
                <p>Akademia Leona Koźmińskiego • AI w Finansach i Controllingu Przedsiębiorstw • KDF „Dialog” • ACCA</p>
            </div>
        </div>
        <div class="header-actions">
            <button class="btn-basket-toggle" onclick="switchTab('tab-bibliography')">
                📚 Moja Bibliografia <span class="badge-counter" id="basketCount">0/30</span>
            </button>
            <button class="btn-theme" id="themeToggleBtn" onclick="toggleTheme()">
                🌙 Ciemny motyw
            </button>
            <a href="https://github.com/BartoszRadziszewski/AIFINC" target="_blank" class="btn-gh">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
                GitHub
            </a>
        </div>
    </header>

    <!-- Navigation Tabs -->
    <nav class="nav-tabs">
        <button class="tab-btn active" id="tabBtn-explorer" onclick="switchTab('tab-explorer')">
            🔍 Eksplorator Zasobów & Multi-Resolver
        </button>
        <button class="tab-btn" id="tabBtn-syllabus" onclick="switchTab('tab-syllabus')">
            📖 Kanon Programowy & TOP 15
        </button>
        <button class="tab-btn" id="tabBtn-navigator" onclick="switchTab('tab-navigator')">
            📋 Nawigator Projektu Końcowego (Rozdziały 1–8)
        </button>
        <button class="tab-btn" id="tabBtn-wig140" onclick="switchTab('tab-wig140')">
            🏢 Katalog Spółek WIG140 & Dane
        </button>
        <button class="tab-btn" id="tabBtn-bibliography" onclick="switchTab('tab-bibliography')">
            📑 Koszyk Bibliografii APA 7 (4 Grupy)
        </button>
    </nav>

    <!-- Main Container -->
    <main class="app-container">

        <!-- TAB 1: EKSPLORATOR & MULTI-RESOLVER -->
        <section id="tab-explorer" class="tab-pane active">
            
            <div class="resolver-card">
                <div class="resolver-header">
                    <h2>⚡ Akademicki Multi-Resolver 2.0 & Wyszukiwarka</h2>
                    <p>Wpisz DOI, SSRN, ORCID, ISBN, ISSN, arXiv, akt UE/RP lub zapytanie badawcze, aby natychmiast otworzyć właściwy rejestr naukowy lub przefiltrować bazę Hubu.</p>
                </div>
                <div class="search-box-row">
                    <input type="text" id="multiQueryInput" class="resolver-input" placeholder="Wpisz DOI (10.1108/...), SSRN (5769382), ORCID (0000-...), ISBN, akt UE (32024R1689) lub frazę (controlling, fraud, cash flow)..." oninput="onLiveSearch()">
                    <button class="btn-resolve" onclick="resolveQuery('auto')">⚡ Rozwiąż identyfikator</button>
                </div>
                <div class="engine-pills">
                    <span class="engine-label">Globalne bazy:</span>
                    <button class="pill-btn" onclick="resolveQuery('scholar')">Google Scholar</button>
                    <button class="pill-btn" onclick="resolveQuery('crossref')">CrossRef / DOI</button>
                    <button class="pill-btn" onclick="resolveQuery('scopus')">Scopus</button>
                    <button class="pill-btn" onclick="resolveQuery('researchgate')">🔬 ResearchGate</button>
                    <button class="pill-btn" onclick="resolveQuery('ssrn')">📑 SSRN</button>
                    <button class="pill-btn" onclick="resolveQuery('eurlex')">⚖️ EUR-Lex (AI Act)</button>
                    <button class="pill-btn" onclick="resolveQuery('isap')">🇵🇱 ISAP (Sejm)</button>
                    <button class="pill-btn" onclick="resolveQuery('gpw')">🏛️ GPW.pl</button>
                </div>
                <div class="resolver-feedback" id="resolverFeedback"></div>
            </div>

            <div class="explorer-layout">
                <aside class="filters-panel">
                    <h3>
                        <span>Filtry Zasobów</span>
                        <button class="btn-reset-filters" onclick="resetFilters()">Wyczyść</button>
                    </h3>

                    <div class="filter-group">
                        <div class="filter-title">Kanon Programowy AI FINC</div>
                        <select id="filterStream" class="filter-select" onchange="renderCards()">
                            <option value="all">Wszystkie strumienie programowe</option>
                            <option value="top15">⭐ Tylko TOP 15 Lektur Obowiązkowych</option>
                            <option value="I. Prawo, Compliance i Regulacje AI">I. Prawo, Compliance i Regulacje AI</option>
                            <option value="II. AI, Transformacja Cyfrowa i Zarządzanie">II. AI, Transformacja Cyfrowa i Zarządzanie</option>
                            <option value="III. CFO, Finanse i Controlling">III. CFO, Finanse i Controlling</option>
                            <option value="IV. Procesy Biznesowe i Dane">IV. Procesy Biznesowe i Dane</option>
                            <option value="V. Zarządzanie Ryzykiem">V. Zarządzanie Ryzykiem</option>
                            <option value="VI. Komunikacja AI i Kultura Organizacyjna">VI. Komunikacja AI i Kultura Organizacyjna</option>
                            <option value="VII. Rekomendacje Rozwojowe">VII. Rekomendacje Rozwojowe</option>
                        </select>
                    </div>

                    <div class="filter-group">
                        <div class="filter-title">Rozdział Projektu ALK</div>
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
                            <option value="Open Access">Open Access (Otwarty dostęp)</option>
                            <option value="Wymaga licencji akademickiej">Wymaga licencji / ALK</option>
                            <option value="Komercyjne">Komercyjne / Monografia</option>
                        </select>
                    </div>
                </aside>

                <div class="cards-column">
                    <div class="cards-header">
                        <div>Znaleziono: <strong id="resultCount">0</strong> pozycji</div>
                        <div id="activeFilterNotice"></div>
                    </div>
                    <div id="cardsContainer" class="cards-grid">
                        <!-- Renderowane dynamicznie z JS -->
                    </div>
                </div>
            </div>
        </section>

        <!-- TAB 2: KANON PROGRAMOWY & TOP 15 -->
        <section id="tab-syllabus" class="tab-pane">
            <div class="top15-banner">
                <h2>⭐ TOP 15 Lektur Obowiązkowych dla AI FINC</h2>
                <p>Ścisły kanon wiedzy menedżerskiej i technologicznej łączący finanse, controlling, inżynierię danych, regulacje i zarządzanie strategiczne.</p>
            </div>

            <div class="syllabus-section">
                <table>
                    <thead>
                        <tr>
                            <th style="width: 5%;">#</th>
                            <th style="width: 25%;">Instytucja / Autor</th>
                            <th style="width: 45%;">Tytuł Dzieła / Publikacji</th>
                            <th style="width: 25%;">Obszar tematyczny w programie</th>
                        </tr>
                    </thead>
                    <tbody id="top15TableBody">
                        <!-- Renderowane dynamicznie -->
                    </tbody>
                </table>
            </div>

            <div class="syllabus-section">
                <h3>I. PRAWO, COMPLIANCE I REGULACJE AI</h3>
                <div class="syllabus-subhead">Lektury obowiązkowe i uzupełniające dotyczące EU AI Act, RODO, Kodeksu Cywilnego i cyberbezpieczeństwa.</div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 30%;">Instytucja / Źródło</th>
                            <th style="width: 45%;">Akt Prawny / Wytyczne</th>
                            <th style="width: 25%;">Status & Odnośnik</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>European Parliament</td>
                            <td><strong>EU AI Act (Rozporządzenie UE 2024/1689 w sprawie sztucznej inteligencji)</strong></td>
                            <td><a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32024R1689" target="_blank">EUR-Lex CELEX:32024R1689</a></td>
                        </tr>
                        <tr>
                            <td>Sejm RP</td>
                            <td><strong>Ustawa z dnia 10 maja 2018 r. o ochronie danych osobowych</strong></td>
                            <td><a href="https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20180001000" target="_blank">ISAP Dz.U. 2018 poz. 1000</a></td>
                        </tr>
                        <tr>
                            <td>Parlament Europejski i Rada UE</td>
                            <td><strong>GDPR / RODO – Rozporządzenie (UE) 2016/679</strong></td>
                            <td><a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:32016R0679" target="_blank">EUR-Lex CELEX:32016R0679</a></td>
                        </tr>
                        <tr>
                            <td>Sejm RP</td>
                            <td><strong>Ustawa z dnia 23 kwietnia 1964 r. – Kodeks cywilny</strong></td>
                            <td><a href="https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU19640160093" target="_blank">ISAP Dz.U. 1964 nr 16 poz. 93</a></td>
                        </tr>
                        <tr>
                            <td>European Parliament</td>
                            <td>Dyrektywa NIS 2 (2022/2555 w sprawie cyberbezpieczeństwa)</td>
                            <td><a href="https://eur-lex.europa.eu/eli/dir/2022/2555" target="_blank">EUR-Lex NIS2</a></td>
                        </tr>
                        <tr>
                            <td>European Parliament</td>
                            <td>European Data Act (Rozporządzenie 2023/2854)</td>
                            <td><a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854" target="_blank">EUR-Lex Data Act</a></td>
                        </tr>
                        <tr>
                            <td>Komisja Europejska</td>
                            <td>Ethics Guidelines for Trustworthy AI (Wytyczne etyczne)</td>
                            <td><a href="https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai" target="_blank">Komisja Europejska</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="syllabus-section">
                <h3>II. AI, TRANSFORMACJA CYFROWA I ZARZĄDZANIE</h3>
                <div class="syllabus-subhead">Globalne raporty strategiczne i standardy profesjonalne (Stanford, McKinsey, Deloitte, ACCA, IBM, CFA, WEF).</div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Instytucja / Autor</th>
                            <th style="width: 50%;">Raport / Publikacja</th>
                            <th style="width: 25%;">Źródło oficjalne</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Stanford University</td>
                            <td><strong>Artificial Intelligence Index Report 2025</strong></td>
                            <td><a href="https://aiindex.stanford.edu" target="_blank">Stanford AI Index</a></td>
                        </tr>
                        <tr>
                            <td>Stanford University</td>
                            <td><strong>Artificial Intelligence Index Report 2024</strong></td>
                            <td><a href="https://aiindex.stanford.edu" target="_blank">Stanford AI Index</a></td>
                        </tr>
                        <tr>
                            <td>McKinsey & Company</td>
                            <td><strong>The State of AI: How Organizations Are Rewiring to Capture Value</strong></td>
                            <td><a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai" target="_blank">McKinsey QuantumBlack</a></td>
                        </tr>
                        <tr>
                            <td>Deloitte</td>
                            <td><strong>State of Generative AI in the Enterprise</strong></td>
                            <td><a href="https://www.deloitte.com" target="_blank">Deloitte AI Institute</a></td>
                        </tr>
                        <tr>
                            <td>ACCA</td>
                            <td><strong>Chief Value Officer: The Important Evolution of the CFO</strong></td>
                            <td><a href="https://www.accaglobal.com" target="_blank">ACCA Global</a></td>
                        </tr>
                        <tr>
                            <td>IBM</td>
                            <td><strong>The CEO's Guide to Generative AI</strong></td>
                            <td><a href="https://www.ibm.com/thought-leadership/institute-business-value" target="_blank">IBM IBV</a></td>
                        </tr>
                        <tr>
                            <td>CFA Institute</td>
                            <td><strong>Handbook of Artificial Intelligence and Big Data Applications in Investments</strong></td>
                            <td><a href="https://rpc.cfainstitute.org" target="_blank">CFA Institute Research</a></td>
                        </tr>
                        <tr>
                            <td>World Economic Forum</td>
                            <td><strong>Artificial Intelligence in Financial Services</strong></td>
                            <td><a href="https://www.weforum.org/reports" target="_blank">WEF Reports</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="syllabus-section">
                <h3>III. CFO, FINANSE I CONTROLLING</h3>
                <div class="syllabus-subhead">Literatura podstawowa i najświeższe badania naukowe z zakresu controllingu, audytu i oceny ryzyka.</div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Autor / Organizacja</th>
                            <th style="width: 50%;">Tytuł publikacji</th>
                            <th style="width: 25%;">Dostęp / Link</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>ACCA</td>
                            <td><strong>AI in the Finance Profession</strong></td>
                            <td><a href="https://www.accaglobal.com" target="_blank">ACCA Publication</a></td>
                        </tr>
                        <tr>
                            <td>ACCA & PwC</td>
                            <td>Transformational Journeys: Finance and the Agile Organisation</td>
                            <td><a href="https://www.accaglobal.com" target="_blank">ACCA Global</a></td>
                        </tr>
                        <tr>
                            <td>Financial Stability Board</td>
                            <td>The Financial Stability Implications of Artificial Intelligence</td>
                            <td><a href="https://www.fsb.org" target="_blank">FSB Report</a></td>
                        </tr>
                        <tr>
                            <td>Harish Kumar Sriram (2024)</td>
                            <td>Leveraging AI/ML for Next-Generation Credit Risk Assessment Models</td>
                            <td><a href="https://esa-research.com/index.php/eajse/article/view/4" target="_blank">EAJSE Article</a></td>
                        </tr>
                        <tr>
                            <td>Pavlović, Gligorić, Zdravković (2024)</td>
                            <td>Revolutionizing Management Accounting: Role of AI in Predictive Analytics</td>
                            <td><a href="https://bi.ue-varna.bg/ojs/index.php/bmc/article/view/77" target="_blank">BMC Publication</a></td>
                        </tr>
                        <tr>
                            <td>Satyadhar Joshi (2025)</td>
                            <td>Gen AI Agentic Framework for Financial Risk Management</td>
                            <td><a href="https://www.researchgate.net/publication/388717177_Gen_AI_for_Market_Risk_and_Credit_Risk_Learn_Agentically_powered_Gen_AI_Gen_AI_Agentic_Framework_for_Financial_Risk_Management" target="_blank">ResearchGate</a></td>
                        </tr>
                        <tr>
                            <td>Losbichler & Lehner (2021)</td>
                            <td>Limits of artificial intelligence in controlling and the ways forward</td>
                            <td><a href="https://doi.org/10.1108/JAAR-10-2020-0207" target="_blank">Emerald Insight</a></td>
                        </tr>
                        <tr>
                            <td>Ergashev (2026)</td>
                            <td>AI-driven financial control systems: machine learning for fraud & compliance</td>
                            <td><a href="https://doi.org/10.1007/s43681-026-01031-4" target="_blank">Springer AI & Ethics</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="syllabus-section">
                <h3>IV. PROCESY BIZNESOWE I DANE</h3>
                <div class="syllabus-subhead">Zarządzanie procesowe (BPM/BPMN) oraz architektura nowoczesnej inżynierii danych korporacyjnych.</div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Autor</th>
                            <th style="width: 50%;">Tytuł monografii / podręcznika</th>
                            <th style="width: 25%;">Wydawnictwo</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Dumas, La Rosa, Mendling, Reijers</td>
                            <td><strong>Business Process Management: Koncepcje, języki, architektury</strong></td>
                            <td><a href="https://ksiegarnia.pwn.pl" target="_blank">PWN (2022)</a></td>
                        </tr>
                        <tr>
                            <td>Marek Szelągowski</td>
                            <td><strong>Zarządzanie procesowe w gospodarce wiedzy</strong></td>
                            <td><a href="https://www.wydawnictwolinia.pl" target="_blank">Wydawnictwo Linia</a></td>
                        </tr>
                        <tr>
                            <td>Zbigniew Misiak</td>
                            <td>Modelowanie procesów biznesowych. BPMN 2.0 od podstaw</td>
                            <td><a href="https://helion.pl" target="_blank">Wydawnictwo Helion</a></td>
                        </tr>
                        <tr>
                            <td>Ewa Brzychczy, Katarzyna Rostek</td>
                            <td>Cyfrowa analiza danych i procesów w przedsiębiorstwie</td>
                            <td><a href="https://pwe.com.pl" target="_blank">PWE</a></td>
                        </tr>
                        <tr>
                            <td>Piotr Plich</td>
                            <td>Zarządzanie zbiorami danych o dużej skali. Data Mesh i Data Fabric</td>
                            <td><a href="https://helion.pl" target="_blank">Wydawnictwo Helion</a></td>
                        </tr>
                        <tr>
                            <td>Joe Reis, Matt Housley</td>
                            <td><strong>Inżynieria danych w praktyce</strong></td>
                            <td><a href="https://helion.pl" target="_blank">Wydawnictwo Helion / O'Reilly</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="syllabus-section">
                <h3>V. ZARZĄDZANIE RYZYKIEM</h3>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Autor / Redaktor</th>
                            <th style="width: 50%;">Tytuł publikacji</th>
                            <th style="width: 25%;">Wydawca</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Krzysztof Jajuga (red.)</td>
                            <td><strong>Zarządzanie ryzykiem</strong></td>
                            <td><a href="https://ksiegarnia.pwn.pl" target="_blank">Wydawnictwo Naukowe PWN</a></td>
                        </tr>
                        <tr>
                            <td>Piyush Ranjan, Brij Kishore Pandey, Rajiv Avacharmal</td>
                            <td>Artificial Intelligence and Financial Security</td>
                            <td><a href="https://bpbonline.com" target="_blank">BPB Online</a></td>
                        </tr>
                        <tr>
                            <td>Mahmoud Galety, Arul Kumar Claver, Sriharsha i in.</td>
                            <td>Data Analytics and AI for Quantitative Risk Assessment and Financial Computation</td>
                            <td><a href="https://www.igi-global.com" target="_blank">IGI Global</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="syllabus-section">
                <h3>VI. KOMUNIKACJA AI I KULTURA ORGANIZACYJNA</h3>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Autorzy</th>
                            <th style="width: 50%;">Tytuł dzieła</th>
                            <th style="width: 25%;">Wydawnictwo</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Jarosław Rubin, Wojciech Grabowski, Marta Naumiuk</td>
                            <td>Zwinnologia 2.0. Agile w zarządzaniu zmianą</td>
                            <td><a href="https://mtbiznes.pl" target="_blank">MT Biznes</a></td>
                        </tr>
                        <tr>
                            <td>Adam Brotman, Andy Sack</td>
                            <td>AI First: The Playbook for a Future-Proof Business and Brand</td>
                            <td><a href="https://store.hbr.org" target="_blank">Harvard Business Review Press</a></td>
                        </tr>
                        <tr>
                            <td>Piotr Czopek (red.)</td>
                            <td>Zarządzanie – komunikacja – nowoczesność</td>
                            <td><a href="https://fnce.pl" target="_blank">FNCE</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="syllabus-section">
                <h3>VII. POZYCJE REKOMENDOWANE DO PROGRAMU</h3>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Autor / Instytucja</th>
                            <th style="width: 50%;">Tytuł raportu / książki</th>
                            <th style="width: 25%;">Wydawca / Źródło</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Ethan Mollick</td>
                            <td><strong>Co-Intelligence: Living and Working with AI</strong></td>
                            <td><a href="https://www.penguinrandomhouse.com" target="_blank">Penguin Random House</a></td>
                        </tr>
                        <tr>
                            <td>Thomas H. Davenport, Randy Bean</td>
                            <td>All-In on AI: How Smart Companies Win Big with Artificial Intelligence</td>
                            <td><a href="https://store.hbr.org" target="_blank">Harvard Business Review Press</a></td>
                        </tr>
                        <tr>
                            <td>Microsoft WorkLab</td>
                            <td>Work Trend Index 2024 / 2025: AI at Work Is Here. Now Comes the Hard Part</td>
                            <td><a href="https://www.microsoft.com/worklab/work-trend-index" target="_blank">Microsoft WorkLab</a></td>
                        </tr>
                        <tr>
                            <td>Boston Consulting Group (BCG)</td>
                            <td>The Widening AI Value Gap: Why Only 10% of Companies Generate Significant Value</td>
                            <td><a href="https://www.bcg.com" target="_blank">BCG Publications</a></td>
                        </tr>
                        <tr>
                            <td>NVIDIA</td>
                            <td>State of AI in Financial Services: Trends, Deployments, and Challenges</td>
                            <td><a href="https://www.nvidia.com" target="_blank">NVIDIA Reports</a></td>
                        </tr>
                        <tr>
                            <td>Hagen Ketterer, Heiko Himmelreich</td>
                            <td>The AI-First Company: How to Compete and Win with AI</td>
                            <td><a href="https://store.hbr.org" target="_blank">Harvard Business Review Press</a></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- TAB 3: NAWIGATOR PROJEKTU KOŃCOWEGO (ROZDZIAŁY 1-8) -->
        <section id="tab-navigator" class="tab-pane">
            <div class="resolver-card">
                <div class="resolver-header" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div>
                        <h2>📋 Przewodnik po Wytycznych Projektu Końcowego (WIG140)</h2>
                        <p>Struktura 8 obowiązkowych rozdziałów merytorycznych określona przez Komisję Egzaminacyjną ALK. Odhaczaj zrealizowane etapy – postęp jest automatycznie zapisywany.</p>
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <div>
                            <div style="font-size: 0.8rem; color: #64748b; margin-bottom: 0.2rem;">Postęp pracy:</div>
                            <strong id="progressText" style="font-size: 1.1rem; color: var(--secondary-color);">0% ukończono</strong>
                        </div>
                        <div style="width: 180px; height: 12px; background: var(--tag-bg); border-radius: 6px; overflow: hidden;">
                            <div id="progressBarFill" style="height: 100%; background: linear-gradient(90deg, #10b981 0%, #059669 100%); width: 0%; transition: width 0.4s;"></div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="chapters-container" id="chaptersContainer" style="display: flex; flex-direction: column; gap: 1.25rem;">
                <!-- Renderowane w JS -->
            </div>
        </section>

        <!-- TAB 4: KATALOG SPÓŁEK WIG140 & DANE -->
        <section id="tab-wig140" class="tab-pane">
            <div class="resolver-card">
                <div class="resolver-header">
                    <h2>🏢 Katalog Spółek WIG140 & Źródła Danych (Smart Connector)</h2>
                    <p>Wytyczne nakazują wybór spółki z indeksu <strong>WIG140</strong> z publicznie dostępnymi danymi. Poniżej znajduje się matryca sektorowa, typowe use-case'y AI w controllingu oraz bezpośrednie odnośniki do pobierania danych.</p>
                </div>
            </div>

            <div class="cards-grid" id="wigGrid" style="margin-top: 1.5rem;">
                <!-- Renderowane w JS -->
            </div>
        </section>

        <!-- TAB 5: KOSZYK BIBLIOGRAFII APA 7 -->
        <section id="tab-bibliography" class="tab-pane">
            <div class="resolver-card" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <div>
                    <h2>📚 Moja Bibliografia do Projektu Końcowego (Format APA 7)</h2>
                    <p>Wytyczne ALK wymagają <strong>min. 20–30 pozycji</strong> podzielonych na cztery grupy. Dodawaj źródła z bazy jednym kliknięciem, a następnie skopiuj gotowy spis do Worda.</p>
                </div>
                <div>
                    <button class="btn-resolve" onclick="copyWholeBibliography()">📋 Kopiuj całą bibliografię do schowka</button>
                    <button class="btn-card-action" onclick="clearBibliography()" style="margin-left: 0.5rem;">Wyczyść koszyk</button>
                </div>
            </div>

            <div id="biblioContainer">
                <!-- Renderowane dynamicznie w JS: 4 grupy APA -->
            </div>
        </section>

    </main>

    <!-- Toast Notification -->
    <div id="toast" class="toast"></div>

    <!-- Footer -->
    <footer>
        <p><strong>AI FINC – Academic Research Hub</strong> • Platforma wsparcia merytorycznego studiów podyplomowych ALK</p>
        <p>Partner kierunku: <a href="https://businessdialog.pl" target="_blank">Klub Dyrektorów Finansowych „Dialog”</a> • Patronat: <a href="https://www.accaglobal.com" target="_blank">ACCA Think Ahead</a></p>
        <p style="margin-top: 0.5rem; font-size: 0.78rem;">Autor: <a href="https://github.com/BartoszRadziszewski" target="_blank">Bartosz Radziszewski</a> • Repozytorium: <a href="https://github.com/BartoszRadziszewski/AIFINC" target="_blank">github.com/BartoszRadziszewski/AIFINC</a> • Licencja MIT</p>
    </footer>

    <!-- Logika aplikacji i Baza Danych -->
    <script>
        const DATABASE = __DATABASE_JSON__;
        const CHAPTERS = __CHAPTERS_JSON__;
        const WIG_SECTORS = __WIG_SECTORS_JSON__;

        let userBasket = JSON.parse(localStorage.getItem('aifinc_basket') || '[]');
        let userChecklist = JSON.parse(localStorage.getItem('aifinc_checklist') || '{}');

        document.addEventListener('DOMContentLoaded', () => {
            initTheme();
            renderCards();
            renderTop15Table();
            renderNavigator();
            renderWigGrid();
            renderBibliography();
            updateProgress();
            updateBasketCount();
        });

        function switchTab(tabId) {
            document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

            const targetPane = document.getElementById(tabId);
            if (targetPane) targetPane.classList.add('active');

            const btnMap = {
                'tab-explorer': 'tabBtn-explorer',
                'tab-syllabus': 'tabBtn-syllabus',
                'tab-navigator': 'tabBtn-navigator',
                'tab-wig140': 'tabBtn-wig140',
                'tab-bibliography': 'tabBtn-bibliography'
            };
            const activeBtn = document.getElementById(btnMap[tabId]);
            if (activeBtn) activeBtn.classList.add('active');

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function renderTop15Table() {
            const tbody = document.getElementById('top15TableBody');
            if (!tbody) return;

            const top15 = DATABASE.filter(d => d.isTop15);
            tbody.innerHTML = top15.map((it, idx) => `
                <tr>
                    <td><strong>${idx + 1}</strong></td>
                    <td>${it.authors}</td>
                    <td><strong><a href="${it.url}" target="_blank">${it.title}</a></strong></td>
                    <td><span class="badge badge-stream">${it.syllabusStream}</span></td>
                </tr>
            `).join('');
        }

        function renderCards() {
            const container = document.getElementById('cardsContainer');
            const searchVal = (document.getElementById('multiQueryInput').value || '').trim().toLowerCase();
            const streamFilter = document.getElementById('filterStream').value;
            const chapterFilter = document.getElementById('filterChapter').value;
            const categoryFilter = document.getElementById('filterCategory').value;
            const sectorFilter = document.getElementById('filterSector').value;
            const accessFilter = document.getElementById('filterAccess').value;

            const filtered = DATABASE.filter(item => {
                if (searchVal) {
                    const fullText = (item.title + ' ' + item.authors + ' ' + item.desc + ' ' + item.businessValue + ' ' + JSON.stringify(item.identifiers || {})).toLowerCase();
                    if (!fullText.includes(searchVal)) return false;
                }
                if (streamFilter === 'top15' && !item.isTop15) return false;
                if (streamFilter !== 'all' && streamFilter !== 'top15' && item.syllabusStream !== streamFilter) return false;
                if (chapterFilter !== 'all' && !item.projectChapters.includes(parseInt(chapterFilter))) return false;
                if (categoryFilter !== 'all' && item.apaCategory !== parseInt(categoryFilter)) return false;
                if (sectorFilter !== 'all' && !(item.sectors || []).includes(sectorFilter)) return false;
                if (accessFilter !== 'all' && item.accessModel !== accessFilter) return false;

                return true;
            });

            document.getElementById('resultCount').textContent = filtered.length;

            if (filtered.length === 0) {
                container.innerHTML = `<div style="grid-column: 1/-1; padding: 3rem; text-align: center; color: #64748b; background: var(--card-bg); border-radius: 12px; border: 1px dashed var(--border-color);">
                    <h3>Brak pozycji spełniających podane kryteria</h3>
                    <p style="margin-top: 0.5rem;">Zmień filtry w panelu bocznym lub skorzystaj z wyszukiwarki globalnej u góry.</p>
                </div>`;
                return;
            }

            container.innerHTML = filtered.map(item => {
                const inBasket = userBasket.some(b => b.id === item.id);
                const categoryNames = {
                    1: '1. Artykuł / Książka',
                    2: '2. Akt prawny',
                    3: '3. Źródło internetowe',
                    4: '4. Raport ekspercki'
                };

                let idBadges = '';
                if (item.identifiers) {
                    if (item.identifiers.doi) idBadges += `<a href="https://doi.org/${item.identifiers.doi}" target="_blank" class="id-badge">DOI: ${item.identifiers.doi}</a>`;
                    if (item.identifiers.ssrn) idBadges += `<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=${item.identifiers.ssrn}" target="_blank" class="id-badge">SSRN: ${item.identifiers.ssrn}</a>`;
                    if (item.identifiers.arxiv) idBadges += `<a href="https://arxiv.org/abs/${item.identifiers.arxiv}" target="_blank" class="id-badge">arXiv: ${item.identifiers.arxiv}</a>`;
                    if (item.identifiers.isbn) idBadges += `<span class="id-badge">ISBN: ${item.identifiers.isbn}</span>`;
                    if (item.identifiers.issn) idBadges += `<span class="id-badge">ISSN: ${item.identifiers.issn}</span>`;
                    if (item.identifiers.celex) idBadges += `<a href="https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:${item.identifiers.celex}" target="_blank" class="id-badge">EUR-Lex: ${item.identifiers.celex}</a>`;
                    if (item.identifiers.isap) idBadges += `<a href="https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=${item.identifiers.isap}" target="_blank" class="id-badge">ISAP: ${item.identifiers.isap}</a>`;
                    if (item.identifiers.orcid) idBadges += `<a href="https://orcid.org/${item.identifiers.orcid}" target="_blank" class="id-badge">ORCID: ${item.identifiers.orcid}</a>`;
                }

                const chaptersBadge = item.projectChapters.map(ch => `<span class="badge badge-chapter">Rozdz. ${ch}</span>`).join(' ');
                const top15Badge = item.isTop15 ? `<span class="badge badge-top15">⭐ TOP 15 KANON</span>` : '';

                return `
                <div class="card">
                    <div class="card-top">
                        <div class="card-meta-badges">
                            ${top15Badge}
                            <span class="badge badge-apa-${item.apaCategory}">${categoryNames[item.apaCategory]}</span>
                            ${chaptersBadge}
                            <span class="badge badge-access">${item.accessModel}</span>
                        </div>
                        <h4 class="card-title"><a href="${item.url}" target="_blank">${item.title}</a></h4>
                        <div class="card-authors">${item.authors} (${item.year})</div>
                        <div style="font-size: 0.78rem; color: var(--secondary-color); font-weight: 700; margin-bottom: 0.4rem;">${item.syllabusStream || ''}</div>
                        <div class="card-desc">${item.desc}</div>
                        <div class="card-callout">
                            <strong>Wartość dla Projektu Końcowego:</strong>
                            ${item.businessValue}
                        </div>
                        <div class="card-identifiers">
                            ${idBadges}
                        </div>
                    </div>
                    <div class="card-footer">
                        <button class="btn-card-action" onclick="copyCitation(${item.id})">📋 Kopiuj APA</button>
                        <button class="btn-card-action btn-add-basket ${inBasket ? 'in-basket' : ''}" id="btnBasket-${item.id}" onclick="toggleBasketItem(${item.id})">
                            ${inBasket ? '✓ W bibliografii' : '+ Do projektu'}
                        </button>
                    </div>
                </div>
                `;
            }).join('');
        }

        function onLiveSearch() {
            renderCards();
        }

        function resetFilters() {
            document.getElementById('multiQueryInput').value = '';
            document.getElementById('filterStream').value = 'all';
            document.getElementById('filterChapter').value = 'all';
            document.getElementById('filterCategory').value = 'all';
            document.getElementById('filterSector').value = 'all';
            document.getElementById('filterAccess').value = 'all';
            renderCards();
            showToast('Zresetowano filtry wyszukiwania');
        }

        function filterByChapter(chId) {
            switchTab('tab-explorer');
            document.getElementById('filterChapter').value = chId;
            renderCards();
            showToast(`Przefiltrowano bazę dla Rozdziału ${chId}`);
        }

        function resolveQuery(engine) {
            const input = document.getElementById('multiQueryInput');
            const feedback = document.getElementById('resolverFeedback');
            const query = input.value.trim();

            if (!query) {
                feedback.textContent = 'Wpisz identyfikator (DOI, SSRN, ISBN, akt prawny) lub frazę tematyczną.';
                feedback.style.color = '#ef4444';
                input.focus();
                return;
            }

            const clean = query.replace(/^(doi:|https?:\/\/doi\.org\/)/i, '')
                               .replace(/^(https?:\/\/orcid\.org\/)/i, '')
                               .replace(/^(arxiv:)/i, '')
                               .replace(/^(https?:\/\/papers\.ssrn\.com\/sol3\/papers\.cfm\?abstract_id=)/i, '')
                               .trim();

            let targetUrl = '';
            let detected = '';

            if (engine === 'auto') {
                if (/^10\.\d{4,9}\/[-._;()/:A-Za-z0-9]+$/i.test(clean)) {
                    targetUrl = `https://doi.org/${clean}`;
                    detected = `Identyfikator DOI (${clean}) → Otwieranie publikacji przez doi.org`;
                } else if (/^0000-000[1-3]-\d{4}-\d{3}[\dX]$/i.test(clean)) {
                    targetUrl = `https://orcid.org/${clean}`;
                    detected = `Identyfikator badacza ORCID (${clean}) → Profil badawczy`;
                } else if (/^ssrn:?(\d+)$/i.test(clean) || /^\d{7}$/.test(clean)) {
                    const id = clean.replace(/^ssrn:?/i, '');
                    targetUrl = `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=${id}`;
                    detected = `Identyfikator SSRN (${id}) → Otwieranie publikacji SSRN`;
                } else if (/^\d{4}\.\d{4,5}(v\d+)?$/i.test(clean)) {
                    targetUrl = `https://arxiv.org/abs/${clean}`;
                    detected = `Preprint arXiv (${clean}) → Repozytorium otwartej nauki`;
                } else if (/^(?:97[89][- ]?)?(?:\d[- ]?){9}[\dX]$/i.test(clean.replace(/[- ]/g, ''))) {
                    targetUrl = `https://isbnsearch.org/isbn/${clean.replace(/[- ]/g, '')}`;
                    detected = `Numer monografii ISBN (${clean}) → Wyszukiwarka książek`;
                } else if (/^\d{4}-\d{3}[\dX]$/i.test(clean)) {
                    targetUrl = `https://portal.issn.org/resource/ISSN/${clean}`;
                    detected = `Czasopismo ISSN (${clean}) → Międzynarodowy Rejestr ISSN`;
                } else if (/^3\d{4}[RL]\d{4}$/i.test(clean)) {
                    targetUrl = `https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=CELEX:${clean}`;
                    detected = `Akt prawny UE CELEX (${clean}) → EUR-Lex`;
                } else {
                    targetUrl = `https://scholar.google.com/scholar?q=${encodeURIComponent(query)}`;
                    detected = `Fraza badawcza (${query}) → Wyszukiwanie pełnotekstowe w Google Scholar`;
                }
            } else if (engine === 'scholar') {
                targetUrl = `https://scholar.google.com/scholar?q=${encodeURIComponent(query)}`;
            } else if (engine === 'crossref') {
                targetUrl = `https://search.crossref.org/?q=${encodeURIComponent(query)}`;
            } else if (engine === 'scopus') {
                targetUrl = `https://www.scopus.com/results/authorNamesList.uri?st1=${encodeURIComponent(query)}`;
            } else if (engine === 'researchgate') {
                targetUrl = `https://www.researchgate.net/search/publication?q=${encodeURIComponent(query)}`;
            } else if (engine === 'ssrn') {
                targetUrl = `https://www.ssrn.com/index.cfm/en/search/?term=${encodeURIComponent(query)}`;
            } else if (engine === 'eurlex') {
                targetUrl = `https://eur-lex.europa.eu/search.html?scope=EURLEX&text=${encodeURIComponent(query)}&lang=pl&type=quick`;
            } else if (engine === 'isap') {
                targetUrl = `https://isap.sejm.gov.pl/isap.nsf/ByName.xsp?key=${encodeURIComponent(query)}`;
            } else if (engine === 'gpw') {
                targetUrl = `https://www.gpw.pl/szukaj?query=${encodeURIComponent(query)}`;
            }

            feedback.style.color = 'var(--secondary-color)';
            feedback.textContent = detected || `Przekierowanie do serwisu: ${targetUrl}`;
            window.open(targetUrl, '_blank', 'noopener,noreferrer');
        }

        function renderNavigator() {
            const container = document.getElementById('chaptersContainer');
            if (!container) return;
            container.innerHTML = CHAPTERS.map(ch => {
                const checkHtml = ch.items.map(it => {
                    const isChecked = userChecklist[it.id] ? 'checked' : '';
                    return `
                    <label style="display: flex; align-items: flex-start; gap: 0.65rem; font-size: 0.88rem; cursor: pointer;">
                        <input type="checkbox" id="${it.id}" ${isChecked} onchange="toggleCheck('${it.id}')" style="margin-top: 0.25rem; accent-color: var(--secondary-color);">
                        <span>${it.text}</span>
                    </label>
                    `;
                }).join('');

                return `
                <div class="card" style="padding: 1.5rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border-color);">
                        <h3 style="font-size: 1.1rem; font-weight: 700;">${ch.title}</h3>
                        <span class="badge badge-chapter">${ch.reqBadge}</span>
                    </div>
                    <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 0.5rem;">${ch.desc}</p>
                    <div style="margin: 1rem 0; display: flex; flex-direction: column; gap: 0.5rem;">
                        ${checkHtml}
                    </div>
                    <div style="margin-top: 1rem; display: flex; justify-content: flex-end;">
                        <button class="btn-card-action" onclick="filterByChapter(${ch.id})">🔍 Zobacz zalecaną literaturę dla Rozdz. ${ch.id}</button>
                    </div>
                </div>
                `;
            }).join('');
        }

        function toggleCheck(id) {
            userChecklist[id] = !userChecklist[id];
            localStorage.setItem('aifinc_checklist', JSON.stringify(userChecklist));
            updateProgress();
        }

        function updateProgress() {
            let total = 0;
            CHAPTERS.forEach(ch => total += ch.items.length);
            let done = 0;
            Object.keys(userChecklist).forEach(k => {
                if (userChecklist[k]) done++;
            });
            const pct = Math.round((done / total) * 100);
            const pText = document.getElementById('progressText');
            const pFill = document.getElementById('progressBarFill');
            if (pText) pText.textContent = `${pct}% ukończono (${done}/${total})`;
            if (pFill) pFill.style.width = `${pct}%`;
        }

        function renderWigGrid() {
            const container = document.getElementById('wigGrid');
            if (!container) return;
            container.innerHTML = WIG_SECTORS.map((s, idx) => `
                <div class="card" style="padding: 1.5rem;">
                    <div style="margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border-color);">
                        <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--primary-color);">${s.sector}</h3>
                        <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.2rem; font-weight: 600;">Spółki w WIG140: ${s.tickers}</div>
                    </div>
                    <div style="margin-bottom: 1rem; font-size: 0.86rem;">
                        <h4 style="font-size: 0.78rem; text-transform: uppercase; color: var(--secondary-color); margin-bottom: 0.35rem;">Główne problemy finansowo-controllingowe:</h4>
                        <div>${s.problem}</div>
                    </div>
                    <div style="margin-bottom: 1rem; font-size: 0.86rem;">
                        <h4 style="font-size: 0.78rem; text-transform: uppercase; color: var(--secondary-color); margin-bottom: 0.35rem;">Kluczowe zastosowania AI (Use Cases):</h4>
                        <div style="white-space: pre-line;">${s.useCases}</div>
                    </div>
                    <div style="margin-bottom: 1rem; font-size: 0.86rem;">
                        <h4 style="font-size: 0.78rem; text-transform: uppercase; color: var(--secondary-color); margin-bottom: 0.35rem;">Publiczne źródła danych:</h4>
                        <div>${s.dataSources}</div>
                    </div>
                    <div style="margin-bottom: 1rem; font-size: 0.86rem;">
                        <h4 style="font-size: 0.78rem; text-transform: uppercase; color: var(--secondary-color); margin-bottom: 0.35rem;">Przykładowy kod w Pythonie:</h4>
                        <div style="background: #0f172a; color: #f8fafc; padding: 0.75rem; border-radius: 6px; font-family: monospace; font-size: 0.75rem; overflow-x: auto; position: relative;">
                            <button onclick="copyText('${s.pythonCode.replace(/\n/g, '\\n').replace(/'/g, "\\'")}')" style="position: absolute; top: 0.4rem; right: 0.4rem; background: rgba(255,255,255,0.15); border: none; color: #fff; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.7rem; cursor: pointer;">Kopiuj kod</button>
                            <pre>${s.pythonCode}</pre>
                        </div>
                    </div>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.5rem;">
                        <a href="https://www.gpw.pl" target="_blank" class="pill-btn">🏛️ Profil na GPW.pl</a>
                        <a href="https://biznes.pap.pl/espi" target="_blank" class="pill-btn">📑 Raporty ESPI/EBI</a>
                        <a href="https://stooq.pl" target="_blank" class="pill-btn">📊 Notowania Stooq</a>
                    </div>
                </div>
            `).join('');
        }

        function toggleBasketItem(id) {
            const item = DATABASE.find(d => d.id === id);
            if (!item) return;

            const idx = userBasket.findIndex(b => b.id === id);
            const btn = document.getElementById(`btnBasket-${id}`);

            if (idx >= 0) {
                userBasket.splice(idx, 1);
                if (btn) {
                    btn.classList.remove('in-basket');
                    btn.textContent = '+ Do projektu';
                }
                showToast(`Usunięto pozycję z bibliografii`);
            } else {
                userBasket.push(item);
                if (btn) {
                    btn.classList.add('in-basket');
                    btn.textContent = '✓ W bibliografii';
                }
                showToast(`Dodano do bibliografii (${userBasket.length}/30)`);
            }

            localStorage.setItem('aifinc_basket', JSON.stringify(userBasket));
            updateBasketCount();
            renderBibliography();
        }

        function updateBasketCount() {
            const cnt = userBasket.length;
            const el = document.getElementById('basketCount');
            if (el) el.textContent = `${cnt}/30`;
        }

        function renderBibliography() {
            const container = document.getElementById('biblioContainer');
            if (!container) return;

            if (userBasket.length === 0) {
                container.innerHTML = `
                <div style="padding: 3rem; text-align: center; color: #64748b; background: var(--card-bg); border-radius: 12px; border: 1px dashed var(--border-color);">
                    <h3>Twój koszyk bibliografii jest pusty</h3>
                    <p style="margin-top: 0.5rem;">Przejdź do Eksploratora lub Kanonu Lektur i klikaj <strong>„+ Do projektu”</strong> przy pozycjach, z których korzystasz w pracy dyplomowej.</p>
                </div>`;
                return;
            }

            const g1 = userBasket.filter(b => b.apaCategory === 1).sort((a,b) => a.authors.localeCompare(b.authors));
            const g2 = userBasket.filter(b => b.apaCategory === 2).sort((a,b) => a.year - b.year);
            const g3 = userBasket.filter(b => b.apaCategory === 3).sort((a,b) => a.title.localeCompare(b.title));
            const g4 = userBasket.filter(b => b.apaCategory === 4).sort((a,b) => a.authors.localeCompare(b.authors));

            const renderGroup = (title, items) => {
                if (items.length === 0) return '';
                const listItems = items.map(item => `
                    <li style="padding: 0.5rem 0.75rem; background: var(--tag-bg); border-radius: 6px; display: flex; justify-content: space-between; align-items: center; gap: 1rem; margin-bottom: 0.5rem;">
                        <div style="flex: 1;">${item.apaCitation}</div>
                        <button onclick="toggleBasketItem(${item.id})" style="color: #ef4444; background: transparent; border: none; cursor: pointer; font-size: 0.9rem; padding: 0.2rem 0.5rem;">✕</button>
                    </li>
                `).join('');

                return `
                <div class="card" style="margin-bottom: 1.5rem; padding: 1.5rem;">
                    <h3 style="font-size: 1.05rem; font-weight: 700; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid var(--border-color); color: var(--secondary-color);">${title} (${items.length})</h3>
                    <ol style="list-style: decimal inside; font-size: 0.88rem; line-height: 1.55;">${listItems}</ol>
                </div>
                `;
            };

            container.innerHTML = `
                ${renderGroup('I. Artykuły i publikacje książkowe (porządek alfabetyczny)', g1)}
                ${renderGroup('II. Akty prawne (porządek chronologiczny)', g2)}
                ${renderGroup('III. Źródła internetowe i bazy danych (porządek alfabetyczny)', g3)}
                ${renderGroup('IV. Inne materiały i raporty eksperckie', g4)}
            `;
        }

        function copyCitation(id) {
            const item = DATABASE.find(d => d.id === id);
            if (!item) return;
            copyText(item.apaCitation);
            showToast('Skopiowano cytowanie APA do schowka!');
        }

        function copyWholeBibliography() {
            if (userBasket.length === 0) {
                showToast('Koszyk bibliografii jest pusty!');
                return;
            }

            const g1 = userBasket.filter(b => b.apaCategory === 1).sort((a,b) => a.authors.localeCompare(b.authors));
            const g2 = userBasket.filter(b => b.apaCategory === 2).sort((a,b) => a.year - b.year);
            const g3 = userBasket.filter(b => b.apaCategory === 3).sort((a,b) => a.title.localeCompare(b.title));
            const g4 = userBasket.filter(b => b.apaCategory === 4).sort((a,b) => a.authors.localeCompare(b.authors));

            let out = 'BIBLIOGRAFIA\n\n';
            if (g1.length > 0) {
                out += 'Artykuły i publikacje książkowe\n';
                g1.forEach((it, idx) => out += `${idx + 1}. ${it.apaCitation}\n`);
                out += '\n';
            }
            if (g2.length > 0) {
                out += 'Akty prawne\n';
                g2.forEach((it, idx) => out += `${idx + 1}. ${it.apaCitation}\n`);
                out += '\n';
            }
            if (g3.length > 0) {
                out += 'Źródła internetowe\n';
                g3.forEach((it, idx) => out += `${idx + 1}. ${it.apaCitation}\n`);
                out += '\n';
            }
            if (g4.length > 0) {
                out += 'Inne materiały i raporty eksperckie\n';
                g4.forEach((it, idx) => out += `${idx + 1}. ${it.apaCitation}\n`);
                out += '\n';
            }

            copyText(out);
            showToast('Skopiowano całą bibliografię (4 grupy APA) do schowka!');
        }

        function clearBibliography() {
            if (!confirm('Czy na pewno chcesz wyczyścić koszyk bibliografii?')) return;
            userBasket = [];
            localStorage.setItem('aifinc_basket', JSON.stringify(userBasket));
            updateBasketCount();
            renderBibliography();
            renderCards();
            showToast('Wyczyszczono bibliografię');
        }

        function copyText(text) {
            navigator.clipboard.writeText(text).catch(() => {
                const ta = document.createElement('textarea');
                ta.value = text;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
            });
        }

        function showToast(msg) {
            const t = document.getElementById('toast');
            t.textContent = msg;
            t.style.display = 'block';
            setTimeout(() => { t.style.display = 'none'; }, 2800);
        }

        function initTheme() {
            const saved = localStorage.getItem('aifinc_theme') || 'light';
            document.documentElement.setAttribute('data-theme', saved);
            updateThemeBtn(saved);
        }

        function toggleTheme() {
            const cur = document.documentElement.getAttribute('data-theme') || 'light';
            const next = cur === 'light' ? 'dark' : 'light';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('aifinc_theme', next);
            updateThemeBtn(next);
        }

        function updateThemeBtn(theme) {
            const btn = document.getElementById('themeToggleBtn');
            if (!btn) return;
            btn.innerHTML = theme === 'dark' ? '☀️ Jasny motyw' : '🌙 Ciemny motyw';
        }
    </script>
</body>
</html>
"""

# Wczytaj bazę z database_dump.json
with open("database_dump.json", "r", encoding="utf-8") as f:
    DATABASE = json.load(f)

# Dodaj także pozycje Losbichler & Lehner, Ergashev, Aldasoro et al. BIS, Subudhi et al., Schreyer, Bao, Szelągowski, Mielcarz
ADDITIONAL_ITEMS = [
    {
        "id": 40,
        "title": "Limits of artificial intelligence in controlling and the ways forward: a call for future accounting research",
        "authors": "Heimo Losbichler, Othmar M. Lehner",
        "year": 2021,
        "apaCategory": 1,
        "syllabusStream": "III. CFO, Finanse i Controlling",
        "isMandatory": True,
        "isTop15": False,
        "apaCitation": "Losbichler, H., & Lehner, O. M. (2021). Limits of artificial intelligence in controlling and the ways forward: a call for future accounting research. Journal of Applied Accounting Research, 22(2), 365–382. https://doi.org/10.1108/JAAR-10-2020-0207",
        "identifiers": { "doi": "10.1108/JAAR-10-2020-0207", "issn": "0967-5426" },
        "url": "https://doi.org/10.1108/JAAR-10-2020-0207",
        "projectChapters": [1, 2, 5, 8],
        "courseModules": ["controlling", "regulacje", "projekty"],
        "sectors": ["Finanse", "Produkcja", "Retail"],
        "accessModel": "Wymaga licencji akademickiej",
        "desc": "Kluczowa publikacja przewodniczącego IGC analizująca ograniczenia AI w controllingu oraz symbiozę człowieka z maszyną.",
        "businessValue": "Rozdział 1.4 (Wyłączenia i ograniczenia) oraz Rozdział 5.14 i 6.3 (Human-in-the-Loop)."
    },
    {
        "id": 41,
        "title": "AI-driven financial control systems: machine learning models for fraud and compliance monitoring",
        "authors": "Ikrom Ergashev",
        "year": 2026,
        "apaCategory": 1,
        "syllabusStream": "III. CFO, Finanse i Controlling",
        "isMandatory": True,
        "isTop15": False,
        "apaCitation": "Ergashev, I. (2026). AI-driven financial control systems: machine learning models for fraud and compliance monitoring. AI and Ethics, 6(2). https://doi.org/10.1007/s43681-026-01031-4",
        "identifiers": { "doi": "10.1007/s43681-026-01031-4" },
        "url": "https://doi.org/10.1007/s43681-026-01031-4",
        "projectChapters": [2, 4, 5, 6],
        "courseModules": ["ryzyko", "regulacje", "controlling"],
        "sectors": ["Finanse", "Retail", "Produkcja"],
        "accessModel": "Wymaga licencji akademickiej",
        "desc": "Badanie modeli uczenia maszynowego w monitoringu compliance, audycie transakcji i zapobieganiu fraudom finansowym.",
        "businessValue": "Rozdział 2 (Zarządzanie ryzykiem regulacyjnym) oraz Rozdział 6.4 (Ciągłe monitorowanie)."
    },
    {
        "id": 42,
        "title": "Intelligent financial system: how AI is transforming finance",
        "authors": "Iñaki Aldasoro, Leonardo Gambacorta, Anton Korinek, Vatsala Shreeti, Merlin Stein",
        "year": 2024,
        "apaCategory": 4,
        "syllabusStream": "III. CFO, Finanse i Controlling",
        "isMandatory": True,
        "isTop15": False,
        "apaCitation": "Aldasoro, I., Gambacorta, L., Korinek, A., Shreeti, V., & Stein, M. (2024). Intelligent financial system: how AI is transforming finance (BIS Working Papers No. 1194). Bank for International Settlements. https://www.bis.org/publ/work1194.htm",
        "identifiers": { "bisWp": "1194" },
        "url": "https://www.bis.org/publ/work1194.htm",
        "projectChapters": [1, 2, 5, 8],
        "courseModules": ["regulacje", "ryzyko", "strategia"],
        "sectors": ["Finanse", "TMT"],
        "accessModel": "Open Access",
        "desc": "Raport Banku Rozrachunków Międzynarodowych na temat transformacji funkcji finansowych pod wpływem GenAI i ryzyka stabilności.",
        "businessValue": "Rozdział 2.1 (Zgodność z regulacjami ostrożnościowymi Basel III) i Rozdział 8.4."
    },
    {
        "id": 43,
        "title": "Future of Research in Management and AI",
        "authors": "Rabi Narayan Subudhi, Saumendra Das, Anita Patra",
        "year": 2025,
        "apaCategory": 1,
        "syllabusStream": "II. AI, Transformacja Cyfrowa i Zarządzanie",
        "isMandatory": False,
        "isTop15": False,
        "apaCitation": "Subudhi, R. N., Das, S., & Patra, A. (2025). Future of Research in Management and AI. SSRN Electronic Journal. https://doi.org/10.2139/ssrn.5769382",
        "identifiers": { "ssrn": "5769382", "doi": "10.2139/ssrn.5769382" },
        "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5769382",
        "projectChapters": [1, 3, 8],
        "courseModules": ["strategia", "projekty"],
        "sectors": ["Produkcja", "TMT", "Retail"],
        "accessModel": "Open Access",
        "desc": "Badanie na platformie SSRN dotyczące przyszłości struktur zarządczych i podejmowania decyzji z udziałem sztucznej inteligencji.",
        "businessValue": "Rozdział 1.2 (Cel budowy w strategii firmy) oraz Rozdział 8.3 (Transformacja modelu)."
    },
    {
        "id": 44,
        "title": "Analiza projektów inwestycyjnych w procesie tworzenia wartości przedsiębiorstw",
        "authors": "Paweł Mielcarz",
        "year": 2018,
        "apaCategory": 1,
        "syllabusStream": "III. CFO, Finanse i Controlling",
        "isMandatory": True,
        "isTop15": False,
        "apaCitation": "Mielcarz, P. (2018). Analiza projektów inwestycyjnych w procesie tworzenia wartości przedsiębiorstw. Wydawnictwo Naukowe PWN.",
        "identifiers": { "isbn": "978-83-01-20150-0" },
        "url": "https://ksiegarnia.pwn.pl",
        "projectChapters": [1, 8],
        "courseModules": ["wycena", "strategia"],
        "sectors": ["Finanse", "Produkcja", "Energetyka"],
        "accessModel": "Wymaga licencji akademickiej",
        "desc": "Monografia Kierownika Katedry Finansów ALK dotycząca wyceny opcji realnych, kalkulacji DCF i pomiaru wartości z inwestycji.",
        "businessValue": "Metodologia wyceny ROI, NPV i korzyści finansowych z AI w Rozdziale 8.2."
    },
    {
        "id": 45,
        "title": "Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoding Networks",
        "authors": "Marco Schreyer, Timur Sattarov, Damian Borth, Andreas Dengel, Peter Pastrana",
        "year": 2020,
        "apaCategory": 1,
        "syllabusStream": "III. CFO, Finanse i Controlling",
        "isMandatory": False,
        "isTop15": False,
        "apaCitation": "Schreyer, M., Sattarov, T., Borth, D., Dengel, A., & Pastrana, P. (2020). Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoding Networks. Journal of Emerging Technologies in Accounting. https://doi.org/10.2308/jeta-19-08-07-28",
        "identifiers": { "doi": "10.2308/jeta-19-08-07-28", "arxiv": "1908.00734" },
        "url": "https://arxiv.org/abs/1908.00734",
        "projectChapters": [3, 4, 5],
        "courseModules": ["controlling", "podstawy"],
        "sectors": ["Produkcja", "Retail", "Finanse"],
        "accessModel": "Open Access",
        "desc": "Uczenie głębokie (Autoenkodery) w detekcji anomalii księgowych w ERP SAP (General Ledger).",
        "businessValue": "Wzorzec architektury i zbiorów danych dla Rozdziału 4 i 5."
    },
    {
        "id": 46,
        "title": "Detecting Accounting Fraud in Publicly Traded U.S. Firms Using Machine Learning",
        "authors": "Donghui Bao, Bin Ke, Bo Li, Y. Julia Su, Yong Zhang",
        "year": 2020,
        "apaCategory": 1,
        "syllabusStream": "III. CFO, Finanse i Controlling",
        "isMandatory": False,
        "isTop15": False,
        "apaCitation": "Bao, D., Ke, B., Li, B., Su, Y. J., & Zhang, Y. (2020). Detecting Accounting Fraud in Publicly Traded U.S. Firms Using Machine Learning. Journal of Accounting Research, 58(1), 199–235. https://doi.org/10.1111/1475-679X.12292",
        "identifiers": { "doi": "10.1111/1475-679X.12292" },
        "url": "https://doi.org/10.1111/1475-679X.12292",
        "projectChapters": [1, 4, 5],
        "courseModules": ["controlling", "ryzyko"],
        "sectors": ["Finanse", "Produkcja"],
        "accessModel": "Wymaga licencji akademickiej",
        "desc": "Wykorzystanie drzew decyzyjnych w wykrywaniu manipulacji w sprawozdaniach spółek giełdowych.",
        "businessValue": "Dobór wskaźników bilansowych i cech w Rozdziale 4."
    },
    {
        "id": 47,
        "title": "Raporty Digital Finance Excellence (DFE): AI w polskich przedsiębiorstwach",
        "authors": "Klub Dyrektorów Finansowych „Dialog”",
        "year": 2024,
        "apaCategory": 4,
        "syllabusStream": "II. AI, Transformacja Cyfrowa i Zarządzanie",
        "isMandatory": True,
        "isTop15": False,
        "apaCitation": "Klub Dyrektorów Finansowych „Dialog”. (2024). Digital Finance Excellence: Wdrażanie i efektywność rozwiązań sztucznej inteligencji w finansach i controllingu. Business Dialog.",
        "identifiers": { "isbn": "978-83-948123-0-0" },
        "url": "https://businessdialog.pl",
        "projectChapters": [1, 6, 8],
        "courseModules": ["controlling", "strategia"],
        "sectors": ["Produkcja", "Retail", "Finanse", "Energetyka"],
        "accessModel": "Open Access",
        "desc": "Raporty praktyczne KDF Dialog – case studies wdrożeń AI w polskich korporacjach.",
        "businessValue": "Benchmarking dojrzałości i kalkulacje ROI do Rozdziału 8.4."
    }
]

ALL_DATABASE = DATABASE + ADDITIONAL_ITEMS

CHAPTERS = [
    {
        "id": 1,
        "title": "Rozdział 1: Wstęp i zdefiniowanie problemu biznesowego",
        "reqBadge": "Waga: Fundament koncepcyjny",
        "desc": "Dokładna identyfikacja problemów biznesowych (błędy, czasochłonność, koszty), mierzalny cel projektu, granice rozwiązania i kryteria sukcesu audytu.",
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
        "desc": "Zapewnienie zgodności z EU AI Act, RODO i Basel III, minimalizacja ryzyk regulacyjnych, zapobieganie stronniczości (bias) i zapewnienie wyjaśnialności (XAI).",
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
        "reqBadge": "Waga: Architektura IT & Finanse",
        "desc": "Określenie wymagań funkcjonalnych, zaprojektowanie architektury technicznej integracji z ERP (SAP/IFS/Comarch/Dynamics) oraz uzasadnienie wyboru modeli.",
        "items": [
            { "id": "ch3_1", "text": "3.1 Wymagania funkcjonalne systemu AI spełniające potrzeby controllingu wybranej spółki" },
            { "id": "ch3_2", "text": "3.2 Projekt architektury technicznej (warstwa danych, modele AI, API, integracja z ERP i Power BI)" },
            { "id": "ch3_3", "text": "3.3 Propozycja rozwiązania (rekomendacja podejścia: gotowe API, open source czy dedykowany model ML)" }
        ]
    },
    {
        "id": 4,
        "title": "Rozdział 4: Zarządzanie danymi",
        "reqBadge": "Waga: Data Governance",
        "desc": "Źródła danych spółki giełdowej, metody czyszczenia, normalizacja, anonimizacja wrażliwych danych finansowych, podział na train/val/test i ocena jakości.",
        "items": [
            { "id": "ch4_1", "text": "4.1 Źródła danych (pochodzenie, formaty ESEF/XBRL, bazy ERP, logi transakcyjne, dane rynkowe GPW)" },
            { "id": "ch4_2", "text": "4.2 Czyszczenie i przygotowanie danych finansowych do modelowania" },
            { "id": "ch4_3", "text": "4.3 Normalizacja i standaryzacja cech (szeregi czasowe, wskaźniki controllingowe)" },
            { "id": "ch4_4", "text": "4.4 Anonimizacja i szyfrowanie danych wrażliwych przed zasileniem modelu" },
            { "id": "ch4_5", "text": "4.5 Dopuszczalność prawna wykorzystania danych (brak ryzyka insider trading i naruszenia tajemnicy)" },
            { "id": "ch4_6", "text": "4.6 Zbiory treningowe, walidacyjne i testowe (zapobieganie data leakage w danych finansowych)" },
            { "id": "ch4_7", "text": "4.7 Ocena i metryki jakości danych (kompletność, spójność, aktualność)" }
        ]
    },
    {
        "id": 5,
        "title": "Rozdział 5: Rozwój i testowanie modeli AI – Algorytm",
        "reqBadge": "Waga: Serce technologiczne (5.1–5.14)",
        "desc": "Uzasadnienie doboru algorytmu, zasady piaskownicy (sandbox), trenowanie, walidacja, testy warunków brzegowych, metryki oceny i interfejs Human-in-the-Loop.",
        "items": [
            { "id": "ch5_1", "text": "5.1–5.2 Analiza dostępności i kryteria wyboru modeli AI (benchmarki modeli)" },
            { "id": "ch5_3", "text": "5.3–5.5 Zasady budowy środowiska testowego (sandbox) i metody trenowania" },
            { "id": "ch5_6", "text": "5.6 Walidacja na zbiorze testowym (uzasadnienie wyników dające prawo do wdrożenia biznesowego)" },
            { "id": "ch5_7", "text": "5.7 Testowanie ograniczeń i warunków brzegowych modelu (stres-testy)" },
            { "id": "ch5_8", "text": "5.8–5.9 Metryki jakości (dokładność, precyzja, Recall, F1, MAPE, RMSE, AUC)" },
            { "id": "ch5_10", "text": "5.10–5.12 Analiza błędów, optymalizacja hiperparametrów i dostrajanie modelu" },
            { "id": "ch5_13", "text": "5.13 Raportowanie działania modelu i obsługa zdarzeń nieprzewidzianych" },
            { "id": "ch5_14", "text": "5.14 Interfejs komunikacji człowiek–model (Human-in-the-Loop w controllingu)" }
        ]
    },
    {
        "id": 6,
        "title": "Rozdział 6: Implementacja (wdrożenie)",
        "reqBadge": "Waga: MLOps & Środowisko produkcyjne",
        "desc": "Przygotowanie infrastruktury produkcyjnej, integracja z bazami spółki, komunikacja w wypadku przekroczenia progów ufności oraz monitoring driftu.",
        "items": [
            { "id": "ch6_1", "text": "6.1 Przygotowanie środowiska produkcyjnego (chmura, on-premise, bezpieczeństwo)" },
            { "id": "ch6_2", "text": "6.2 Integracja modelu z systemami IT spółki (konektory, harmonogram batch/real-time)" },
            { "id": "ch6_3", "text": "6.3 Komunikacja z człowiekiem i procedury fallback (co gdy pewność modelu spada poniżej progu)" },
            { "id": "ch6_4", "text": "6.4 Monitorowanie w czasie rzeczywistym i obsługa driftu danych finansowych (MLOps)" }
        ]
    },
    {
        "id": 7,
        "title": "Rozdział 7: Dokumentacja i szkolenia",
        "reqBadge": "Waga: Zarządzanie zmianą & Utrzymanie",
        "desc": "Kompletna dokumentacja techniczna, procedury aktualizacji danych, plan szkoleń dla personelu controllingu i wsparcie powdrożeniowe.",
        "items": [
            { "id": "ch7_1", "text": "7.1 Dokumentacja techniczna systemu i karty modeli (Model Cards)" },
            { "id": "ch7_2", "text": "7.2 Program szkoleń dla użytkowników końcowych (kontrolerów i dyrektorów finansowych)" },
            { "id": "ch7_3", "text": "7.3 Procedury wsparcia powdrożeniowego i eskalacji błędów" }
        ]
    },
    {
        "id": 8,
        "title": "Rozdział 8: Wpływ na efektywność operacyjną i wartość biznesową",
        "reqBadge": "Waga: Uzasadnienie CFO & Wycena",
        "desc": "Kalkulacja ROI i korzyści finansowych (oszczędności, redukcja błędów, uwolniony kapitał), transformacja modelu biznesowego, benchmarking rynkowy i ryzyka wtórne.",
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

final_html = HTML_TEMPLATE.replace("__DATABASE_JSON__", json.dumps(ALL_DATABASE, ensure_ascii=False))
final_html = final_html.replace("__CHAPTERS_JSON__", json.dumps(CHAPTERS, ensure_ascii=False))
final_html = final_html.replace("__WIG_SECTORS_JSON__", json.dumps(WIG_SECTORS, ensure_ascii=False))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Wygenerowano pomyślnie index.html. Łączna liczba pozycji w bazie: {len(ALL_DATABASE)}")
