# AI FINC – Academic Research Hub

[![Live Demo - GitHub Pages](https://img.shields.io/badge/Live_Demo-GitHub_Pages-0b2545?style=for-the-badge&logo=github)](https://bartoszradziszewski.github.io/AIFINC/)
[![Akademia Leona Koźmińskiego](https://img.shields.io/badge/Uczelnia-Koźmiński_University-b4865e?style=for-the-badge)](https://www.kozminski.edu.pl/pl/oferta-edukacyjna/studia-podyplomowe/ai-w-finansach-i-controllingu-przedsiebiorstw)
[![Partner: KDF Dialog](https://img.shields.io/badge/Partner-KDF_Dialog-dc2626?style=for-the-badge)](https://businessdialog.pl)
[![Patronat: ACCA](https://img.shields.io/badge/Patronat-ACCA_Think_Ahead-black?style=for-the-badge)](https://www.accaglobal.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**AI FINC – Academic Research Hub** to autonomiczny, interaktywny dashboard badawczo-dydaktyczny (Single-Page Application zapisany w jednym pliku HTML, *zero-dependency*), stworzony jako dedykowane repozytorium zasobów naukowych i operacyjny asystent przygotowania **Projektu Końcowego** na studiach podyplomowych **„AI w finansach i controllingu przedsiębiorstw”** w Akademii Leona Koźmińskiego w Warszawie.

🔗 **Wersja online (Live Demo):** [https://bartoszradziszewski.github.io/AIFINC/](https://bartoszradziszewski.github.io/AIFINC/)

---

## 🎯 Cel i geneza projektu

Głównym celem Hubu jest ułatwienie słuchaczom studiów menedżerskich (CFO, dyrektorom finansowym, głównym księgowym, kontrolerom zarządczym oraz liderom transformacji IT) usystematyzowania wiedzy oraz przejścia przez rygorystyczne **Wytyczne do Projektu Końcowego Grupowego (WIG140)**.

Narzędzie łączy:
* **Wymagania formalne ALK:** 8 obowiązkowych rozdziałów merytorycznych, wybór spółki z indeksu **WIG140**, min. 20–30 pozycji bibliograficznych w systemie **APA 7** z podziałem na 4 grupy.
* **Standardy profesjonalne:** Ramy certyfikacji **ACCA „Ethical Artificial Intelligence (AI)”** oraz standardy **Klubu Dyrektorów Finansowych „Dialog” (Digital Finance Excellence - DFE)**.
* **Nowoczesną architekturę SPA:** Inspirowaną projektem [FINDT](https://github.com/BartoszRadziszewski/FINDT/), działającą w 100% lokalnie w przeglądarce bez instalowania frameworków czy serwerów.

---

## 🚀 Główne moduły funkcjonalne

### 1. ⚡ Akademicki Multi-Resolver 2.0 & Globalne Bazy
Zintegrowany silnik rozpoznawania identyfikatorów naukowych i prawnych:
* **Inteligentne dopasowanie (Smart Regex):**
  * `DOI` (`10.xxxx/...`) ➔ bezpośrednie rozwiązanie przez doi.org / CrossRef.
  * `SSRN` (`abstract_id=...` lub `ssrn:5769382`) ➔ otwarcie abstraktu w Social Science Research Network.
  * `ORCID` (`0000-xxxx-xxxx-xxxx`) ➔ profil badacza i jego dorobek naukowy.
  * `Scopus Author ID` & `WoS ResearcherID` ➔ bazy cytowań Elsevier i Clarivate.
  * `arXiv` ➔ najnowsze preprinty otwartej nauki.
  * `ISBN` / `ISSN` ➔ międzynarodowe rejestry monografii i czasopism.
  * `Akty Prawne UE (CELEX np. 32024R1689)` ➔ baza EUR-Lex (EU AI Act, RODO).
  * `Akty Prawne RP` ➔ Internetowy System Aktów Prawnych (ISAP Sejm).
* **Przyciski 1-kliknięciem:** Google Scholar, CrossRef, Scopus, **🔬 ResearchGate**, **📑 SSRN**, **⚖️ EUR-Lex**, **🇵🇱 ISAP**, **🏛️ GPW.pl**.

### 2. 📋 Nawigator Projektu Końcowego (Rozdziały 1–8 Wytycznych ALK)
* Interaktywny przewodnik odwzorowujący 8 obowiązkowych rozdziałów pracy dyplomowej:
  * **Rozdział 1:** Wstęp i zdefiniowanie problemu biznesowego (1.1–1.5).
  * **Rozdział 2:** Zgodność z regulacjami oraz aspekty etyczne (AI Act, RODO, Basel III, XAI).
  * **Rozdział 3:** Projektowanie rozwiązania i architektura integracji z ERP.
  * **Rozdział 4:** Zarządzanie danymi (czyszczenie, anonimizacja, data leakage, jakość).
  * **Rozdział 5:** Rozwój i testowanie modeli AI – Algorytm (sandbox, walidacja, metryki, Human-in-the-Loop).
  * **Rozdział 6:** Implementacja produkcyjna i MLOps (monitoring driftu, fallback).
  * **Rozdział 7:** Dokumentacja techniczna i zarządzanie zmianą (szkolenia, Model Cards).
  * **Rozdział 8:** Wpływ na efektywność operacyjną i wartość biznesową (szacunek ROI, NPV, TCO, benchmarking).
* **Automatyczny pasek postępu (0–100%)** i checklisty zapisywane trwale w pamięci podręcznej przeglądarki (`localStorage`).
* Przycisk **„🔍 Zobacz zalecaną literaturę”** filtrujący bazę pod wymagania konkretnego rozdziału.

### 3. 🏢 Katalog Spółek WIG140 & Smart Data Connector
Ułatwienie doboru spółki giełdowej i pozyskania publicznych danych:
* **Matryca sektorowa:** Banki & Finanse, Przemysł & Produkcja, Handel & E-commerce, Energetyka & Utilities, Technologie & TMT, Budownictwo.
* **Baza typowych use-case'ów AI w controllingu:** Predykcja cash flow, dynamiczny budżet, detekcja fraudów w ERP SAP, klasyfikacja faktur kosztowych, optymalizacja working capital.
* **Bezpośrednie konektory:** Odnośniki do profili na GPW.pl, komunikatów ESPI/EBI PAP, sprawozdań ESEF/iXBRL, pobierania notowań CSV ze Stooq oraz danych makro NBP API.
* **Gotowe snippety w Pythonie:** 1-kliknięciem kopiowany kod do Google Colab / Jupyter Notebook.

### 4. 📚 Generator i Koszyk Bibliografii APA 7 (Wymóg 4 Grup ALK)
* Automatyczne grupowanie wyselekcjonowanych źródeł w **cztery obowiązkowe grupy**:
  1. *Artykuły i publikacje książkowe* (układ alfabetyczny wg autorów).
  2. *Akty prawne* (układ chronologiczny).
  3. *Źródła internetowe i bazy danych* (układ alfabetyczny, bez dat wyświetlenia strony).
  4. *Inne materiały i raporty eksperckie* (KDF Dialog, ACCA, Big4).
* Przycisk **„📋 Kopiuj całą bibliografię do Worda”** generujący gotowy, sformatowany tekst.

---

## 📖 Kanon literatury naukowej zawarty w Hubie

W bazie wiedzy Hubu znalazły się kluczowe, recenzowane publikacje światowe i polskie:
* **Losbichler H., Lehner O. M. (2021)** – *Limits of artificial intelligence in controlling and the ways forward*, Journal of Applied Accounting Research (Emerald).
* **Ergashev I. (2026)** – *AI-driven financial control systems: machine learning models for fraud and compliance monitoring*, AI and Ethics (Springer).
* **Aldasoro I. et al. (2024)** – *Intelligent financial system: how AI is transforming finance*, BIS Working Papers No. 1194 (Bank for International Settlements).
* **Subudhi R. N., Das S., Patra A. (2025)** – *Future of Research in Management and AI*, SSRN Electronic Journal.
* **Szelągowski M. (2019)** – *Dynamic BPM in the Knowledge Economy: Creating Value from Intellectual Capital*, Springer.
* **Mielcarz P. (2018)** – *Analiza projektów inwestycyjnych w procesie tworzenia wartości przedsiębiorstw*, PWN.
* **Bao D. et al. (2020)** – *Detecting Accounting Fraud in Publicly Traded U.S. Firms Using Machine Learning*, Journal of Accounting Research.
* **Schreyer M. et al. (2020)** – *Detection of Anomalies in Large Scale Accounting Data using Deep Autoencoding Networks*, JETA (AAA).
* **Cao S. et al. (2024)** – *How to Talk When a Machine Listens: Corporate Disclosure in the Age of AI*, Review of Financial Studies.
* **Rozporządzenie UE 2024/1689 (EU AI Act)** oraz **RODO (GDPR)**.
* **Raporty KDF Dialog (Digital Finance Excellence)** oraz wytyczne **ACCA Ethical AI**.

---

## 💻 Uruchomienie lokalne

Plik nie wymaga instalacji Node.js, Pythona, Dockera ani żadnych zewnętrznych zależności:

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/BartoszRadziszewski/AIFINC.git
   ```
2. Otwórz plik `index.html` w dowolnej nowoczesnej przeglądarce internetowej (Chrome, Edge, Firefox, Safari).

---

## 👤 Autor i Partnerzy

* **Autor koncepcji i wdrożenia:** [Bartosz Radziszewski](https://github.com/BartoszRadziszewski) (Prezes Fundacji Klub Dyrektorów Finansowych, wykładowca na studiach AI FINC na ALK).
* **Uczelnia:** Akademia Leona Koźmińskiego w Warszawie (Centrum Doradztwa i Kształcenia Menedżerów / Koźmiński Executive Business School).
* **Partner kierunku:** Klub Dyrektorów Finansowych „Dialog”.
* **Patronat:** ACCA (Association of Chartered Certified Accountants).

---

## 📄 Licencja

Projekt udostępniony na licencji [MIT](LICENSE).
