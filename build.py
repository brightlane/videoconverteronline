#!/usr/bin/env python3
"""
Landingi Affiliate Site Builder
High-performance static SEO generator for GitHub Pages

Features:
- Programmatic SEO page generation
- Modern responsive HTML
- Internal linking engine
- Sitemap + robots.txt
- llms.txt for AI crawler discovery
- JSON-LD structured data
- Category hubs
- Homepage generation
- Clean URL architecture
- Auto meta descriptions
- Fast static deployment
"""

import os
import html
from pathlib import Path
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# =========================================================
# CONFIG
# =========================================================

CONFIG = {
    "BASE_URL": "https://brightlane.github.io/landingl",
    "AFFILIATE_URL": "https://try.landingi.com/w5farvpasbpn?utm_source=deploy",
    "SITE_TITLE": "Landingi Review 2026",
    "SITE_DESCRIPTION": "Landing page software reviews, funnel strategies, and conversion optimization guides.",
    "AUTHOR": "Benny Palmarino",
    "OUTPUT_DIR": "site",
    "POSTS_PER_CATEGORY": 50,
}

# =========================================================
# DATA ENGINE
# =========================================================

NICHES = [
    "Real Estate",
    "SaaS",
    "Roofing",
    "HVAC",
    "Legal",
    "Dental",
    "Crypto",
    "Fitness",
    "Insurance",
    "Plumbing",
    "Marketing Agency",
    "Coaching",
]

ACTIONS = [
    "Lead Capture",
    "PPC Funnels",
    "Webinar Signup",
    "Appointment Booking",
    "Email Opt-In",
    "Free Trial Funnel",
    "Demo Requests",
]

FEATURES = [
    "high-converting templates",
    "drag-and-drop builder",
    "fast publishing",
    "A/B testing",
    "mobile optimization",
    "CRM integrations",
]


def slugify(text: str) -> str:
    return (
        text.lower()
        .replace("&", "and")
        .replace(" ", "-")
        .replace("/", "-")
    )


def get_data():
    posts = []

    for niche in NICHES:
        for action in ACTIONS:
            slug = f"landingi-for-{slugify(niche)}-{slugify(action)}"

            posts.append({
                "niche": niche,
                "action": action,
                "slug": slug,
                "title": f"Landingi for {niche} {action} in 2026",
                "description": (
                    f"Discover how {niche} businesses use "
                    f"Landingi for {action.lower()} to increase conversions."
                ),
            })

    return posts


# =========================================================
# HTML COMPONENTS
# =========================================================

def structured_data(post):
    return f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{html.escape(post['title'])}",
  "author": {{
    "@type": "Person",
    "name": "{CONFIG['AUTHOR']}"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Brightlane"
  }},
  "datePublished": "{datetime.utcnow().strftime('%Y-%m-%d')}",
  "mainEntityOfPage": "{CONFIG['BASE_URL']}/blog/{post['slug']}.html"
}}
</script>
"""


def global_styles():
    return """
<style>
:root{
    --bg:#0f172a;
    --card:#111827;
    --text:#e5e7eb;
    --muted:#94a3b8;
    --accent:#38bdf8;
}

*{
    box-sizing:border-box;
}

body{
    margin:0;
    padding:0;
    background:var(--bg);
    color:var(--text);
    font-family:Arial,sans-serif;
    line-height:1.7;
}

.container{
    width:min(1100px,92%);
    margin:auto;
}

header{
    padding:40px 0;
    border-bottom:1px solid #1e293b;
}

.logo{
    font-size:2rem;
    font-weight:bold;
}

.hero{
    padding:60px 0;
}

.card{
    background:var(--card);
    padding:25px;
    border-radius:16px;
    margin-bottom:25px;
    border:1px solid #1f2937;
}

.button{
    display:inline-block;
    padding:14px 22px;
    background:var(--accent);
    color:#000;
    text-decoration:none;
    border-radius:10px;
    font-weight:bold;
    margin-top:10px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:20px;
}

a{
    color:var(--accent);
    text-decoration:none;
}

footer{
    margin-top:60px;
    padding:40px 0;
    border-top:1px solid #1e293b;
    color:var(--muted);
}

ul{
    padding-left:20px;
}

.meta{
    color:var(--muted);
    font-size:.95rem;
}
</style>
"""


def html_wrapper(title, content, canonical, description, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>{html.escape(title)}</title>

<meta name="description" content="{html.escape(description)}">
<meta name="author" content="{CONFIG['AUTHOR']}">

<link rel="canonical" href="{canonical}">

<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">

{global_styles()}

{extra_head}
</head>

<body>

<header>
    <div class="container">
        <div class="logo">
            {CONFIG['SITE_TITLE']}
        </div>
    </div>
</header>

<main class="container">
{content}
</main>

<footer>
    <div class="container">
        <p>
            © {datetime.now().year} {CONFIG['AUTHOR']} • Built for SEO & AI Discovery
        </p>
    </div>
</footer>

</body>
</html>
"""


# =========================================================
# CONTENT ENGINE
# =========================================================

def build_internal_links(posts, current_slug, limit=5):
    related = [p for p in posts if p["slug"] != current_slug][:limit]

    links = "".join([
        f"<li><a href='/blog/{p['slug']}.html'>{p['title']}</a></li>"
        for p in related
    ])

    return f"""
    <div class="card">
        <h3>Related Guides</h3>
        <ul>{links}</ul>
    </div>
    """


