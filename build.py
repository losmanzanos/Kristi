#!/usr/bin/env python3
"""Assemble the Commend Counseling static site.

Nine pages share one shell so the nav, footer, meta and asset links can never
drift apart. Edit the CONTENT blocks below and re-run:  python3 build.py
"""
import os, re

SITE = "https://losmanzanos.github.io/Kristi/"
PHONE_H = "720.507.5722"
PHONE_T = "7205075722"
EMAIL = "kristi.cobble@commendcounseling.com"
ADDR1, ADDR2 = "5808 South Rapp Street, Suite 235", "Littleton, CO 80120"

NAV = [("index.html","Home"),("about.html","About"),("services.html","Therapy"),
       ("consultation.html","Consultation"),("fees.html","Fees"),
       ("faq.html","FAQ"),("contact.html","Contact")]

def F(t):
    """Wrap text Kristi still needs to confirm."""
    return f'<span class="fill">{t}</span>'

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}{slug}">
<meta name="theme-color" content="#2E3D46">
<meta name="robots" content="noindex,nofollow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Commend Counseling">
<meta property="og:url" content="{site}{slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}og-image.jpg">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="icon-512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Imperial+Script&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
{schema}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <filter id="grainF"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
</defs></svg>
<div class="grain" aria-hidden="true"><svg><rect width="100%" height="100%" filter="url(#grainF)" opacity=".4"/></svg></div>

<nav>
  <div class="wrap nav-in">
    <a class="brand" href="index.html"><b>Commend</b><i>counseling</i></a>
    <button class="navtoggle" aria-expanded="false" aria-controls="navlinks">Menu</button>
    <div class="nav-links" id="navlinks">{nav}</div>
  </div>
</nav>

<main id="main">
{body}
</main>

<footer>
  <div class="wrap">
    <div class="f-in">
      <div>
        <div class="hand" style="font-size:46px;margin-bottom:10px">Commend</div>
        <p>Counseling and clinical consultation in Littleton, Colorado.</p>
        <p style="margin-top:14px"><a href="tel:{phone_t}">{phone_h}</a><br><a href="mailto:{email}">{email}</a></p>
      </div>
      <div>
        <div class="f-h">Visit</div>
        <p>{addr1}<br>{addr2}</p>
      </div>
      <div>
        <div class="f-h">Explore</div>
        <ul>{fnav}</ul>
      </div>
      <div>
        <div class="f-h">Practice</div>
        <ul>
          <li><a href="good-faith-estimate.html">Good Faith Estimate</a></li>
          <li><a href="privacy.html">Privacy &amp; Notices</a></li>
        </ul>
      </div>
    </div>
    <div class="f-bot">
      <span>&copy; 2026 Commend Counseling</span>
      <span>Kristi Cobble, LPC &middot; Littleton, Colorado</span>
    </div>
    <p class="f-dis">This website is for general information and does not create a therapist&ndash;client
      relationship or constitute medical advice. If you are in crisis or thinking about harming yourself,
      call or text <strong>988</strong> to reach the Suicide &amp; Crisis Lifeline, or call 911.</p>
  </div>
</footer>

<div class="fillnote">
  <b>Draft &mdash; <span data-count>0</span> to confirm</b>
  Highlighted text is drafted from Kristi&rsquo;s existing site and public listings and still needs her sign-off.
  <button type="button">Hide placeholders</button>
</div>

<script src="assets/site.js"></script>
</body>
</html>
"""

SCHEMA = """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":["LocalBusiness","ProfessionalService"],
  "name":"Commend Counseling",
  "description":"Counseling and clinical consultation in Littleton, Colorado. Kristi Cobble, LPC.",
  "url":"https://losmanzanos.github.io/Kristi/",
  "telephone":"+1-720-507-5722",
  "email":"kristi.cobble@commendcounseling.com",
  "address":{"@type":"PostalAddress","streetAddress":"5808 South Rapp Street, Suite 235",
    "addressLocality":"Littleton","addressRegion":"CO","postalCode":"80120","addressCountry":"US"},
  "founder":{"@type":"Person","name":"Kristi Cobble","honorificSuffix":"LPC",
    "jobTitle":"Licensed Professional Counselor",
    "alumniOf":{"@type":"CollegeOrUniversity","name":"Denver Seminary"}},
  "areaServed":{"@type":"State","name":"Colorado"},
  "priceRange":"$$"
}
</script>"""


# =====================================================================
#  PAGE CONTENT
# =====================================================================

HOME = f"""
<header class="hero sec" style="padding-top:clamp(40px,5vw,70px)">
  <div class="geo g-ring geo-lg" data-sp="0.30" style="color:var(--brass);opacity:.24;width:600px;height:600px;left:-230px;top:-60px"></div>
  <div class="geo g-dot" data-sp="0.55" style="color:rgba(205,155,98,.30);width:280px;height:280px;right:7%;top:5%"></div>
  <div class="wrap hero-in">
    <div class="hero-copy rv" style="--hs:1">
      <span class="eyebrow">Counseling &amp; clinical consultation &middot; Littleton, Colorado</span>
      <span class="hand hand-xl" style="margin:0 0 10px -3px">Commend</span>
      <h1 style="font-size:calc(clamp(34px,4.8vw,66px) * var(--hs))">Therapy that<br>takes you<br>seriously.</h1>
      <p class="lead" style="font-size:calc(18.5px * var(--hs));margin-top:calc(22px * var(--hs))">
        Kristi Cobble is a Licensed Professional Counselor in Littleton. She has been in private
        practice since 2016 and has spent most of that time teaching other therapists how to do
        this work well.</p>
      <div style="margin-top:calc(30px * var(--hs));display:flex;gap:13px;flex-wrap:wrap">
        <a class="btn" href="contact.html">Book a consultation</a>
        <a class="btn" href="about.html">About Kristi</a>
      </div>
      <div style="margin-top:calc(34px * var(--hs));padding-top:calc(22px * var(--hs));border-top:1px solid var(--line);display:flex;gap:26px;flex-wrap:wrap;font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--mute);font-weight:700">
        <div>Accepting <b style="color:var(--brass-lt)">new clients</b></div>
        <div>In network with <b style="color:var(--brass-lt)">Kaiser Permanente</b></div>
        <div>Licensed in <b style="color:var(--brass-lt)">Colorado</b></div>
      </div>
    </div>
    <div class="stage" style="height:clamp(340px,42vw,500px)">
      <div class="ph" data-sp="0.16" style="width:72%;height:96%;right:2%;top:0">
        <img src="kristi-iceberg.jpg" fetchpriority="high" alt="Glacial water meeting black volcanic rock and snow">
      </div>
      <div class="geo g-frame" data-sp="-0.55" style="color:var(--brass);opacity:.8;width:230px;height:230px;left:-2%;top:14%"></div>
      <div class="ph cut-hex" data-sp="0.85" style="width:170px;height:190px;left:0;bottom:7%">
        <img loading="lazy" decoding="async" src="compass-map.jpg" alt="A compass resting on a topographic map">
      </div>
      <div class="geo g-fill" data-sp="-0.9" style="color:var(--ember-lt);opacity:.95;width:66px;height:66px;left:45%;bottom:2%;transform:rotate(14deg)"></div>
    </div>
  </div>
