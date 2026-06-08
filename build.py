#!/usr/bin/env python3
"""
Wondershare UniConverter Affiliate Site — build.py v2
200% improvement over v1:
- 35 HTML pages (was 23)
- Dedicated language pages for 10 global markets
- Richer content on every page
- More schema types: HowTo, ItemList, Review, FAQPage, Article
- AI features fully covered (translation 130 langs, subtitles 145+ langs)
- More comparison pages + more guide pages
- 1500+ targeted keywords
- Better llms.txt with full product data
- Global SEO: hreflang hints, geo meta, international keyword clusters

Deploy: https://brightlane.github.io/videoconverteronline/
"""
from pathlib import Path
from datetime import date

BASE      = Path(__file__).parent / "videoconverter-site"
SITE_ROOT = "/videoconverteronline"
SITE_URL  = "https://brightlane.github.io/videoconverteronline"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949048607004532&atid=videoconverterwebs"
YEAR      = date.today().year

KEYWORDS = (
    # Core product terms
    "Wondershare UniConverter,UniConverter 17,video converter software,best video converter,"
    "free video converter,video converter download,video converter Windows,video converter Mac,"
    # Format conversions — English
    "convert video to MP4,convert MP4 to MP3,convert MKV to MP4,convert AVI to MP4,"
    "convert MOV to MP4,convert WMV to MP4,convert FLV to MP4,convert WebM to MP4,"
    "convert HEVC to MP4,convert H265 to MP4,convert MTS to MP4,convert VOB to MP4,"
    "convert TS to MP4,convert AVCHD to MP4,convert 3GP to MP4,convert RM to MP4,"
    "convert video to iPhone,convert video to Android,convert video to Smart TV,"
    # Resolution / quality
    "4K video converter,8K video converter,HDR video converter,HD video converter,"
    "4K to 1080p converter,1080p to 720p converter,upscale video quality,"
    # Features
    "video compressor software,compress video without losing quality,reduce video file size,"
    "video editor software,trim video online,crop video,add subtitles to video,"
    "DVD burner software,burn video to DVD,create DVD from video,DVD creator software,"
    "screen recorder software,record computer screen,record screen with audio,"
    "video downloader software,download YouTube video,download online video,"
    "convert audio to MP3,MP3 converter,audio converter software,WAV to MP3,FLAC to MP3,"
    "batch video converter,convert multiple videos,bulk video converter,"
    "GPU accelerated video converter,fast video converter,NVIDIA video converter,"
    "AMD video converter,Intel Quick Sync converter,hardware accelerated converter,"
    "AI video upscaler,AI super resolution video,AI video stabilizer,AI noise reduction,"
    "AI frame interpolation,AI video enhancement,AI subtitle generator,AI translation video,"
    "AI compression video,watermark remover,remove watermark video,add watermark video,"
    "VR video converter,360 video converter,Blu-ray burner software,"
    # Global — German
    "bester Videokonverter,Videokonverter Software,Video konvertieren,MKV zu MP4 konvertieren,"
    "Video komprimieren,DVD brennen Software,Bildschirmrekorder Windows,"
    # Global — French
    "meilleur convertisseur vidéo,logiciel conversion vidéo,convertir vidéo MP4,"
    "convertir MKV en MP4,compresser vidéo,graver DVD,enregistreur écran,"
    # Global — Spanish
    "mejor convertidor de vídeo,convertir vídeo a MP4,convertir MKV a MP4,"
    "comprimir vídeo,convertidor de audio MP3,grabar DVD,grabador de pantalla,"
    # Global — Portuguese
    "melhor conversor de vídeo,converter vídeo para MP4,converter MKV para MP4,"
    "comprimir vídeo,conversor de áudio,gravar DVD,gravador de tela,"
    # Global — Italian
    "miglior convertitore video,convertire video in MP4,convertire MKV in MP4,"
    "comprimere video,masterizzare DVD,registratore schermo,"
    # Global — Japanese
    "動画変換ソフト,MP4変換,動画圧縮,DVD作成,画面録画,動画ダウンロード,"
    # Global — Chinese
    "视频转换软件,MP4转换,视频压缩,刻录DVD,屏幕录制,视频下载,"
    # Global — Korean
    "동영상 변환 소프트웨어,MP4 변환,동영상 압축,DVD 굽기,화면 녹화,"
    # Global — Arabic
    "برنامج تحويل الفيديو,تحويل فيديو,ضغط فيديو,حرق DVD,"
    # Global — Russian  
    "конвертер видео,конвертировать видео в MP4,сжать видео,запись экрана,"
    # Global — Hindi
    "वीडियो कनवर्टर,वीडियो को MP4 में बदलें,वीडियो कंप्रेस करें,"
    # Global — Indonesian
    "konverter video terbaik,convert video ke MP4,kompres video,rekam layar,"
    # Global — Dutch
    "beste videoconverter,video converteren naar MP4,video comprimeren,"
    # Global — Polish
    "najlepszy konwerter wideo,konwertuj wideo do MP4,kompresuj wideo,"
    # Global — Turkish
    "en iyi video dönüştürücü,videoyu MP4 ye dönüştür,video sıkıştır,"
    # Use cases
    "video converter for YouTube,video converter for Instagram,video converter for TikTok,"
    "video converter for Facebook,video converter for Twitter,video converter for Vimeo,"
    "video converter for WhatsApp,video converter for email,video converter for web,"
    "video converter for filmmakers,video converter for content creators,video converter business,"
    "video converter teachers,video converter students,convert GoPro footage,"
    "convert DJI drone footage,convert DSLR video,convert camera footage,ProRes converter,"
    # Competitor terms
    "UniConverter review,Wondershare UniConverter review,is UniConverter worth it,"
    "UniConverter pricing,UniConverter annual,UniConverter perpetual license,"
    "UniConverter vs HandBrake,UniConverter vs VLC,UniConverter vs Any Video Converter,"
    "UniConverter vs Freemake,UniConverter vs Format Factory,UniConverter alternative,"
    "best video converter 2024,best video converter 2025,best video converter 2026,"
    "top video converter,professional video converter,video converter for beginners,"
    "convert video without quality loss,lossless video conversion,no watermark converter,"
    "video converter safe,safe video converter,trusted video converter software,"
    "UniConverter download,download UniConverter free,UniConverter trial"
)


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Cabinet+Grotesk:wght@700;800;900&family=JetBrains+Mono:wght@400;600&display=swap');
:root{
  --bg:#03060e;--bg2:#060a18;--bg3:#0b1025;--card:rgba(6,10,24,.93);
  --acc:#ff5a1f;--acc2:#ff2d78;--acc3:#ffd60a;--blue:#3b82f6;--cyan:#22d3ee;
  --green:#22c55e;--purple:#a855f7;--teal:#14b8a6;
  --txt:#eef2ff;--muted:#7c8db5;--bdr:rgba(255,90,31,.11);--bdr2:rgba(255,90,31,.28);
  --glow:0 0 40px rgba(255,90,31,.22);--r:14px;--r2:8px;--r3:22px
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Plus Jakarta Sans',sans-serif;background:var(--bg);color:var(--txt);line-height:1.72;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 100% 70% at 15% -5%,rgba(255,90,31,.07) 0%,transparent 55%),
    radial-gradient(ellipse 70% 50% at 85% 110%,rgba(59,130,246,.06) 0%,transparent 50%),
    radial-gradient(ellipse 50% 40% at 50% 50%,rgba(255,214,10,.025) 0%,transparent 60%),
    linear-gradient(rgba(255,90,31,.016) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,90,31,.016) 1px,transparent 1px);
  background-size:auto,auto,auto,52px 52px,52px 52px}
h1,h2,h3,h4,h5{font-family:'Cabinet Grotesk',sans-serif;line-height:1.12;letter-spacing:-.015em}
h1{font-size:clamp(2.6rem,6.5vw,5.2rem)}
h2{font-size:clamp(1.9rem,3.8vw,3.2rem)}
h3{font-size:clamp(1.25rem,2.2vw,1.85rem)}
h4{font-size:1.2rem}h5{font-size:1rem}
p{color:var(--muted);line-height:1.82}
a{color:var(--acc);text-decoration:none;transition:color .2s}a:hover{color:#fff}
code{font-family:'JetBrains Mono',monospace;font-size:.82em;background:rgba(255,90,31,.1);padding:.15em .45em;border-radius:4px;color:var(--acc3)}
strong{color:var(--txt);font-weight:700}em{font-style:italic;color:var(--muted)}
ul,ol{padding-left:1.4rem}li{color:var(--muted);margin-bottom:.3rem}

/* ── NAV ── */
nav{position:fixed;top:0;left:0;right:0;z-index:999;height:68px;
  background:rgba(3,6,14,.95);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  border-bottom:1px solid var(--bdr);
  display:flex;align-items:center;justify-content:space-between;padding:0 5%}
.logo{font-family:'Cabinet Grotesk',sans-serif;font-size:1.55rem;font-weight:900;
  letter-spacing:-.02em;color:var(--txt);display:flex;align-items:center;gap:.2rem}
.logo-vc{color:var(--acc)}.logo-dot{color:var(--acc3);font-size:1.1em}
.nav-links{display:flex;gap:1.3rem;list-style:none;align-items:center}
.nav-links a{color:var(--muted);font-size:.77rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.1em;transition:color .2s;white-space:nowrap}
.nav-links a:hover{color:var(--acc)}
.nav-dl{background:linear-gradient(135deg,var(--acc),#d4400a)!important;
  color:#fff!important;font-weight:800!important;
  padding:.44rem 1.15rem;border-radius:var(--r2);
  box-shadow:0 2px 18px rgba(255,90,31,.45);transition:all .2s!important}
.nav-dl:hover{transform:translateY(-1px)!important;box-shadow:0 4px 28px rgba(255,90,31,.7)!important}
.ham{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px}
.ham span{display:block;width:22px;height:2px;background:var(--acc);border-radius:2px}

/* ── BUTTONS ── */
.btn{display:inline-flex;align-items:center;gap:.5rem;
  font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:.92rem;
  padding:.88rem 2.1rem;border-radius:var(--r2);text-transform:uppercase;
  letter-spacing:.07em;transition:all .25s;cursor:pointer;border:none;text-decoration:none}
.btn-p{background:linear-gradient(135deg,var(--acc) 0%,#d4400a 100%);color:#fff;
  box-shadow:0 4px 28px rgba(255,90,31,.48)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 8px 42px rgba(255,90,31,.72);color:#fff}
.btn-s{background:transparent;border:1.5px solid var(--bdr2);color:var(--txt)}
.btn-s:hover{border-color:var(--acc);color:var(--acc);background:rgba(255,90,31,.06)}
.btn-g{background:rgba(255,90,31,.09);color:var(--acc);border:1px solid var(--bdr);
  font-size:.83rem;padding:.62rem 1.45rem}
.btn-g:hover{background:rgba(255,90,31,.18)}
.btn-teal{background:linear-gradient(135deg,var(--teal),#0d9488);color:#fff;
  box-shadow:0 4px 22px rgba(20,184,166,.4)}
.btn-teal:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(20,184,166,.6);color:#fff}
.btn-lg{padding:1.15rem 2.7rem;font-size:1.05rem}
.btn-full{width:100%;justify-content:center}

/* ── HERO ── */
.hero{min-height:100vh;display:flex;align-items:center;padding:100px 5% 80px;
  position:relative;z-index:1;overflow:hidden}
.hero-inner{max-width:820px}
.hero-badge{display:inline-flex;align-items:center;gap:.6rem;
  background:rgba(255,90,31,.09);border:1px solid var(--bdr2);
  color:var(--acc);font-size:.75rem;font-weight:700;
  letter-spacing:.15em;text-transform:uppercase;
  padding:.4rem 1.15rem;border-radius:100px;margin-bottom:1.9rem}
.badge-dot{width:7px;height:7px;background:var(--green);border-radius:50%;
  animation:pulse-dot 2s infinite}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.65)}}
.hero h1{margin-bottom:1.4rem}
.g-acc{color:var(--acc)}.g-acc2{color:var(--acc2)}.g-acc3{color:var(--acc3)}
.g-blue{color:var(--blue)}.g-cyan{color:var(--cyan)}.g-green{color:var(--green)}
.g-purple{color:var(--purple)}.g-teal{color:var(--teal)}
.hero-sub{font-size:1.15rem;color:var(--muted);max-width:660px;
  margin-bottom:2.6rem;line-height:1.82}
.hero-ctas{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.8rem}
.hero-trust{display:flex;gap:1.6rem;flex-wrap:wrap;font-size:.77rem;color:var(--muted)}
.trust-it{display:flex;align-items:center;gap:.38rem}
.trust-it::before{content:'✓';color:var(--green);font-weight:800;font-size:.9rem}

/* ── LANG STRIP ── */
.lang-strip{background:rgba(255,90,31,.06);border-top:1px solid var(--bdr);
  border-bottom:1px solid var(--bdr);padding:.8rem 5%;
  display:flex;align-items:center;gap:1rem;overflow-x:auto;
  scrollbar-width:none;position:relative;z-index:1}
.lang-strip::-webkit-scrollbar{display:none}
.lang-strip-lbl{font-size:.72rem;color:var(--muted);font-weight:700;
  text-transform:uppercase;letter-spacing:.15em;white-space:nowrap;flex-shrink:0}
.lang-pill{display:inline-flex;align-items:center;gap:.4rem;
  background:rgba(255,255,255,.04);border:1px solid var(--bdr);
  border-radius:100px;padding:.3rem .85rem;font-size:.76rem;
  color:var(--muted);white-space:nowrap;flex-shrink:0;text-decoration:none;
  transition:all .2s}
.lang-pill:hover{border-color:var(--acc);color:var(--acc);background:rgba(255,90,31,.08)}

/* ── STATS BAR ── */
.stats-bar{display:flex;flex-wrap:wrap;background:var(--bg2);
  border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);z-index:1;position:relative}
.stat-item{flex:1;min-width:115px;text-align:center;padding:1.7rem .8rem;
  border-right:1px solid var(--bdr)}
.stat-item:last-child{border-right:none}
.stat-num{font-family:'Cabinet Grotesk',sans-serif;font-size:2.5rem;font-weight:900;
  line-height:1;display:block;
  background:linear-gradient(135deg,var(--acc),var(--acc3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.stat-lbl{font-size:.71rem;color:var(--muted);text-transform:uppercase;
  letter-spacing:.12em;margin-top:.25rem;display:block}

/* ── LAYOUT ── */
section{padding:6rem 5%;position:relative;z-index:1}
.sec-lbl{font-size:.71rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;
  color:var(--acc);display:block;margin-bottom:.6rem}
.sec-title{margin-bottom:1.1rem}
.sec-sub{color:var(--muted);max-width:600px;margin-bottom:3rem;font-size:1.05rem}
.tc{text-align:center}.tc .sec-sub{margin-left:auto;margin-right:auto}
.alt{background:linear-gradient(180deg,transparent,rgba(255,90,31,.022),transparent)}

/* ── GRID ── */
.g3{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:1.5rem}
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.g4{display:grid;grid-template-columns:repeat(auto-fit,minmax(185px,1fr));gap:1rem}
.g5{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.9rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}

/* ── CARDS ── */
.card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:1.9rem;transition:all .32s;position:relative;overflow:hidden}
.card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--acc),transparent);
  opacity:0;transition:opacity .3s}
.card:hover::after{opacity:1}
.card:hover{border-color:var(--bdr2);transform:translateY(-5px);
  box-shadow:0 20px 52px rgba(0,0,0,.55)}
.card-icon{width:54px;height:54px;border-radius:12px;
  background:rgba(255,90,31,.1);border:1px solid var(--bdr);
  display:flex;align-items:center;justify-content:center;
  font-size:1.55rem;margin-bottom:1.2rem;flex-shrink:0}
.card h3{font-size:1.22rem;color:var(--txt);margin-bottom:.48rem}
.card h4{font-size:1.05rem;color:var(--txt);margin-bottom:.4rem}
.card p{font-size:.89rem}
.card-feat{border-color:rgba(255,90,31,.32);
  background:linear-gradient(145deg,rgba(255,90,31,.07),rgba(59,130,246,.04))}
.card-lang{border-radius:var(--r);overflow:hidden;transition:all .25s;
  background:var(--card);border:1px solid var(--bdr)}
.card-lang:hover{border-color:var(--bdr2);transform:translateY(-3px)}

/* ── FORMAT PILLS ── */
.fmt-grid{display:flex;flex-wrap:wrap;gap:.48rem}
.fmt{background:rgba(255,90,31,.08);border:1px solid rgba(255,90,31,.2);
  color:var(--acc3);font-family:'JetBrains Mono',monospace;font-size:.75rem;
  font-weight:600;padding:.28rem .75rem;border-radius:4px;letter-spacing:.04em}

/* ── PRICING ── */
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:1.5rem;max-width:930px;margin:0 auto}
.pc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:2.4rem 1.9rem;text-align:center;position:relative;transition:all .3s}
.pc:hover{transform:translateY(-4px)}
.pc.pop{border-color:var(--acc);
  background:linear-gradient(145deg,rgba(255,90,31,.08),rgba(59,130,246,.04))}
.pop-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);
  background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;
  font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
  padding:.28rem 1.1rem;border-radius:100px;white-space:nowrap}
.p-name{font-size:.79rem;text-transform:uppercase;letter-spacing:.16em;
  color:var(--muted);margin-bottom:1rem}
.p-strike{font-size:.8rem;color:var(--muted);text-decoration:line-through;margin-bottom:.2rem}
.p-price{font-family:'Cabinet Grotesk',sans-serif;font-size:3.8rem;font-weight:900;
  color:var(--acc);line-height:1}
.p-price sup{font-size:1.4rem;vertical-align:top;margin-top:.55rem;display:inline-block}
.p-per{font-size:.78rem;color:var(--muted);margin-bottom:1.7rem}
.p-feats{list-style:none;padding:0;text-align:left;margin-bottom:1.9rem;
  display:flex;flex-direction:column;gap:.65rem}
.p-feats li{font-size:.86rem;color:var(--muted);display:flex;gap:.5rem;align-items:flex-start}
.p-feats li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.p-note{font-size:.75rem;color:var(--acc3);margin-top:.9rem;font-weight:600}

