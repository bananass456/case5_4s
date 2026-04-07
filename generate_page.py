from pathlib import Path


ORG = {
    "name": "ООО «ПримерКомпания»",
    "short": "ПримерКомпания",
    "city": "Москва",
    "address": "ул. Примерная, д. 10",
    "phone": "+7 (000) 000-00-00",
    "email": "info@example.ru",
    "site": "https://example.ru",
    "about": "Компания занимается разработкой программных решений и технической поддержкой клиентов.",
    "official_font": "Inter",
    "font_variant": "official",  # official | alt-1 | alt-2 | alt-3 | alt-4 | alt-5
}


HTML_TEMPLATE = """<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{short} — информация об организации</title>
    <style>
{css}
    </style>
  </head>
  <body>
    <main class="page">
      <header class="hero">
        <h1 class="title">Наименование организации на базе, которой Вы проходите практическую подготовку</h1>
        <p class="subtitle">{name}</p>
      </header>

      <section class="card">
        <h2 class="card__title">Об организации</h2>
        <dl class="facts">
          <div class="facts__row"><dt>Город</dt><dd>{city}</dd></div>
          <div class="facts__row"><dt>Адрес</dt><dd>{address}</dd></div>
          <div class="facts__row"><dt>Телефон</dt><dd>{phone}</dd></div>
          <div class="facts__row"><dt>E-mail</dt><dd><a href="mailto:{email}">{email}</a></dd></div>
          <div class="facts__row"><dt>Сайт</dt><dd><a href="{site}" target="_blank" rel="noreferrer">{site}</a></dd></div>
        </dl>
        <p class="about">{about}</p>
      </section>

      <section class="card">
        <h2 class="card__title">Шрифты</h2>
        <p class="muted">
          По умолчанию используется официальный шрифт компании. Переключить можно в <code>generate_page.py</code>
          (поле <code>font_variant</code>).
        </p>
        <ul class="list">
          <li><strong>1)</strong> Official: <code>{official_font}</code></li>
          <li><strong>2)</strong> Alternative: <code>Roboto</code></li>
          <li><strong>3)</strong> Alternative: <code>Manrope</code></li>
          <li><strong>4)</strong> Alternative: <code>Montserrat</code></li>
          <li><strong>5)</strong> Alternative: <code>Open Sans</code></li>
          <li><strong>6)</strong> Alternative: <code>PT Sans</code></li>
        </ul>
      </section>

      <footer class="footer">
        <span>Сгенерировано: {name}</span>
      </footer>
    </main>
  </body>
</html>
"""


CSS_TEMPLATE = """@import url("https://fonts.googleapis.com/css2?family={official_font_url}:wght@400;600;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@400;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=PT+Sans:wght@400;700&display=swap");

:root {{
  --bg: #0b1220;
  --card: #111a2e;
  --text: #e8eefc;
  --muted: #b7c4e5;
  --line: rgba(255, 255, 255, 0.08);
  --accent: #7aa2ff;

  --font-official: "{official_font}", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  --font-alt-1: "Roboto", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  --font-alt-2: "Manrope", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  --font-alt-3: "Montserrat", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  --font-alt-4: "Open Sans", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
  --font-alt-5: "PT Sans", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;

  --font: var(--font-{font_variant});
}}

* {{ box-sizing: border-box; }}

body {{
  margin: 0;
  background: radial-gradient(1200px 700px at 10% 0%, rgba(122, 162, 255, 0.22), transparent 55%),
    radial-gradient(900px 600px at 90% 10%, rgba(122, 255, 197, 0.10), transparent 50%),
    var(--bg);
  color: var(--text);
  font-family: var(--font);
  line-height: 1.55;
}}

a {{
  color: var(--accent);
  text-decoration: none;
}}

a:hover {{
  text-decoration: underline;
}}

code {{
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  font-size: 0.95em;
  color: #d6e1ff;
}}

.page {{
  max-width: 920px;
  margin: 0 auto;
  padding: 40px 18px 56px;
}}

.hero {{
  padding: 22px 20px;
  border: 1px solid var(--line);
  background: rgba(17, 26, 46, 0.65);
  backdrop-filter: blur(10px);
  border-radius: 16px;
}}

.title {{
  margin: 0 0 10px;
  font-size: 26px;
  letter-spacing: 0.2px;
}}

.subtitle {{
  margin: 0;
  color: var(--muted);
  font-size: 16px;
}}

.card {{
  margin-top: 14px;
  padding: 18px 20px;
  border: 1px solid var(--line);
  background: rgba(17, 26, 46, 0.55);
  border-radius: 16px;
}}

.card__title {{
  margin: 0 0 12px;
  font-size: 18px;
}}

.facts {{
  margin: 0;
}}

.facts__row {{
  display: grid;
  grid-template-columns: 160px 1fr;
  gap: 10px;
  padding: 10px 0;
  border-top: 1px solid var(--line);
}}

.facts__row:first-child {{
  border-top: 0;
  padding-top: 0;
}}

dt {{
  color: var(--muted);
}}

dd {{
  margin: 0;
}}

.about {{
  margin: 14px 0 0;
  color: var(--text);
}}

.muted {{
  margin: 0 0 12px;
  color: var(--muted);
}}

.list {{
  margin: 0;
  padding-left: 18px;
  color: var(--text);
}}

.footer {{
  margin-top: 18px;
  color: rgba(183, 196, 229, 0.8);
  font-size: 13px;
  text-align: center;
}}

@media (max-width: 520px) {{
  .facts__row {{
    grid-template-columns: 1fr;
    gap: 6px;
  }}
}}
"""


def _font_to_google_url_name(font_name: str) -> str:
    return font_name.strip().replace(" ", "+")


def main() -> None:
    root = Path(__file__).resolve().parent

    allowed = {"official", "alt-1", "alt-2", "alt-3", "alt-4", "alt-5"}
    if ORG["font_variant"] not in allowed:
        ORG["font_variant"] = "official"

    css = CSS_TEMPLATE.format(
        official_font=ORG["official_font"],
        official_font_url=_font_to_google_url_name(ORG["official_font"]),
        font_variant=ORG["font_variant"],
    ).strip()
    html = HTML_TEMPLATE.format(**ORG, css=css)

    (root / "index.html").write_text(html, encoding="utf-8")

    print("Готово: index.html создан.")


if __name__ == "__main__":
    main()