</header>

<section class="sec lt">
  <div class="geo g-dot" data-sp="0.3" style="color:rgba(38,51,59,.12);width:100%;height:100%;left:0;top:0"></div>
  <div class="wrap">
    <div class="narrow rv" style="margin:0 auto;text-align:center">
      <span class="eyebrow">What to expect</span>
      <span class="hand hand-lg">an honest room</span>
      <h2 style="margin-top:6px">You won't be managed.</h2>
      <p class="lead" style="margin:20px auto 0">Some people come in knowing exactly what they want to work
        on. Most don't, and that's a perfectly good place to start. The first session is mostly you
        talking and Kristi listening for what's underneath it.</p>
    </div>
    <div class="three" style="margin-top:56px">
      <div class="card rv"><span class="n">i</span><h3>Individual therapy</h3><div class="hr"></div>
        <p>Ongoing work for adults navigating {F('anxiety, depression, life transitions, grief, and the kind of stuck that is hard to name out loud')}. Weekly to start, and we adjust from there.</p></div>
      <div class="card rv"><span class="n">ii</span><h3>Clinical consultation</h3><div class="hr"></div>
        <p>Consultation and supervision for therapists, from newly licensed clinicians to people well into practice. Kristi spent six years inside counselor education, most recently running a doctoral program in it.</p></div>
      <div class="card rv"><span class="n">iii</span><h3>Straightforward logistics</h3><div class="hr"></div>
        <p>In network with Kaiser Permanente, and reachable through Sondermind and Collective Counseling Solutions. {F('Self-pay and out-of-network options available, with superbills provided on request.')}</p></div>
    </div>
    <div class="rv" style="text-align:center;margin-top:46px"><a class="btn btn-dark" href="services.html">More about therapy</a></div>
  </div>
</section>

<section class="sec" style="position:relative">
  <div class="stmt-bg" style="position:absolute;inset:0;z-index:0">
    <img loading="lazy" decoding="async" src="terrain-aerial.jpg" alt="" style="width:100%;height:124%;object-fit:cover;object-position:50% 38%;opacity:.26">
    <div style="position:absolute;inset:0;background:linear-gradient(180deg,var(--slate) 1%,rgba(46,61,70,.76) 45%,var(--slate) 99%)"></div>
  </div>
  <div class="wrap rv" style="position:relative;z-index:5;max-width:900px">
    <span class="eyebrow">Approach</span>
    <span class="hand hand-lg" style="margin:0 0 14px -4px">under the surface</span>
    <p style="font-size:clamp(22px,2.7vw,36px);line-height:1.16;font-weight:700;text-transform:uppercase;letter-spacing:-.008em;color:var(--bone)">
      Most of what shapes a life sits below the waterline &mdash; and it rarely announces itself.</p>
    <div class="two" style="margin-top:38px;padding-top:32px;border-top:1px solid var(--line)">
      <p>Kristi works {F('systemically and from a Gestalt frame')}: less interested in tidy explanations than
        in what is actually happening between you, in the room, right now. Patterns tend to show up
        live long before anyone can describe them.</p>
      <p>That means sessions are conversational rather than clinical-sounding, and you will be asked
        direct questions. {F('You are welcome to push back. Most of the useful work happens when you do.')}</p>
    </div>
  </div>
</section>