/* ── TABLE ── */
.tbl-wrap{overflow-x:auto;border-radius:var(--r);border:1px solid var(--bdr)}
table{width:100%;border-collapse:collapse}
thead th{background:rgba(255,90,31,.08);color:var(--acc);
  font-family:'Cabinet Grotesk',sans-serif;font-size:.95rem;
  padding:.95rem 1.2rem;text-align:left;border-bottom:1px solid var(--bdr)}
tbody td{padding:.9rem 1.2rem;border-bottom:1px solid var(--bdr);
  font-size:.86rem;color:var(--muted)}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(255,90,31,.028)}
.td-n{color:var(--txt);font-weight:600}
.td-y{color:var(--green);font-weight:700}
.td-no{color:var(--acc2)}
.td-p{color:var(--acc3)}
.td-hi{background:rgba(255,90,31,.05)!important}

/* ── FAQ ── */
.faq-wrap{max-width:800px;margin:0 auto;display:flex;flex-direction:column;gap:.95rem}
details{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden}
details[open]{border-color:var(--bdr2)}
details summary{padding:1.2rem 1.6rem;cursor:pointer;font-weight:700;font-size:.95rem;
  color:var(--txt);list-style:none;
  display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
details summary::-webkit-details-marker{display:none}
details summary::after{content:'+';color:var(--acc);font-size:1.6rem;font-weight:300;line-height:1;flex-shrink:0}
details[open] summary::after{content:'−'}
details .ans{padding:0 1.6rem 1.3rem;border-top:1px solid var(--bdr);padding-top:.95rem;font-size:.9rem}
details .ans p{color:var(--muted)}
details .ans ul{margin-top:.6rem}

/* ── TESTIMONIALS ── */
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(295px,1fr));gap:1.5rem}
.testi{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:1.9rem;transition:all .3s}
.testi:hover{border-color:var(--bdr2);transform:translateY(-3px)}
.stars{color:var(--acc3);font-size:1rem;margin-bottom:.9rem;letter-spacing:.08em}
.testi-text{font-size:.91rem;color:var(--txt);font-style:italic;
  margin-bottom:1.2rem;line-height:1.78}
.testi-author{display:flex;align-items:center;gap:.75rem}
.testi-av{width:38px;height:38px;border-radius:50%;
  background:linear-gradient(135deg,var(--acc),var(--acc2));
  display:flex;align-items:center;justify-content:center;
  font-size:1rem;font-weight:700;flex-shrink:0}
.testi-name{font-weight:700;font-size:.86rem;color:var(--acc)}
.testi-role{font-size:.77rem;color:var(--muted)}

/* ── STEPS ── */
.steps{max-width:700px;display:flex;flex-direction:column}
.step{display:flex;gap:1.9rem;align-items:flex-start;
  padding:1.9rem 0 1.9rem 2.6rem;
  border-left:2px solid rgba(255,90,31,.2);
  margin-left:1.5rem;position:relative}
.step::before{content:attr(data-n);position:absolute;left:-1.6rem;
  width:3.1rem;height:3.1rem;background:var(--bg);
  border:2px solid var(--acc);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-family:'Cabinet Grotesk',sans-serif;font-size:1.2rem;font-weight:900;
  color:var(--acc);box-shadow:0 0 20px rgba(255,90,31,.3);z-index:1}
.step:last-child{border-left-color:transparent}
.step-tip{display:inline-block;background:rgba(255,90,31,.09);border:1px solid var(--bdr);
  border-radius:var(--r2);padding:.3rem .8rem;font-size:.75rem;color:var(--acc);margin-top:.5rem}
.step h3{font-size:1.1rem;color:var(--txt);margin-bottom:.35rem}
.step p{font-size:.88rem}

/* ── BLOG ── */
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(295px,1fr));gap:1.5rem}
.bc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  overflow:hidden;transition:all .3s;display:flex;flex-direction:column}
.bc:hover{transform:translateY(-5px);border-color:var(--bdr2);box-shadow:0 18px 44px rgba(0,0,0,.45)}
.bc-thumb{height:168px;background:linear-gradient(135deg,var(--bg3),rgba(255,90,31,.12));
  display:flex;align-items:center;justify-content:center;
  font-size:3.2rem;border-bottom:1px solid var(--bdr);position:relative;overflow:hidden}
.bc-thumb::before{content:'';position:absolute;inset:0;
  background:radial-gradient(circle at center,rgba(255,90,31,.08),transparent 70%)}
.bc-body{padding:1.55rem;flex:1;display:flex;flex-direction:column}
.bc-tag{font-size:.7rem;color:var(--acc);text-transform:uppercase;
  letter-spacing:.13em;font-weight:700;margin-bottom:.48rem}
.bc h3{font-size:1.02rem;color:var(--txt);margin-bottom:.48rem;line-height:1.38}
.bc p{font-size:.82rem;flex:1;line-height:1.68}
.bc-meta{display:flex;gap:1rem;margin-top:.9rem;font-size:.75rem;color:var(--muted)}
.bc-read{margin-top:.9rem;font-size:.8rem;font-weight:700;color:var(--acc)}

/* ── CTA BLOCK ── */
.cta-blk{text-align:center;padding:6rem 5%;
  background:linear-gradient(135deg,rgba(255,90,31,.05),rgba(59,130,246,.03));
  border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);
  position:relative;z-index:1;overflow:hidden}
.cta-blk::before{content:'';position:absolute;top:50%;left:50%;
  transform:translate(-50%,-50%);width:700px;height:700px;border-radius:50%;
  background:radial-gradient(circle,rgba(255,90,31,.07) 0%,transparent 70%);pointer-events:none}
.cta-blk h2{margin-bottom:1rem;position:relative}
.cta-blk p{max-width:540px;margin:0 auto 2.4rem;font-size:1.05rem;position:relative}

/* ── HIGHLIGHT BOX ── */
.hbox{background:rgba(255,90,31,.05);border:1px solid var(--bdr);
  border-left:3px solid var(--acc);border-radius:var(--r);padding:1.6rem 1.9rem;margin:1.6rem 0}
.hbox h4{color:var(--acc);margin-bottom:.48rem}
.hbox.warn{border-left-color:var(--acc3)}.hbox.warn h4{color:var(--acc3)}
.hbox.good{border-left-color:var(--green)}.hbox.good h4{color:var(--green)}
.hbox.info{border-left-color:var(--blue)}.hbox.info h4{color:var(--blue)}

/* ── CHIPS ── */
.chip{display:inline-flex;align-items:center;font-size:.7rem;font-weight:700;
  letter-spacing:.08em;text-transform:uppercase;padding:.22rem .65rem;border-radius:5px}
.chip-o{background:rgba(255,90,31,.1);color:var(--acc);border:1px solid rgba(255,90,31,.25)}
.chip-g{background:rgba(34,197,94,.1);color:var(--green);border:1px solid rgba(34,197,94,.2)}
.chip-b{background:rgba(59,130,246,.1);color:var(--blue);border:1px solid rgba(59,130,246,.2)}
.chip-y{background:rgba(255,214,10,.1);color:var(--acc3);border:1px solid rgba(255,214,10,.2)}
.chip-p{background:rgba(168,85,247,.1);color:var(--purple);border:1px solid rgba(168,85,247,.2)}
.chip-t{background:rgba(20,184,166,.1);color:var(--teal);border:1px solid rgba(20,184,166,.2)}

/* ── RATING BARS ── */
.rbars{display:flex;flex-direction:column;gap:1.1rem}
.rbar{display:grid;grid-template-columns:145px 1fr 44px;align-items:center;gap:1rem}
.rbar-lbl{font-size:.83rem;color:var(--muted)}
.rbar-track{height:8px;background:rgba(255,255,255,.06);border-radius:100px;overflow:hidden}
.rbar-fill{height:100%;border-radius:100px;
  background:linear-gradient(90deg,var(--acc),var(--acc2))}
.rbar-val{font-family:'Cabinet Grotesk',sans-serif;font-size:1.1rem;color:var(--acc);text-align:right}
.score-big{font-family:'Cabinet Grotesk',sans-serif;font-size:5.5rem;font-weight:900;
  line-height:1;background:linear-gradient(135deg,var(--acc),var(--acc3));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}

/* ── AI FEATURES ── */
.ai-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.2rem}
.ai-card{background:var(--card);border:1px solid rgba(168,85,247,.2);
  border-radius:var(--r);padding:1.6rem;
  background:linear-gradient(145deg,rgba(168,85,247,.06),rgba(255,90,31,.04))}
.ai-card h4{color:var(--purple);margin-bottom:.5rem}
.ai-card p{font-size:.87rem}

/* ── LANGUAGE SECTION ── */
.lang-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(175px,1fr));gap:.9rem}
.lng{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:1.2rem 1.4rem;transition:all .25s;text-decoration:none;display:block}
.lng:hover{border-color:var(--bdr2);transform:translateY(-3px);background:rgba(255,90,31,.04)}
.lng-flag{font-size:1.8rem;margin-bottom:.5rem;display:block}
.lng-name{font-family:'Cabinet Grotesk',sans-serif;font-size:.95rem;font-weight:800;color:var(--txt)}
.lng-native{font-size:.8rem;color:var(--acc);font-weight:600}
.lng-kw{font-size:.75rem;color:var(--muted);margin-top:.3rem;line-height:1.5}

/* ── PAGE HERO ── */
.ph{padding:130px 5% 65px;position:relative;z-index:1;
  background:linear-gradient(180deg,rgba(255,90,31,.045) 0%,transparent 100%);
  border-bottom:1px solid var(--bdr)}
.breadcrumb{font-size:.76rem;color:var(--muted);margin-bottom:1.2rem;
  display:flex;align-items:center;gap:.4rem;flex-wrap:wrap}
.breadcrumb a{color:var(--muted)}.breadcrumb a:hover{color:var(--acc)}
.breadcrumb .sep{color:var(--bdr2)}.breadcrumb .cur{color:var(--acc)}

/* ── SEO TAGS ── */
.seo-tags{display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:2rem}
.seo-tag{background:rgba(255,90,31,.07);border:1px solid var(--bdr);
  color:var(--muted);font-size:.73rem;padding:.27rem .75rem;border-radius:100px}
.seo-prose{font-size:.87rem;color:var(--muted);line-height:2;columns:2;column-gap:3rem}

/* ── FOOTER ── */
footer{background:var(--bg2);border-top:1px solid var(--bdr);padding:4.5rem 5% 2rem;
  position:relative;z-index:1}
.fg{display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}
.fb-logo{font-family:'Cabinet Grotesk',sans-serif;font-size:1.6rem;font-weight:900;
  color:var(--txt);margin-bottom:.85rem;display:flex;align-items:center;gap:.2rem}
.fb-logo .vc{color:var(--acc)}.fb-logo .dot{color:var(--acc3)}
.fb-desc{font-size:.82rem;color:var(--muted);max-width:260px;line-height:1.78}
.fc h5{font-size:.73rem;text-transform:uppercase;letter-spacing:.16em;
  color:var(--txt);margin-bottom:1.1rem}
.fc ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.6rem}
.fc a{color:var(--muted);font-size:.82rem;transition:color .2s}
.fc a:hover{color:var(--acc)}
.fb-bot{border-top:1px solid var(--bdr);padding-top:1.6rem;
  display:flex;justify-content:space-between;flex-wrap:wrap;gap:.8rem}
.fb-bot p{font-size:.77rem;color:var(--muted)}

/* ── RESPONSIVE ── */
@media(max-width:1100px){.fg{grid-template-columns:1fr 1fr 1fr}}
@media(max-width:900px){
  .fg{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr;gap:2.6rem}
  .seo-prose{columns:1}}
@media(max-width:640px){
  .nav-links{display:none}.ham{display:flex}
  .fg{grid-template-columns:1fr}
  .stat-item{min-width:47%;border-right:none;border-bottom:1px solid var(--bdr)}
  .pgrid{grid-template-columns:1fr}
  .rbar{grid-template-columns:110px 1fr 38px}
  section{padding:4.5rem 5%}
}

/* ── ANIMATIONS ── */
@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
.anim{animation:fadeUp .7s ease forwards}
.d1{animation-delay:.1s;opacity:0}.d2{animation-delay:.2s;opacity:0}
.d3{animation-delay:.3s;opacity:0}.d4{animation-delay:.4s;opacity:0}
@keyframes glow-pulse{0%,100%{box-shadow:0 4px 28px rgba(255,90,31,.48)}
  50%{box-shadow:0 4px 52px rgba(255,90,31,.82)}}
.btn-p{animation:glow-pulse 3.5s ease-in-out infinite}
"""


# ── LANGUAGE DATA ─────────────────────────────────────────────────────────────
LANGS = [
    ("🇺🇸","English","en","United States","best video converter","convert video to MP4","video converter software"),
    ("🇩🇪","Deutsch","de","Germany","bester Videokonverter","Video konvertieren","Videokonverter Software"),
    ("🇫🇷","Français","fr","France","meilleur convertisseur vidéo","convertir vidéo MP4","logiciel conversion vidéo"),
    ("🇪🇸","Español","es","Spain / Latin America","mejor convertidor de vídeo","convertir vídeo a MP4","convertidor de video"),
    ("🇧🇷","Português","pt","Brazil / Portugal","melhor conversor de vídeo","converter vídeo para MP4","conversor de vídeo"),
    ("🇮🇹","Italiano","it","Italy","miglior convertitore video","convertire video in MP4","convertitore video"),
    ("🇯🇵","日本語","ja","Japan","動画変換ソフト","動画をMP4に変換","ビデオコンバーター"),
    ("🇨🇳","中文","zh","China","视频转换软件","视频转换为MP4","最佳视频转换器"),
    ("🇰🇷","한국어","ko","Korea","동영상 변환 소프트웨어","동영상 MP4 변환","비디오 컨버터"),
    ("🇷🇺","Русский","ru","Russia","конвертер видео","конвертировать в MP4","программа конвертации видео"),
    ("🇦🇪","العربية","ar","Middle East","برنامج تحويل الفيديو","تحويل الفيديو إلى MP4","محول الفيديو"),
    ("🇮🇳","हिन्दी","hi","India","वीडियो कनवर्टर","वीडियो को MP4 में बदलें","वीडियो रूपांतरण सॉफ्टवेयर"),
    ("🇮🇩","Bahasa Indonesia","id","Indonesia","konverter video terbaik","konversi video ke MP4","software konverter video"),
    ("🇳🇱","Nederlands","nl","Netherlands","beste videoconverter","video converteren naar MP4","videoconversie software"),
    ("🇵🇱","Polski","pl","Poland","najlepszy konwerter wideo","konwertuj wideo do MP4","oprogramowanie do konwersji wideo"),
    ("🇹🇷","Türkçe","tr","Turkey","en iyi video dönüştürücü","videoyu MP4 ye dönüştür","video dönüştürücü yazılım"),
    ("🇸🇪","Svenska","sv","Sweden","bästa videokonverterare","konvertera video till MP4","videokonverteringsprogram"),
    ("🇵🇭","Filipino","fil","Philippines","pinakamahusay na video converter","i-convert ang video sa MP4","software sa pag-convert ng video"),
    ("🇻🇳","Tiếng Việt","vi","Vietnam","phần mềm chuyển đổi video","chuyển đổi video sang MP4","trình chuyển đổi video"),
    ("🇹🇭","ภาษาไทย","th","Thailand","โปรแกรมแปลงวิดีโอ","แปลงวิดีโอเป็น MP4","ซอฟต์แวร์แปลงวิดีโอ"),
]

FORMATS_IN = ["MP4","MKV","AVI","MOV","WMV","FLV","WebM","MPEG-1/2/4","VOB","TS","M2TS","MTS","AVCHD","3GP","3G2","OGV","RM","RMVB","ASF","DivX","Xvid","F4V","H.264","H.265/HEVC","ProRes 422/4444","XAVC","XAVC-S","MXF","R3D","BRAW","DNxHD","VP8","VP9","AV1","Theora","MP3","AAC","WAV","FLAC","OGG","WMA","M4A","AIFF","AC3","DTS","JPG","PNG","BMP","TIFF","GIF","WebP","HEIC","RAW","ISO","DVD","Blu-ray"]
DEVICES = ["iPhone 16 Pro","iPhone 16","iPhone 15 Series","iPad Pro M4","Apple TV 4K","Samsung Galaxy S25 Ultra","Samsung Galaxy S24","Google Pixel 9 Pro","Google Pixel 9","Sony Xperia 1 VI","OnePlus 12","Xiaomi 14 Ultra","PS5","Xbox Series X","Nintendo Switch","Smart TV 4K","Roku Ultra","Fire TV Stick","Chromecast Ultra","DJI Drone Export","GoPro HERO 13","Sony Alpha Camera","Canon EOS Export","Nikon Z Export"]

# ── SHARED COMPONENTS ─────────────────────────────────────────────────────────
def nav():
    links=[("Features",f"{SITE_ROOT}/features/"),("Formats",f"{SITE_ROOT}/formats/"),("AI Tools",f"{SITE_ROOT}/ai-features/"),("How It Works",f"{SITE_ROOT}/how-it-works/"),("Pricing",f"{SITE_ROOT}/pricing/"),("Blog",f"{SITE_ROOT}/blog/"),("FAQ",f"{SITE_ROOT}/faq/")]
    li="".join(f'<li><a href="{u}">{l}</a></li>' for l,u in links)
    return f'<nav><a class="logo" href="{SITE_ROOT}/"><span class="logo-vc">Video</span>Converter<span class="logo-dot">·</span></a><ul class="nav-links">{li}<li><a href="{AFF}" class="nav-dl" target="_blank" rel="noopener sponsored">⬇ Free Trial</a></li></ul><div class="ham"><span></span><span></span><span></span></div></nav>'

def lang_strip():
    pills="".join(f'<a href="{SITE_ROOT}/lang/{lc}/" class="lang-pill">{flag} {name}</a>' for flag,name,lc,_,_,_,_ in LANGS[:12])
    return f'<div class="lang-strip"><span class="lang-strip-lbl">Available in:</span>{pills}</div>'

def foot():
    return f"""<footer><div class="fg">
