#!/usr/bin/env python3
"""Static site for upliftinlife.com (company page + one page per app).

Run `python3 build.py`; it writes HTML into docs/ (served by GitHub Pages).
Languages: de (root), en, bg. Texts live in T below.
"""
import html, os
from texts_i18n import T_EXTRA, FORMAL

DOMAIN = "https://upliftinlife.com"
LANGS = ["de", "en", "bg", "es", "fr", "it", "pl", "nl", "ro", "el", "ru", "uk", "tr", "sr"]
LANG_NAME = {"bg": "Български", "en": "English", "de": "Deutsch", "es": "Español", "fr": "Français", "it": "Italiano", "pl": "Polski", "nl": "Nederlands", "ro": "Română", "el": "Ελληνικά", "ru": "Русский", "uk": "Українська", "tr": "Türkçe", "sr": "Srpski"}
ORDER = list(LANG_NAME)
PREFIX = {l: ("" if l == "de" else l + "/") for l in LANGS}

T = {
 "de": {
  "home_title": "Uplift in Life: Apps aus Wien",
  "home_desc": "Uplift in Life entwickelt ehrliche, durchdachte Apps für den Alltag: Macrolia für Kalorien und Makros, Stiege für die ÖSD-Prüfung.",
  "home_eyebrow": "Apps aus Wien",
  "home_h1": "Apps, die im Alltag wirklich helfen.",
  "home_lead": "Uplift in Life ist ein kleines App-Studio in Wien. Jede App macht eine Sache gründlich: ehrlich im Preis, ohne Werbung, in vielen Sprachen.",
  "apps_h2": "Unsere Apps",
  "macrolia_tag": "Kalorien & Makros",
  "macrolia_txt": "Genaue Kalorien und Makros vom Etikett, mit Ihren Rezepten, Portionen und Zielen.",
  "stiege_tag": "Hilft Ihnen bei der Vorbereitung auf die ÖSD-Prüfung A1–C1",
  "stiege_txt": "Gleicher Aufbau, gleiche Aufgabentypen, gleiche Zeit wie bei der ÖSD-Prüfung. Die Texte sind neu.",
  "soon": "Bald bei Google Play",
  "more": "Mehr erfahren",
  "values_h2": "Wofür wir stehen",
  "values": [("Ehrlich", "Sie sehen vor dem Kauf genau, was enthalten ist."),
             ("Ohne Werbung", "Keine Werbung, keine Tricks, keine ständigen Kaufaufforderungen."),
             ("Viele Sprachen", "Menü und Erklärungen in 14 Sprachen.")],
  "s_title": "Stiege: Hilfe bei der Vorbereitung auf die ÖSD-Prüfung A1–C1",
  "s_desc": "Üben Sie Lesen, Hören, Schreiben und Sprechen im Format der ÖSD-Prüfung, A1 bis C1. Mit Tagesplan bis zum Prüfungstermin und KI-Feedback.",
  "s_h1": "Stufe für Stufe zur ÖSD-Prüfung.",
  "s_lead": "Gleicher Aufbau, gleiche Aufgabentypen, gleiche Zeit wie bei der ÖSD-Prüfung. Die Texte sind neu, das Format ist dasselbe.",
  "s_name": "Warum „Stiege“?",
  "s_name_txt": "In Wien heißt das Stiegenhaus „Stiege“. Wie beim Hinaufgehen kommen Sie Stufe für Stufe an Ihr Ziel: die bestandene Prüfung.",
  "s_feat_h2": "Was Stiege kann",
  "s_feat": [("Alle vier Teile", "Lesen, Hören, Schreiben und Sprechen für die Niveaus A1, A2, B1, B2 und C1."),
             ("Wie bei der Prüfung", "Aufgabentypen, Reihenfolge und Zeiten nach den offiziellen Modellsätzen. Auf Wunsch mit Prüfungs-Timer."),
             ("Tagesplan bis zum Termin", "Sie geben Ihr Prüfungsdatum ein, Stiege plant jeden Tag. Verpasste Tage werden ohne Strafe verteilt."),
             ("Feedback zu Schreiben und Sprechen", "Eine KI bewertet Ihre Texte nach den Kriterien der Prüfung und zeigt, was fehlt."),
             ("Struktur statt Auswendiglernen", "Sie lernen den Aufbau eines Textes und füllen ihn mit Ihren eigenen Sätzen."),
             ("Österreichische Themen", "Standarddeutsch, wie bei der Prüfung verlangt, mit Wörtern und Themen aus Österreich.")],
  "s_free_h2": "Kostenlos testen",
  "s_free_txt": "A1 Lesen und Hören sind komplett kostenlos. In allen anderen Teilen und Niveaus können Sie Aufgaben gratis ausprobieren. Danach: 7,99 € im Monat, 21,99 € für 3 Monate oder 54,99 € im Jahr. Ohne Werbung.",
  "s_note": "Stiege ist ein unabhängiges Übungsprogramm und steht in keiner Verbindung zum Österreichischen Sprachdiplom Deutsch (ÖSD). Alle Texte und Aufnahmen sind eigene Inhalte.",
  "imp_title": "Impressum",
  "imp_body": "<p><b>Uplift in Life</b><br>Wien, Österreich</p><p>Die vollständigen Angaben zum Unternehmen (Firmenbuch, UID, Anschrift) werden nach der Gründung im Jänner 2027 ergänzt.</p>",
  "privacy": "Datenschutz",
  "imprint": "Impressum",
  "home": "Startseite",
 },
 "en": {
  "home_title": "Uplift in Life: apps from Vienna",
  "home_desc": "Uplift in Life makes honest, thoughtful apps for everyday life: Macrolia for calories and macros, Stiege for the ÖSD exam.",
  "home_eyebrow": "Apps from Vienna",
  "home_h1": "Apps that actually help in everyday life.",
  "home_lead": "Uplift in Life is a small app studio in Vienna. Each app does one thing well: honest pricing, no ads, many languages.",
  "apps_h2": "Our apps",
  "macrolia_tag": "Calories & macros",
  "macrolia_txt": "Accurate calories and macros from the label, with your recipes, portions and goals.",
  "stiege_tag": "Helps you prepare for the ÖSD exam A1–C1",
  "stiege_txt": "Same structure, same task types, same time as the ÖSD exam. The texts are new.",
  "soon": "Coming soon to Google Play",
  "more": "Learn more",
  "values_h2": "What we stand for",
  "values": [("Honest", "You see exactly what is included before you pay."),
             ("No ads", "No ads, no tricks, no constant requests to pay."),
             ("Many languages", "Menus and explanations in 14 languages.")],
  "s_title": "Stiege: helps you prepare for the ÖSD exam A1–C1",
  "s_desc": "Practise reading, listening, writing and speaking in the ÖSD exam format, A1 to C1. With a daily plan up to your exam date and AI feedback.",
  "s_h1": "Step by step to the ÖSD exam.",
  "s_lead": "Same structure, same task types, same time as the ÖSD exam. The texts are new, the format is the same.",
  "s_name": "Why “Stiege”?",
  "s_name_txt": "In Vienna, a staircase is called a “Stiege”. Like climbing the stairs, you reach your goal one step at a time: passing the exam.",
  "s_feat_h2": "What Stiege does",
  "s_feat": [("All four parts", "Reading, listening, writing and speaking for levels A1, A2, B1, B2 and C1."),
             ("Like the real exam", "Task types, order and timing follow the official model tests. Exam timer if you want it."),
             ("A daily plan to your exam date", "Enter your exam date and Stiege plans every day. Missed days are spread out, without penalty."),
             ("Feedback on writing and speaking", "AI rates your texts by the exam criteria and shows what is missing."),
             ("Structure, not memorising", "You learn how a text is built and fill it with your own sentences."),
             ("Austrian topics", "Standard German, as the exam requires, with words and topics from Austria.")],
  "s_free_h2": "Try it for free",
  "s_free_txt": "A1 reading and listening are completely free. In all other parts and levels you can try tasks for free. After that: €7.99 a month, €21.99 for 3 months or €54.99 a year. No ads.",
  "s_note": "Stiege is an independent practice app and is not affiliated with the Österreichisches Sprachdiplom Deutsch (ÖSD). All texts and recordings are our own.",
  "imp_title": "Legal notice",
  "imp_body": "<p><b>Uplift in Life</b><br>Vienna, Austria</p><p>Full company details (register number, VAT ID, address) will be added after the company is founded in January 2027.</p>",
  "privacy": "Privacy",
  "imprint": "Legal notice",
  "home": "Home",
 },
 "bg": {
  "home_title": "Uplift in Life: приложения от Виена",
  "home_desc": "Uplift in Life прави честни и обмислени приложения за всеки ден: Macrolia за калории и макроси, Stiege за изпита ÖSD.",
  "home_eyebrow": "Приложения от Виена",
  "home_h1": "Приложения, които наистина помагат всеки ден.",
  "home_lead": "Uplift in Life е малко студио за приложения във Виена. Всяко приложение прави едно нещо добре: честна цена, без реклами, на много езици.",
  "apps_h2": "Нашите приложения",
  "macrolia_tag": "Калории и макроси",
  "macrolia_txt": "Точни калории и макроси от етикета, с твоите рецепти, порции и цели.",
  "stiege_tag": "Помага ти да се подготвиш за изпита ÖSD A1–C1",
  "stiege_txt": "Същата структура, същите видове задачи и същото време като на изпита ÖSD. Текстовете са нови.",
  "soon": "Скоро в Google Play",
  "more": "Научи повече",
  "values_h2": "В какво вярваме",
  "values": [("Честно", "Преди да платиш, виждаш точно какво получаваш."),
             ("Без реклами", "Без реклами, без трикове, без постоянни покани за плащане."),
             ("Много езици", "Меню и обяснения на 14 езика.")],
  "s_title": "Stiege: помага ти да се подготвиш за изпита ÖSD A1–C1",
  "s_desc": "Упражнявай четене, слушане, писане и говорене във формата на изпита ÖSD, от A1 до C1. С дневен план до датата на изпита и AI оценка.",
  "s_h1": "Стъпало по стъпало до изпита ÖSD.",
  "s_lead": "Същата структура, същите видове задачи и същото време като на изпита ÖSD. Текстовете са нови, форматът е същият.",
  "s_name": "Защо „Stiege“?",
  "s_name_txt": "Във Виена стълбището се казва „Stiege“. Както по стълбите, стигаш до целта стъпало по стъпало: взетия изпит.",
  "s_feat_h2": "Какво може Stiege",
  "s_feat": [("Всички четири части", "Четене, слушане, писане и говорене за нивата A1, A2, B1, B2 и C1."),
             ("Като на изпита", "Видове задачи, ред и време според официалните модел-тестове. Ако искаш, с таймер като на изпита."),
             ("Дневен план до датата", "Въвеждаш датата на изпита и Stiege планира всеки ден. Пропуснатото се разпределя напред без наказание."),
             ("Оценка на писането и говоренето", "AI оценява текстовете ти по критериите на изпита и показва какво липсва."),
             ("Структура, не наизустяване", "Учиш как е построен текстът и го пълниш със свои изречения."),
             ("Австрийски теми", "Стандартен немски, какъвто се иска на изпита, с думи и теми от Австрия.")],
  "s_free_h2": "Пробвай безплатно",
  "s_free_txt": "A1 четене и слушане са изцяло безплатни. Във всички други части и нива можеш да пробваш задачи безплатно. След това: 7,99 € на месец, 21,99 € за 3 месеца или 54,99 € за година. Без реклами.",
  "s_note": "Stiege е независимо приложение за упражнения и не е свързано с Österreichisches Sprachdiplom Deutsch (ÖSD). Всички текстове и записи са наши.",
  "imp_title": "Impressum",
  "imp_body": "<p><b>Uplift in Life</b><br>Виена, Австрия</p><p>Пълните данни на фирмата (фирмен регистър, ДДС номер, адрес) ще бъдат добавени след регистрацията ѝ през януари 2027.</p>",
  "privacy": "Поверителност",
  "imprint": "Impressum",
  "home": "Начало",
 },
}