<section class="sec lt lt2">
  <div class="wrap two-a">
    <div class="stage rv">
      <div class="ph" data-sp="0.16" style="width:74%;height:94%;left:8%;top:3%">
        <img loading="lazy" decoding="async" src="kristi-headshot.jpg" alt="Kristi Cobble, LPC">
      </div>
      <div class="geo g-ring" data-sp="-0.6" style="color:var(--ember);opacity:.55;width:190px;height:190px;left:-8%;bottom:2%"></div>
    </div>
    <div class="rv">
      <span class="eyebrow">Who you'd be working with</span>
      <span class="hand hand-md" style="margin:0 0 4px -3px">Kristi Cobble</span>
      <h2>LPC &middot; Denver Seminary faculty</h2>
      <p style="margin-top:20px">In private practice since 2016. Six years at Denver Seminary, most recently as
        Associate Director of its PhD program in Counselor Education and Supervision, where she still
        teaches as adjunct faculty.</p>
      <p>Which is a long way of saying she has spent a decade thinking carefully about what actually
        helps &mdash; from both chairs.</p>
      <div style="margin-top:28px"><a class="btn btn-dark" href="about.html">Read more</a></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="geo g-ring geo-lg" data-sp="0.45" style="color:var(--brass);opacity:.24;width:520px;height:520px;left:-190px;top:-100px"></div>
  <div class="wrap narrow rv" style="margin:0 auto;text-align:center">
    <span class="eyebrow">Getting started</span>
    <span class="hand hand-lg">say hello</span>
    <h2 style="margin-top:6px">A short call first.</h2>
    <p class="lead" style="margin:20px auto 0">{F('A brief phone consultation, at no charge, to see whether this is a good fit')}.
      If it isn't, Kristi will say so and point you somewhere better.</p>
    <div style="margin-top:32px;display:flex;gap:13px;flex-wrap:wrap;justify-content:center">
      <a class="btn" href="mailto:{EMAIL}">Email Kristi</a>
      <a class="btn" href="tel:{PHONE_T}">{PHONE_H}</a>
    </div>
  </div>
</section>
"""

ABOUT = f"""
<section class="phead">
  <div class="geo g-dot geo-lg" data-sp="0.4" style="color:rgba(205,155,98,.26);width:300px;height:300px;right:5%;top:0"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> &middot; About</div>
    <span class="hand hand-xl" style="margin-left:-3px">Kristi Cobble</span>
    <h1 style="margin-top:6px">Licensed Professional Counselor</h1>
    <p class="lead">Littleton, Colorado. In practice since 2016.</p>
  </div>
</section>

<section class="sec-sm lt">
  <div class="wrap two-a">
    <div class="stage rv" style="height:clamp(320px,38vw,430px)">
      <div class="ph" data-sp="0.15" style="width:72%;height:94%;left:8%;top:3%">
        <img src="kristi-headshot.jpg" fetchpriority="high" alt="Kristi Cobble, LPC">
      </div>
      <div class="geo g-frame" data-sp="-0.5" style="color:var(--ember);opacity:.6;width:180px;height:180px;right:2%;bottom:2%"></div>
    </div>
    <div class="rv">
      <span class="eyebrow">Background</span>
      <h2>Both chairs.</h2>
      <p style="margin-top:20px">Kristi has run her own practice since 2016. Alongside it she spent six years at
        Denver Seminary &mdash; first in student services, later as Associate Director of the seminary's PhD
        program in Counselor Education and Supervision. She still teaches there as adjunct faculty.</p>
      <p>That combination is unusual, and it shapes how she works. Teaching supervision means spending
        years watching what helps and what merely sounds like it should, then having to explain the
        difference to people who will ask hard questions about it.</p>
      <p>{F('She is a Kaiser Permanente affiliated provider and also sees clients through Sondermind and Collective Counseling Solutions.')}</p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap two">
    <div class="rv">
      <span class="eyebrow">How she works</span>
      <span class="hand hand-lg" style="margin:0 0 8px -4px">in the room</span>
      <h2>Direct, and<br>not precious<br>about it.</h2>
    </div>
    <div class="rv">
      <p class="lead">{F('Her work is anchored in systemic thinking and real-time Gestalt processing')} &mdash; which
        in practice means less time constructing explanations about your life and more time noticing
        what is happening while you describe it.</p>
      <p style="margin-top:18px">Patterns show up live. The way you brace before a certain subject, what you
        skip past, where the energy leaves your voice. Those are usually more useful than anything
        either of you could theorize about afterward.</p>
      <p>{F('You should expect to be asked direct questions, and to be welcome to push back on them. Humor is allowed. Most people find they need it.')}</p>
    </div>
  </div>
</section>

<section class="sec-sm lt">
  <div class="geo g-dot" data-sp="0.3" style="color:rgba(38,51,59,.12);width:100%;height:100%;left:0;top:0"></div>
  <div class="wrap two-b" style="align-items:start">
   <div>
    <div class="rv" style="margin-bottom:36px">
      <span class="eyebrow">Credentials</span>
      <span class="hand hand-md" style="margin:0 0 6px -3px">the formal part</span>
      <h2>On paper.</h2>
    </div>
    <dl class="dl rv">
      <div><dt>License</dt><dd>Licensed Professional Counselor, State of Colorado {F('&middot; license #')}</dd></div>
      <div><dt>Education</dt><dd>Denver Seminary {F('&middot; MA in Counseling')}</dd></div>
      <div><dt>Teaching</dt><dd>Adjunct Faculty, Denver Seminary. Former Associate Director, PhD in Counselor Education &amp; Supervision.</dd></div>
      <div><dt>Practice</dt><dd>Private practice since 2016. Kaiser Permanente affiliated since 2024.</dd></div>
      <div><dt>Networks</dt><dd>Collective Counseling Solutions &middot; Sondermind</dd></div>
      <div><dt>Focus</dt><dd>{F('Adults, individual therapy, and clinical supervision and consultation for therapists')}</dd></div>
    </dl>
    <div class="rv" style="margin-top:36px"><a class="btn btn-dark" href="contact.html">Get in touch</a></div>
   </div>
   <div class="stage rv" style="height:clamp(340px,40vw,470px)">
     <div class="ph cut-hex" data-sp="0.22" style="width:66%;height:74%;right:4%;top:0">
       <img loading="lazy" decoding="async" src="terrain-aerial.jpg" alt="Aerial view of green ridgelines and ravines">
     </div>
     <div class="geo g-frame" data-sp="-0.5" style="color:var(--ember);opacity:.6;width:190px;height:190px;left:0;top:22%"></div>
     <div class="ph" data-sp="0.8" style="width:150px;height:170px;left:14%;bottom:2%">
       <img loading="lazy" decoding="async" src="compass-map.jpg" alt="">
     </div>
     <div class="geo g-fill cut-tri" data-sp="-0.85" style="color:var(--ember);opacity:.85;width:82px;height:82px;right:8%;bottom:10%"></div>
   </div>
  </div>