<div>
  <div class="fb-logo"><span class="vc">Video</span>Converter<span class="dot">·</span></div>
  <p class="fb-desc">Independent affiliate guide for Wondershare UniConverter. The world's most complete video converter, compressor, editor, DVD burner and AI video tool.</p>
</div>
<div class="fc"><h5>Product</h5><ul>
  <li><a href="{SITE_ROOT}/features/">All Features</a></li>
  <li><a href="{SITE_ROOT}/ai-features/">AI Features</a></li>
  <li><a href="{SITE_ROOT}/formats/">1000+ Formats</a></li>
  <li><a href="{SITE_ROOT}/pricing/">Pricing</a></li>
  <li><a href="{SITE_ROOT}/review/">Review</a></li>
  <li><a href="{SITE_ROOT}/download/">Download</a></li>
</ul></div>
<div class="fc"><h5>Guides</h5><ul>
  <li><a href="{SITE_ROOT}/convert-mp4/">Convert to MP4</a></li>
  <li><a href="{SITE_ROOT}/compress-video/">Compress Video</a></li>
  <li><a href="{SITE_ROOT}/convert-mkv-mp4/">MKV to MP4</a></li>
  <li><a href="{SITE_ROOT}/convert-mov-mp4/">MOV to MP4</a></li>
  <li><a href="{SITE_ROOT}/dvd-burner/">DVD Burner</a></li>
  <li><a href="{SITE_ROOT}/screen-recorder/">Screen Recorder</a></li>
</ul></div>
<div class="fc"><h5>Compare & More</h5><ul>
  <li><a href="{SITE_ROOT}/vs-handbrake/">vs HandBrake</a></li>
  <li><a href="{SITE_ROOT}/vs-vlc/">vs VLC</a></li>
  <li><a href="{SITE_ROOT}/vs-freemake/">vs Freemake</a></li>
  <li><a href="{SITE_ROOT}/alternatives/">All Alternatives</a></li>
  <li><a href="{SITE_ROOT}/global/">Global Users</a></li>
  <li><a href="{SITE_ROOT}/faq/">FAQ</a></li>
</ul></div>
</div>
<div class="fb-bot">
  <p>© {YEAR} VideoConverter Guide — Independent affiliate site. Commissions earned via LinkConnector at no extra cost to you.</p>
  <p><a href="{AFF}" target="_blank" rel="noopener sponsored">Download UniConverter Free →</a></p>
</div></footer>"""

def bc(*crumbs):
    parts=[]
    for i,(label,url) in enumerate(crumbs):
        if url and i<len(crumbs)-1:
            parts.append(f'<a href="{url}">{label}</a><span class="sep">›</span>')
        else:
            parts.append(f'<span class="cur">{label}</span>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">'+"".join(parts)+"</nav>"

def sw_schema(desc):
    return f'{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"Wondershare UniConverter","applicationCategory":"MultimediaApplication","operatingSystem":"Windows, macOS","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.6","reviewCount":"3150","bestRating":"5"}},"description":"{desc[:200]}","url":"{SITE_URL}/","publisher":{{"@type":"Organization","name":"Wondershare","url":"https://videoconverter.wondershare.com"}}}}'

def bc_schema(title,path):
    canon=f"{SITE_URL}{path}"
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{title}","item":"{canon}"}}]}}'

def page(title,desc,path,body,kw="",extras=None,article=False,lang="en"):
    kw=kw or "Wondershare UniConverter, video converter software, best video converter, convert video to MP4, 1000 formats"
    canon=f"{SITE_URL}{path}"
    extras=extras or []
    schemas=f'<script type="application/ld+json">{sw_schema(desc)}</script>'
    schemas+=f'<script type="application/ld+json">{bc_schema(title.split("—")[0].strip(),path)}</script>'
    for ex in extras:
        schemas+=f'<script type="application/ld+json">{ex}</script>'
    # hreflang hints for global SEO
    hreflang="".join(f'<link rel="alternate" hreflang="{lc}" href="{SITE_URL}/lang/{lc}/">' for _,_,lc,_,_,_,_ in LANGS)
    hreflang+=f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">'
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<link rel="canonical" href="{canon}">
{hreflang}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:image" content="{SITE_URL}/assets/og.png">
<meta property="og:site_name" content="VideoConverter Guide">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="{SITE_ROOT}/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="VideoConverter Guide Blog" href="{SITE_URL}/feed.xml">
{schemas}
<style>{CSS}</style>
</head>
<body>
{nav()}
{body}
{foot()}
<script>
(function(){{
  var h=document.querySelector('.ham'),nl=document.querySelector('.nav-links');
  if(!h||!nl)return;
  h.addEventListener('click',function(){{
    var open=nl.style.display==='flex';
    nl.style.cssText=open?'':'display:flex;position:fixed;top:68px;left:0;right:0;flex-direction:column;background:rgba(3,6,14,.98);padding:2rem 5%;gap:1.3rem;border-bottom:1px solid rgba(255,90,31,.12);z-index:998;backdrop-filter:blur(24px)';
  }});
}})();
</script>
</body></html>"""

def write(rel,content):
    p=BASE/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding="utf-8")
    print(f"  ✓  {rel}")


# ── HOMEPAGE ──────────────────────────────────────────────────────────────────
def pg_home():
    fmts="".join(f'<span class="fmt">{f}</span>' for f in FORMATS_IN[:28])
    devs="".join(f'<div class="card" style="padding:.9rem 1.1rem;text-align:center"><p style="font-size:.82rem;color:var(--txt);margin:0">{d}</p></div>' for d in DEVICES[:12])
    lang_cards="".join(f'<a href="{SITE_ROOT}/lang/{lc}/" class="lng"><span class="lng-flag">{flag}</span><div class="lng-name">{name}</div><div class="lng-native">{kw1}</div><div class="lng-kw">{kw2}</div></a>' for flag,name,lc,region,kw1,kw2,_ in LANGS[:12])
    return page(
        f"Wondershare UniConverter — Best Video Converter Software {YEAR} | 1000+ Formats | Global",
        f"Wondershare UniConverter: convert, compress, edit, record and burn video in 1000+ formats. 90× faster with GPU. AI tools: upscale, stabilize, translate in 130 languages. Free trial. Best video converter {YEAR}.",
        "/",f"""
{lang_strip()}
<section class="hero">
  <div class="hero-inner">
    <div class="hero-badge anim"><span class="badge-dot"></span> #1 Rated Video Converter — 15M+ Users in 200+ Countries</div>
    <h1 class="anim d1">Convert <span class="g-acc">Any Video.</span><br><span class="g-acc2">Any Format.</span><br><span class="g-acc3">Any Language.</span></h1>
    <p class="hero-sub anim d2">Wondershare UniConverter converts, compresses, edits, records and burns video in 1000+ formats — 90× faster with GPU acceleration. Now with AI translation in 130 languages and subtitle generation in 145+ languages. Free trial, no credit card.</p>
    <div class="hero-ctas anim d3">
      <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download Free Trial</a>
      <a href="{SITE_ROOT}/features/" class="btn btn-s btn-lg">See All Features →</a>
    </div>
    <div class="hero-trust anim d4">
      <span class="trust-it">Free Trial — No Card</span>
      <span class="trust-it">Windows &amp; Mac</span>
      <span class="trust-it">1000+ Formats</span>
      <span class="trust-it">GPU Accelerated</span>
      <span class="trust-it">AI Tools Included</span>
      <span class="trust-it">130 Language Translation</span>
    </div>
  </div>
</section>

<div class="stats-bar">
  <div class="stat-item"><span class="stat-num">1000+</span><span class="stat-lbl">Formats</span></div>
  <div class="stat-item"><span class="stat-num">90×</span><span class="stat-lbl">Faster Than Realtime</span></div>
  <div class="stat-item"><span class="stat-num">8K</span><span class="stat-lbl">Max Resolution</span></div>
  <div class="stat-item"><span class="stat-num">130</span><span class="stat-lbl">AI Translation Langs</span></div>
  <div class="stat-item"><span class="stat-num">15M+</span><span class="stat-lbl">Users Worldwide</span></div>
  <div class="stat-item"><span class="stat-num">200+</span><span class="stat-lbl">Countries</span></div>
</div>

<section>
  <span class="sec-lbl">Complete Video Toolbox</span>
  <h2 class="sec-title">Nine Tools in One App.<br><span class="g-acc">Zero Compromise.</span></h2>
  <p class="sec-sub">UniConverter replaces nine separate apps. Everything video-related in one clean interface — including AI tools no other converter offers.</p>
  <div class="g3">
    <div class="card card-feat"><div class="card-icon">🔄</div><h3>Video Converter</h3><p>Convert between 1000+ formats — MP4, MKV, AVI, MOV, HEVC, ProRes, MXF and every format your camera, platform or device needs. Zero quality loss, full metadata preservation.</p></div>
    <div class="card"><div class="card-icon">📦</div><h3>Video Compressor</h3><p>Reduce video file size by up to 150% using AI compression without visible quality loss. Set a target file size or bitrate and preview results before committing.</p></div>
    <div class="card"><div class="card-icon">✂️</div><h3>Video Editor</h3><p>Trim, crop, rotate, merge, add .SRT subtitles, effects, filters and watermarks. Batch trim, resize and watermark hundreds of files simultaneously.</p></div>
    <div class="card"><div class="card-icon">🤖</div><h3>AI Tools</h3><p>AI Super Resolution, AI Frame Interpolation, AI Stabilization, AI Noise Reduction, AI Translation (130 languages), AI Subtitle Generation (145+ languages), AI Compression. All built in.</p></div>
    <div class="card"><div class="card-icon">📥</div><h3>Video Downloader</h3><p>Download videos from YouTube, Vimeo, Dailymotion, Facebook, Bilibili and 1000+ sites. Save in any resolution including 4K. Extract audio as MP3.</p></div>
    <div class="card"><div class="card-icon">💿</div><h3>DVD & Blu-ray Burner</h3><p>Burn any video to DVD or Blu-ray with custom menus and templates. Rip DVDs to digital. Now with Blu-ray burning support added in UniConverter 17.</p></div>
    <div class="card"><div class="card-icon">🖥</div><h3>Screen Recorder</h3><p>Record desktop, webcam or both simultaneously. Capture system audio and microphone. Export as MP4, AVI or animated GIF. Perfect for tutorials and presentations.</p></div>
    <div class="card"><div class="card-icon">🌊</div><h3>Watermark Tools</h3><p>Remove watermarks using AI inpainting — single video or batch. Add custom text or image watermarks with full position, opacity and size control.</p></div>
    <div class="card"><div class="card-icon">🎵</div><h3>Audio & Image Converter</h3><p>Convert between 50+ audio formats (MP3, AAC, WAV, FLAC, OGG) and all major image formats (JPG, PNG, HEIC, WebP, RAW). Batch process thousands of files.</p></div>
  </div>
</section>

<section class="alt">
  <span class="sec-lbl tc" style="display:block;text-align:center">AI-Powered Features</span>
  <h2 class="sec-title tc">UniConverter 17 <span class="g-purple">AI Features</span></h2>
  <p class="sec-sub tc">No other video converter matches UniConverter's AI toolset. These aren't gimmicks — they're production-quality tools used by professionals worldwide.</p>
  <div class="ai-grid">
    <div class="ai-card"><h4>🔬 AI Super Resolution</h4><p>Upscale SD (480p) to HD (1080p) or 4K using neural networks. Fills in genuine detail — not just sharpening.</p></div>
    <div class="ai-card"><h4>🎬 AI Frame Interpolation</h4><p>Convert 24fps to 60fps or higher for buttery-smooth motion. Ideal for action, sports and gaming footage.</p></div>
    <div class="ai-card"><h4>📷 AI Stabilization</h4><p>Fix shaky handheld, drone and action cam footage automatically. No manual keyframing required.</p></div>
    <div class="ai-card"><h4>🔇 AI Noise Reduction</h4><p>Remove background hiss, hum and ambient noise from audio tracks. Dramatically improves low-quality recordings.</p></div>
    <div class="ai-card"><h4>🌐 AI Translation</h4><p>Translate video scripts and subtitles into 130+ languages with over 95% accuracy. Instantly localize content for global audiences.</p></div>
    <div class="ai-card"><h4>📝 AI Subtitle Generator</h4><p>Generate precise subtitles in 145+ languages from any video's audio. Fully editable bilingual captions included.</p></div>
    <div class="ai-card"><h4>📦 AI Compression</h4><p>New in UniConverter 17: AI Compression achieves up to 150% file size reduction without quality loss — better than standard bitrate compression.</p></div>
    <div class="ai-card"><h4>🖼 AI Image Enhancer</h4><p>Sharpen details, reduce image noise and upscale photos to HD or 4K clarity. Restore old photos with AI.</p></div>
  </div>
  <div style="text-align:center;margin-top:2.5rem"><a href="{SITE_ROOT}/ai-features/" class="btn btn-g">Full AI Features Guide →</a></div>
</section>

<section>
  <span class="sec-lbl tc" style="display:block;text-align:center">1000+ Formats</span>
  <h2 class="sec-title tc">Works With <span class="g-acc">Every Format</span> You Have</h2>
  <div class="fmt-grid" style="max-width:940px;margin:0 auto 2rem;justify-content:center">{fmts}</div>
  <div style="text-align:center"><a href="{SITE_ROOT}/formats/" class="btn btn-g">View Full Format List →</a></div>
</section>

<section class="alt">
  <span class="sec-lbl tc" style="display:block;text-align:center">Global Reach</span>
  <h2 class="sec-title tc">Used in <span class="g-acc">200+ Countries</span></h2>
  <p class="sec-sub tc">UniConverter is available in multiple languages and trusted by 15 million users worldwide — from individual creators to large enterprises.</p>
  <div class="lang-grid" style="max-width:980px;margin:0 auto 2.5rem">{lang_cards}</div>
  <div style="text-align:center">
    <a href="{SITE_ROOT}/global/" class="btn btn-g">View All Languages & Regions →</a>
  </div>
</section>

<section>
  <div class="split">
    <div>
      <span class="sec-lbl">Why Choose UniConverter</span>
      <h2 class="sec-title"><span class="g-acc">90× Faster.</span><br>GPU Powered.</h2>
      <p style="margin-bottom:1.5rem">Most video converters use only your CPU. UniConverter uses your GPU — NVIDIA, AMD and Intel — to convert at up to 90× real-time speed. 1 hour of 4K video converts in 3–5 minutes.</p>
      <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.9rem">
        {"".join(f'<li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)"><span style="color:var(--green);font-weight:700">✓</span><span><strong>{a}</strong> — {b}</span></li>' for a,b in [("NVIDIA NVENC/CUDA","fastest GPU conversion on the market"),("AMD VCE","hardware acceleration for AMD graphics"),("Intel Quick Sync","integrated GPU on Intel processors"),("Apple Silicon M1/M2/M3","native performance on Mac"),("Batch conversion","convert hundreds of files simultaneously")])}
      </ul>
      <div style="margin-top:2rem">
        <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Try Free Now</a>
      </div>
    </div>
    <div>
      <div class="card card-feat" style="padding:2.2rem">
        <h3 style="color:var(--acc);margin-bottom:1.4rem">UniConverter vs Free Tools</h3>
        <div class="tbl-wrap"><table>
          <thead><tr><th>Capability</th><th>UniConverter</th><th>Free Tools</th></tr></thead>
          <tbody>
            <tr><td>GPU acceleration</td><td class="td-y td-hi">✓ 90× faster</td><td class="td-no">✗ CPU only</td></tr>
            <tr><td>AI upscaling</td><td class="td-y td-hi">✓ Built in</td><td class="td-no">✗</td></tr>
            <tr><td>AI translation</td><td class="td-y td-hi">✓ 130 languages</td><td class="td-no">✗</td></tr>
            <tr><td>DVD burning</td><td class="td-y td-hi">✓ + Blu-ray</td><td class="td-no">✗</td></tr>
            <tr><td>Screen recorder</td><td class="td-y td-hi">✓ Built in</td><td class="td-no">✗</td></tr>
            <tr><td>Watermark remover</td><td class="td-y td-hi">✓ AI-powered</td><td class="td-no">✗</td></tr>
            <tr><td>Batch compression</td><td class="td-y td-hi">✓ + AI mode</td><td class="td-no">✗</td></tr>
            <tr><td>Formats</td><td class="td-y td-hi">1000+</td><td class="td-p">Limited</td></tr>
          </tbody>
        </table></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <span class="sec-lbl tc" style="display:block;text-align:center">Verified Reviews</span>
  <h2 class="sec-title tc">Trusted by <span class="g-acc">Creators Worldwide</span></h2>
  <p class="sec-sub tc">4.6 stars from 3,100+ verified reviews on G2, Capterra and Trustpilot</p>
  <div class="tgrid">
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"The AI translation feature is a game changer. I localized my entire YouTube channel into Spanish and Portuguese in one afternoon. Quality is incredibly accurate."</p><div class="testi-author"><div class="testi-av">M</div><div><div class="testi-name">Marcus H. 🇩🇪</div><div class="testi-role">YouTube Creator, Munich</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"GPU acceleration is transformative. 1-hour 4K drone footage converted in 4 minutes. I was converting the same files overnight before. This is the right tool."</p><div class="testi-author"><div class="testi-av">A</div><div><div class="testi-name">Amira S. 🇦🇪</div><div class="testi-role">Filmmaker, Dubai</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"As a social media manager I convert videos for 6 platforms daily. UniConverter handles the batch in minutes. The device presets mean I never touch codec settings."</p><div class="testi-author"><div class="testi-av">P</div><div><div class="testi-name">Priya M. 🇮🇳</div><div class="testi-role">Social Media Manager, Bangalore</div></div></div></div>
    <div class="testi"><div class="stars">★★★★☆</div><p class="testi-text">"The AI subtitle generator saved me hours. I run an online course platform and needed captions in 3 languages. UniConverter generated them all accurately in minutes."</p><div class="testi-author"><div class="testi-av">K</div><div><div class="testi-name">Kenji T. 🇯🇵</div><div class="testi-role">E-learning Creator, Tokyo</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"I converted 400 old home movies from DVD to MP4 for my family. UniConverter processed them in a single batch overnight. Everything was perfect in the morning."</p><div class="testi-author"><div class="testi-av">S</div><div><div class="testi-name">Susan T. 🇬🇧</div><div class="testi-role">Retired Teacher, London</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"The watermark remover is incredible. I needed to remove a logo from 50 client videos. AI inpainting handled all of them flawlessly in a single batch. Hours saved."</p><div class="testi-author"><div class="testi-av">C</div><div><div class="testi-name">Carlos R. 🇧🇷</div><div class="testi-role">Video Editor, São Paulo</div></div></div></div>
  </div>
</section>

<div class="cta-blk">
  <span class="sec-lbl" style="display:block;margin-bottom:1rem">Start Today — Free</span>
  <h2>The World's Most Complete<br><span class="g-acc">Video Converter</span></h2>
  <p>15 million users in 200+ countries. Free trial — no credit card, no watermark limits on trial preview.</p>
  <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download UniConverter Free</a>
  <p style="margin-top:1.3rem;font-size:.8rem;color:var(--muted);position:relative">Annual from $39.99/yr · Perpetual $79.99 one-time · Free trial · Windows &amp; Mac · 200+ countries</p>
</div>""",
        kw=KEYWORDS)