T.update(T_EXTRA)
for _l, _o in FORMAL.items(): T[_l].update(_o)

CSS = """:root{--bg:#fbf7ef;--paper:#fff;--ink:#1d2433;--mut:#5d6575;--line:#e8e1d3;--brand:#24508f;--ac:#2f63b0;--sun:#f2b632;--tint:#eef3fb;
--body:system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans",Arial,sans-serif}
@media (prefers-color-scheme:dark){:root{--bg:#121722;--paper:#1a2130;--ink:#eef1f7;--mut:#a3acbd;--line:#2a3344;--brand:#9bbcf0;--ac:#8fb3ef;--tint:#1e2a40;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 var(--body)}
a{color:var(--ac)}img{max-width:100%;display:block}
.w{max-width:1000px;margin:0 auto;padding-inline:max(18px,env(safe-area-inset-left,0px))}
header{display:flex;justify-content:space-between;align-items:center;gap:12px;padding-block:18px}
.brand{white-space:nowrap;font-weight:900;font-size:20px;letter-spacing:-.01em;color:var(--ink);text-decoration:none}
.brand span{color:var(--sun)}
details.lang{position:relative}
details.lang summary{list-style:none;cursor:pointer;font-size:15px;color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:6px 14px;background:var(--paper)}
details.lang summary::-webkit-details-marker{display:none}
details.lang div{position:absolute;right:0;top:calc(100% + 6px);background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:6px;display:grid;grid-template-columns:1fr 1fr;width:max-content;max-width:calc(100vw - 36px);z-index:5;box-shadow:0 10px 30px rgba(0,0,0,.12)}
details.lang a{padding:7px 12px;border-radius:8px;text-decoration:none;color:var(--ink);font-size:15px}
details.lang a[aria-current]{color:var(--brand);font-weight:700}
details.lang a:hover{background:var(--tint)}
.eyebrow{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--ac)}
h1{font-size:clamp(34px,6vw,58px);line-height:1.05;font-weight:900;letter-spacing:-.02em;margin:10px 0 16px;text-wrap:balance}
h2{font-size:clamp(24px,3.4vw,32px);line-height:1.2;margin:0 0 20px;text-wrap:balance}
h3{margin:0 0 6px;font-size:19px}
.lead{font-size:clamp(18px,2.2vw,21px);color:var(--mut);max-width:40em;margin:0}
section{padding-block:40px}
.hero{padding-top:24px}
.apps{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
.card{background:var(--paper);border:1px solid var(--line);border-radius:20px;padding:22px;display:flex;flex-direction:column;gap:10px}
.card .top{display:flex;gap:14px;align-items:center}
.card img{width:64px;height:64px;border-radius:16px}
.card .tag{color:var(--mut);font-size:15px;margin:0}
.card p{margin:0}
.pill{display:inline-block;font-size:13px;font-weight:700;color:var(--brand);background:var(--tint);border-radius:999px;padding:3px 10px;align-self:flex-start}
.btn{display:inline-block;margin-top:auto;align-self:flex-start;background:var(--brand);color:#fff;text-decoration:none;font-weight:700;border-radius:12px;padding:10px 16px}
@media (prefers-color-scheme:dark){.btn{color:#0f1420}}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.grid3 div{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:18px}
.grid3 p{margin:0;color:var(--mut)}
.shero{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center}
.shero img{width:160px;height:160px;border-radius:36px;box-shadow:0 12px 30px rgba(36,80,143,.18)}
@media (max-width:640px){.shero{grid-template-columns:1fr}.shero img{width:112px;height:112px;border-radius:26px}}
.box{background:var(--tint);border-radius:18px;padding:22px}
.box p{margin:0}
.note{font-size:14px;color:var(--mut);border-top:1px solid var(--line);padding-top:16px}
footer{border-top:1px solid var(--line);padding-block:24px;color:var(--mut);font-size:14px;display:flex;flex-wrap:wrap;gap:8px 18px;justify-content:space-between}
footer a{color:var(--mut)}
"""