</section>
"""

SERVICES = f"""
<section class="phead">
  <div class="geo g-dot" data-sp="0.4" style="color:rgba(205,155,98,.24);width:280px;height:280px;right:6%;top:0"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> &middot; Therapy</div>
    <span class="hand hand-xl" style="margin-left:-3px">Therapy</span>
    <h1 style="margin-top:6px">Individual counseling<br>for adults</h1>
    <p class="lead">Ongoing, conversational, and paced to you rather than to a protocol.</p>
  </div>
</section>

<section class="sec-sm lt">
  <div class="wrap">
    <div class="narrow rv"><span class="eyebrow">What people bring</span>
      <h2>Common starting points.</h2>
      <p style="margin-top:18px">This isn't a menu, and you don't need a diagnosis or a tidy summary to make an
        appointment. Most people arrive with something closer to "this isn't working and I can't
        tell you exactly why."</p>
    </div>
    <div class="three" style="margin-top:44px">
      <div class="card rv"><h3>Anxiety &amp; depression</h3><div class="hr"></div>
        <p>{F('Persistent worry, low mood, the exhausting work of holding it together in public. Both the immediate relief and the pattern underneath it.')}</p></div>
      <div class="card rv"><h3>Life transitions</h3><div class="hr"></div>
        <p>{F('Career changes, becoming a parent, the end of a relationship, grief, or moving into a chapter you did not plan for.')}</p></div>
      <div class="card rv"><h3>Identity &amp; meaning</h3><div class="hr"></div>
        <p>{F('Questions about faith, purpose, and who you are becoming &mdash; especially when the answer has started shifting.')}</p></div>
      <div class="card rv"><h3>Relationships</h3><div class="hr"></div>
        <p>{F('Family patterns, conflict that keeps repeating itself, boundaries, and the roles you learned early and never quite put down.')}</p></div>
      <div class="card rv"><h3>Burnout</h3><div class="hr"></div>
        <p>{F('Particularly common among helpers, clinicians, clergy, and caregivers &mdash; people practiced at attending to everyone else.')}</p></div>
      <div class="card rv"><h3>Self-knowledge</h3><div class="hr"></div>
        <p>{F('Work that is less about crisis and more about wanting to understand your own patterns before they choose for you.')}</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="geo g-ring geo-lg" data-sp="0.4" style="color:var(--brass);opacity:.22;width:480px;height:480px;right:-170px;top:6%"></div>
  <div class="geo g-hatch" data-sp="-0.45" style="color:rgba(154,166,174,.34);width:190px;height:250px;left:2%;bottom:8%"></div>
  <div class="wrap two">
    <div class="rv">
      <span class="eyebrow">The shape of it</span>
      <span class="hand hand-lg" style="margin:0 0 8px -4px">how it goes</span>
      <h2>Session by session.</h2>
    </div>
    <div class="rv">
      <dl class="dl">
        <div><dt>First contact</dt><dd>{F('A short phone call, at no charge, so you can ask questions and get a feel for whether this fits.')}</dd></div>
        <div><dt>First session</dt><dd>Mostly you talking. Some history, some present tense, and a conversation about what you'd want to be different.</dd></div>
        <div><dt>Frequency</dt><dd>{F('Weekly to begin with. Some people move to every other week once things settle.')}</dd></div>
        <div><dt>Length</dt><dd>{F('50 minutes.')}</dd></div>
        <div><dt>Format</dt><dd>{F('In person in Littleton, with telehealth available for Colorado residents.')}</dd></div>
        <div><dt>Ending</dt><dd>{F('Deliberately, and with a conversation about it &mdash; not by quietly drifting off the schedule.')}</dd></div>
      </dl>
      <div style="margin-top:32px;display:flex;gap:13px;flex-wrap:wrap">
        <a class="btn" href="contact.html">Book a consultation</a>
        <a class="btn" href="fees.html">Fees &amp; insurance</a>
      </div>
    </div>
  </div>
</section>

<section class="sec-sm lt lt2">
  <div class="geo g-dot" data-sp="0.28" style="color:rgba(38,51,59,.14);width:100%;height:100%;left:0;top:0"></div>
  <div class="geo g-ring geo-lg" data-sp="0.5" style="color:rgba(162,82,48,.34);width:380px;height:380px;right:-120px;top:-90px"></div>
  <div class="wrap narrow rv" style="margin:0 auto;text-align:center">
    <span class="eyebrow">Also available</span>
    <span class="hand hand-md">for clinicians</span>
    <h2 style="margin-top:4px">Consultation for therapists.</h2>
    <p class="lead" style="margin:18px auto 0">If you're a clinician rather than a prospective client, Kristi
      offers supervision and consultation drawing on six years inside counselor education.</p>
    <div style="margin-top:28px"><a class="btn btn-dark" href="consultation.html">Consultation &amp; supervision</a></div>
  </div>
</section>
"""

CONSULT = f"""
<section class="phead">
  <div class="geo g-dot" data-sp="0.4" style="color:rgba(205,155,98,.24);width:280px;height:280px;right:6%;top:0"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> &middot; Consultation</div>
    <span class="hand hand-xl" style="margin-left:-3px">Consultation</span>
    <h1 style="margin-top:6px">Supervision &amp; consultation<br>for clinicians</h1>
    <p class="lead">For therapists who want somewhere serious to bring the work.</p>
  </div>
</section>