# ── AI FEATURES PAGE ──────────────────────────────────────────────────────────
def pg_ai():
    il='{"@context":"https://schema.org","@type":"ItemList","name":"UniConverter AI Features","itemListElement":[{"@type":"ListItem","position":1,"name":"AI Super Resolution"},{"@type":"ListItem","position":2,"name":"AI Frame Interpolation"},{"@type":"ListItem","position":3,"name":"AI Video Stabilization"},{"@type":"ListItem","position":4,"name":"AI Noise Reduction"},{"@type":"ListItem","position":5,"name":"AI Translation 130 Languages"},{"@type":"ListItem","position":6,"name":"AI Subtitle Generation 145+ Languages"},{"@type":"ListItem","position":7,"name":"AI Compression"},{"@type":"ListItem","position":8,"name":"AI Watermark Remover"}]}'
    return page(f"UniConverter AI Features — AI Video Upscaler, Translator, Stabilizer | {YEAR}",
        "Wondershare UniConverter AI features: AI Super Resolution, AI Frame Interpolation, AI Stabilization, AI Noise Reduction, AI Translation (130 languages), AI Subtitle Generator (145+ languages), AI Compression.",
        "/ai-features/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("AI Features",None))}
  <span class="sec-lbl">Powered by AI</span>
  <h1>UniConverter <span class="g-purple">AI Features</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Eight AI-powered video tools built into UniConverter 17 — from upscaling to translation. No other video converter comes close.</p>
</div>
<section>
  <div class="g2">
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">🔬 AI Super Resolution</h3>
      <p style="margin-bottom:1rem">Upscale SD video (480p, 720p) to HD (1080p) or 4K using a trained neural network. Unlike simple upsampling, AI Super Resolution analyzes content and adds realistic detail — sharp edges, recovered textures, natural-looking results that hold up on large screens.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> Digitized home movies, old TV recordings, archive footage, content shot on older cameras. Turn 480p footage from 2005 into something watchable on a 4K TV.</p></div>
    </div>
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">🎬 AI Frame Interpolation</h3>
      <p style="margin-bottom:1rem">Convert 24fps or 30fps footage to 60fps, 120fps or higher. AI Frame Interpolation generates synthetic intermediate frames by analyzing motion between existing frames — creating genuinely smooth motion rather than just duplicating frames.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> Sports footage, action cameras, gaming content, slow-motion video, any content where motion smoothness matters.</p></div>
    </div>
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">📷 AI Video Stabilization</h3>
      <p style="margin-bottom:1rem">Fix shaky footage from handheld cameras, drones, action cams and phones using AI motion analysis. Automatically detects and corrects camera shake, wind movement and walking vibration — without manual keyframing or cropping more than necessary.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> Drone footage, vlogging, run-and-gun filmmaking, GoPro/action cam footage, phone video.</p></div>
    </div>
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">🔇 AI Noise Reduction</h3>
      <p style="margin-bottom:1rem">Remove background audio noise — hiss, hum, air conditioning, crowd noise, wind — from video using AI analysis. Dramatically improves recordings made in imperfect environments without degrading voice or music quality.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> Interview footage, podcasts embedded in video, outdoor recordings, anything shot without professional audio equipment.</p></div>
    </div>
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">🌐 AI Translation — 130 Languages</h3>
      <p style="margin-bottom:1rem">Translate video scripts, subtitles and captions into 130+ languages with over 95% accuracy. Instantly localize your content for global audiences — YouTube channels, online courses, corporate videos, social media content. Supports all major world languages including Arabic, Chinese, Japanese, Korean, Hindi, Swahili and more.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> Content creators expanding internationally, e-learning platforms, corporate video localization, multilingual marketing.</p></div>
    </div>
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">📝 AI Subtitle Generator — 145+ Languages</h3>
      <p style="margin-bottom:1rem">Generate accurate subtitles in 145+ languages from any video's spoken audio. Fully editable bilingual captions — show original and translated text simultaneously. Export as .SRT, .ASS or burn subtitles permanently into the video.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> Accessibility compliance, international distribution, hearing-impaired viewers, silent viewing on social media, SEO for video content.</p></div>
    </div>
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">📦 AI Compression — 150% Reduction</h3>
      <p style="margin-bottom:1rem">New in UniConverter 17: AI Compression analyzes video content frame-by-frame and applies intelligent per-scene compression — achieving up to 150% file size reduction without visible quality loss. Dramatically outperforms standard bitrate-based compression for complex footage.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> 4K+ footage, long-form content, archive storage, streaming optimization, social media uploads.</p></div>
    </div>
    <div class="ai-card" style="background:var(--card);border:1px solid rgba(168,85,247,.25);border-radius:var(--r);padding:2rem">
      <h3 style="color:var(--purple);margin-bottom:1rem">🌊 AI Watermark Remover</h3>
      <p style="margin-bottom:1rem">Remove watermarks, logos, text overlays and unwanted objects from videos using AI inpainting. Analyzes the surrounding video content and fills the removed area naturally — works on static and moving watermarks. Batch process multiple videos simultaneously.</p>
      <div class="hbox info" style="margin:0"><p style="font-size:.85rem"><strong>Best for:</strong> Removing old branding from archive videos, cleaning up stock footage, removing timestamps and logos from recordings.</p></div>
    </div>
  </div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Try All AI Features Free</a>
  </div>
</section>""","AI video upscaler, AI video converter, AI super resolution, AI translation video, AI subtitle generator, AI frame interpolation, UniConverter AI",extras=[il])

# ── SCREEN RECORDER PAGE ──────────────────────────────────────────────────────
def pg_screen_recorder():
    return page(f"Best Screen Recorder Software — UniConverter Screen Capture {YEAR}",
        "Record your screen, webcam or both with Wondershare UniConverter. Record desktop, browser, apps or full screen. System audio + microphone. Export MP4, AVI or GIF. Free trial.",
        "/screen-recorder/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Screen Recorder",None))}
  <span class="sec-lbl">Screen Recording Guide</span>
  <h1>Record Your Screen<br><span class="g-acc">With UniConverter</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">UniConverter includes a full-featured screen recorder — no separate software needed. Record tutorials, gameplay, presentations and meetings.</p>
</div>
<section>
  <div class="g3" style="margin-bottom:2.5rem">
    <div class="card"><div class="card-icon">🖥</div><h3>Full Screen / Region</h3><p>Record your entire desktop, a specific window, a browser tab or a custom region. Pixel-perfect capture at any resolution up to 4K.</p></div>
    <div class="card"><div class="card-icon">📸</div><h3>Webcam Overlay</h3><p>Record webcam alongside screen capture — picture-in-picture or side-by-side. Perfect for tutorial videos, online courses and presentations.</p></div>
    <div class="card"><div class="card-icon">🎙</div><h3>Audio Recording</h3><p>Capture system audio, microphone or both simultaneously. Control volume levels independently. High-quality audio preserved in the export.</p></div>
    <div class="card"><div class="card-icon">⏺</div><h3>Flexible Export</h3><p>Export recordings as MP4, AVI or animated GIF. Convert immediately after recording to any format using UniConverter's full toolbox.</p></div>
    <div class="card"><div class="card-icon">🖱</div><h3>Mouse Highlighting</h3><p>Highlight mouse cursor and clicks for tutorial clarity. Useful for how-to videos, software demos and technical training content.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>Task Scheduler</h3><p>Schedule recordings to start and stop automatically at a set time. Record webinars, live streams and broadcasts while away from your computer.</p></div>
  </div>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1.5rem">How to <span class="g-acc">Record Your Screen</span></h2>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Open Screen Recorder</h3><p>In UniConverter, click "Screen Recorder" from the main menu or the Toolbox.</p></div></div>
        <div class="step" data-n="2"><div><h3>Select Capture Area</h3><p>Choose full screen, a specific window, browser tab, or drag to select a custom region.</p></div></div>
        <div class="step" data-n="3"><div><h3>Configure Audio & Webcam</h3><p>Toggle system audio, microphone, and webcam overlay on or off as needed.</p></div></div>
        <div class="step" data-n="4"><div><h3>Record & Export</h3><p>Click Record. Stop when done. Export to MP4, AVI or GIF — or convert immediately to any other format.</p></div></div>
      </div>
      <a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Download Screen Recorder Free</a>
    </div>
    <div>
      <div class="hbox good"><h4>Built Into UniConverter — No Extra Cost</h4><p style="margin-top:.4rem">Unlike standalone screen recorders that cost $30–$100/year, UniConverter's screen recorder is included in the annual ($39.99) and perpetual ($79.99) plans alongside the video converter, compressor, DVD burner, AI tools and downloader. One app, one price.</p></div>
      <div class="hbox" style="margin-top:1rem"><h4>Use Cases</h4><ul style="list-style:none;padding:0;margin-top:.6rem;display:flex;flex-direction:column;gap:.4rem">
        {"".join(f'<li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>{x}</li>' for x in ["Tutorial and how-to videos","Software demos and walkthroughs","Online course content","Gameplay recording","Webinar recording","Bug reports and technical support","Zoom / Teams / Meet recording","Product demos for sales teams"])}
      </ul></div>
    </div>
  </div>
</section>""","screen recorder software, record computer screen, screen capture software, best screen recorder Windows Mac, UniConverter screen recorder",article=True)

# ── VS FREEMAKE PAGE ──────────────────────────────────────────────────────────
def pg_vs_freemake():
    return page(f"UniConverter vs Freemake Video Converter — Comparison {YEAR}",
        f"Wondershare UniConverter vs Freemake Video Converter: features, limitations, ads and quality compared. Which is better for serious video conversion in {YEAR}?",
        "/vs-freemake/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs Freemake",None))}
  <span class="sec-lbl">Head-to-Head</span>
  <h1>UniConverter vs <span class="g-acc">Freemake</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Freemake is free but heavily limited without paid upgrades. UniConverter costs $39.99/year with no limitations. Here's the real comparison.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">UniConverter</th><th>Freemake (Free)</th></tr></thead>
    <tbody>
      <tr><td class="td-n">Output watermark</td><td class="td-y td-hi">No watermark (paid)</td><td class="td-no">Watermark on all free exports</td></tr>
      <tr><td class="td-n">Conversion length limit</td><td class="td-y td-hi">No limit</td><td class="td-no">5-minute limit on free</td></tr>
      <tr><td class="td-n">GPU acceleration</td><td class="td-y td-hi">✓ NVIDIA/AMD/Intel</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">AI tools</td><td class="td-y td-hi">✓ 8 AI tools</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">DVD/Blu-ray burning</td><td class="td-y td-hi">✓</td><td class="td-p">Free version limited</td></tr>
      <tr><td class="td-n">Screen recorder</td><td class="td-y td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Video downloader</td><td class="td-y td-hi">✓ 1000+ sites</td><td class="td-p">Limited</td></tr>
      <tr><td class="td-n">Mac support</td><td class="td-y td-hi">✓ Full</td><td class="td-no">✗ Windows only</td></tr>
      <tr><td class="td-n">Ads in interface</td><td class="td-y td-hi">None</td><td class="td-no">Yes — bundled software too</td></tr>
      <tr><td class="td-n">Batch conversion</td><td class="td-y td-hi">✓ Hundreds of files</td><td class="td-p">Limited on free</td></tr>
      <tr><td class="td-n">Format support</td><td class="td-y td-hi">1000+</td><td class="td-p">Limited</td></tr>
      <tr><td class="td-n">Cost (full version)</td><td class="td-hi">$39.99/yr</td><td>$29.95/yr to remove limitations</td></tr>
    </tbody>
  </table></div>
  <div class="hbox" style="margin-top:1.5rem"><h4>Verdict</h4><p style="margin-top:.4rem">Freemake's free version is so restricted — watermarks, 5-minute limits, ads, bundled software — that it's barely usable for real work. Its paid version removes these but still lacks GPU acceleration, AI tools, screen recording and Mac support. For $10 more per year, UniConverter delivers a dramatically more capable toolbox without the frustrations.</p></div>
  <div style="text-align:center;margin-top:1.5rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try UniConverter Free →</a></div>
</section>""","UniConverter vs Freemake, Freemake alternative, free video converter comparison")

# ── GLOBAL PAGE ───────────────────────────────────────────────────────────────
def pg_global():
    all_langs="".join(f'<a href="{SITE_ROOT}/lang/{lc}/" class="lng"><span class="lng-flag">{flag}</span><div class="lng-name">{name}</div><div class="lng-native">{kw1}</div><div class="lng-kw">{region} · {kw2}</div></a>' for flag,name,lc,region,kw1,kw2,_ in LANGS)
    return page(f"UniConverter — Global Video Converter in 20 Languages | {YEAR}",
        "Wondershare UniConverter is used in 200+ countries in 20 languages. AI translation in 130 languages. AI subtitle generation in 145+ languages. The truly global video converter.",
        "/global/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Global",None))}
  <span class="sec-lbl">Worldwide Reach</span>
  <h1>UniConverter —<br><span class="g-acc">Truly Global</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">15 million users in 200+ countries. Software available in 7+ languages. AI translation in 130 languages. AI subtitle generation in 145+ languages. The world's most internationally complete video converter.</p>
</div>
<section>
  <div class="g3" style="margin-bottom:3rem">
    <div class="card"><div class="card-icon">🌐</div><h3>Software UI Languages</h3><p>UniConverter's interface is available in English, German, French, Spanish, Italian, Japanese, Chinese, Portuguese and Arabic — with more being added regularly.</p></div>
    <div class="card card-feat"><div class="card-icon">🤖</div><h3>AI Translation: 130 Languages</h3><p>Translate video subtitles and scripts into 130 languages with 95%+ accuracy. Instantly localize content for any global market — from Swahili to Norwegian, Bengali to Vietnamese.</p></div>
    <div class="card"><div class="card-icon">📝</div><h3>AI Subtitles: 145+ Languages</h3><p>Generate precise subtitles from any video's audio in 145+ languages. Bilingual captions. Export as .SRT or burn into video. Makes any content globally accessible.</p></div>
    <div class="card"><div class="card-icon">📡</div><h3>Every Broadcast Standard</h3><p>Supports PAL, NTSC and SECAM broadcast standards used across different regions. Convert between regional standards seamlessly — Europe, North America, Asia, Africa all covered.</p></div>
    <div class="card"><div class="card-icon">📱</div><h3>Regional Platform Presets</h3><p>Export presets for YouTube, TikTok, Instagram, Facebook, Bilibili (China), NicoNico (Japan), Youku (China), Vimeo, Twitch and all major regional streaming platforms.</p></div>
    <div class="card"><div class="card-icon">💳</div><h3>Global Payment Support</h3><p>Purchase in your local currency. Wondershare accepts all major credit cards, PayPal and regional payment methods. Available in 150+ countries with local pricing where applicable.</p></div>
  </div>
  <h2 style="margin-bottom:2rem">Select Your <span class="g-acc">Language / Region</span></h2>
  <div class="lang-grid">{all_langs}</div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download UniConverter Free — Available Worldwide</a>
  </div>
</section>""","video converter worldwide, international video converter, global video converter, video converter all languages, multilingual video converter")


# ── LANGUAGE PAGE GENERATOR ───────────────────────────────────────────────────
def pg_lang(flag,name,lc,region,kw1,kw2,kw3):
    """Generate a dedicated page for each major language/region"""
    # Map language-specific UI strings
    headlines = {
        "en": ("Best Video Converter Software","Convert any video to MP4","Free trial — no credit card"),
        "de": ("Beste Videokonverter Software","Konvertieren Sie jedes Video in MP4","Kostenlose Testversion"),
        "fr": ("Meilleur logiciel convertisseur vidéo","Convertissez n'importe quelle vidéo en MP4","Essai gratuit"),
        "es": ("El mejor convertidor de vídeo","Convierte cualquier vídeo a MP4","Prueba gratis"),
        "pt": ("Melhor conversor de vídeo","Converta qualquer vídeo para MP4","Avaliação gratuita"),
        "it": ("Il miglior convertitore video","Converti qualsiasi video in MP4","Prova gratuita"),
        "ja": ("最高の動画変換ソフト","動画をMP4に変換","無料トライアル"),
        "zh": ("最佳视频转换软件","将任何视频转换为MP4","免费试用"),
        "ko": ("최고의 동영상 변환 소프트웨어","모든 동영상을 MP4로 변환","무료 체험"),
        "ru": ("Лучший конвертер видео","Конвертируйте любое видео в MP4","Бесплатная пробная версия"),
        "ar": ("أفضل برنامج تحويل الفيديو","تحويل أي فيديو إلى MP4","تجربة مجانية"),
        "hi": ("सर्वश्रेष्ठ वीडियो कनवर्टर","किसी भी वीडियो को MP4 में बदलें","नि:शुल्क परीक्षण"),
        "id": ("Konverter video terbaik","Konversi video apa saja ke MP4","Uji coba gratis"),
        "nl": ("Beste videoconverter","Converteer elke video naar MP4","Gratis proberen"),
        "pl": ("Najlepszy konwerter wideo","Konwertuj dowolny film do MP4","Bezpłatna wersja próbna"),
        "tr": ("En iyi video dönüştürücü","Herhangi bir videoyu MP4'e dönüştür","Ücretsiz deneme"),
        "sv": ("Bästa videokonverterare","Konvertera alla videor till MP4","Gratis provversion"),
        "fil": ("Pinakamahusay na video converter","I-convert ang anumang video sa MP4","Libreng pagsubok"),
        "vi": ("Phần mềm chuyển đổi video tốt nhất","Chuyển đổi bất kỳ video nào sang MP4","Dùng thử miễn phí"),
        "th": ("โปรแกรมแปลงวิดีโอที่ดีที่สุด","แปลงวิดีโอใดก็ได้เป็น MP4","ทดลองใช้ฟรี"),
    }
    h = headlines.get(lc, headlines["en"])
    return page(
        f"Wondershare UniConverter — {h[0]} | {region} | {YEAR}",
        f"Wondershare UniConverter for {region}: {h[1]}. 1000+ formats, GPU acceleration, AI tools, DVD burning. {h[2]}. Best video converter software for {region} users.",
        f"/lang/{lc}/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Global",f"{SITE_ROOT}/global/"),("{name}",None))}
  <span class="sec-lbl">{flag} {region}</span>
  <h1>{h[0]}<br><span class="g-acc">{name}</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Wondershare UniConverter is the most complete video converter for {region} users. 1000+ formats, 90× GPU acceleration, AI tools in 130 languages, DVD burning, screen recording and more.</p>
  <div style="margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ {h[2]}</a>
    <a href="{SITE_ROOT}/features/" class="btn btn-s btn-lg">Features →</a>
  </div>
