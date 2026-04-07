from pathlib import Path

ORG = dict(
    name="ООО «ПримерКомпания»",
    short="ПримерКомпания",
    city="Москва",
    address="ул. Примерная, д. 10",
    phone="+7 (000) 000-00-00",
    email="info@example.ru",
    site="https://example.ru",
    about="Компания занимается разработкой программных решений и технической поддержкой клиентов.",
    official_font="Inter",
    font_variant="official",  # official / alt-1..alt-5
)

FONTS = {
    "official": ORG["official_font"],
    "alt-1": "Roboto",
    "alt-2": "Manrope",
    "alt-3": "Montserrat",
    "alt-4": "Open Sans",
    "alt-5": "PT Sans",
}


def gfont(name: str) -> str:
    return name.replace(" ", "+")


def main() -> None:
    v = (ORG.get("font_variant") or "").strip().lower()
    if v not in FONTS:
        v = "official"

    imports = "\n".join(
        f'@import url("https://fonts.googleapis.com/css2?family={gfont(n)}:wght@400;700&display=swap");'
        for n in {ORG["official_font"], *FONTS.values()}
    )

    font_list = "\n".join(
        "          "
        + f"<li><b>{i})</b> {('Official' if k == 'official' else 'Alternative')}: "
        + f"<code>{n}</code> (<code>{k}</code>)</li>"
        for i, (k, n) in enumerate(FONTS.items(), 1)
    )

    css = f"""{imports}

body {{
  margin: 0;
  background: #0c1220;
  color: #eef3ff;
  font: 16px/1.55 "{FONTS[v]}", system-ui, "Segoe UI", Arial, sans-serif;
}}

main {{
  max-width: 920px;
  margin: 0 auto;
  padding: 36px 16px;
}}

header, section, footer {{
  background: #121b2f;
  border: 1px solid rgba(238, 243, 255, 0.12);
  border-radius: 14px;
  padding: 18px 20px;
  margin-top: 12px;
}}

h1 {{
  margin: 0 0 10px;
  font-size: 24px;
}}

h2 {{
  margin: 0 0 10px;
  font-size: 18px;
}}

.muted {{
  opacity: 0.75;
  margin: 0 0 10px;
}}

a {{
  color: #86a8ff;
  text-decoration: none;
}}

a:hover {{
  text-decoration: underline;
}}

dl {{
  margin: 0;
}}

dt {{
  opacity: 0.75;
}}

dd {{
  margin: 0 0 10px;
}}

code {{
  font-family: ui-monospace, Consolas, monospace;
}}
"""

    html = f"""<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{ORG['short']} — информация об организации</title>
    <style>
{css}
    </style>
  </head>
  <body>
    <main>
      <header>
        <h1>Наименование организации на базе, которой Вы проходите практическую подготовку</h1>
        <p class="muted">{ORG['name']}</p>
      </header>

      <section>
        <h2>Об организации</h2>
        <dl>
          <dt>Город</dt>
          <dd>{ORG['city']}</dd>

          <dt>Адрес</dt>
          <dd>{ORG['address']}</dd>

          <dt>Телефон</dt>
          <dd>{ORG['phone']}</dd>

          <dt>E-mail</dt>
          <dd><a href="mailto:{ORG['email']}">{ORG['email']}</a></dd>

          <dt>Сайт</dt>
          <dd><a href="{ORG['site']}" target="_blank" rel="noreferrer">{ORG['site']}</a></dd>
        </dl>
        <p>{ORG['about']}</p>
      </section>

      <section>
        <h2>Шрифты</h2>
        <p class="muted">
          Переключение: <code>font_variant</code> в <code>generate_page.py</code>. Сейчас: <code>{v}</code>.
        </p>
        <ul>
{font_list}
        </ul>
      </section>

      <footer class="muted">Сгенерировано: {ORG['name']}</footer>
    </main>
  </body>
</html>
"""

    (Path(__file__).resolve().parent / "index.html").write_text(html, encoding="utf-8")
    print("Done: index.html created")


if __name__ == "__main__":
    main()