<section class="sec-sm lt">
  <div class="wrap two-b">
    <div class="rv">
      <span class="eyebrow">Why Kristi</span>
      <h2>She taught this for a living.</h2>
      <p style="margin-top:20px">Most clinical supervisors are experienced therapists who took on supervision.
        Kristi's route was the other way round: six years at Denver Seminary, most recently as
        Associate Director of its PhD program in <strong>Counselor Education and Supervision</strong> &mdash;
        the doctorate that trains supervisors &mdash; while running her own practice throughout.</p>
      <p>So the questions she asks tend to be the ones underneath the case: what you were actually
        doing there, what you were avoiding, and whether your explanation would survive being said
        out loud to someone who knows the literature.</p>
    </div>
    <div class="stage rv" style="height:clamp(300px,34vw,400px)">
      <div class="ph cut-hex" data-sp="0.2" style="width:70%;height:92%;right:6%;top:2%">
        <img loading="lazy" decoding="async" src="compass-map.jpg" alt="A compass resting on a topographic map">
      </div>
      <div class="geo g-frame" data-sp="-0.5" style="color:var(--ember);opacity:.6;width:170px;height:170px;left:2%;bottom:4%"></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
  <div class="geo g-hatch" data-sp="0.5" style="color:rgba(205,155,98,.5);width:160px;height:210px;right:3%;top:6%"></div>
    <div class="narrow rv"><span class="eyebrow">Who it's for</span>
      <span class="hand hand-lg" style="margin:0 0 8px -4px">who comes</span>
      <h2>Three kinds of clinician.</h2></div>
    <div class="three" style="margin-top:44px">
      <div class="card rv"><span class="n">i</span><h3>Pre-licensure supervision</h3><div class="hr"></div>
        <p>{F('Required supervision toward Colorado LPC licensure, including documentation and hours.')} Structured, and treated as formation rather than paperwork.</p></div>
      <div class="card rv"><span class="n">ii</span><h3>Post-licensure consultation</h3><div class="hr"></div>
        <p>For clinicians who are licensed and want a place to think carefully about difficult cases, countertransference, and the parts of the work that don't fit a manual.</p></div>
      <div class="card rv"><span class="n">iii</span><h3>Groups &amp; organizations</h3><div class="hr"></div>
        <p>{F('Consultation for practices and organizations on clinical culture, clinician retention, and how supervision structures actually function day to day.')}</p></div>
    </div>
  </div>
</section>

<section class="sec-sm lt lt2">
  <div class="geo g-dot" data-sp="0.3" style="color:rgba(38,51,59,.13);width:100%;height:100%;left:0;top:0"></div>
  <div class="geo g-ring geo-lg" data-sp="0.45" style="color:rgba(162,82,48,.32);width:400px;height:400px;left:-140px;bottom:-120px"></div>
  <div class="wrap two">
    <div class="rv">
      <span class="eyebrow">Practical</span>
      <span class="hand hand-md" style="margin:0 0 6px -3px">the details</span>
      <h2>Format &amp; rates.</h2>
      <p style="margin-top:18px">{F('Individual and small-group consultation, in person in Littleton or online for Colorado clinicians.')}</p>
    </div>
    <div class="rv">
      <dl class="dl">
        <div><dt>Individual</dt><dd>{F('$— per hour')}</dd></div>
        <div><dt>Group</dt><dd>{F('$— per session, small groups')}</dd></div>
        <div><dt>Cadence</dt><dd>{F('Weekly, every other week, or monthly depending on what you need.')}</dd></div>
        <div><dt>Sliding scale</dt><dd>Available, and genuinely meant. Recent graduates are the reason it exists &mdash; mention it in your first email and that's the whole process.</dd></div>
      </dl>
      <div style="margin-top:30px"><a class="btn btn-dark" href="contact.html">Enquire about consultation</a></div>
    </div>
  </div>
</section>
"""

FEES = f"""
<section class="phead">
  <div class="geo g-dot" data-sp="0.4" style="color:rgba(205,155,98,.24);width:260px;height:260px;right:6%;top:0"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> &middot; Fees</div>
    <span class="hand hand-xl" style="margin-left:-3px">Fees</span>
    <h1 style="margin-top:6px">Fees &amp; insurance</h1>
    <p class="lead">Written plainly, because money is hard enough to bring up in a first phone call.</p>
  </div>
</section>

<section class="sec-sm lt">
  <div class="wrap two">
    <div class="rv">
      <span class="eyebrow">Rates</span>
      <h2>What sessions cost.</h2>
      <p style="margin-top:18px">{F('Rates below are current as of 2026 and are discussed before your first appointment, never after.')}</p>
    </div>
    <div class="rv">
      <dl class="dl">
        <div><dt>Individual therapy</dt><dd>{F('$— per 50-minute session')}</dd></div>
        <div><dt>Initial consultation</dt><dd>{F('Complimentary, by phone, about 15 minutes')}</dd></div>
        <div><dt>Clinical supervision</dt><dd>{F('$— per hour &middot; see Consultation')}</dd></div>
        <div><dt>Sliding scale</dt><dd>{F('A limited number of reduced-fee slots are held open. Ask &mdash; there is no form and no means testing.')}</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="sec">
  <div class="geo g-ring geo-lg" data-sp="0.4" style="color:var(--brass);opacity:.2;width:460px;height:460px;left:-160px;bottom:-120px"></div>
  <div class="wrap">
    <div class="narrow rv"><span class="eyebrow">Insurance</span>
      <span class="hand hand-lg" style="margin:0 0 8px -4px">coverage</span>
      <h2>What's accepted.</h2></div>
    <div class="three" style="margin-top:40px">
      <div class="card rv"><h3>Kaiser Permanente</h3><div class="hr"></div>
        <p>Kristi has been an affiliated Kaiser Permanente provider since 2024. {F('Coverage and copays depend on your specific plan &mdash; worth confirming with Kaiser directly before your first session.')}</p></div>
      <div class="card rv"><h3>Sondermind</h3><div class="hr"></div>
        <p>She also sees clients through Sondermind, which works with {F('a number of Colorado insurance plans')}. Booking through them may be the simplest route depending on your carrier.</p></div>
      <div class="card rv"><h3>Self-pay &amp; out-of-network</h3><div class="hr"></div>
        <p>{F('Self-pay is welcome. Superbills are provided on request so you can seek out-of-network reimbursement from your insurer.')}</p></div>
    </div>
    <div class="rv" style="margin-top:52px;position:relative;height:clamp(200px,22vw,270px)">
      <div class="ph" data-sp="0.15" style="width:52%;height:100%;left:0;top:0">
        <img loading="lazy" decoding="async" src="terrain-aerial.jpg" alt="">
      </div>
      <div class="ph cut-hex" data-sp="0.7" style="width:150px;height:168px;left:44%;top:14%">
        <img loading="lazy" decoding="async" src="kristi-iceberg.jpg" alt="">
      </div>
      <div class="geo g-frame" data-sp="-0.5" style="color:var(--brass);opacity:.7;width:180px;height:180px;right:6%;top:6%"></div>
      <div class="geo g-fill" data-sp="0.9" style="color:var(--ember-lt);opacity:.9;width:56px;height:56px;right:2%;bottom:4%;transform:rotate(-14deg)"></div>
    </div>
    <div class="rv" style="margin-top:44px;max-width:70ch">
      <p><strong>Worth knowing:</strong> using insurance requires a mental health diagnosis on file with your
      insurer. That is routine and often perfectly fine, but some people prefer to self-pay for
      privacy. Either choice is reasonable, and Kristi is happy to talk it through.</p>
    </div>
  </div>