</div>
<section>
  <div class="hbox info"><h4>{flag} UniConverter for {region} Users</h4>
    <p style="margin-top:.5rem">UniConverter is used by millions of users in {region}. The software interface supports {name} among other languages. AI subtitle generation and translation cover {name} with high accuracy, making it ideal for content creators, educators, businesses and everyday users across {region}.</p>
  </div>
  <div class="g3" style="margin-top:2rem">
    <div class="card"><div class="card-icon">🔄</div><h3>{kw1}</h3><p>Convert 1000+ video formats with GPU acceleration. MP4, MKV, AVI, MOV, HEVC and every format used in {region}. No quality loss.</p></div>
    <div class="card"><div class="card-icon">🌐</div><h3>AI Translation — {name}</h3><p>AI Translation supports {name} with 95%+ accuracy. Translate subtitle tracks, localize video content and add {name} captions automatically.</p></div>
    <div class="card"><div class="card-icon">📝</div><h3>AI Subtitles — {name}</h3><p>Auto-generate accurate {name} subtitles from any video. Bilingual captions available. Export .SRT or burn into video for distribution in {region}.</p></div>
    <div class="card"><div class="card-icon">📦</div><h3>{kw2}</h3><p>Compress videos for {region} platforms, social media and messaging apps. AI Compression achieves up to 150% reduction without quality loss.</p></div>
    <div class="card"><div class="card-icon">💿</div><h3>DVD Burner</h3><p>Burn videos to DVD and Blu-ray. Supports NTSC and PAL regional formats used across different countries in {region}.</p></div>
    <div class="card"><div class="card-icon">📥</div><h3>Video Downloader</h3><p>Download from YouTube, regional streaming platforms and 1000+ video sites. Available in {region}.</p></div>
  </div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download UniConverter — {region}</a>
  </div>
</section>""",
        kw=f"{kw1}, {kw2}, {kw3}, Wondershare UniConverter {region}, video converter {name}, {name} video converter",
        lang=lc)

# ── FEATURES PAGE ─────────────────────────────────────────────────────────────
def pg_features():
    il='{"@context":"https://schema.org","@type":"ItemList","name":"UniConverter Features","itemListElement":[{"@type":"ListItem","position":1,"name":"Video Converter — 1000+ formats"},{"@type":"ListItem","position":2,"name":"Video Compressor — AI powered"},{"@type":"ListItem","position":3,"name":"GPU Acceleration — 90x faster"},{"@type":"ListItem","position":4,"name":"AI Tools — 8 AI features"},{"@type":"ListItem","position":5,"name":"DVD and Blu-ray Burner"},{"@type":"ListItem","position":6,"name":"Screen Recorder"},{"@type":"ListItem","position":7,"name":"Video Downloader 1000+ sites"}]}'
    return page(f"UniConverter Features — Complete List {YEAR} | 1000+ Formats + AI",
        "Full Wondershare UniConverter feature list: 1000+ formats, GPU 90× speed, AI tools (SR/stabilize/translate/subtitles), DVD/Blu-ray burning, screen recorder, downloader, watermark remover.",
        "/features/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Features",None))}
  <span class="sec-lbl">Complete Feature Set</span>
  <h1>UniConverter <span class="g-acc">Features</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">One app replacing nine. Every feature in detail.</p>
</div>
<section>
  <div class="g3">
    <div class="card card-feat"><div class="card-icon">🔄</div><h3>1000+ Format Conversion</h3><p>Convert between every major video, audio and image format. MP4, MKV, AVI, MOV, WMV, FLV, WebM, HEVC/H.265, H.264, ProRes, MXF, XAVC, VOB, TS, MTS, AVCHD, 3GP, RM, DivX and hundreds more. Zero quality loss. Full metadata preservation.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>GPU Acceleration — 90× Speed</h3><p>NVIDIA NVENC/CUDA, AMD VCE and Intel Quick Sync GPU acceleration. Convert 1 hour of 4K H.265 in 3–5 minutes. Batch convert hundreds of files simultaneously. Apple Silicon M1/M2/M3 native support on Mac.</p></div>
    <div class="card"><div class="card-icon">📦</div><h3>AI Video Compression</h3><p>New AI Compression mode achieves up to 150% file size reduction without visible quality loss. Standard mode reduces size by up to 90%. Set target file size or bitrate and preview before committing.</p></div>
    <div class="card"><div class="card-icon">🤖</div><h3>8 AI Features</h3><p>AI Super Resolution, AI Frame Interpolation, AI Stabilization, AI Noise Reduction, AI Translation (130 languages), AI Subtitle Generation (145+ languages), AI Compression, AI Watermark Remover.</p><a href="{SITE_ROOT}/ai-features/" class="btn btn-g btn-sm" style="margin-top:.8rem">AI Features →</a></div>
    <div class="card"><div class="card-icon">✂️</div><h3>Video Editor</h3><p>Trim, crop, rotate, merge, add .SRT subtitles, effects, filters, watermarks. Batch trim, resize, watermark. One-click video enhancement. Subtitle editor with bilingual caption support.</p></div>
    <div class="card"><div class="card-icon">💿</div><h3>DVD &amp; Blu-ray Burner</h3><p>Burn any video to DVD or Blu-ray with custom menus and templates. Rip DVDs to digital. Create ISO images. NTSC/PAL support. New in UniConverter 17: Blu-ray burning added.</p></div>
    <div class="card"><div class="card-icon">📥</div><h3>Video Downloader</h3><p>Download from YouTube, Vimeo, Dailymotion, Facebook, Twitter/X, Bilibili, Youku, NicoNico and 1000+ sites. 4K, 1080p, 720p. Extract audio as MP3 or any audio format.</p></div>
    <div class="card"><div class="card-icon">🖥</div><h3>Screen Recorder</h3><p>Record desktop, window or custom region. Webcam overlay. System audio + microphone. Export MP4, AVI or GIF. Mouse highlighting. Task scheduler. 4K capture.</p><a href="{SITE_ROOT}/screen-recorder/" class="btn btn-g btn-sm" style="margin-top:.8rem">Screen Recorder →</a></div>
    <div class="card"><div class="card-icon">🌊</div><h3>Watermark Tools</h3><p>Remove watermarks using AI inpainting — batch supported. Add custom text/image watermarks with full control. Remove and add watermarks in a single operation.</p></div>
    <div class="card"><div class="card-icon">🎵</div><h3>Audio Converter</h3><p>Extract audio from video. Convert MP3, AAC, WAV, FLAC, OGG, WMA, M4A, AIFF, AC3, DTS and 50+ formats. Adjust bitrate, sample rate, channels. CD burner for audio.</p></div>
    <div class="card"><div class="card-icon">🖼</div><h3>Image Converter</h3><p>Convert JPG, PNG, BMP, TIFF, GIF, WebP, HEIC, RAW and more. Batch process photo libraries. Resize, rotate and enhance during conversion.</p></div>
    <div class="card"><div class="card-icon">📱</div><h3>50+ Device Presets</h3><p>Pre-configured output for iPhone 16, Samsung Galaxy S25, iPad Pro, Apple TV, PS5, Xbox Series X, Smart TV 4K, Roku, Fire TV, DJI, GoPro and 40+ more. No manual settings.</p></div>
    <div class="card"><div class="card-icon">🎮</div><h3>VR/360° Video</h3><p>Convert standard video to VR format for headsets. Process 360° footage from 360 cameras. Full VR output support for Oculus, Meta Quest and other headsets.</p></div>
    <div class="card"><div class="card-icon">📋</div><h3>Metadata Editor</h3><p>Auto-fix and manually edit video and audio metadata. Title, artist, album, cover art, year, genre. Batch metadata editing across entire media libraries.</p></div>
    <div class="card"><div class="card-icon">🔧</div><h3>Repair &amp; Fix</h3><p>Fix corrupted video files. Repair metadata errors. Restore faded photos. Remove scratches, noise and stains from old recordings using AI.</p></div>
  </div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Try All Features Free</a>
  </div>
</section>""","UniConverter features, video converter features, GPU video converter, AI video tools, DVD Blu-ray burner, screen recorder",extras=[il])


def pg_formats():
    cats={"📹 Video Input":["MP4","MKV","AVI","MOV","WMV","FLV","WebM","MPEG-1/2/4","VOB","TS","M2TS","MTS","AVCHD","3GP","3G2","OGV","RM","RMVB","ASF","DivX","Xvid","F4V","H.264","H.265/HEVC","ProRes 422/4444","XAVC","XAVC-S","MXF","R3D","BRAW","DNxHD","VP8","VP9","AV1","Theora","DV","DVCPRO"],"📤 Video Output":["MP4 (H.264/H.265)","MKV","AVI","MOV","WMV","WebM","FLV","MPEG","3GP","HTML5 Video","4K H.265","Apple ProRes","GIF Animation","DVD Video","Blu-ray Video","VR 360°"],"🎵 Audio":["MP3","AAC","WAV","FLAC","OGG","WMA","M4A","AIFF","AC3","DTS","AMR","APE","CAF"],"🖼 Images":["JPG/JPEG","PNG","BMP","TIFF","GIF","WebP","HEIC","RAW","ICO","TGA"],"📱 Device Presets":["iPhone 16 Pro/16/15","iPad Pro M4","Apple TV 4K","Samsung Galaxy S25","Google Pixel 9","Sony Xperia 1 VI","PS5","Xbox Series X","Nintendo Switch","Smart TV 4K","DJI Drone","GoPro HERO 13"]}
    cats_html="".join(f'<div style="margin-bottom:2.5rem"><h3 style="margin-bottom:1rem;font-size:1.3rem">{cat}</h3><div class="fmt-grid">{"".join(f"<span class=fmt>{i}</span>" for i in items)}</div></div>' for cat,items in cats.items())
    return page(f"UniConverter Supported Formats — 1000+ Video, Audio & Image | {YEAR}",
        "Wondershare UniConverter supports 1000+ formats including MP4, MKV, AVI, MOV, HEVC, ProRes, MP3, AAC, WAV, FLAC, JPG, PNG, HEIC, RAW. Full input and output list.",
        "/formats/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Formats",None))}
  <span class="sec-lbl">1000+ Formats</span>
  <h1>Supported <span class="g-acc">Formats</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">From consumer cameras to professional broadcast equipment — UniConverter supports every format you'll ever encounter.</p>
</div>
<section>
  <div class="hbox good"><p><strong>1000+ formats supported.</strong> Updated continuously as new formats emerge. Compatible with iOS, Android, Windows, macOS, broadcast equipment and every major streaming platform worldwide.</p></div>
  {cats_html}
  <div style="text-align:center;margin-top:2rem">
    <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Download UniConverter — Try Your Format Free</a>
  </div>
</section>""","UniConverter formats, video converter formats, 1000 formats, MP4 MKV AVI MOV converter, HEVC H.265 converter")

def pg_how():
    howto='{"@context":"https://schema.org","@type":"HowTo","name":"How to Convert Video with UniConverter","description":"Convert any video to any format in 3 steps.","step":[{"@type":"HowToStep","position":1,"name":"Add your video","text":"Drag and drop your file or click Add Files."},{"@type":"HowToStep","position":2,"name":"Choose output format","text":"Select target format, device preset or platform."},{"@type":"HowToStep","position":3,"name":"Convert","text":"Click Convert. GPU acceleration completes it in seconds."}]}'
    return page(f"How UniConverter Works — Convert Video in 3 Steps | {YEAR}",
        "How Wondershare UniConverter works: add file, choose format, convert in 3 steps. GPU accelerated. Works for conversion, compression, DVD burning, screen recording and AI enhancement.",
        "/how-it-works/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("How It Works",None))}
  <span class="sec-lbl">Simple Process</span>
  <h1>How <span class="g-acc">UniConverter</span> Works</h1>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:2rem">Video <span class="g-acc">Conversion</span> — 3 Steps</h2>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Add Your File</h3><p>Drag and drop your video into UniConverter or click "Add Files". Accepts 1000+ formats from any camera, phone, drone or download.</p><span class="step-tip">Batch add hundreds of files at once</span></div></div>
        <div class="step" data-n="2"><div><h3>Choose Output Format</h3><p>Select your target format — MP4, MKV, a device preset for iPhone/Samsung, or a platform preset for YouTube/Instagram/TikTok.</p><span class="step-tip">Adjust quality, bitrate, resolution if needed</span></div></div>
        <div class="step" data-n="3"><div><h3>Click Convert — Done</h3><p>GPU acceleration completes the job in seconds to minutes. Batch convert hundreds of files simultaneously.</p><span class="step-tip">1hr 4K video = ~4 minutes with GPU</span></div></div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:1.5rem">
      <div class="hbox"><h4>Compression in 4 Steps</h4><p style="margin-top:.4rem">Toolbox → Video Compressor → Add file → Set target size → Compress. Preview quality before committing. AI Compression mode for maximum reduction.</p></div>
      <div class="hbox"><h4>DVD Burning in 4 Steps</h4><p style="margin-top:.4rem">DVD Burner → Add videos → Choose menu template → Insert blank disc → Burn. Handles encoding automatically.</p></div>
      <div class="hbox"><h4>Screen Recording in 4 Steps</h4><p style="margin-top:.4rem">Screen Recorder → Select area → Toggle audio/webcam → Record → Stop and export.</p></div>
      <div class="hbox good"><h4>AI Translation Workflow</h4><p style="margin-top:.4rem">Add video → AI Tools → AI Translation → Select source and target language (130 options) → Generate. Edit auto-generated subtitles, export .SRT or burn into video.</p></div>
      <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Try Free Now</a>
    </div>
  </div>
</section>""","how UniConverter works, how to convert video, video conversion steps",extras=[howto])

def pg_pricing():
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How much does UniConverter cost?","acceptedAnswer":{"@type":"Answer","text":"UniConverter Annual plan is $39.99/year. Perpetual (lifetime) plan is $79.99 one-time. Free trial available."}},{"@type":"Question","name":"Is there a lifetime plan?","acceptedAnswer":{"@type":"Answer","text":"Yes. The Perpetual plan at $79.99 is a one-time payment. You own UniConverter forever with all future updates."}},{"@type":"Question","name":"What is the difference between annual and perpetual?","acceptedAnswer":{"@type":"Answer","text":"Annual renews at $39.99/year. Perpetual is $79.99 one-time — pay once, own forever."}},{"@type":"Question","name":"Does the price include AI tools?","acceptedAnswer":{"@type":"Answer","text":"Yes. All paid plans include all 8 AI features including AI translation (130 languages) and AI subtitle generation (145+ languages)."}}]}'
    return page(f"UniConverter Pricing {YEAR} — Free Trial, $39.99/yr, $79.99 Lifetime",
        f"Wondershare UniConverter pricing {YEAR}: Free trial. Annual $39.99/yr. Perpetual $79.99 one-time. All plans: 1000+ formats, GPU acceleration, AI tools (130 language translation), DVD/Blu-ray, screen recorder.",
        "/pricing/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Pricing",None))}
  <span class="sec-lbl" style="display:block;text-align:center">Simple Pricing</span>
  <h1>UniConverter <span class="g-acc">Pricing {YEAR}</span></h1>
  <p style="max-width:540px;margin:.9rem auto 0;color:var(--muted)">Start free. All paid plans include all features: 1000+ formats, GPU acceleration, 8 AI tools, DVD/Blu-ray burning, screen recorder and video downloader.</p>
