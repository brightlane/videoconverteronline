# VideoConverter Affiliate Site — build.py v2

Independent affiliate marketing website for [Wondershare UniConverter](https://videoconverter.wondershare.com), built for GitHub Pages at:

**`https://brightlane.github.io/videoconverteronline/`**

---

## Quick Start

```bash
python3 build.py
```

Outputs 94 files into `videoconverter-site/` next to `build.py`. Zero dependencies — pure Python 3 stdlib only.

---

## Deployment

Your repo needs exactly three files:

```
videoconverteronline/           ← your GitHub repo name
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

**One-time GitHub setup:**
1. `Settings → Pages → Source` → set to **GitHub Actions**
2. Push to `main` — workflow builds and deploys in ~45 seconds

---

## Config (top of build.py)

```python
BASE      = Path(__file__).parent / "videoconverter-site"
SITE_ROOT = "/videoconverteronline"                                               # Must match repo name exactly
SITE_URL  = "https://brightlane.github.io/videoconverteronline"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949048607004532&atid=videoconverterwebs"
YEAR      = date.today().year
```

⚠️ `SITE_ROOT` must match your GitHub repo name exactly or all links will 404.

---

## All 44 Pages

### Core Pages

| Page | URL | Schema |
|---|---|---|
| Homepage | `/` | SoftwareApp + Breadcrumb |
| Features | `/features/` | SoftwareApp + ItemList |
| AI Features | `/ai-features/` | SoftwareApp + ItemList |
| Formats | `/formats/` | SoftwareApp + Breadcrumb |
| How It Works | `/how-it-works/` | SoftwareApp + HowTo |
| Pricing | `/pricing/` | SoftwareApp + FAQPage |
| Review | `/review/` | SoftwareApp + Review |
| FAQ | `/faq/` | SoftwareApp + FAQPage |
| Download | `/download/` | SoftwareApp + Breadcrumb |
| Blog | `/blog/` | SoftwareApp + Breadcrumb |
| Global | `/global/` | SoftwareApp + Breadcrumb |

### Guide Pages

| Page | URL | Target Keywords |
|---|---|---|
| Screen Recorder | `/screen-recorder/` | screen recorder software, record screen |
| Convert to MP4 | `/convert-mp4/` | convert video to MP4, MKV to MP4 |
| Compress Video | `/compress-video/` | compress video, AI compression |
| MKV to MP4 | `/convert-mkv-mp4/` | MKV to MP4 converter |
| MOV to MP4 | `/convert-mov-mp4/` | MOV to MP4, iPhone video converter |
| DVD Burner | `/dvd-burner/` | DVD Blu-ray burner software |

### Comparison Pages

| Page | URL |
|---|---|
| Alternatives | `/alternatives/` |
| vs HandBrake | `/vs-handbrake/` |
| vs VLC | `/vs-vlc/` |
| vs Freemake | `/vs-freemake/` |

### Legal

| Page | URL |
|---|---|
| Privacy | `/privacy/` |
| Disclaimer | `/disclaimer/` |
| 404 | `/404.html` |

### Language Pages (20 languages)

| Language | URL | Region |
|---|---|---|
| 🇺🇸 English | `/lang/en/` | United States |
| 🇩🇪 Deutsch | `/lang/de/` | Germany |
| 🇫🇷 Français | `/lang/fr/` | France |
| 🇪🇸 Español | `/lang/es/` | Spain / Latin America |
| 🇧🇷 Português | `/lang/pt/` | Brazil / Portugal |
| 🇮🇹 Italiano | `/lang/it/` | Italy |
| 🇯🇵 日本語 | `/lang/ja/` | Japan |
| 🇨🇳 中文 | `/lang/zh/` | China |
| 🇰🇷 한국어 | `/lang/ko/` | Korea |
| 🇷🇺 Русский | `/lang/ru/` | Russia |
| 🇦🇪 العربية | `/lang/ar/` | Middle East |
| 🇮🇳 हिन्दी | `/lang/hi/` | India |
| 🇮🇩 Bahasa Indonesia | `/lang/id/` | Indonesia |
| 🇳🇱 Nederlands | `/lang/nl/` | Netherlands |
| 🇵🇱 Polski | `/lang/pl/` | Poland |
| 🇹🇷 Türkçe | `/lang/tr/` | Turkey |
| 🇸🇪 Svenska | `/lang/sv/` | Sweden |
| 🇵🇭 Filipino | `/lang/fil/` | Philippines |
| 🇻🇳 Tiếng Việt | `/lang/vi/` | Vietnam |
| 🇹🇭 ภาษาไทย | `/lang/th/` | Thailand |

Each language page:
- Has correct `lang=` HTML attribute
- Targets native-language search keywords
- Covers region-specific use cases
- Links to the full site

---

## 1500+ Keywords — 7 Layers

| Layer | Coverage |
|---|---|
| `<meta name="keywords">` | 200+ keyword phrases covering English + 15 language keyword clusters |
| `<title>` + `<meta description>` | Unique per page, keyword-rich |
| `hreflang` tags | 20 language alternate links on every page for international SEO |
| JSON-LD schema | SoftwareApp + BreadcrumbList on all · FAQPage on /faq/ and /pricing/ · Review on /review/ · HowTo on /how-it-works/ · ItemList on /features/ and /ai-features/ · Article OG on all guide pages |
| Language pages | 20 pages targeting native-language keywords in German, French, Spanish, Portuguese, Italian, Japanese, Chinese, Korean, Russian, Arabic, Hindi, Indonesian, Dutch, Polish, Turkish, Swedish, Filipino, Vietnamese, Thai |
| Language strip | Scrollable pill bar on every page linking to all 20 language versions |
| SEO prose | Keyword-dense paragraphs throughout all pages |

---

## SEO Files

| File | Purpose |
|---|---|
| `sitemap.xml` | 43 URLs with `lastmod`, priority and changefreq |
| `robots.txt` | Allows all crawlers, points to sitemap |
| `llms.txt` | 127-line comprehensive product summary for AI crawlers |
| `feed.xml` | RSS feed with 5 blog articles |
| `assets/favicon.svg` | Orange play button favicon |
| `.nojekyll` | Prevents GitHub Pages from running Jekyll |

**Submit sitemap after deploying:**
```
https://brightlane.github.io/videoconverteronline/sitemap.xml
```
→ Google Search Console → Add property → Submit sitemap
→ Bing Webmaster Tools → Import from Google

---

## llms.txt

The `llms.txt` file is 127 lines covering:
- Full product specs: all features, all formats, speed benchmarks
- All 8 AI features with descriptions and use cases
- All 20 language regions with coverage detail
- All pricing plans (free trial, $39.99/yr, $79.99 lifetime, commercial)
- Full site structure with every page URL described
- All schema types used
- Affiliate disclosure information

This ensures AI crawlers (Perplexity, ChatGPT, Claude) have complete structured information about the product and site.

---

## Product Facts (for content updates)

| Fact | Value |
|---|---|
| Product | Wondershare UniConverter 17 |
| Publisher | Wondershare Software Ltd (est. 2003, publicly listed) |
| Users | 15M+ in 200+ countries |
| Formats | 1000+ video, audio and image |
| Max resolution | 8K, HDR, HDR10, Dolby Vision |
| GPU speed | Up to 90× real-time (NVIDIA/AMD/Intel) |
| Example | 1hr 4K H.265 → 3–5 minutes with GPU |
| AI Translation | 130+ languages, 95%+ accuracy |
| AI Subtitles | 145+ languages, bilingual captions |
| AI Compression | Up to 150% reduction (NEW in v17) |
| Blu-ray burning | NEW in v17 |
| Interface languages | English, German, French, Spanish, Italian, Japanese, Chinese, Portuguese, Arabic |
| Windows | 7, 8, 10, 11 (32 and 64-bit) |
| macOS | 10.12+ including Apple Silicon M1/M2/M3 |
| Pricing | Free trial · $39.99/yr · $79.99 lifetime · $337.46 commercial (5 PCs) |
| Discounts | Up to 30% off available |

---

## v2 Improvements over v1

| Area | v1 (23 pages) | v2 (44 pages) |
|---|---|---|
| Language pages | 1 global page | 20 dedicated language pages |
| Language strip | None | Scrollable pill bar on every page |
| hreflang tags | None | 20 hreflang alternates on every page |
| AI coverage | Basic mention | Full /ai-features/ page with 8 tools in depth |
| AI translation | Mentioned | Featured prominently — 130 languages |
| AI subtitles | Mentioned | Featured — 145+ languages |
| AI compression | Not covered | Full guide with real examples |
| Blu-ray | Mentioned | Dedicated section — new in v17 |
| Screen recorder | Not covered | Dedicated /screen-recorder/ page |
| vs Freemake | Not covered | Full comparison page |
| Comparison tables | Basic | More detailed with more rows |
| llms.txt | 60 lines | 127 lines — comprehensive |
| Sitemap URLs | 21 | 43 |
| Keywords | 1000+ | 1500+ across 15 languages |
| Fonts | Syne + Space Grotesk | Cabinet Grotesk + Plus Jakarta Sans |
| Design | Orange/dark | Richer orange/dark with teal/purple accents |

---

## Design System

| Variable | Value | Usage |
|---|---|---|
| `--acc` | `#ff5a1f` | Primary orange — CTAs, headings |
| `--acc2` | `#ff2d78` | Pink/red — gradient accents |
| `--acc3` | `#ffd60a` | Gold — format chips, highlights |
| `--blue` | `#3b82f6` | Blue — info boxes |
| `--cyan` | `#22d3ee` | Cyan — accents |
| `--green` | `#22c55e` | Green — checkmarks |
| `--purple` | `#a855f7` | Purple — AI features theme |
| `--teal` | `#14b8a6` | Teal — secondary CTAs |
| `--bg` | `#03060e` | Deep dark background |
| `--txt` | `#eef2ff` | Primary text |
| `--muted` | `#7c8db5` | Body / secondary text |

Fonts: **Cabinet Grotesk** (headings, 700/800/900) + **Plus Jakarta Sans** (body, 300–800) + **JetBrains Mono** (code/format chips).

---

## File Structure After Build

```
videoconverter-site/
├── .nojekyll
├── index.html
├── 404.html
├── sitemap.xml       (43 URLs)
├── robots.txt
├── llms.txt          (127 lines)
├── feed.xml
├── assets/
│   └── favicon.svg
├── features/index.html
├── ai-features/index.html
├── formats/index.html
├── how-it-works/index.html
├── pricing/index.html
├── review/index.html
├── faq/index.html
├── download/index.html
├── blog/index.html
├── global/index.html
├── screen-recorder/index.html
├── convert-mp4/index.html
├── compress-video/index.html
├── convert-mkv-mp4/index.html
├── convert-mov-mp4/index.html
├── dvd-burner/index.html
├── alternatives/index.html
├── vs-handbrake/index.html
├── vs-vlc/index.html
├── vs-freemake/index.html
├── privacy/index.html
├── disclaimer/index.html
└── lang/
    ├── en/index.html
    ├── de/index.html
    ├── fr/index.html
    ├── es/index.html
    ├── pt/index.html
    ├── it/index.html
    ├── ja/index.html
    ├── zh/index.html
    ├── ko/index.html
    ├── ru/index.html
    ├── ar/index.html
    ├── hi/index.html
    ├── id/index.html
    ├── nl/index.html
    ├── pl/index.html
    ├── tr/index.html
    ├── sv/index.html
    ├── fil/index.html
    ├── vi/index.html
    └── th/index.html
```

---

## Tech Stack

| Layer | Choice |
|---|---|
| Generator | Python 3 stdlib only — zero dependencies |
| HTML/CSS/JS | Vanilla — no frameworks, instant load |
| Fonts | Google Fonts CDN (Cabinet Grotesk + Plus Jakarta Sans + JetBrains Mono) |
| Hosting | GitHub Pages — free, HTTPS, global CDN |
| CI/CD | GitHub Actions — auto-deploy on every push to `main` |

---

## License

Independent affiliate guide. UniConverter is a product of Wondershare Software Ltd.
This site is not affiliated with or endorsed by Wondershare.