</section>

<section class="sec-sm lt lt2">
  <div class="wrap two">
    <div class="rv">
      <span class="eyebrow">Policies</span>
      <h2>The fine print,<br>in plain words.</h2>
    </div>
    <div class="rv">
      <dl class="dl">
        <div><dt>Cancellations</dt><dd>{F('24 hours notice, or the session is charged in full. Genuine emergencies are treated as emergencies.')}</dd></div>
        <div><dt>Payment</dt><dd>{F('Due at the time of service. Card, HSA and FSA accepted.')}</dd></div>
        <div><dt>Good Faith Estimate</dt><dd>If you are uninsured or not using insurance, you are entitled to a written estimate of costs. <a href="good-faith-estimate.html" style="color:var(--ember);font-weight:600">Read more</a>.</dd></div>
      </dl>
    </div>
  </div>
</section>
"""

FAQ = f"""
<section class="phead">
  <div class="geo g-dot" data-sp="0.4" style="color:rgba(205,155,98,.24);width:260px;height:260px;right:6%;top:0"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> &middot; FAQ</div>
    <span class="hand hand-xl" style="margin-left:-3px">Questions</span>
    <h1 style="margin-top:6px">Before you call</h1>
    <p class="lead">The things people usually want to know and don't always ask.</p>
  </div>
</section>

<section class="sec-sm lt">
  <div class="geo g-dot" data-sp="0.3" style="color:rgba(38,51,59,.11);width:100%;height:100%;left:0;top:0"></div>
  <div class="geo g-ring geo-lg" data-sp="0.45" style="color:rgba(162,82,48,.28);width:420px;height:420px;right:-150px;top:4%"></div>
  <div class="geo g-fill cut-tri" data-sp="-0.7" style="color:var(--brass);opacity:.75;width:96px;height:96px;left:1%;top:12%"></div>
  <div class="wrap">
    <div class="faq-list rv" style="margin:0 auto">
      <details open><summary>I've never done therapy before. What actually happens?</summary>
        <div class="body"><p>The first session is mostly you talking. Kristi will ask what brought you in, some
        background, and what you'd want to be different. You do not need a prepared summary, and you
        will not be handed a treatment plan at the end of the hour.</p></div></details>
      <details><summary>How long does this take?</summary>
        <div class="body"><p>{F('It depends entirely on what you are working on. Some people come for a few months around a specific transition; others stay longer because the work keeps being useful. It gets discussed openly rather than assumed.')}</p></div></details>
      <details><summary>Do you take my insurance?</summary>
        <div class="body"><p>Kristi is an affiliated Kaiser Permanente provider and also sees clients through
        Sondermind. {F('For other carriers, self-pay with a superbill for out-of-network reimbursement is usually the route.')} See <a href="fees.html" style="color:var(--ember);font-weight:600">Fees &amp; insurance</a>.</p></div></details>
      <details><summary>Do you offer telehealth?</summary>
        <div class="body"><p>{F('Yes, for clients located in Colorado. Some people do all their sessions online, others mix. In-person is in Littleton.')}</p></div></details>
      <details><summary>Is what I say confidential?</summary>
        <div class="body"><p>Yes, with the legal exceptions every Colorado therapist shares: risk of serious harm
        to yourself or someone else, suspected abuse or neglect of a child or at-risk adult, and court
        orders. Kristi will go through this in the first session rather than burying it in paperwork.</p></div></details>
      <details><summary>What if we're not a good fit?</summary>
        <div class="body"><p>Then she'll say so and help you find someone better suited. Fit matters more than almost
        anything else in this work, and it is not an insult to either party when it isn't there.</p></div></details>
      <details><summary>Do you work with couples or families?</summary>
        <div class="body"><p>{F('Kristi primarily sees individual adults. Ask when you call &mdash; if it is not a fit she keeps a referral list of trusted clinicians who do this work.')}</p></div></details>
      <details><summary>I'm a therapist looking for supervision, not therapy.</summary>
        <div class="body"><p>That's a large part of the practice. See <a href="consultation.html" style="color:var(--ember);font-weight:600">Consultation &amp; supervision</a>.</p></div></details>
      <details><summary>What if I'm in crisis right now?</summary>
        <div class="body"><p>This website isn't the right channel and email isn't monitored around the clock. Call or
        text <strong>988</strong> for the Suicide &amp; Crisis Lifeline, or call 911. Colorado Crisis Services is
        also available at <strong>1-844-493-8255</strong>.</p></div></details>
    </div>
    <div class="rv" style="text-align:center;margin-top:44px"><a class="btn btn-dark" href="contact.html">Still have a question</a></div>
  </div>
