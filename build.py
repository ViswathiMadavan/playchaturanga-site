#!/usr/bin/env python3
"""Writes the site's pages. Edit the text here, run `python3 build.py`, commit the result.
Each page is plain HTML with one shared stylesheet; there are no scripts, cookies or trackers."""
import os

SUPPORT = "support@playchaturanga.com"
PRIVACY = "privacy@playchaturanga.com"
UPDATED = "November 24, 2026"
NAV = [("/", "Home"), ("/support/", "Support"), ("/privacy/", "Privacy"), ("/terms/", "Terms")]


def mail(address):
    return '<a href="mailto:%s">%s</a>' % (address, address)


def page(path, title, desc, body):
    links = []
    for href, text in NAV:
        current = ' aria-current="page"' if href == path else ""
        links.append('<a href="%s"%s>%s</a>' % (href, current, text))
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header>
<a class="name" href="/">Chaturanga</a>
<nav aria-label="Site">%s</nav>
</header>
<main>
%s
</main>
<footer>
<a href="/support/">Support</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a>
<p>Chaturanga is made by an independent developer. Contact: %s</p>
</footer>
</body>
</html>
""" % (title, desc, "".join(links), body.strip(), mail(SUPPORT))
    out = "index.html" if path == "/" else os.path.join(path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        f.write(html)


page("/", "Chaturanga — chess, the ancient game it came from, and four-player play",
     "Chaturanga is an app for chess, the ancient Indian game chess came from, and four-player games, with an opponent that matches your level.",
     """
<section class="hero">
<h1>Chaturanga</h1>
<p class="lead">Chess, the ancient game it came from, and four armies on one board.</p>
<p>Chaturanga is an app for iPhone and iPad. Pick the game you want and start playing: the app chooses an opponent at your level and moves it as you improve.</p>
</section>
<ul class="cards">
<li><strong>Chess</strong>The classic game.</li>
<li><strong>Chaturanga</strong>The ancient Indian game chess came from, with its own pieces and rules.</li>
<li><strong>Four-player</strong>Four armies on one board, every player for themselves.</li>
<li><strong>Four-player teams</strong>Two against two.</li>
</ul>
<h2>What is in it</h2>
<ul>
<li>A computer opponent for every game, picked for your level.</li>
<li>Puzzles, openings and endgames to practise, chosen for you.</li>
<li>A review of each finished chess and chaturanga game.</li>
<li>A simpler, picture-based version for children.</li>
<li>Everything works without a connection and without an account.</li>
</ul>
<h2>Availability</h2>
<p>Chaturanga is being prepared for the App Store. This page will link to it when it is released.</p>
<h2>Questions</h2>
<p>See <a href="/support/">Support</a>, or write to %s.</p>
""" % mail(SUPPORT))

page("/privacy/", "Privacy Policy — Chaturanga",
     "What the Chaturanga app stores, what can leave your device, and your choices.",
     """
<h1>Privacy Policy</h1>
<p class="updated">Last updated: {updated}</p>
<p>This policy covers the Chaturanga app for iPhone and iPad and this website. If anything in it is unclear, write to {privacy}.</p>
<div class="summary">
<ul>
<li>There is no account. Your games, ratings, progress and settings are stored only on your device.</li>
<li>The app has no advertising and does not track you.</li>
<li>Nothing is sent anywhere unless you turn on crash reports or choose to email us.</li>
<li>We do not sell or share personal information.</li>
</ul>
</div>

<h2 id="on-device">What stays on your device</h2>
<p>The app stores the following on your device and nowhere else:</p>
<ul>
<li>The games you play and their reviews.</li>
<li>Your rating in each game, your puzzle rating, and your progress in puzzles, lessons, openings and endgames.</li>
<li>Your settings, including which games you chose and whether the app is set up for a child or a grown-up.</li>
<li>Problem reports you have written but not sent.</li>
</ul>
<p>The app asks for no name, email address, birth date, location, contacts, photos, camera or microphone. All play, including the computer opponent and game review, runs on the device.</p>

