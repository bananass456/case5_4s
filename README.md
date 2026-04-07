### Как запустить

В папке проекта выполните:

```bash
py generate_page.py
```

После этого откройте `index.html` в браузере.

### Что менять под свою организацию

В файле `generate_page.py` в словаре `ORG` отредактируйте:

- `name`, `short`
- `city`, `address`
- `phone`, `email`, `site`
- `about`
- `official_font` (официальный шрифт компании)
 - `font_variant` (official или один из 5 вариантов)

### Варианты шрифтов

Меняется в `generate_page.py` через `font_variant`:

- `official` — официальный шрифт (берётся из `official_font`)
- `alt-1` — Roboto
- `alt-2` — Manrope
- `alt-3` — Montserrat
- `alt-4` — Open Sans
- `alt-5` — PT Sans