</section>
"""

CONTACT = f"""
<section class="phead">
  <div class="geo g-ring geo-lg" data-sp="0.4" style="color:var(--brass);opacity:.24;width:480px;height:480px;left:-180px;top:-110px"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> &middot; Contact</div>
    <span class="hand hand-xl" style="margin-left:-3px">Say hello</span>
    <h1 style="margin-top:6px">Get in touch</h1>
    <p class="lead">A phone call or a short email is always welcome, and there's no form to fill in first.</p>
  </div>
</section>

<section class="sec-sm lt">
  <div class="wrap two">
    <div class="rv">
      <div class="cbox">
        <span class="eyebrow">Direct</span>
        <h2 style="font-size:26px">Call, text, or email.</h2>
        <p style="margin-top:18px;font-size:19px"><a href="tel:{PHONE_T}">{PHONE_H}</a></p>
        <p style="font-size:17px"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p style="margin-top:20px;font-size:15px">{F('Kristi returns messages within one business day. If you are reaching out about consultation or supervision rather than therapy, mention that and she will send rates and current availability.')}</p>
      </div>
    </div>
    <div class="rv">
      <div class="cbox">
        <span class="eyebrow">Visit</span>
        <h2 style="font-size:26px">The office.</h2>
        <p style="margin-top:18px;font-size:17px">{ADDR1}<br>{ADDR2}</p>
        <p style="margin-top:16px;font-size:15px">{F('Free parking on site. The suite is on the second floor with elevator access.')}</p>
        <p style="margin-top:18px"><a href="https://maps.google.com/?q=5808+S+Rapp+St+Ste+235+Littleton+CO+80120" rel="noopener">Open in Maps</a></p>
      </div>
    </div>
  </div>
  <div class="wrap rv" style="margin-top:44px;position:relative;height:clamp(210px,24vw,300px)">
    <div class="ph" data-sp="0.14" style="width:56%;height:100%;right:0;top:0">
      <img loading="lazy" decoding="async" src="kristi-iceberg.jpg" alt="">
    </div>
    <div class="ph cut-hex" data-sp="0.75" style="width:158px;height:176px;left:34%;top:12%">
      <img loading="lazy" decoding="async" src="compass-map.jpg" alt="">
    </div>
    <div class="geo g-frame" data-sp="-0.5" style="color:var(--ember);opacity:.65;width:200px;height:200px;left:2%;top:8%"></div>
    <div class="geo g-hatch" data-sp="0.9" style="color:rgba(205,155,98,.6);width:120px;height:150px;left:22%;bottom:0"></div>
  </div>
  <div class="wrap rv" style="margin-top:36px">
    <div class="cbox" style="border-color:var(--ember)">
      <span class="eyebrow" style="color:var(--ember)">If you need help now</span>
      <p style="margin-top:6px">This practice does not provide emergency services and email is not monitored
      around the clock. If you are in crisis or thinking about harming yourself, call or text
      <strong>988</strong> for the Suicide &amp; Crisis Lifeline, call <strong>911</strong>, or reach
      Colorado Crisis Services at <strong>1-844-493-8255</strong>.</p>
    </div>
  </div>
</section>
"""

GFE = f"""
<section class="phead">
  <div class="wrap">
    <div class="geo g-fill cut-tri" data-sp="-0.6" style="color:var(--brass);opacity:.8;width:88px;height:88px;right:6%;top:10%"></div>
    <div class="crumb"><a href="index.html">Home</a> &middot; Good Faith Estimate</div>
    <span class="hand hand-lg" style="margin-left:-3px">Your right to</span>
    <h1 style="margin-top:2px">A Good Faith Estimate</h1>
  </div>
</section>

<section class="sec-sm lt">
  <div class="geo g-dot" data-sp="0.28" style="color:rgba(38,51,59,.11);width:100%;height:100%;left:0;top:0"></div>
  <div class="geo g-ring geo-lg" data-sp="0.4" style="color:rgba(162,82,48,.26);width:360px;height:360px;right:-130px;top:8%"></div>
  <div class="wrap narrow rv">
    <p class="lead">Under the federal No Surprises Act, you have the right to receive a written estimate of
      what your care will cost if you are uninsured or are not using insurance.</p>
    <ul class="plain" style="margin-top:26px">
      <li>You have the right to receive a Good Faith Estimate explaining how much your care will cost.</li>
      <li>Providers must give people who are uninsured or not using insurance a written estimate of the
        expected charges for services, including psychotherapy.</li>
      <li>You can ask for a Good Faith Estimate before scheduling, and you are entitled to one for any
        service on request.</li>
      <li>If you receive a bill that is at least $400 more than your Good Faith Estimate, you can dispute
        it through the federal patient&ndash;provider dispute resolution process.</li>
      <li>Keep a copy of your estimate.</li>
    </ul>
    <p style="margin-top:26px">Because psychotherapy is ongoing and its length is decided collaboratively, an
      estimate is typically given as a per-session rate together with an anticipated range of sessions,
      and is revisited if things change.</p>
    <p style="margin-top:16px">For questions or more information, visit
      <a href="https://www.cms.gov/nosurprises" rel="noopener" style="color:var(--ember);font-weight:600">cms.gov/nosurprises</a>
      or call 1-800-985-3059. To request an estimate, contact Kristi at
      <a href="mailto:{EMAIL}" style="color:var(--ember);font-weight:600">{EMAIL}</a>.</p>
    <div style="margin-top:34px"><a class="btn btn-dark" href="contact.html">Request an estimate</a></div>
  </div>