def esc(s): return html.escape(s, quote=True)

def tx(s): return esc(s).replace("A1–C1", '<span style="white-space:nowrap">A1–C1</span>')

def page(lang, path, title, desc, body):
    """path: '' for home, 'stiege/', 'impressum/'"""
    t = T[lang]
    depth = (PREFIX[lang] + path).count("/")
    up = "../" * depth
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{PREFIX[l]}{path}">' for l in LANGS)
    langs = "".join(f'<a href="{up}{PREFIX[l]}{path}" lang="{l}" hreflang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{LANG_NAME[l]}</a>' for l in ORDER)
    icon = "stiege-192.png" if path.startswith("stiege") else "stiege-192.png"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{DOMAIN}/{PREFIX[lang]}{path}">
{alts}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta name="theme-color" content="#24508f">
<link rel="icon" href="{up}img/{icon}">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<div class="w">
<header><a class="brand" href="{up}{PREFIX[lang]}">Uplift in Life<span>.</span></a><details class="lang"><summary>🌐 {LANG_NAME[lang]} ▾</summary><div>{langs}</div></details></header>
{body}
<footer><div>© 2026 Uplift in Life · Wien</div><div><a href="{up}{PREFIX[lang]}">{t['home']}</a> · <a href="{up}{PREFIX[lang]}stiege/">Stiege</a> · <a href="https://macrolia.app/">Macrolia</a> · <a href="{up}{PREFIX[lang]}impressum/">{t['imprint']}</a></div></footer>
</div>
</body>
</html>
"""

def home(lang):
    t = T[lang]; up = "../" * PREFIX[lang].count("/")
    vals = "".join(f"<div><h3>{esc(a)}</h3><p>{esc(b)}</p></div>" for a, b in t["values"])
    body = f"""<section class="hero"><div class="eyebrow">{esc(t['home_eyebrow'])}</div><h1>{esc(t['home_h1'])}</h1><p class="lead">{esc(t['home_lead'])}</p></section>