<h2 id="leaves-device">What can leave your device</h2>
<p><strong>Crash reports, only if you turn them on.</strong> The setting "Share crash reports" is off unless you switch it on. When it is on and the app crashes, a report is sent through Firebase Crashlytics, a service run by Google. A report contains technical details of the crash, your device model, system version, app version and an identifier for the app installation. It does not contain your name, email address or your games. Google processes these reports for us under its own terms and keeps them for a limited period (90 days at the time of writing). You can switch the setting off at any time in the app.</p>
<p><strong>Problem reports and emails, only if you send them.</strong> "Report a problem" in the app prepares an email in your own mail app. It contains what you wrote and, if you leave "Attach device details" on, your device model, system version, app version and the app's recent activity log. Nothing is sent until you press Send. If you email us, we receive your email address and whatever you write, and we use them only to answer you and fix the problem.</p>
<p><strong>Information from Apple.</strong> Apple gives app developers combined figures such as download counts and crash counts, and only from people who agreed in their device settings to share them with developers. These figures do not identify anyone.</p>

<h2 id="do-not">What we do not do</h2>
<ul>
<li>No advertising, and no advertising identifiers.</li>
<li>No tracking across apps or websites.</li>
<li>No usage analytics: the app does not report what you tap or play.</li>
<li>No accounts, sign-in or online play in this version.</li>
<li>No purchases in this version.</li>
</ul>

<h2 id="do-not-sell">Selling and sharing</h2>
<p>We do not sell personal information and do not share it for advertising. The only outside party that processes any data from the app is Google, for crash reports, and only when you have turned them on.</p>

<h2 id="children">Children</h2>
<p>Children can use the app, and it has a version designed for them. The app does not knowingly collect personal information from children, or from anyone: it works without an account and asks for no personal details. In the child version, settings, links that leave the app and sending email sit behind a question meant for a grown-up. "Share crash reports" is off unless a grown-up switches it on.</p>
<p>If you believe a child has sent us personal information by email, write to {privacy} and we will delete it.</p>

<h2 id="choices">Your choices</h2>
<ul>
<li><strong>Crash reports:</strong> switch "Share crash reports" on or off in the app at any time.</li>
<li><strong>Your games and progress:</strong> delete single games in the app's game list, or delete the app to remove everything it stored.</li>
<li><strong>Emails you sent us:</strong> ask us to delete them at {privacy}.</li>
</ul>
<p id="rights"><span id="gdpr"></span><span id="india"></span><span id="russia"></span><span id="international"></span>Depending on where you live, you may have legal rights to see, correct or delete personal information held about you, and to object to how it is used. Because the app keeps your data on your device and we hold no account for you, the only personal information we can hold is email you sent us. To use any of these rights, write to {privacy}; we answer within 30 days.</p>

<h2 id="website">This website</h2>
<p>This website sets no cookies and uses no analytics. It is hosted by GitHub Pages and served through Cloudflare, which, like any web host, process technical data such as your IP address in order to deliver the pages. Email to our addresses is forwarded by Cloudflare to our inbox.</p>

<h2 id="changes">Changes to this policy</h2>
<p>If the app starts to handle data differently, for example if accounts, online play or purchases are added, this policy will be updated before that version is released, and the date at the top will change.</p>

<h2 id="contact">Contact</h2>
<p>{privacy}</p>
""".format(updated=UPDATED, privacy=mail(PRIVACY)))

page("/terms/", "Terms of Use — Chaturanga",
     "The terms for using the Chaturanga app and this website.",
     """
<h1>Terms of Use</h1>
<p class="updated">Last updated: {updated}</p>
<p>These terms apply to the Chaturanga app and this website. By using the app you agree to them. If you do not agree, please do not use the app.</p>

<h2>Using the app</h2>
<p>You may install and use the app on devices you own or control, for your own personal, non-commercial use, as allowed by the App Store's usage rules. A parent or guardian should agree to these terms on behalf of a child who uses the app.</p>