def generate_article(post, posts):
    feature_list = "".join([
        f"<li>{feature.title()}</li>"
        for feature in FEATURES
    ])

    related_links = build_internal_links(posts, post["slug"])

    return f"""
<section class="hero">
    <h1>{post['title']}</h1>

    <p class="meta">
        Updated {datetime.utcnow().strftime('%B %d, %Y')}
    </p>

    <div class="card">
        <p>
            Looking for the best landing page builder for
            <strong>{post['niche']}</strong> campaigns?

            Landingi helps businesses improve
            <strong>{post['action']}</strong>
            with optimized templates and conversion-focused funnels.
        </p>

        <a class="button" href="{CONFIG['AFFILIATE_URL']}" target="_blank" rel="nofollow sponsored">
            Start Free Trial
        </a>
    </div>

    <div class="card">
        <h2>Why {post['niche']} Businesses Use Landingi</h2>

        <p>
            Modern marketers need fast-loading landing pages,
            conversion tracking, and easy funnel deployment.
            Landingi simplifies the entire process.
        </p>

        <ul>
            {feature_list}
        </ul>
    </div>

    <div class="card">
        <h2>Best Use Cases</h2>

        <p>
            Landingi works especially well for:
        </p>

        <ul>
            <li>{post['action']} funnels</li>
            <li>Paid advertising campaigns</li>
            <li>Lead generation</li>
            <li>Appointment scheduling</li>
            <li>Email capture pages</li>
        </ul>
    </div>

    {related_links}

</section>
"""


# =========================================================
# FILE HELPERS
# =========================================================

def write_file(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# =========================================================
# GENERATORS
# =========================================================

def build_homepage(posts):
    cards = ""

    for post in posts[:18]:
        cards += f"""
        <div class="card">
            <h3>{post['title']}</h3>

            <p>{post['description']}</p>

            <a href="/blog/{post['slug']}.html">
                Read Guide →
            </a>
        </div>
        """

    content = f"""
<section class="hero">
    <h1>Landingi Review & Funnel Strategy Hub</h1>

    <p>
        Discover landing page strategies, funnel optimization,
        and conversion tactics for modern businesses.
    </p>

    <div class="grid">
        {cards}
    </div>
</section>
"""

    html_output = html_wrapper(
        title=CONFIG["SITE_TITLE"],
        content=content,
        canonical=f"{CONFIG['BASE_URL']}/",
        description=CONFIG["SITE_DESCRIPTION"],
    )

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/index.html",
        html_output
    )


def build_articles(posts):
    urls = []

    for post in posts:
        article_content = generate_article(post, posts)

        html_output = html_wrapper(
            title=post["title"],
            content=article_content,
            canonical=f"{CONFIG['BASE_URL']}/blog/{post['slug']}.html",
            description=post["description"],
            extra_head=structured_data(post),
        )

        output_path = (
            f"{CONFIG['OUTPUT_DIR']}/blog/{post['slug']}.html"
        )

        write_file(output_path, html_output)

        urls.append(
            f"{CONFIG['BASE_URL']}/blog/{post['slug']}.html"
        )

    return urls


def build_404():
    content = """
<section class="hero">
    <div class="card">
        <h1>404 — Page Not Found</h1>

        <p>
            The page you requested could not be found.
        </p>

        <a class="button" href="/">
            Return Home
        </a>
    </div>
</section>
"""

    html_output = html_wrapper(
        title="404 - Page Not Found",
        content=content,
        canonical="",
        description="Page not found.",
    )

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/404.html",
        html_output
    )


def build_robots():
    robots = f"""User-agent: *
Allow: /

Sitemap: {CONFIG['BASE_URL']}/sitemap.xml
"""

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/robots.txt",
        robots
    )


def build_sitemap(urls):
    urlset = Element(
        "urlset",
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    )

    for url in urls:
        url_tag = SubElement(urlset, "url")

        loc = SubElement(url_tag, "loc")
        loc.text = url

        lastmod = SubElement(url_tag, "lastmod")
        lastmod.text = datetime.utcnow().strftime("%Y-%m-%d")

    xml_string = minidom.parseString(
        tostring(urlset)
    ).toprettyxml(indent="  ")

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/sitemap.xml",
        xml_string
    )


def build_llms_txt(posts):
    content = "# Landingi SEO Authority Hub\n\n"
    content += "## Programmatic SEO Pages\n\n"

    for post in posts:
        content += (
            f"- {post['title']} | "
            f"{CONFIG['BASE_URL']}/blog/{post['slug']}.html\n"
        )

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/llms.txt",
        content
    )


# =========================================================
# MAIN BUILD
# =========================================================

def build():
    print("Starting build...")

    posts = get_data()

    Path(CONFIG["OUTPUT_DIR"]).mkdir(
        exist_ok=True
    )

    build_homepage(posts)

    urls = [CONFIG["BASE_URL"] + "/"]

    urls.extend(build_articles(posts))

    build_404()
    build_robots()
    build_sitemap(urls)
    build_llms_txt(posts)

    print("=" * 50)
    print("BUILD COMPLETE")
    print("=" * 50)
    print(f"Generated Pages : {len(posts)}")
    print(f"Output Directory: {CONFIG['OUTPUT_DIR']}")
    print(f"Sitemap URLs    : {len(urls)}")
    print("=" * 50)


if __name__ == "__main__":
    build()