<section><h2>{esc(t['apps_h2'])}</h2><div class="apps">
<div class="card"><div class="top"><img src="{up}img/stiege-256.webp" alt="" width="64" height="64"><div><h3>Stiege</h3><p class="tag">{tx(t['stiege_tag'])}</p></div></div><span class="pill">{esc(t['soon'])}</span><p>{esc(t['stiege_txt'])}</p><a class="btn" href="stiege/">{esc(t['more'])}</a></div>
<div class="card"><div class="top"><img src="{up}img/macrolia-192.png" alt="" width="64" height="64"><div><h3>Macrolia</h3><p class="tag">{esc(t['macrolia_tag'])}</p></div></div><span class="pill">{esc(t['soon'])}</span><p>{esc(t['macrolia_txt'])}</p><a class="btn" href="https://macrolia.app/{'' if lang=='en' else lang+'/'}">macrolia.app</a></div>
</div></section>
<section><h2>{esc(t['values_h2'])}</h2><div class="grid3">{vals}</div></section>"""
    return page(lang, "", t["home_title"], t["home_desc"], body)

def stiege(lang):
    t = T[lang]; up = "../" * (PREFIX[lang] + "stiege/").count("/")
    feats = "".join(f"<div><h3>{esc(a)}</h3><p>{esc(b)}</p></div>" for a, b in t["s_feat"])
    body = f"""<section class="hero shero"><img src="{up}img/stiege-256.webp" alt="Stiege" width="160" height="160"><div><div class="eyebrow">{esc(t['soon'])}</div><h1>{esc(t['s_h1'])}</h1><p class="lead">{esc(t['s_lead'])}</p></div></section>
