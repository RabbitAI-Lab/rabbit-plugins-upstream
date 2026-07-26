/* Football hub app. Reads window.HUB_DATA from data.js. No frameworks. */
(function () {
  "use strict";

  var DATA = window.HUB_DATA || {};
  var LEAGUE = DATA.league || { id: "unknown", name: "League", fullName: "League", brandColor: "#00ff87" };
  var TEAMS = DATA.teams || [];
  var STORE_KEY = "hub_team_" + LEAGUE.id;
  var currentFormation = "433";

  var $ = function (id) { return document.getElementById(id); };

  /* ---------- helpers ---------- */

  function parseTs(ts) {
    // TheSportsDB timestamps are naive UTC.
    return ts ? new Date(ts.replace(" ", "T") + "Z") : null;
  }

  var dFmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Africa/Johannesburg", day: "2-digit", month: "2-digit", year: "numeric"
  });
  var tFmt = new Intl.DateTimeFormat("en-GB", {
    timeZone: "Africa/Johannesburg", hour: "2-digit", minute: "2-digit", hour12: false
  });

  function fmtDate(ts) { var d = parseTs(ts); return d ? dFmt.format(d) : ""; }
  function fmtTime(ts) { var d = parseTs(ts); return d ? tFmt.format(d) + " SAST" : ""; }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function teamById(id) {
    for (var i = 0; i < TEAMS.length; i++) if (TEAMS[i].id === id) return TEAMS[i];
    return null;
  }

  function scorers(ev) {
    var bits = [];
    if (ev.homeGoals) bits.push(ev.home + ": " + ev.homeGoals);
    if (ev.awayGoals) bits.push(ev.away + ": " + ev.awayGoals);
    return bits.join(" | ");
  }

  /* ---------- theming ---------- */

  function applyTheme(team) {
    var r = document.documentElement.style;
    if (team) {
      r.setProperty("--c1", team.colors[0] || LEAGUE.brandColor || "#00ff87");
      r.setProperty("--c2", team.colors[1] || "#3d195b");
      r.setProperty("--c3", team.colors[2] || "#0a0e14");
    } else {
      r.setProperty("--c1", LEAGUE.brandColor || "#00ff87");
      r.setProperty("--c2", "#3d195b");
      r.setProperty("--c3", "#0a0e14");
    }
  }

  function renderHero(team) {
    var crest = $("heroCrest"), name = $("heroName"), meta = $("heroMeta"),
        tag = $("heroTag"), cta = $("heroCta");
    if (team) {
      if (team.badge) { crest.src = team.badge; crest.alt = team.name + " crest"; crest.classList.remove("hidden"); }
      else crest.classList.add("hidden");
      name.textContent = team.name;
      tag.textContent = "YOUR CLUB";
      var bits = [];
      if (team.stadium) bits.push(team.stadium);
      if (team.formed) bits.push("Founded " + team.formed);
      meta.textContent = bits.join("  ·  ");
      cta.classList.add("hidden");
    } else {
      crest.classList.add("hidden");
      name.textContent = LEAGUE.name;
      tag.textContent = "YOUR LEAGUE";
      meta.textContent = "Pick your club and the whole page turns your colours.";
      cta.classList.remove("hidden");
    }
  }

  /* ---------- picker ---------- */

  function renderPicker(selectedId) {
    var grid = $("pickerGrid");
    grid.innerHTML = "";
    TEAMS.forEach(function (t) {
      var d = document.createElement("div");
      d.className = "pick" + (t.id === selectedId ? " active" : "");
      d.innerHTML = (t.badge ? '<img src="' + esc(t.badge) + '" alt="' + esc(t.name) + ' crest" loading="lazy">' : "") +
        "<span>" + esc(t.name) + "</span>";
      d.addEventListener("click", function () { selectTeam(t.id); });
      grid.appendChild(d);
    });
  }

  /* ---------- fixtures & results ---------- */

  function fixtureCard(ev, big) {
    var card = document.createElement("div");
    card.className = "glass fcard";
    var mid;
    if (ev.homeScore != null && ev.awayScore != null) {
      mid = '<div class="fscore">' + ev.homeScore + " - " + ev.awayScore + "</div>";
      var sc = scorers(ev);
      if (sc) mid += '<div class="fscorers">' + esc(sc) + "</div>";
    } else {
      mid = '<div class="fteams"><span class="fvs">Kick-off</span><span>' + esc(fmtTime(ev.timestamp)) + "</span></div>";
    }
    card.innerHTML =
      '<div class="fdate">' + esc(fmtDate(ev.timestamp)) + "</div>" +
      '<div class="fteams"><span>' + esc(ev.home) + '</span><span class="fvs">vs</span><span>' + esc(ev.away) + "</span></div>" +
      mid +
      (ev.venue ? '<div class="fvenue">' + esc(ev.venue) + "</div>" : "");
    if (big) card.classList.add("result-card");
    return card;
  }

  function miniCard(ev) {
    var d = document.createElement("div");
    d.className = "mini";
    var score = (ev.homeScore != null && ev.awayScore != null)
      ? ev.homeScore + " - " + ev.awayScore
      : fmtTime(ev.timestamp);
    d.innerHTML = '<div class="mdate">' + esc(fmtDate(ev.timestamp)) + "</div>" +
      '<div class="mteams">' + esc(ev.home) + " v " + esc(ev.away) + "</div>" +
      '<div class="mscore">' + esc(score) + "</div>";
    return d;
  }

  function emptyNote(el, msg) {
    el.innerHTML = "";
    var d = document.createElement("div");
    d.className = "glass empty-note";
    d.textContent = msg;
    el.appendChild(d);
  }

  function renderFixtures(team) {
    var clubBox = $("clubFixtures");
    clubBox.innerHTML = "";
    var tf = (DATA.teamFixtures || {})[team.id] || { next: [], past: [] };
    if (tf.next.length) {
      tf.next.forEach(function (ev) { clubBox.appendChild(fixtureCard(ev)); });
    } else {
      emptyNote(clubBox, "No upcoming fixtures listed for " + team.name + " right now. Check back soon.");
    }
    var strip = $("leagueFixtures");
    strip.innerHTML = "";
    var lf = DATA.leagueFixtures || [];
    if (lf.length) lf.forEach(function (ev) { strip.appendChild(miniCard(ev)); });
    else emptyNote(strip, "No league fixtures listed right now.");
  }

  function renderResults(team) {
    var tf = (DATA.teamFixtures || {})[team.id] || { past: [] };
    var card = $("resultCard");
    card.innerHTML = "";
    var wText = $("writeupText");
    if (tf.past.length) {
      card.appendChild(fixtureCard(tf.past[0]));
      var w = (DATA.writeups || {})[team.id];
      wText.textContent = w || "No write-up for this one yet.";
    } else {
      card.innerHTML = '<div class="empty-note">No recent results listed for ' + esc(team.name) + ".</div>";
      wText.textContent = "Once the season gets going, match notes land here after every game.";
    }
    var strip = $("leagueResults");
    strip.innerHTML = "";
    var lr = DATA.leagueResults || [];
    if (lr.length) lr.forEach(function (ev) { strip.appendChild(miniCard(ev)); });
    else emptyNote(strip, "No league results listed right now.");
  }

  /* ---------- formation ---------- */

  var FORMATIONS = {
    "433": [
      { x: 200, y: 575, label: "GK", pos: "Goalkeeper" },
      { x: 66, y: 468, label: "LB", pos: "Defender" },
      { x: 156, y: 488, label: "CB", pos: "Defender" },
      { x: 244, y: 488, label: "CB", pos: "Defender" },
      { x: 334, y: 468, label: "RB", pos: "Defender" },
      { x: 108, y: 338, label: "CM", pos: "Midfielder" },
      { x: 200, y: 355, label: "CM", pos: "Midfielder" },
      { x: 292, y: 338, label: "CM", pos: "Midfielder" },
      { x: 78, y: 192, label: "LW", pos: "Forward" },
      { x: 200, y: 165, label: "ST", pos: "Forward" },
      { x: 322, y: 192, label: "RW", pos: "Forward" }
    ],
    "442": [
      { x: 200, y: 575, label: "GK", pos: "Goalkeeper" },
      { x: 66, y: 468, label: "LB", pos: "Defender" },
      { x: 156, y: 488, label: "CB", pos: "Defender" },
      { x: 244, y: 488, label: "CB", pos: "Defender" },
      { x: 334, y: 468, label: "RB", pos: "Defender" },
      { x: 62, y: 330, label: "LM", pos: "Midfielder" },
      { x: 152, y: 348, label: "CM", pos: "Midfielder" },
      { x: 248, y: 348, label: "CM", pos: "Midfielder" },
      { x: 338, y: 330, label: "RM", pos: "Midfielder" },
      { x: 148, y: 185, label: "ST", pos: "Forward" },
      { x: 252, y: 185, label: "ST", pos: "Forward" }
    ],
    "352": [
      { x: 200, y: 575, label: "GK", pos: "Goalkeeper" },
      { x: 108, y: 482, label: "CB", pos: "Defender" },
      { x: 200, y: 495, label: "CB", pos: "Defender" },
      { x: 292, y: 482, label: "CB", pos: "Defender" },
      { x: 58, y: 352, label: "LWB", pos: "Midfielder" },
      { x: 132, y: 322, label: "CM", pos: "Midfielder" },
      { x: 200, y: 350, label: "CM", pos: "Midfielder" },
      { x: 268, y: 322, label: "CM", pos: "Midfielder" },
      { x: 342, y: 352, label: "RWB", pos: "Midfielder" },
      { x: 148, y: 185, label: "ST", pos: "Forward" },
      { x: 252, y: 185, label: "ST", pos: "Forward" }
    ]
  };

  function pitchMarkings() {
    return '' +
      '<rect x="0" y="0" width="400" height="620" rx="18" fill="#0d2b1a"/>' +
      '<g opacity="0.16">' +
      '<rect x="20" y="20" width="60" height="580" fill="#1d5c35"/>' +
      '<rect x="140" y="20" width="60" height="580" fill="#1d5c35"/>' +
      '<rect x="260" y="20" width="60" height="580" fill="#1d5c35"/>' +
      '</g>' +
      '<g fill="none" stroke="rgba(255,255,255,0.75)" stroke-width="2.5">' +
      '<rect x="20" y="20" width="360" height="580" rx="4"/>' +
      '<line x1="20" y1="310" x2="380" y2="310"/>' +
      '<circle cx="200" cy="310" r="55"/>' +
      '<rect x="90" y="20" width="220" height="100"/>' +
      '<rect x="140" y="20" width="120" height="45"/>' +
      '<rect x="90" y="500" width="220" height="100"/>' +
      '<rect x="140" y="555" width="120" height="45"/>' +
      '<path d="M 155 120 A 55 55 0 0 0 245 120"/>' +
      '<path d="M 155 500 A 55 55 0 0 1 245 500"/>' +
      '</g>' +
      '<g fill="rgba(255,255,255,0.85)">' +
      '<circle cx="200" cy="310" r="3.5"/>' +
      '<circle cx="200" cy="88" r="3.5"/>' +
      '<circle cx="200" cy="532" r="3.5"/>' +
      '</g>';
  }

  function shortName(full) {
    var parts = String(full || "").trim().split(/\s+/);
    return parts.length > 1 ? parts[parts.length - 1] : (parts[0] || "");
  }

  function renderPitch(team) {
    var slots = FORMATIONS[currentFormation];
    var squad = (DATA.squads || {})[team.id] || [];
    var pools = { Goalkeeper: [], Defender: [], Midfielder: [], Forward: [] };
    squad.forEach(function (p) { if (pools[p.position]) pools[p.position].push(p); });
    var leftover = [];

    var dots = "";
    slots.forEach(function (s) {
      var p = pools[s.pos].shift();
      var name = p ? shortName(p.name) : s.label;
      var isReal = !!p;
      dots +=
        '<g class="dot">' +
        '<circle cx="' + s.x + '" cy="' + s.y + '" r="15" fill="var(--c1)" stroke="#0a0e14" stroke-width="3"/>' +
        (isReal && p.number
          ? '<text x="' + s.x + '" y="' + (s.y + 4) + '" text-anchor="middle" font-size="11" font-weight="800" fill="#0a0e14">' + esc(p.number) + "</text>"
          : "") +
        '<text x="' + s.x + '" y="' + (s.y + 33) + '" text-anchor="middle" font-size="12.5" font-weight="700" fill="#ffffff" stroke="rgba(0,0,0,0.65)" stroke-width="3" paint-order="stroke">' + esc(name) + "</text>" +
        "</g>";
    });

    $("pitch").innerHTML = pitchMarkings() + dots;
  }

  function bindFormationButtons(team) {
    var btns = $("formationBtns").querySelectorAll(".fbtn");
    btns.forEach(function (b) {
      b.onclick = function () {
        btns.forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        currentFormation = b.getAttribute("data-f");
        renderPitch(team);
      };
    });
  }

  /* ---------- squad ---------- */

  function renderSquad(team) {
    var box = $("squadGroups");
    box.innerHTML = "";
    var squad = (DATA.squads || {})[team.id] || [];
    if (!squad.length) {
      emptyNote(box, "Squad list is not available for " + team.name + " right now.");
      return;
    }
    ["Goalkeeper", "Defender", "Midfielder", "Forward"].forEach(function (pos) {
      var group = squad.filter(function (p) { return p.position === pos; });
      if (!group.length) return;
      var h = document.createElement("h3");
      h.className = "squad-pos-title";
      h.textContent = pos + "s";
      box.appendChild(h);
      var g = document.createElement("div");
      g.className = "squad-grid";
      group.forEach(function (p) {
        var d = document.createElement("div");
        d.className = "player";
        d.innerHTML =
          '<div class="pnum">' + esc(p.number || "-") + "</div>" +
          "<div><div class='pname'>" + esc(p.name) + "</div>" +
          "<div class='pnat'>" + esc(p.nationality || "") + "</div></div>";
        g.appendChild(d);
      });
      box.appendChild(g);
    });
  }

  /* ---------- stats ---------- */

  function renderStats() {
    var s = DATA.stats || {};
    var strip = $("statsStrip");
    strip.innerHTML = "";
    var items = [
      { num: s.avgGoals != null ? s.avgGoals : "-", label: "Goals per game" },
      { num: s.homeWinPct != null ? s.homeWinPct + "%" : "-", label: "Home wins" },
      { num: s.bttsPct != null ? s.bttsPct + "%" : "-", label: "Both teams score" },
      { num: s.topScoringTeam ? s.topScoringTeam.name : "-", label: "Top scoring side" + (s.topScoringTeam ? " (" + s.topScoringTeam.goals + ")" : "") }
    ];
    items.forEach(function (it) {
      var d = document.createElement("div");
      d.className = "glass stat";
      d.innerHTML = '<div class="snum">' + esc(it.num) + '</div><div class="slabel">' + esc(it.label) + "</div>";
      strip.appendChild(d);
    });
  }

  /* ---------- selection flow ---------- */

  function selectTeam(id) {
    var team = teamById(id);
    if (!team) return;
    try { localStorage.setItem(STORE_KEY, id); } catch (e) {}
    applyTheme(team);
    renderHero(team);
    renderPicker(id);
    renderFixtures(team);
    renderResults(team);
    renderPitch(team);
    bindFormationButtons(team);
    renderSquad(team);
    $("clubContent").classList.remove("hidden");
    $("picker").classList.add("hidden");
    $("changeClub").classList.remove("hidden");
    
  }

  function showPicker() {
    $("picker").classList.remove("hidden");
  }

  /* ---------- boot ---------- */

  function boot() {
    $("navLeague").textContent = LEAGUE.name;
    $("ctaLeague").textContent = LEAGUE.name;
    document.title = LEAGUE.name + " Fan Hub | igamingreviews.org";
    renderStats();

    var saved = null;
    try { saved = localStorage.getItem(STORE_KEY); } catch (e) {}
    if (saved && teamById(saved)) {
      selectTeam(saved);
    } else {
      applyTheme(null);
      renderHero(null);
      renderPicker(null);
    }

    $("changeClub").addEventListener("click", function (e) {
      showPicker();
    });
    $("heroCta").addEventListener("click", function () {
      showPicker();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