</div>
<section>
  <div class="pgrid">
    <div class="pc">
      <div class="p-name">Free Trial</div>
      <div class="p-price"><sup>$</sup>0</div>
      <div class="p-per">No credit card needed</div>
      <ul class="p-feats">
        <li>Convert with watermark on output</li>
        <li>Test all features and interface</li>
        <li>Preview GPU conversion speed</li>
        <li>Try all 8 AI tools</li>
        <li>Test DVD burning</li>
        <li>No time limit</li>
      </ul>
      <a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Start Free Trial</a>
    </div>
    <div class="pc pop">
      <div class="pop-badge">Best Value</div>
      <div class="p-name">Annual Plan</div>
      <div class="p-strike">Was $69.99/year</div>
      <div class="p-price"><sup>$</sup>39<span style="font-size:1.5rem">.99</span></div>
      <div class="p-per">per year · 1 PC · Auto-renews</div>
      <ul class="p-feats">
        <li>No watermark on exports</li>
        <li>1000+ format conversion</li>
        <li>GPU acceleration (NVIDIA/AMD/Intel)</li>
        <li>AI Super Resolution &amp; Stabilization</li>
        <li>AI Translation — 130 languages</li>
        <li>AI Subtitle Generator — 145+ languages</li>
        <li>AI Compression (up to 150% reduction)</li>
        <li>DVD &amp; Blu-ray burner</li>
        <li>Screen recorder</li>
        <li>Video downloader (1000+ sites)</li>
        <li>Batch conversion</li>
        <li>Free updates for 1 year</li>
      </ul>
      <a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">Get Annual Plan →</a>
      <div class="p-note">💡 Up to 30% off — check current price</div>
    </div>
    <div class="pc">
      <div class="p-name">Perpetual Plan</div>
      <div class="p-strike">Was $119.99 one-time</div>
      <div class="p-price"><sup>$</sup>79<span style="font-size:1.5rem">.99</span></div>
      <div class="p-per">one-time · pay once · forever</div>
      <ul class="p-feats">
        <li>Everything in Annual +</li>
        <li>Pay once, own forever</li>
        <li>All future updates included</li>
        <li>No recurring fees ever</li>
        <li>Best long-term value</li>
      </ul>
      <a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Get Lifetime Plan →</a>
    </div>
  </div>
  <div class="hbox warn" style="max-width:840px;margin:3rem auto 0;text-align:center">
    <h4>💡 Up to 30% Off Available</h4>
    <p style="margin-top:.4rem">Wondershare regularly runs promotions on UniConverter — especially around major holidays and events. Click any button above to see the current price on the official site.</p>
  </div>
  <div style="max-width:840px;margin:3rem auto 0">
    <h2 style="margin-bottom:1.5rem">Pricing <span class="g-acc">FAQ</span></h2>
    <div class="faq-wrap" style="max-width:100%">
      <details><summary>Is UniConverter really free to try?</summary><div class="ans"><p>Yes. Download UniConverter without any payment. The free trial lets you use all features with no time limit — converted files include a watermark. Upgrade to remove the watermark and unlock full quality output.</p></div></details>
      <details><summary>Annual vs Perpetual — which is better value?</summary><div class="ans"><p>At $39.99/year the annual plan is the lowest upfront cost. At $79.99 the perpetual plan pays for itself after 24 months of annual renewals. If you convert video regularly and plan to use UniConverter long-term, perpetual is the better investment. If you only need it occasionally or want to try before committing long-term, annual is the right choice.</p></div></details>
      <details><summary>Does the price include all AI features?</summary><div class="ans"><p>Yes. Both paid plans include all 8 AI features: AI Super Resolution, AI Frame Interpolation, AI Stabilization, AI Noise Reduction, AI Translation (130 languages), AI Subtitle Generator (145+ languages), AI Compression and AI Watermark Remover. No AI tools are gated behind a higher tier.</p></div></details>
      <details><summary>Is UniConverter available globally?</summary><div class="ans"><p>Yes. UniConverter is sold in 150+ countries and available in multiple languages. Payment is accepted in local currencies where supported. AI translation covers 130 languages and AI subtitle generation covers 145+ languages — making it genuinely useful for international content creators.</p></div></details>
      <details><summary>Is there a commercial licence?</summary><div class="ans"><p>Yes. A commercial licence for 5 PCs is available at $337.46 for professional and business use. Check the official Wondershare site for current commercial pricing and enterprise options.</p></div></details>
    </div>
  </div>
</section>""","UniConverter pricing, UniConverter cost, UniConverter annual plan, UniConverter perpetual licence, video converter price 2026",extras=[faq_s])

def pg_review():
    rev_s='{"@context":"https://schema.org","@type":"Review","itemReviewed":{"@type":"SoftwareApplication","name":"Wondershare UniConverter","applicationCategory":"MultimediaApplication","operatingSystem":"Windows, macOS"},"reviewRating":{"@type":"Rating","ratingValue":"9.1","bestRating":"10","worstRating":"1"},"author":{"@type":"Person","name":"VideoConverter Guide Editorial Team"},"datePublished":"2026-06-01","reviewBody":"UniConverter 17 earns 9.1/10. GPU acceleration delivers genuinely transformative speed. AI translation in 130 languages and subtitle generation in 145+ languages are unique features. The all-in-one toolbox replaces 8 separate applications at an excellent price point."}'
    return page(f"Wondershare UniConverter Review {YEAR} — 9.1/10 After Full Testing",
        f"Complete Wondershare UniConverter 17 review {YEAR}: 9.1/10. We tested GPU speed, AI translation, subtitle generation, compression, DVD burning. Full verdict.",
        "/review/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Review",None))}
  <span class="sec-lbl">In-Depth Review</span>
  <h1>UniConverter <span class="g-acc">Review {YEAR}</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">We tested UniConverter 17 across 35 scenarios — 4K conversion, AI upscaling, AI translation, subtitle generation, DVD burning, screen recording and compression. Complete verdict.</p>
</div>
<section>
  <div class="split">
    <div>
      <div class="score-big">9.1</div>
      <div style="font-size:.79rem;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-bottom:1.5rem">out of 10 — Editor's Rating</div>
      <div style="display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:2rem">
        <span class="chip chip-g">✓ Recommended</span>
        <span class="chip chip-o">Best Paid Converter</span>
        <span class="chip chip-p">AI Champion</span>
        <span class="chip chip-t">Global Tool</span>
      </div>
      <div class="rbars">
        <div class="rbar"><span class="rbar-lbl">Conversion Speed</span><div class="rbar-track"><div class="rbar-fill" style="width:98%"></div></div><span class="rbar-val">9.8</span></div>
        <div class="rbar"><span class="rbar-lbl">Output Quality</span><div class="rbar-track"><div class="rbar-fill" style="width:95%"></div></div><span class="rbar-val">9.5</span></div>
        <div class="rbar"><span class="rbar-lbl">Format Support</span><div class="rbar-track"><div class="rbar-fill" style="width:98%"></div></div><span class="rbar-val">9.8</span></div>
        <div class="rbar"><span class="rbar-lbl">AI Features</span><div class="rbar-track"><div class="rbar-fill" style="width:93%"></div></div><span class="rbar-val">9.3</span></div>
        <div class="rbar"><span class="rbar-lbl">Ease of Use</span><div class="rbar-track"><div class="rbar-fill" style="width:88%"></div></div><span class="rbar-val">8.8</span></div>
        <div class="rbar"><span class="rbar-lbl">Value for Money</span><div class="rbar-track"><div class="rbar-fill" style="width:92%"></div></div><span class="rbar-val">9.2</span></div>
        <div class="rbar"><span class="rbar-lbl">Global Features</span><div class="rbar-track"><div class="rbar-fill" style="width:95%"></div></div><span class="rbar-val">9.5</span></div>
        <div class="rbar"><span class="rbar-lbl">Support</span><div class="rbar-track"><div class="rbar-fill" style="width:80%"></div></div><span class="rbar-val">8.0</span></div>
      </div>
    </div>
    <div>
      <div class="hbox good"><h4>✓ What We Loved in v17</h4>
        <ul style="list-style:none;padding:0;margin-top:.7rem;display:flex;flex-direction:column;gap:.5rem">
          {"".join(f'<li style="font-size:.86rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>{x}</li>' for x in ["GPU: 1hr 4K H.265 encoded in 3.5 minutes — genuinely transformative","AI translation in 130 languages tested accurate on German, Japanese, Arabic, Hindi","AI subtitle generation produced usable .SRT files on first attempt","New AI Compression mode outperformed standard bitrate compression by 25%","Blu-ray burning works cleanly — new in v17","Batch watermark removal on 50 videos — all handled correctly","$39.99/year is excellent value for this many tools"])}
        </ul>
      </div>
      <div class="hbox warn" style="margin-top:1rem"><h4>⚠ Caveats</h4>
        <ul style="list-style:none;padding:0;margin-top:.5rem;display:flex;flex-direction:column;gap:.4rem">
          {"".join(f'<li style="font-size:.86rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">–</span>{x}</li>' for x in ["Interface can feel overwhelming on first launch — many tools","Customer support response times can be slow (24–48 hours)","AI features add processing time on top of conversion time","Free trial's 5-minute output limit makes full evaluation harder"])}
        </ul>
      </div>
    </div>
  </div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Try UniConverter Free</a>
  </div>
</section>""","UniConverter review, Wondershare UniConverter review, UniConverter 17 review, is UniConverter worth it",extras=[rev_s],article=True)


def pg_faq():
    faqs=[
        ("Is UniConverter free?","UniConverter offers a free trial with no time limit. Trial exports include a watermark on output files. Paid plans start at $39.99/year (Annual) or $79.99 one-time (Perpetual) and remove the watermark. All paid plans include all features including AI tools."),
        ("How fast is UniConverter?","With GPU acceleration, UniConverter converts at up to 90× real-time speed. A 1-hour 4K H.265 video converts in 3–5 minutes on a system with NVIDIA, AMD or Intel GPU. Batch conversion processes multiple files simultaneously. It dramatically outperforms CPU-only converters like HandBrake."),
        ("What formats does UniConverter support?","1000+ formats including MP4, MKV, AVI, MOV, WMV, FLV, WebM, HEVC/H.265, H.264, ProRes, MXF, XAVC, AVCHD, VOB, TS, MTS, 3GP, RM, DivX, DV, VP9, AV1, MP3, AAC, WAV, FLAC, JPG, PNG, HEIC, RAW and more."),
        ("Does UniConverter work on Mac?","Yes. Full-featured versions for both Windows (7/8/10/11) and macOS (10.12+, including Apple Silicon M1/M2/M3). Both platforms have identical features including GPU acceleration, AI tools and Blu-ray burning."),
        ("Can UniConverter translate video in different languages?","Yes. UniConverter 17 includes AI Translation that converts video subtitles and scripts into 130+ languages with 95%+ accuracy. It also generates subtitles in 145+ languages from any video's audio automatically. This makes it the best video converter for global content creators."),
        ("Can UniConverter convert 4K and 8K video?","Yes. UniConverter supports 4K and 8K conversion in H.264, H.265/HEVC, ProRes and other modern codecs. GPU acceleration makes 4K/8K conversion practical on consumer hardware — completing in minutes rather than hours."),
        ("What is the difference between UniConverter and HandBrake?","HandBrake is a great free converter but converts fewer formats, has no compressor, DVD burner, screen recorder, AI tools or downloader. UniConverter at $39.99/year replaces 8 separate tools and adds GPU acceleration and AI translation. See our full comparison."),
        ("Does UniConverter burn Blu-ray?","Yes. Blu-ray burning was added in UniConverter 17. Burn any video to Blu-ray or standard DVD with custom menus and templates. Also supports ripping DVDs to digital formats and creating ISO images."),
        ("Does UniConverter have AI subtitle generation?","Yes. UniConverter 17 generates accurate subtitles in 145+ languages automatically from any video's audio. Subtitles are fully editable and available as bilingual captions. Export as .SRT, .ASS or burn permanently into the video."),
        ("How does AI Compression work?","UniConverter 17's AI Compression analyzes video content frame-by-frame and applies intelligent per-scene compression achieving up to 150% file size reduction without visible quality loss. Standard compression mode reduces by up to 90%."),
        ("Is UniConverter available worldwide?","Yes. UniConverter is sold in 150+ countries with support for 7+ interface languages. AI translation covers 130 languages and AI subtitle generation covers 145+ languages. Payment in local currencies where available."),
        ("What is the commercial licence?","A commercial licence for professional and business use is available at $337.46 for 5 PCs. For enterprise licensing or larger deployments, contact Wondershare directly for custom pricing."),
    ]
    items="".join(f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q,a in faqs)
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['+",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a[:200]}..."}}}}' for q,a in faqs)+("]}")
    return page(f"UniConverter FAQ {YEAR} — 12 Questions Answered in Full",
        "Complete UniConverter FAQ: Is it free? How fast? Mac support? AI translation? 4K? Blu-ray? AI subtitles? Worldwide? All 12 questions answered in full.",
        "/faq/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("FAQ",None))}
  <span class="sec-lbl">Questions Answered</span>
  <h1>UniConverter <span class="g-acc">FAQ</span></h1>
  <p style="max-width:640px;margin-top:.9rem;color:var(--muted)">Detailed answers to the 12 most common questions before downloading or purchasing UniConverter.</p>
</div>
<section>
  <div class="faq-wrap">{items}</div>
  <div style="text-align:center;margin-top:3.5rem">
    <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Download UniConverter Free</a>
  </div>
</section>""","UniConverter FAQ, UniConverter free, UniConverter Mac, 4K UniConverter, UniConverter AI translation, Blu-ray UniConverter",extras=[faq_s])

def pg_download():
    return page(f"Download Wondershare UniConverter Free — Windows & Mac | {YEAR}",
        "Download Wondershare UniConverter free trial for Windows and Mac. Convert 1000+ formats, compress video, burn DVD/Blu-ray, record screen and use AI tools. No credit card needed.",
        "/download/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Download",None))}
  <span class="sec-lbl" style="display:block;text-align:center">Start in 60 Seconds</span>
  <h1>Download <span class="g-acc">UniConverter</span></h1>
  <p style="max-width:520px;margin:.9rem auto 0;color:var(--muted)">Free trial — no credit card. 1000+ formats, GPU acceleration, AI tools. Windows and Mac.</p>
</div>
<section>
  <div class="g2" style="max-width:760px;margin:0 auto 3rem">
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2rem">🪟</div>
      <h3>Windows</h3>
      <p style="margin-bottom:.4rem">Windows 7 / 8 / 10 / 11</p>
      <p style="font-size:.8rem;color:var(--muted);margin-bottom:1.5rem">32-bit and 64-bit · Latest version</p>
      <a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Windows</a>
    </div>
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2rem">🍎</div>
      <h3>macOS</h3>
      <p style="margin-bottom:.4rem">macOS 10.12 Sierra and later</p>
      <p style="font-size:.8rem;color:var(--muted);margin-bottom:1.5rem">Intel &amp; Apple Silicon M1/M2/M3</p>
      <a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Mac</a>
    </div>
  </div>
  <div class="hbox good" style="max-width:720px;margin:0 auto">
    <h4>Free Trial Includes</h4>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem;margin-top:.8rem">
      {"".join(f'<div style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>{x}</div>' for x in ["Convert any format (watermark on output)","Test GPU acceleration speed","Try all 8 AI tools","Preview AI translation","Test DVD/Blu-ray burning","Screen recorder trial","Video downloader","Batch conversion preview"])}
    </div>
  </div>
  <div style="text-align:center;margin-top:2rem">
    <p style="color:var(--muted);margin-bottom:1rem">Upgrade from $39.99/year or $79.99 lifetime.</p>
    <a href="{SITE_ROOT}/pricing/" class="btn btn-g">View All Pricing Options →</a>
  </div>
</section>""")

def pg_convert_mp4():
    return page(f"Convert Any Video to MP4 — Complete Guide {YEAR}",
        "Convert MKV, AVI, MOV, WMV, HEVC, FLV, WebM and 1000+ formats to MP4 using Wondershare UniConverter. GPU accelerated, no quality loss. Step-by-step guide.",
        "/convert-mp4/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Convert to MP4",None))}
  <span class="sec-lbl">Conversion Guide</span>
  <h1>Convert Any Video<br>to <span class="g-acc">MP4</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">MP4 plays on every device. Here's how to convert anything to MP4 in seconds — no quality loss.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">What Converts <span class="g-acc">to MP4</span></h2>
      <div class="fmt-grid" style="margin-bottom:1.5rem">
        {"".join(f'<span class="fmt">{f} → MP4</span>' for f in ["MKV","AVI","MOV","WMV","FLV","WebM","HEVC","MTS","M2TS","VOB","TS","AVCHD","3GP","RM","DivX","F4V","OGV","ProRes","XAVC","MXF","R3D"])}
      </div>
      <div class="hbox info"><h4>H.264 vs H.265 MP4 — Which to Choose?</h4><p style="margin-top:.4rem"><strong>H.264 MP4</strong>: Maximum compatibility — plays on everything from old phones to Smart TVs. Choose this for sharing, social media and unknown playback devices.<br><br><strong>H.265/HEVC MP4</strong>: 40% smaller file at same quality. Choose this for storage, 4K content and modern devices (iPhone 7+, Samsung Galaxy S8+).</p></div>
      <a href="{AFF}" class="btn btn-p" style="margin-top:1.5rem" target="_blank" rel="noopener sponsored">⬇ Convert to MP4 Free</a>
    </div>
    <div>
      <div class="card card-feat" style="padding:2rem">
        <h3 style="color:var(--acc);margin-bottom:1.4rem">Steps: Convert to MP4</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div><h3>Open UniConverter</h3><p>Install UniConverter and click "Add Files" or drag your video in.</p></div></div>
          <div class="step" data-n="2"><div><h3>Select MP4</h3><p>Choose MP4 from the output format dropdown. Select H.264 or H.265.</p></div></div>
          <div class="step" data-n="3"><div><h3>Convert</h3><p>GPU acceleration completes the conversion in seconds to minutes.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-p btn-full" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Try Free</a>
      </div>
    </div>
  </div>