<section><h2>{esc(t['s_feat_h2'])}</h2><div class="grid3">{feats}</div></section>
<section><div class="box"><h2>{esc(t['s_name'])}</h2><p>{esc(t['s_name_txt'])}</p></div></section>
<section><h2>{esc(t['s_free_h2'])}</h2><p>{esc(t['s_free_txt'])}</p></section>
<section><p class="note">{esc(t['s_note'])}</p></section>"""
    return page(lang, "stiege/", t["s_title"], t["s_desc"], body)

def impressum(lang):
    t = T[lang]
    body = f"""<section class="hero"><h1>{esc(t['imp_title'])}</h1>{t['imp_body']}</section>"""
    return page(lang, "impressum/", t["imp_title"] + " · Uplift in Life", t["imp_title"], body)

def write(p, s):
    p = os.path.join("docs", p); os.makedirs(os.path.dirname(p) or "docs", exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    for l in LANGS:
        write(PREFIX[l] + "index.html", home(l))
        write(PREFIX[l] + "stiege/index.html", stiege(l))
        write(PREFIX[l] + "impressum/index.html", impressum(l))
    write("style.css", CSS)
    write("CNAME", "upliftinlife.com\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    urls = [f"{DOMAIN}/{PREFIX[l]}{p}" for l in LANGS for p in ("", "stiege/", "impressum/")]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print("built", len(urls), "pages")