</section>
"""

PRIVACY = f"""
<section class="phead">
  <div class="wrap">
    <div class="geo g-fill cut-tri" data-sp="-0.6" style="color:var(--brass);opacity:.8;width:88px;height:88px;right:6%;top:10%"></div>
    <div class="crumb"><a href="index.html">Home</a> &middot; Privacy</div>
    <span class="hand hand-lg" style="margin-left:-3px">Privacy &amp;</span>
    <h1 style="margin-top:2px">Notices</h1>
  </div>
</section>

<section class="sec-sm lt">
  <div class="geo g-dot" data-sp="0.28" style="color:rgba(38,51,59,.11);width:100%;height:100%;left:0;top:0"></div>
  <div class="geo g-ring geo-lg" data-sp="0.4" style="color:rgba(162,82,48,.26);width:360px;height:360px;left:-130px;bottom:4%"></div>
  <div class="wrap narrow rv">
    <h3>Confidentiality</h3>
    <p style="margin-top:12px">What you say in session is confidential and protected under Colorado law and HIPAA.
      There are limited legal exceptions that apply to every licensed therapist in Colorado: when there
      is a serious risk of harm to you or someone else, when abuse or neglect of a child or at-risk
      adult is suspected, and when records are compelled by a court. These are reviewed with you at
      the start of treatment.</p>

    <h3 style="margin-top:32px">This website</h3>
    <p style="margin-top:12px">{F('This site does not use analytics, advertising trackers, or cookies. Nothing you do here is recorded.')}
      Fonts are loaded from Google Fonts, which means Google receives a request from your browser when
      the page loads.</p>

    <h3 style="margin-top:32px">Email &amp; text</h3>
    <p style="margin-top:12px">Ordinary email and text messages are not secure and are not a confidential channel.
      Please keep anything you send that way brief and logistical &mdash; scheduling rather than clinical
      detail. Email is not monitored around the clock and should never be used in an emergency.</p>

    <h3 style="margin-top:32px">Records</h3>
    <p style="margin-top:12px">{F('Clinical records are maintained securely and retained as required by Colorado law. You have the right to request access to your record.')}</p>

    <h3 style="margin-top:32px">Questions</h3>
    <p style="margin-top:12px">Contact Kristi at <a href="mailto:{EMAIL}" style="color:var(--ember);font-weight:600">{EMAIL}</a>
      or {PHONE_H}.</p>

    <p style="margin-top:30px;font-size:14px;color:rgba(38,51,59,.6)">{F('Last updated: [date]')}</p>
  </div>
</section>
"""

PAGES = [
 ("index.html","Commend Counseling &middot; Kristi Cobble, LPC &middot; Littleton, Colorado",
  "Counseling for adults and clinical consultation for therapists in Littleton, Colorado. Kristi Cobble, LPC, in practice since 2016.", HOME, True),
 ("about.html","About Kristi Cobble, LPC &middot; Commend Counseling",
  "Kristi Cobble is a Licensed Professional Counselor in Littleton, Colorado, in private practice since 2016 and adjunct faculty at Denver Seminary.", ABOUT, False),
 ("services.html","Individual Therapy in Littleton, CO &middot; Commend Counseling",
  "Individual counseling for adults in Littleton, Colorado. Anxiety, depression, life transitions, relationships, and burnout.", SERVICES, False),
 ("consultation.html","Clinical Supervision &amp; Consultation for Therapists &middot; Commend Counseling",
  "Clinical supervision and consultation for Colorado therapists, from a former Associate Director of a PhD program in Counselor Education and Supervision.", CONSULT, False),
 ("fees.html","Fees &amp; Insurance &middot; Commend Counseling",
  "Session rates, Kaiser Permanente and Sondermind, self-pay, superbills, and sliding scale availability.", FEES, False),
 ("faq.html","Frequently Asked Questions &middot; Commend Counseling",
  "What happens in a first session, insurance, telehealth, confidentiality, and what to do in a crisis.", FAQ, False),
 ("contact.html","Contact &middot; Commend Counseling &middot; Littleton, CO",
  "Call, text, or email Kristi Cobble, LPC. Office at 5808 South Rapp Street, Suite 235, Littleton, Colorado.", CONTACT, False),
 ("good-faith-estimate.html","Good Faith Estimate &middot; Commend Counseling",
  "Your right to a Good Faith Estimate under the federal No Surprises Act.", GFE, False),
 ("privacy.html","Privacy &amp; Notices &middot; Commend Counseling",
  "Confidentiality, website privacy, email security, and records.", PRIVACY, False),
]

here = os.path.dirname(os.path.abspath(__file__))
fill_total = 0
for slug,title,desc,body,is_home in PAGES:
    CUR = ' aria-current="page"'
    nav = "".join(
        '<a href="%s"%s>%s</a>' % (h, CUR if h == slug else '', lab)
        for h, lab in NAV)
    fnav = "".join(f'<li><a href="{h}">{lab}</a></li>' for h,lab in NAV[1:])
    html = SHELL.format(
        title=title, desc=desc, slug="" if is_home else slug, site=SITE,
        schema=SCHEMA if is_home else "", nav=nav, fnav=fnav, body=body,
        phone_h=PHONE_H, phone_t=PHONE_T, email=EMAIL, addr1=ADDR1, addr2=ADDR2)
    n = html.count('class="fill"')
    fill_total += n
    open(os.path.join(here,slug),"w",encoding="utf-8").write(html)
    print(f"  {slug:28} {len(html)//1024:>3} KB   {n:>2} to confirm")

print(f"\n{len(PAGES)} pages, {fill_total} placeholders total")