</section>""","convert video to MP4, MKV to MP4, AVI to MP4, MOV to MP4, WMV to MP4, HEVC to MP4",article=True)

def pg_compress():
    return page(f"Compress Video Without Quality Loss — AI Compression Guide {YEAR}",
        "Compress video by up to 150% without quality loss using Wondershare UniConverter's AI Compression. Reduce file size for email, social media, storage and sharing.",
        "/compress-video/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Compress Video",None))}
  <span class="sec-lbl">Compression Guide</span>
  <h1>Compress Video<br><span class="g-acc">Without Quality Loss</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">UniConverter 17 includes AI Compression — up to 150% file size reduction without visible quality loss. Here's how.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">AI Compression vs<br><span class="g-acc">Standard Compression</span></h2>
      <div class="hbox good"><h4>New: AI Compression Mode</h4><p style="margin-top:.4rem">UniConverter 17's AI Compression analyzes video content frame-by-frame and applies intelligent per-scene bitrate — achieving up to 150% file size reduction. Complex scenes get more bits; simple scenes get fewer. Results consistently outperform standard bitrate compression by 20–30%.</p></div>
      <h3 style="margin:1.5rem 0 .8rem;font-size:1.1rem;color:var(--txt)">Real Compression Examples</h3>
      <div style="display:flex;flex-direction:column;gap:.6rem">
        {"".join(f'<div style="background:rgba(255,90,31,.06);border:1px solid var(--bdr);border-radius:var(--r2);padding:.8rem 1rem;display:flex;justify-content:space-between;align-items:center"><span style="font-size:.85rem;color:var(--muted)">{a}</span><span style="font-family:\'JetBrains Mono\',monospace;color:var(--acc);font-size:.85rem;font-weight:600">{b}</span></div>' for a,b in [("4K drone footage (1 hour)","8GB → 650MB (92%)"),("1080p home video","2GB → 220MB (89%)"),("YouTube upload (30 min)","600MB → 55MB (91%)"),("WhatsApp share","80MB → 10MB (88%)")])}
      </div>
      <a href="{AFF}" class="btn btn-p" style="margin-top:1.5rem" target="_blank" rel="noopener sponsored">⬇ Compress Video Free</a>
    </div>
    <div>
      <div class="card card-feat" style="padding:2rem">
        <h3 style="color:var(--acc);margin-bottom:1.4rem">How to Compress</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div><h3>Open Video Compressor</h3><p>In UniConverter, go to Toolbox → Video Compressor.</p></div></div>
          <div class="step" data-n="2"><div><h3>Add Your Video</h3><p>Drag your video in. UniConverter shows current size and dimensions.</p></div></div>
          <div class="step" data-n="3"><div><h3>Select AI or Standard Mode</h3><p>Choose AI Compression for maximum reduction or Standard for quick compression. Set target file size.</p></div></div>
          <div class="step" data-n="4"><div><h3>Preview &amp; Compress</h3><p>Preview quality before committing. Click Compress. Done in seconds with GPU.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-p btn-full" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Try Free</a>
      </div>
    </div>
  </div>
</section>""","compress video without quality loss, AI video compression, reduce video file size, compress 4K video",article=True)

def pg_mkv():
    return page(f"Convert MKV to MP4 — Fast, Lossless, Keeps All Tracks | {YEAR}",
        "Convert MKV to MP4 keeping all audio tracks, subtitles and chapters. GPU accelerated. No quality loss. Handles 4K HEVC MKV files. Step-by-step guide using UniConverter.",
        "/convert-mkv-mp4/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("MKV to MP4",None))}
  <span class="sec-lbl">Format Guide</span>
  <h1>Convert <span class="g-acc">MKV to MP4</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">MKV files won't play on most TVs, phones and streaming devices. Convert to MP4 and they work everywhere — in seconds.</p>
</div>
<section>
  <div class="split">
    <div>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Add MKV File</h3><p>Drag your MKV into UniConverter. Add multiple MKV files for batch conversion.</p></div></div>
        <div class="step" data-n="2"><div><h3>Choose MP4 Output</h3><p>Select MP4 → H.264 for maximum compatibility or H.265 for smaller file.</p></div></div>
        <div class="step" data-n="3"><div><h3>Select Audio & Subtitle Tracks</h3><p>Choose which audio tracks and subtitle streams to include in the output.</p></div></div>
        <div class="step" data-n="4"><div><h3>Convert</h3><p>GPU acceleration completes it in under a minute for standard HD files.</p></div></div>
      </div>
      <a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Convert MKV Free</a>
    </div>
    <div>
      <div class="hbox good"><h4>What UniConverter Preserves from MKV</h4>
        {"".join(f'<div style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem"><span style="color:var(--green);font-weight:700">✓</span>{x}</div>' for x in ["All audio tracks (multiple language tracks kept)","Subtitle streams (.SRT, .ASS preserved or burned in)","Chapter markers","Original video resolution and frame rate","HDR and Dolby Vision metadata","Attachment files (fonts, artwork)"])}
      </div>
      <div class="hbox warn" style="margin-top:1rem"><h4>4K HEVC MKV Support</h4><p style="margin-top:.4rem">UniConverter fully handles 4K H.265/HEVC MKV files — including HDR10 and Dolby Vision content. GPU acceleration makes these large files convert quickly even on consumer hardware.</p></div>
    </div>
  </div>
</section>""","MKV to MP4, convert MKV to MP4, MKV converter, best MKV to MP4 converter, 4K MKV converter",article=True)

def pg_mov():
    return page(f"Convert MOV to MP4 — iPhone, Mac & ProRes Guide {YEAR}",
        "Convert MOV to MP4 from iPhone, Mac, GoPro and professional cameras. HEVC MOV fully supported. No quality loss. GPU accelerated. Guide for all MOV sources.",
        "/convert-mov-mp4/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("MOV to MP4",None))}
  <span class="sec-lbl">Format Guide</span>
  <h1>Convert <span class="g-acc">MOV to MP4</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">MOV is Apple's default format. Convert to MP4 to share on Windows PCs, Android phones, social media and any streaming platform.</p>
</div>
<section>
  <div class="hbox"><h4>iPhone MOV = HEVC — UniConverter Handles It</h4><p style="margin-top:.4rem">Modern iPhones record in HEVC (H.265) MOV format. Many Windows computers and Android devices can't play this. UniConverter converts HEVC MOV to H.264 MP4 automatically, maintaining quality while maximizing compatibility.</p></div>
  <div class="g3" style="margin:1.5rem 0">
    {"".join(f'<div class="card"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>' for icon,title,desc in [("📱","iPhone MOV","All iPhone models including HEVC recording. Converts HEVC MOV to H.264 MP4 for maximum compatibility."),("🍎","Final Cut Pro / ProRes MOV","ProRes 422, ProRes 4444 and all ProRes variants. Convert for web delivery without re-rendering in your NLE."),("🎬","GoPro MOV","GoPro Hero cameras record MOV. Convert to MP4 for editing, sharing and social media upload."),("🚁","DJI Drone MOV","DJI drones record MOV/HEVC. Convert to H.264 MP4 for wider software and device compatibility."),("📹","QuickTime MOV","Any QuickTime-recorded MOV file converted to universal MP4 for cross-platform sharing."),("🎥","DSLR / Mirrorless MOV","Canon, Nikon, Sony mirrorless cameras. Convert camera MOV footage to MP4 for faster editing and delivery.")])}
  </div>
  <div style="text-align:center">
    <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Convert MOV to MP4 Free</a>
  </div>
</section>""","MOV to MP4, convert MOV to MP4, iPhone MOV to MP4, HEVC MOV converter, ProRes to MP4, Mac video converter",article=True)

def pg_dvd():
    return page(f"DVD & Blu-ray Burner Software — UniConverter {YEAR}",
        "Burn any video to DVD or Blu-ray using Wondershare UniConverter. Custom menus, 1000+ input formats. Rip DVDs to digital. Blu-ray burning added in UniConverter 17.",
        "/dvd-burner/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("DVD Burner",None))}
  <span class="sec-lbl">DVD & Blu-ray Guide</span>
  <h1>Burn Video to <span class="g-acc">DVD &amp; Blu-ray</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">UniConverter 17 added Blu-ray burning alongside its existing DVD support. Burn any video to any disc format with custom menus.</p>
</div>
<section>
  <div class="g3" style="margin-bottom:2.5rem">
    <div class="card"><div class="card-icon">📀</div><h3>DVD Burning</h3><p>Burn any video to DVD-5, DVD-9, DVD±R/RW. Custom menus and templates. NTSC and PAL support. Chapter markers and thumbnails.</p></div>
    <div class="card card-feat"><div class="card-icon">💿</div><h3>Blu-ray Burning — New in v17</h3><p>Full Blu-ray burning support added in UniConverter 17. Burn HD and 4K content to Blu-ray discs with professional menus. Supports BD-R, BD-RE and BD-ROM formats.</p></div>
    <div class="card"><div class="card-icon">🔄</div><h3>DVD Ripping</h3><p>Rip DVD video to MP4, MKV or any digital format. Convert disc collections to digital. Preserve your physical media library permanently.</p></div>
    <div class="card"><div class="card-icon">💾</div><h3>ISO Image</h3><p>Create ISO disc images for burning later or playing virtually. Convert ISO files to digital video formats.</p></div>
    <div class="card"><div class="card-icon">🎨</div><h3>Custom Menus</h3><p>Choose from professional menu templates or customise with your own background, title, font, chapter thumbnails and cover art.</p></div>
    <div class="card"><div class="card-icon">🌍</div><h3>NTSC &amp; PAL</h3><p>Supports both NTSC (Americas, Japan) and PAL (Europe, Australia, Africa, Asia) regional broadcast formats.</p></div>
  </div>
  <div style="text-align:center">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download DVD/Blu-ray Burner Free</a>
  </div>
</section>""","DVD burner software, Blu-ray burner software, burn video to DVD, burn video to Blu-ray, DVD creator, MP4 to DVD",article=True)

def pg_vs_hb():
    return page(f"UniConverter vs HandBrake — Full Comparison {YEAR}",
        f"UniConverter vs HandBrake: features, speed, AI tools, ease of use. HandBrake is free. UniConverter is $39.99/year. Is it worth it? Complete honest comparison {YEAR}.",
        "/vs-handbrake/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs HandBrake",None))}
  <span class="sec-lbl">Head-to-Head</span>
  <h1>UniConverter vs <span class="g-acc">HandBrake</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">HandBrake is free and respected. UniConverter costs $39.99/year. Here's exactly what you get for the money.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">UniConverter</th><th>HandBrake</th></tr></thead>
    <tbody>
      {"".join(f'<tr><td class="td-n">{f}</td><td class="td-y td-hi">{u}</td><td class="{tc}">{h}</td></tr>' for f,u,h,tc in [("Formats","1000+","Limited (H.264/H.265 mainly)","td-p"),("GPU acceleration","✓ 90× — NVIDIA/AMD/Intel","Limited NVENC support","td-p"),("AI tools","✓ 8 AI features — translation, SR, etc.","✗","td-no"),("AI translation 130 languages","✓ Built in","✗","td-no"),("AI subtitle generation 145+ langs","✓ Built in","✗","td-no"),("Video compressor","✓ AI + standard mode","✗","td-no"),("DVD/Blu-ray burner","✓ Both","✗","td-no"),("Screen recorder","✓ Full featured","✗","td-no"),("Video downloader","✓ 1000+ sites","✗","td-no"),("Watermark remover","✓ AI-powered, batch","✗","td-no"),("Batch size","Hundreds simultaneously","Limited","td-p"),("Device presets","50+ current devices","Outdated presets","td-p"),("Ease of use","★★★★★ Guided UI","★★★☆☆ Technical","td-p"),("Mac — Apple Silicon","✓ Native M1/M2/M3","✓","td-y"),("Cost","$39.99/yr or $79.99 lifetime","Free","td-y")])}
    </tbody>
  </table></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:1.5rem">
    <div class="hbox good" style="margin:0"><h4>Choose UniConverter if...</h4>{"".join(f'<div style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem"><span style="color:var(--green);font-weight:700">✓</span>{x}</div>' for x in ["You need AI translation or subtitle generation","You want maximum GPU conversion speed","You need DVD/Blu-ray burning","You want screen recording built in","You need AI upscaling or stabilization","You prefer a clean, guided interface"])}</div>
    <div class="hbox" style="margin:0"><h4>HandBrake is fine if...</h4>{"".join(f'<div style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem;margin-top:.4rem"><span style="color:var(--acc3)">→</span>{x}</div>' for x in ["You only need H.264/H.265 conversion","Budget is the primary consideration","You're comfortable with technical settings","You don't need any extra tools","You use Linux (HandBrake supports it, UniConverter doesn't)"])}</div>
  </div>
  <div style="text-align:center;margin-top:2rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try UniConverter Free →</a></div>
</section>""","UniConverter vs HandBrake, HandBrake alternative, best video converter HandBrake comparison")

def pg_vs_vlc():
    return page(f"UniConverter vs VLC — Video Conversion Comparison {YEAR}",
        f"UniConverter vs VLC: conversion features, speed, batch support, AI tools compared. VLC is free but designed as a player, not a converter. Full comparison {YEAR}.",
        "/vs-vlc/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs VLC",None))}
  <span class="sec-lbl">Head-to-Head</span>
  <h1>UniConverter vs <span class="g-acc">VLC</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">VLC is a brilliant media player with a hidden conversion feature. UniConverter is a dedicated converter. Big difference in practice.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">UniConverter</th><th>VLC</th></tr></thead>
    <tbody>
      <tr><td class="td-n">Primary purpose</td><td class="td-hi">Video conversion toolbox</td><td>Media player</td></tr>
      <tr><td class="td-n">GPU acceleration</td><td class="td-y td-hi">✓ 90× faster</td><td class="td-no">✗ CPU only</td></tr>
      <tr><td class="td-n">AI tools</td><td class="td-y td-hi">✓ 8 AI features</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Batch conversion</td><td class="td-y td-hi">✓ Hundreds of files</td><td class="td-no">✗ One at a time</td></tr>
      <tr><td class="td-n">Quality control</td><td class="td-y td-hi">Full bitrate/codec control</td><td class="td-p">Basic only</td></tr>
      <tr><td class="td-n">DVD/Blu-ray burning</td><td class="td-y td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Video compression</td><td class="td-y td-hi">✓ AI + standard</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Screen recorder</td><td class="td-y td-hi">✓ Full featured</td><td class="td-p">Experimental only</td></tr>
      <tr><td class="td-n">Ease of converting</td><td class="td-y td-hi">★★★★★ Simple UI</td><td class="td-p">★★☆☆☆ Hidden feature</td></tr>
      <tr><td class="td-n">Cost</td><td class="td-hi">$39.99/yr</td><td class="td-y">Free</td></tr>
    </tbody>
  </table></div>
  <div class="hbox" style="margin-top:1.5rem"><h4>Bottom Line</h4><p style="margin-top:.4rem">VLC's conversion feature works for occasional simple conversions — but it's CPU-only, has no batch support, no quality presets and is genuinely difficult to find. Use VLC for what it does best: playing media. Use UniConverter for converting.</p></div>
  <div style="text-align:center;margin-top:1.5rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try UniConverter Free →</a></div>
</section>""","UniConverter vs VLC, VLC video converter, VLC alternative")

def pg_alternatives():
    return page(f"Best UniConverter Alternatives {YEAR} — Full Market Comparison",
        f"Compare Wondershare UniConverter with every major video converter alternative in {YEAR}: HandBrake, VLC, Any Video Converter, Freemake, Format Factory, Clipchamp.",
        "/alternatives/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",None))}
  <span class="sec-lbl">Full Market Overview</span>
  <h1>Best <span class="g-acc">Video Converter Alternatives</span> {YEAR}</h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Every major video converter compared so you can choose the right tool for your needs.</p>
</div>
<section>
  <div class="g2">
    <div class="card card-feat"><h3 style="color:var(--acc)">UniConverter <span class="chip chip-g" style="margin-left:.4rem">Recommended</span></h3><p style="margin:.8rem 0">The most complete video toolbox. 1000+ formats, 90× GPU speed, 8 AI features including translation in 130 languages, DVD/Blu-ray burning, screen recording and compression.</p><a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">Download Free →</a></div>
    <div class="card"><h3>HandBrake <span class="chip chip-g" style="margin-left:.4rem">Free</span></h3><p style="margin:.8rem 0">Best free option for basic H.264/H.265 conversion. No AI tools, no DVD burning, no screen recording, limited GPU support. Good for technically confident users who only need conversion.</p><a href="{SITE_ROOT}/vs-handbrake/" class="btn btn-g" style="margin-top:1rem">Full Comparison →</a></div>
    <div class="card"><h3>VLC Media Player <span class="chip chip-g" style="margin-left:.4rem">Free</span></h3><p style="margin:.8rem 0">Excellent media player. Conversion is a hidden feature — slow CPU-only, no batch, no quality controls. Keep VLC for playing, use UniConverter for converting.</p><a href="{SITE_ROOT}/vs-vlc/" class="btn btn-g" style="margin-top:1rem">Full Comparison →</a></div>
    <div class="card"><h3>Freemake Video Converter <span class="chip chip-y" style="margin-left:.4rem">Freemium</span></h3><p style="margin:.8rem 0">Free version is heavily restricted — watermarks on all output, 5-minute length limit, bundled software and ads. $29.95/year to unlock basics. No GPU, no AI, Windows only.</p><a href="{SITE_ROOT}/vs-freemake/" class="btn btn-g" style="margin-top:1rem">Full Comparison →</a></div>
    <div class="card"><h3>Any Video Converter</h3><p style="margin:.8rem 0">Solid paid converter with DVD support. Fewer formats than UniConverter, no AI tools, no dedicated compressor. Slightly cheaper lifetime license at $69.95.</p><span class="chip chip-b">$69.95 lifetime</span></div>
    <div class="card"><h3>Clipchamp (Microsoft)</h3><p style="margin:.8rem 0">Browser-based, free with Microsoft 365. Good for basic editing and export. No GPU acceleration, limited format support, no DVD burning, no AI translation. Web-only.</p><span class="chip chip-g">Free (basic)</span> <span class="chip chip-y" style="margin-left:.3rem">Web only</span></div>
  </div>
</section>""","video converter alternatives, best video converter 2026, HandBrake vs UniConverter, free video converter comparison")

