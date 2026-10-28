"""Build the site from template.html.

Outputs:
  index.html       - page body only, for publishing as a Claude artifact
  docs/index.html  - full standalone page, served by GitHub Pages
"""
import base64
from pathlib import Path

ROOT = Path(__file__).parent
SITE_URL = "https://itayfurman.github.io/"

template = (ROOT / "template.html").read_text(encoding="utf-8")
photo = base64.b64encode((ROOT / "docs" / "photo.jpg").read_bytes()).decode()
body = template.replace("__PHOTO__", photo)

(ROOT / "index.html").write_text(body, encoding="utf-8")

head = f"""<!doctype html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta property="og:type" content="profile">
<meta property="og:title" content="Itay Furman">
<meta property="og:description" content="Analyst & Regulation Auditor at the Bank of Israel. Economics & Business Administration student, Hebrew University.">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:image" content="{SITE_URL}photo.jpg">
<link rel="icon" href="photo.jpg">
<style>
  :root {{ color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
  body {{ margin: 0; font-size: 14px; font-family: system-ui, sans-serif; }}
  img {{ max-width: 100%; }}
  [hidden] {{ display: none !important; }}
</style>
"""
(ROOT / "docs" / "index.html").write_text(head + body + "\n</html>\n", encoding="utf-8")
print("built index.html and docs/index.html")