<h2>What belongs to us</h2>
<p>The app, its game engine and evaluation files, its puzzles, lessons, artwork and text belong to the developer of Chaturanga and are protected by law. You may not copy, extract, reverse engineer, modify, redistribute or sell any part of the app, except where the law gives you a right that these terms cannot remove.</p>

<h2>What belongs to you</h2>
<p>The games you play are yours. The app stores them on your device, and you can export or delete them.</p>

<h2>Fair use</h2>
<p>Please do not use the app in a way that breaks the law, or try to interfere with how it works.</p>

<h2>No warranty</h2>
<p>The app is provided as it is. We work to keep it accurate and reliable, but we do not promise that it is free of mistakes, that its analysis of a game is always right, or that it will always be available. To the extent the law allows, we give no warranties of any kind.</p>

<h2>Limit of liability</h2>
<p>To the extent the law allows, the developer of Chaturanga is not liable for indirect or consequential losses arising from your use of the app, and our total liability is limited to the amount you paid for the app in the twelve months before the claim. Nothing in these terms limits liability that cannot be limited by law.</p>

<h2>The App Store</h2>
<p>These terms are between you and the developer of Chaturanga, not Apple. Apple is not responsible for the app or for support. Where these terms say nothing, Apple's standard Licensed Application End User License Agreement applies.</p>

<h2>Changes</h2>
<p>We may update these terms when the app changes, for example if accounts, online play or purchases are added. The date at the top shows the latest version. Continuing to use the app after a change means you accept the updated terms.</p>

<h2>Contact</h2>
<p>{support}</p>
""".format(updated=UPDATED, support=mail(SUPPORT)))

page("/support/", "Support — Chaturanga",
     "Help with the Chaturanga app: common questions and how to reach us.",
     """
<h1>Support</h1>
<p>Write to {support}. We read every message and aim to answer within a few days.</p>
<p>The fastest way to report something that went wrong is inside the app: open <strong>Me</strong>, then <strong>Report a problem</strong>. It prepares an email with the details we need.</p>

<h2>Common questions</h2>
<h3>How is my opponent chosen?</h3>
<p>The app picks a level you can beat about six games in ten and moves it as you improve. <strong>Easier</strong> and <strong>Harder</strong> on the home screen shift it one step, and <strong>Game options</strong> lets you choose any level.</p>
<h3>What is my rating?</h3>
<p>Each game has its own rating, kept on your device. It moves after every finished game against the computer. The first few games move it faster while the app finds your level.</p>
<h3>How are puzzles chosen?</h3>
<p>Puzzles have their own rating. Solving one with no wrong move and no hint raises it; a wrong first move or a hint lowers it. The next puzzle is picked close to that rating.</p>
<h3>How do I switch games or add one?</h3>
<p>Tap a game at the top of the home screen. Add or hide games under <strong>Me</strong>, then <strong>Games shown</strong>. A hidden game keeps its rating and history.</p>
<h3>How do I set the app up for a child?</h3>
<p>Under <strong>Me</strong>, set <strong>Who is playing</strong> to <strong>A child</strong>. The child version uses large picture tiles, shows no rating number, and keeps settings behind a question for a grown-up.</p>
<h3>Where are my past games?</h3>
<p>Under <strong>Me</strong>, then <strong>My games</strong>. Open any game to replay it; chess and chaturanga games also have a move-by-move review.</p>
<h3>Does the app need a connection or an account?</h3>
<p>No. Everything runs on your device, and there is nothing to sign in to.</p>
<h3>How do I delete my data?</h3>
<p>Everything the app stores is on your device. Delete single games in <strong>My games</strong>, or delete the app to remove all of it. See the <a href="/privacy/">Privacy Policy</a> for details.</p>
<h3>I have a new phone. Where is my progress?</h3>
<p>Progress is stored on the device and is included in a device backup. If you set up the new phone from a backup of the old one, your games and ratings should come with it.</p>
""".format(support=mail(SUPPORT)))
print("pages written")