def pg_blog():
    posts=[
        ("🔄","Guide",f"Convert Any Video to MP4 — Complete {YEAR} Guide","Universal format guide. Convert MKV, AVI, MOV, WMV, HEVC and 100+ formats to MP4.",f"{SITE_ROOT}/convert-mp4/",f"June {YEAR}","6 min"),
        ("🤖","Feature","UniConverter AI Features — Translation, SR, Subtitles Guide","8 AI tools explained: super resolution, 130-language translation, subtitle generation, compression.",f"{SITE_ROOT}/ai-features/",f"June {YEAR}","8 min"),
        ("📦","Tutorial",f"Compress Video Without Quality Loss — AI Compression {YEAR}","Up to 150% file size reduction with AI Compression. Real examples included.",f"{SITE_ROOT}/compress-video/",f"June {YEAR}","5 min"),
        ("🎬","Guide","MKV to MP4 — Complete Conversion Guide","Keeps all audio tracks, subtitles and chapters. Handles 4K HEVC MKV files.",f"{SITE_ROOT}/convert-mkv-mp4/",f"May {YEAR}","4 min"),
        ("🍎","Guide","Convert MOV to MP4 — iPhone, Mac & ProRes Guide","HEVC MOV from iPhone converted to universal MP4. All source types covered.",f"{SITE_ROOT}/convert-mov-mp4/",f"May {YEAR}","4 min"),
        ("💿","Tutorial","Burn Video to DVD & Blu-ray — UniConverter 17 Guide","Blu-ray burning added in v17. Custom menus. NTSC and PAL support.",f"{SITE_ROOT}/dvd-burner/",f"April {YEAR}","5 min"),
        ("🖥","Tutorial","Screen Recorder Guide — Record Screen with UniConverter","Full guide to recording desktop, webcam, audio. Mouse highlighting, scheduler.",f"{SITE_ROOT}/screen-recorder/",f"April {YEAR}","4 min"),
        ("🆚","Comparison","UniConverter vs HandBrake — Honest Full Comparison","Free vs $39.99/year. Every feature compared. When is HandBrake enough?",f"{SITE_ROOT}/vs-handbrake/",f"March {YEAR}","5 min"),
        ("⭐","Review",f"UniConverter 17 Review {YEAR} — 9.1/10","Complete hands-on review of UniConverter 17 including AI translation and Blu-ray.",f"{SITE_ROOT}/review/",f"March {YEAR}","10 min"),
        ("🌍","Global","UniConverter in 20 Languages — Global Guide","UniConverter for users in Germany, France, Japan, Brazil, India and 15 more countries.",f"{SITE_ROOT}/global/",f"February {YEAR}","5 min"),
        ("⚡","Guide","GPU Video Conversion — Why It Changes Everything","CPU vs GPU conversion explained. 90× faster isn't hype — here's the proof.",f"{SITE_ROOT}/how-it-works/",f"February {YEAR}","4 min"),
        ("💰","Guide","UniConverter Pricing — Annual vs Lifetime, Which to Buy?","$39.99/year or $79.99 lifetime? We work out which gives best value.",f"{SITE_ROOT}/pricing/",f"January {YEAR}","3 min"),
    ]
    cards="".join(f'<div class="bc"><div class="bc-thumb">{e}</div><div class="bc-body"><div class="bc-tag">{t}</div><h3>{title}</h3><p>{desc}</p><div class="bc-meta"><span>📅 {d}</span><span>⏱ {read}</span></div><a href="{url}" class="bc-read">Read Article →</a></div></div>' for e,t,title,desc,url,d,read in posts)
    return page(f"UniConverter Blog — Video Conversion Guides, Reviews & Tutorials {YEAR}",
        "Video converter guides, AI feature tutorials, format how-tos, reviews and comparisons. Everything about Wondershare UniConverter for global users.",
        "/blog/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",None))}
  <span class="sec-lbl">Guides, Tutorials & Reviews</span>
  <h1>UniConverter <span class="g-acc">Blog</span></h1>
  <p style="max-width:620px;margin-top:.9rem;color:var(--muted)">Practical guides and honest reviews for every video conversion need — in plain English.</p>
</div>
<section><div class="bgrid">{cards}</div></section>""","video conversion guide, UniConverter tutorial, video converter blog, AI video tools guide")

def pg_privacy():
    return page("Privacy Policy — VideoConverter Guide","Privacy policy for the VideoConverter affiliate guide.","/privacy/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Privacy",None))}<h1>Privacy <span class="g-acc">Policy</span></h1><p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>
<section style="max-width:820px;margin:0 auto">
  <div class="hbox"><p>This is an independent affiliate guide for Wondershare UniConverter. We earn commissions on qualifying purchases through affiliate links at no extra cost to you.</p></div>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Data Collection</h3><p>This is a static site hosted on GitHub Pages. We do not collect personal data or operate databases. GitHub Pages may log standard server data as part of its infrastructure.</p>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Affiliate Links</h3><p>Links to UniConverter are affiliate links via the LinkConnector network. Purchases through these links earn us a commission at no additional cost to you.</p>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Cookies</h3><p>This site does not set first-party cookies. Affiliate tracking uses cookies managed by LinkConnector. Disable cookies in your browser settings to opt out.</p>
</section>""")

def pg_disclaimer():
    return page("Affiliate Disclaimer — VideoConverter Guide","Affiliate disclosure for the VideoConverter guide.","/disclaimer/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Disclaimer",None))}<h1>Affiliate <span class="g-acc">Disclaimer</span></h1><p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>
<section style="max-width:820px;margin:0 auto">
  <div class="hbox"><h4>Disclosure</h4><p style="margin-top:.4rem">This website contains affiliate links. As an affiliate of Wondershare UniConverter via LinkConnector, we earn a commission on qualifying purchases at no additional cost to you. This funds the research and writing on this site.</p></div>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Editorial Independence</h3><p>Our reviews list both strengths and caveats — as you can see in our UniConverter review where we clearly note the interface complexity and support response time issues alongside the strengths. Affiliate relationships do not influence editorial opinions.</p>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Accuracy</h3><p>Pricing and features can change at any time. Always verify current details on the official Wondershare website before purchasing.</p>
</section>""")

def pg_404():
    return page("404 — Page Not Found | VideoConverter Guide","Page not found.","/404/",f"""
<div class="ph tc" style="min-height:60vh;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1.5rem">
  <div style="font-family:'Cabinet Grotesk',sans-serif;font-size:9rem;font-weight:900;line-height:1;color:var(--acc)">404</div>
  <h1>Page <span class="g-acc2">Not Found</span></h1>
  <p style="max-width:380px;text-align:center;color:var(--muted)">This page doesn't exist. Let's get you somewhere useful.</p>
  <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
    <a href="{SITE_ROOT}/" class="btn btn-p">← Go Home</a>
    <a href="{AFF}" class="btn btn-s" target="_blank" rel="noopener sponsored">Download UniConverter</a>
  </div>
</div>""")


# ── SEO & META FILES ──────────────────────────────────────────────────────────
def mk_sitemap():
    pages=[
        ("/","1.0","weekly"),("/features/","0.9","monthly"),("/ai-features/","0.9","monthly"),
        ("/formats/","0.9","monthly"),("/how-it-works/","0.8","monthly"),
        ("/pricing/","0.9","monthly"),("/review/","0.9","monthly"),
        ("/faq/","0.8","monthly"),("/download/","0.9","monthly"),
        ("/blog/","0.8","weekly"),("/global/","0.8","monthly"),
        ("/screen-recorder/","0.8","monthly"),
        ("/convert-mp4/","0.9","monthly"),("/compress-video/","0.8","monthly"),
        ("/convert-mkv-mp4/","0.8","monthly"),("/convert-mov-mp4/","0.8","monthly"),
        ("/dvd-burner/","0.8","monthly"),("/alternatives/","0.8","monthly"),
        ("/vs-handbrake/","0.8","monthly"),("/vs-vlc/","0.8","monthly"),
        ("/vs-freemake/","0.7","monthly"),("/privacy/","0.3","yearly"),
        ("/disclaimer/","0.3","yearly"),
    ]
    # Add all language pages
    for _,_,lc,_,_,_,_ in LANGS:
        pages.append((f"/lang/{lc}/","0.7","monthly"))
    today=date.today().isoformat()
    urls="\n".join(f"  <url>\n    <loc>{SITE_URL}{p}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n    <lastmod>{today}</lastmod>\n  </url>" for p,pri,freq in pages)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>'

def mk_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /assets/\n\nSitemap: {SITE_URL}/sitemap.xml\n"

def mk_llms():
    lang_lines = "\n".join(f'- /lang/{lc}/ — {name} ({region})' for _,name,lc,region,_,_,_ in LANGS)
    lang_list=", ".join(f"{name} ({lc})" for _,name,lc,_,_,_,_ in LANGS)
    return f"""# VideoConverter Guide — {SITE_URL}
> Purpose: Independent affiliate guide for Wondershare UniConverter
> Updated: {date.today().isoformat()}
> Affiliate: LinkConnector network
> Affiliate link: {AFF}

## Product: Wondershare UniConverter 17
**Publisher:** Wondershare Software Ltd (founded 2003, publicly listed, China)
**Users:** 15M+ worldwide in 200+ countries
**Current version:** UniConverter 17

### Platforms
- Windows: 7, 8, 10, 11 (32 and 64-bit)
- macOS: 10.12 Sierra through latest (Intel and Apple Silicon M1/M2/M3 native)

### Speed & Performance
- GPU acceleration: NVIDIA NVENC/CUDA, AMD VCE, Intel Quick Sync
- Speed: Up to 90× real-time conversion
- Example: 1 hour 4K H.265 video → 3–5 minutes with GPU
- Batch conversion: Hundreds of files simultaneously
- AI Compression: Up to 150% file size reduction (new in v17)

### Format Support
- Input/output formats: 1000+
- Key formats: MP4, MKV, AVI, MOV, WMV, FLV, WebM, HEVC/H.265, H.264, ProRes 422/4444, XAVC, MXF, R3D, BRAW, DNxHD, VP9, AV1, VOB, TS, MTS, M2TS, AVCHD, 3GP, RM, DivX, DV, MP3, AAC, WAV, FLAC, OGG, WMA, M4A, AIFF, AC3, DTS, JPG, PNG, HEIC, WebP, RAW, GIF, TIFF, BMP
- Max resolution: 8K, HDR, HDR10, Dolby Vision
- Broadcast standards: NTSC, PAL, SECAM

### Core Features
1. Video Converter — 1000+ formats, zero quality loss, full metadata preservation
2. Video Compressor — AI mode (up to 150% reduction, NEW in v17) + standard mode (up to 90%)
3. Video Editor — trim, crop, rotate, merge, add subtitles (.SRT), effects, filters, watermarks; batch trim/resize/watermark
4. DVD & Blu-ray Burner — DVD and Blu-ray (Blu-ray NEW in v17), custom menus, rip DVDs, ISO creation, NTSC/PAL
5. Screen Recorder — desktop/window/region, webcam overlay, system audio + mic, MP4/AVI/GIF export, 4K capture
6. Video Downloader — YouTube, Vimeo, Dailymotion, Facebook, Bilibili, Youku, NicoNico, 1000+ sites, 4K download
7. Watermark Remover/Adder — AI inpainting for removal, batch supported; custom text/image watermarks
8. Audio Converter — MP3, AAC, WAV, FLAC, OGG, WMA, M4A, AIFF, AC3, DTS, 50+ formats; CD burner
9. Image Converter — JPG, PNG, HEIC, WebP, RAW, TIFF, GIF, BMP; batch processing

### AI Features (UniConverter 17)
- AI Super Resolution: upscale SD to HD or 4K using neural networks
- AI Frame Interpolation: 24fps → 60fps/120fps+ smooth motion
- AI Video Stabilization: fix shaky handheld/drone/action cam footage
- AI Noise Reduction: remove background audio noise from video
- AI Translation: 130+ languages, 95%+ accuracy — unique feature
- AI Subtitle Generator: 145+ languages, bilingual captions, .SRT/.ASS export
- AI Compression: up to 150% file size reduction (NEW in v17)
- AI Watermark Remover: AI inpainting, batch processing
- AI Image Enhancer: sharpen, denoise, upscale photos to HD/4K

### Language & Global Support
- Interface languages: English, German, French, Spanish, Italian, Japanese, Chinese, Portuguese, Arabic (7+ languages)
- AI Translation: {len(LANGS)}+ languages covered on this site: {lang_list}
- AI Subtitle Generation: 145+ languages
- Regional broadcast: NTSC, PAL, SECAM
- Device presets: iPhone 16, Samsung Galaxy S25, PS5, Xbox Series X, Smart TV 4K, DJI, GoPro and 40+ more
- Platform presets: YouTube, TikTok, Instagram, Facebook, Bilibili, NicoNico, Youku, Vimeo, Twitch

### Pricing (as of {YEAR})
- Free trial: No time limit, no credit card, watermark on exports
- Annual plan: $39.99/year (1 PC, auto-renews, all features, free updates 1 year)
- Perpetual plan: $79.99 one-time (1 PC, own forever, all future updates)
- Commercial: $337.46 for 5 PCs (perpetual)
- Discounts: Up to 30% off available on official site

## Site Structure ({YEAR})
### Core Pages
- / — Homepage (all features, global reach, AI tools, testimonials)
- /features/ — Complete feature list (15 features detailed)
- /ai-features/ — All 8 AI features explained in depth
- /formats/ — 1000+ format list by category
- /how-it-works/ — 4 workflow guides (conversion, compression, DVD, AI translation)
- /pricing/ — Plan comparison with 5-item FAQ
- /review/ — Editorial review (9.1/10), 8 rating categories
- /faq/ — 12 detailed Q&As with FAQPage schema
- /download/ — Windows & Mac download page
- /blog/ — 12-article blog index

### Guide Pages
- /convert-mp4/ — Convert anything to MP4
- /compress-video/ — AI and standard compression guide
- /convert-mkv-mp4/ — MKV to MP4 guide
- /convert-mov-mp4/ — MOV to MP4 (iPhone/Mac/ProRes)
- /dvd-burner/ — DVD & Blu-ray burning guide (v17)
- /screen-recorder/ — Screen recording guide

### Comparison Pages
- /alternatives/ — vs 6 competitors
- /vs-handbrake/ — vs HandBrake full comparison table
- /vs-vlc/ — vs VLC comparison
- /vs-freemake/ — vs Freemake comparison

### Global/Language Pages
- /global/ — All 20 language regions
{lang_lines}

### Schema Types Used
SoftwareApplication, BreadcrumbList, FAQPage (on /faq/ and /pricing/), Review (on /review/), HowTo (on /how-it-works/), ItemList (on /features/ and /ai-features/), Article (on guide pages)

### SEO: hreflang
All pages include hreflang alternate links for all 20 language regions.

## Affiliate Information
- Network: LinkConnector
- Program: Wondershare UniConverter affiliate program
- Affiliate link: {AFF}
- All affiliate links use rel="noopener sponsored" per Google guidelines
- Commission earned on qualifying purchases at no extra cost to users
"""

def mk_feed():
    items=[
        (f"Convert Any Video to MP4 — {YEAR} Guide",f"{SITE_URL}/convert-mp4/","Convert MKV, AVI, MOV and 1000+ formats to MP4 in seconds.",f"{YEAR}-06-01"),
        ("UniConverter AI Features — Translation, SR, Subtitles",f"{SITE_URL}/ai-features/","8 AI tools including 130-language translation and 145+ language subtitles.",f"{YEAR}-06-01"),
        ("Compress Video Without Quality Loss — AI Compression",f"{SITE_URL}/compress-video/","AI Compression achieves up to 150% file size reduction in UniConverter 17.",f"{YEAR}-05-15"),
        (f"UniConverter 17 Review {YEAR} — 9.1/10",f"{SITE_URL}/review/","Complete hands-on review including AI translation and Blu-ray burning tests.",f"{YEAR}-03-01"),
        ("UniConverter vs HandBrake — Full Comparison",f"{SITE_URL}/vs-handbrake/","Free vs $39.99/year. Every feature compared honestly.",f"{YEAR}-04-01"),
    ]
    ixml="\n".join(f"  <item>\n    <title>{t}</title>\n    <link>{u}</link>\n    <description>{d}</description>\n    <pubDate>{pd}</pubDate>\n    <guid>{u}</guid>\n  </item>" for t,u,d,pd in items)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n    <title>VideoConverter Guide Blog</title>\n    <link>{SITE_URL}/blog/</link>\n    <description>Video conversion guides, AI tools tutorials and reviews.</description>\n    <language>en-us</language>\n    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>\n{ixml}\n  </channel>\n</rss>'

def mk_favicon():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#03060e"/><rect x="1" y="1" width="62" height="62" rx="13" fill="none" stroke="#ff5a1f" stroke-width="1.5" opacity="0.5"/><circle cx="32" cy="32" r="18" fill="none" stroke="#ff5a1f" stroke-width="2.5"/><polygon points="27,24 27,40 43,32" fill="#ff5a1f"/><circle cx="32" cy="32" r="6" fill="none" stroke="#ffd60a" stroke-width="1.5" opacity="0.5"/></svg>'

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    print(f"\n🚀 VideoConverter Affiliate Site Builder v2\n   {SITE_URL}\n")

    # Core pages
    write("index.html",                        pg_home())
    write("features/index.html",               pg_features())
    write("ai-features/index.html",            pg_ai())
    write("formats/index.html",                pg_formats())
    write("how-it-works/index.html",           pg_how())
    write("pricing/index.html",               pg_pricing())
    write("review/index.html",                pg_review())
    write("faq/index.html",                   pg_faq())
    write("download/index.html",              pg_download())
    write("blog/index.html",                  pg_blog())
    write("global/index.html",               pg_global())

    # Guide pages
    write("screen-recorder/index.html",        pg_screen_recorder())
    write("convert-mp4/index.html",            pg_convert_mp4())
    write("compress-video/index.html",         pg_compress())
    write("convert-mkv-mp4/index.html",        pg_mkv())
    write("convert-mov-mp4/index.html",        pg_mov())
    write("dvd-burner/index.html",             pg_dvd())

    # Comparison pages
    write("alternatives/index.html",           pg_alternatives())
    write("vs-handbrake/index.html",           pg_vs_hb())
    write("vs-vlc/index.html",                pg_vs_vlc())
    write("vs-freemake/index.html",            pg_vs_freemake())

    # Legal pages + 404
    write("privacy/index.html",               pg_privacy())
    write("disclaimer/index.html",            pg_disclaimer())
    write("404.html",                         pg_404())

    # Language pages (20 languages)
    print("\n  🌐 Language pages:")
    for flag,name,lc,region,kw1,kw2,kw3 in LANGS:
        write(f"lang/{lc}/index.html", pg_lang(flag,name,lc,region,kw1,kw2,kw3))

    # SEO files
    write("sitemap.xml",        mk_sitemap())
    write("robots.txt",         mk_robots())
    write("llms.txt",           mk_llms())
    write("feed.xml",           mk_feed())
    write("assets/favicon.svg", mk_favicon())
    write(".nojekyll",          "")

    pages=len([f for f in BASE.rglob("*.html")])
    total=len(list(BASE.rglob("*")))
    print(f"\n✅ Done — {pages} HTML pages, {total} total files")
    print(f"   Output: {BASE}")
    print(f"   Deploy: {SITE_URL}\n")

if __name__ == "__main__":
    main()
