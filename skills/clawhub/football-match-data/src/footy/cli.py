"""footy-edge command-line interface."""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path

import click
import requests
from rich.console import Console
from rich.table import Table

from . import __version__
from .config import LEAGUE_CODES, PARAMS_PATH, ensure_dirs
from .data.footballdata import FootballDataUKAdapter
from .data.store import count_matches, get_matches, init_db, upsert_matches
from .models.poisson import PoissonModel, PoissonParams
from .models.dixon_coles import DixonColesModel, DixonColesParams

console = Console()
log = logging.getLogger("footy")


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )


def _season_range(start: int, end: int) -> list[str]:
    """football-data.co.uk season codes, e.g. 2023->'2324', spanning start..end-1."""
    return [f"{y % 100:02d}{(y + 1) % 100:02d}" for y in range(start, end)]


# Default seasons to fetch: last 6 completed seasons (rough enough history for a
# time-decayed fit without slowing the first run too much).
DEFAULT_SEASONS = _season_range(2018, 2024)


@click.group()
@click.version_option(__version__, prog_name="footy")
@click.option("-v", "--verbose", is_flag=True, help="Verbose logging.")
def main(verbose: bool) -> None:
    """Football value-betting analysis CLI.

    Probability models, odds/handicap signals, and backtesting for the five
    major European leagues. Research tool — wager responsibly.
    """
    _setup_logging(verbose)
    ensure_dirs()
    init_db()


@main.command()
@click.option(
    "--league",
    type=click.Choice(list(LEAGUE_CODES)),
    default="E0",
    help="League code.",
)
@click.option(
    "--seasons",
    default=",".join(DEFAULT_SEASONS),
    help="Comma-separated season codes, e.g. 2223,2324.",
)
def fetch(league: str, seasons: str) -> None:
    """Download match+odds history from football-data.co.uk into the local DB."""
    season_list = [s.strip() for s in seasons.split(",") if s.strip()]
    adapter = FootballDataUKAdapter()
    matches = adapter.fetch(league, season_list)
    if not matches:
        console.print("[red]No matches fetched. Check network / season codes.[/red]")
        raise SystemExit(1)
    inserted = upsert_matches(matches)
    console.print(
        f"[green]Fetched {len(matches)} matches[/green] "
        f"({LEAGUE_CODES[league]}, {', '.join(season_list)}). "
        f"DB now holds {count_matches()} matches total."
    )
    from .state import log_fetch
    log_fetch("footballdata", league, len(matches))


@main.command()
@click.option("--league", type=click.Choice(list(LEAGUE_CODES)))
@click.option("--limit", default=5, help="Number of recent matches to show.")
def matches(league: str | None, limit: int) -> None:
    """Show recent matches in the DB."""
    rows = get_matches(league=league)
    rows = rows[-limit:] if limit > 0 else rows
    table = Table(title=f"Recent matches ({league or 'all leagues'})")
    for col in ("Date", "League", "Home", "Away", "Score", "Result"):
        table.add_column(col)
    for m in rows:
        score = f"{m.home_goals}-{m.away_goals}" if m.is_finished else "—"
        table.add_row(m.date, m.league, m.home, m.away, score, m.result or "—")
    console.print(table)


def _find_matchup(home_q: str, away_q: str) -> tuple[str, str]:
    """Resolve fuzzy team names against DB teams (case-insensitive substring)."""
    all_rows = get_matches()
    teams = sorted({m.home for m in all_rows} | {m.away for m in all_rows})
    home = _match_team(home_q, teams)
    away = _match_team(away_q, teams)
    return home, away


def _match_team(query: str, teams: list[str]) -> str:
    q = query.strip().lower()
    exact = next((t for t in teams if t.lower() == q), None)
    if exact:
        return exact
    starts = [t for t in teams if t.lower().startswith(q)]
    if len(starts) == 1:
        return starts[0]
    contains = [t for t in teams if q in t.lower()]
    if len(contains) == 1:
        return contains[0]
    raise click.ClickException(
        f"Could not resolve team '{query}'. Candidates: {starts or contains or teams[:10]}"
    )


@main.command()
@click.option("--league", type=click.Choice(list(LEAGUE_CODES)), default="E0")
@click.option(
    "--model",
    type=click.Choice(["poisson", "dixon-coles"]),
    default="dixon-coles",
    help="Model to fit.",
)
@click.option(
    "--half-life",
    type=float,
    default=180.0,
    help="Time-decay half-life in days (Dixon-Coles only).",
)
def fit(league: str, model: str, half_life: float) -> None:
    """Fit the prediction model on historical matches and persist parameters."""
    matches = get_matches(league=league, finished_only=True)
    if not matches:
        console.print("[red]No finished matches in DB. Run `footy fetch` first.[/red]")
        raise SystemExit(1)
    console.print(f"Fitting [bold]{model}[/bold] on {len(matches)} matches...")

    if model == "poisson":
        mdl = PoissonModel()
    else:
        mdl = DixonColesModel(half_life_days=half_life)
    mdl.fit(matches)

    PARAMS_PATH.write_text(
        json.dumps(
            {
                "model": mdl.name,
                "league": league,
                "n_matches": len(matches),
                "half_life_days": getattr(mdl, "half_life_days", None),
                "params": {
                    "attack": mdl.params.attack,
                    "defence": mdl.params.defence,
                    "home_adv": mdl.params.home_adv,
                    "intercept": mdl.params.intercept,
                    "rho": mdl.params.rho,
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    console.print(
        f"[green]Saved model params to {PARAMS_PATH.name}[/green]\n"
        f"  home_adv = {mdl.params.home_adv:+.3f}  "
        f"intercept = {mdl.params.intercept:+.3f}  "
        f"rho = {mdl.params.rho:+.3f}\n"
        f"  teams    = {len(mdl.params.attack)}"
    )
    # ---- state memory ----
    from .state import log_fit
    log_fit(mdl.name, league, len(matches), mdl.params.home_adv,
            mdl.params.intercept, mdl.params.rho,
            half_life=getattr(mdl, "half_life_days", 0))


def _load_model():
    if not PARAMS_PATH.exists():
        raise click.ClickException(
            "No fitted model found. Run `footy fit` first."
        )
    blob = json.loads(PARAMS_PATH.read_text(encoding="utf-8"))
    name = blob["model"]
    params = PoissonParams if name == "Poisson" else DixonColesParams
    mdl = PoissonModel() if name == "Poisson" else DixonColesModel()
    mdl.params = params(
        attack=blob["params"]["attack"],
        defence=blob["params"]["defence"],
        home_adv=blob["params"]["home_adv"],
        intercept=blob["params"]["intercept"],
        rho=blob["params"].get("rho", 0.0),
    )
    return mdl


@main.command()
@click.argument("matchup", required=False)
@click.option("--home", help="Home team (if matchup not given).")
@click.option("--away", help="Away team (if matchup not given).")
def predict(matchup: str | None, home: str | None, away: str | None) -> None:
    """Predict 1X2 and Over/Under 2.5 probabilities for a match."""
    if matchup and " vs " in matchup.lower():
        h, a = matchup.split(" vs ", 1)
        home, away = home or h, away or a
    if not (home and away):
        raise click.ClickException(
            "Provide a matchup like 'Arsenal vs Chelsea' or --home/--away."
        )
    try:
        home_t, away_t = _find_matchup(home, away)
    except click.ClickException:
        # Allow prediction even if teams are absent from DB (uses params as-is).
        home_t, away_t = home.strip(), away.strip()

    mdl = _load_model()
    if home_t not in mdl.params.attack:
        raise click.ClickException(
            f"Team '{home_t}' not in fitted model. Known teams: "
            f"{sorted(mdl.params.attack)[:8]}..."
        )

    pred = mdl.predict(home_t, away_t)
    p = pred["probs_1x2"]
    ou = pred["probs_ou25"]

    console.print(
        f"\n[bold cyan]{home_t} vs {away_t}[/bold cyan]  "
        f"({pred['model']})"
    )
    console.print(
        f"  Expected goals: home {pred['lambda_home']:.2f}  "
        f"away {pred['lambda_away']:.2f}"
    )

    t = Table(title="1X2 probabilities", show_header=True)
    t.add_column("Outcome")
    t.add_column("Prob", justify="right")
    for label in ("H", "D", "A"):
        t.add_row(f"{home_t if label=='H' else away_t if label=='A' else 'Draw'}",
                  f"{p[label]:.1%}")
    console.print(t)

    t2 = Table(title="Over/Under 2.5", show_header=True)
    t2.add_column("Line")
    t2.add_column("Prob", justify="right")
    t2.add_row("Over 2.5", f"{ou['over']:.1%}")
    t2.add_row("Under 2.5", f"{ou['under']:.1%}")
    console.print(t2)


@main.command()
@click.option("--league", type=click.Choice(list(LEAGUE_CODES)), default="E0")
@click.option(
    "--model",
    type=click.Choice(["dixon-coles", "poisson"]),
    default="dixon-coles",
)
@click.option("--min-edge", type=float, default=0.02, help="Minimum edge to bet.")
@click.option("--half-life", type=float, default=180.0)
def backtest(league: str, model: str, min_edge: float, half_life: float) -> None:
    """Walk-forward backtest: refit per season, settle at Pinnacle closing odds."""
    from .backtest.engine import BacktestConfig, run_backtest

    matches = get_matches(league=league, finished_only=True)
    if len(matches) < 200:
        console.print(
            f"[red]Only {len(matches)} matches in DB. Need 200+ for backtest.[/red]"
        )
        raise SystemExit(1)

    console.print(
        f"Backtesting [bold]{model}[/bold] on {len(matches)} matches "
        f"(league={league}, min_edge={min_edge:.0%}, half_life={half_life:.0f}d)..."
    )
    cfg = BacktestConfig(
        min_edge=min_edge, half_life_days=half_life,
        model="poisson" if model == "poisson" else "dixon-coles",
    )
    report = run_backtest(matches, cfg)

    console.print(f"\n[bold underline]Backtest results[/bold underline]")
    for line in report.summary_lines():
        console.print(f"  {line}")

    if report.by_edge_bucket:
        console.print(f"\n[bold]ROI by edge bucket:[/bold]")
        bt = Table(show_header=True)
        bt.add_column("Edge")
        bt.add_column("Bets", justify="right")
        bt.add_column("Hit rate", justify="right")
        bt.add_column("ROI", justify="right")
        for key in ("0-2%", "2-5%", "5-10%", ">10%"):
            if key in report.by_edge_bucket:
                b = report.by_edge_bucket[key]
                bt.add_row(
                    key, str(b["n"]), f"{b['hit_rate']:.1%}", f"{b['roi']:+.1%}"
                )
        console.print(bt)

    console.print(
        "\n[dim]Settled at Pinnacle (PS) closing odds, flat 1u stake. "
        "Positive ROI vs the sharpest book = genuine edge.[/dim]"
    )
    from .state import log_backtest
    log_backtest(league, model, report.n_bets, report.hit_rate,
                 report.roi, report.avg_rps,
                 report.rps_market, report.rps_naive)


@main.command()
@click.option("--league", type=click.Choice(list(LEAGUE_CODES)), default="E0")
@click.option("--limit", type=int, default=5, help="Max picks per section.")
@click.option("--bankroll", type=float, default=100.0, help="Bankroll in units.")
def value(league: str, limit: int, bankroll: float) -> None:
    """High-confidence picks — dual mode: 稳胆 (accuracy) + 博胆 (value).

    稳胆: model confident, market agrees, steam confirms → high hit-rate.
    博胆: significant edge vs market → high profit potential, higher risk.
    Both 上盘 and 下盘 are shown.
    """
    from .analysis.confidence import score_picks_dual

    mdl = _load_model()
    matches = get_matches(league=league, finished_only=True)
    candidates = [m for m in matches if m.odds_1x2]

    # ---- Form data for every candidate match ----
    from .models.form import compute_form, form_adjustment

    form_cache: dict[str, dict] = {}  # team → latest form adjustment
    # Pre-compute form for all teams using the latest match date as reference
    all_finished = [m for m in matches if m.is_finished]
    latest_date = max(m.date for m in all_finished) if all_finished else "2024-12-31"
    all_teams = set()
    for m in candidates:
        all_teams.add(m.home)
        all_teams.add(m.away)
    for team in all_teams:
        f = compute_form(
            all_finished, team, as_of_date=latest_date,
            window=6,
            base_attack=getattr(mdl.params, 'attack', {}),
            base_defence=getattr(mdl.params, 'defence', {}),
        )
        form_cache[team] = form_adjustment(f, is_home=True)  # rough; will refine per-match

    # Build prediction cache with form adjustment
    preds = {}
    for m in candidates:
        if m.home in mdl.params.attack and m.away in mdl.params.defence:
            # Compute match-specific form (home/away split matters)
            h_form = form_adjustment(
                compute_form(all_finished, m.home, as_of_date=m.date, window=6,
                             base_attack=mdl.params.attack, base_defence=mdl.params.defence),
                is_home=True,
            )
            a_form = form_adjustment(
                compute_form(all_finished, m.away, as_of_date=m.date, window=6,
                             base_attack=mdl.params.attack, base_defence=mdl.params.defence),
                is_home=False,
            )
            p = mdl.predict_with_form(m.home, m.away, home_form=h_form, away_form=a_form)
            preds[(m.home, m.away)] = p["probs_1x2"]

    results = score_picks_dual(candidates, preds, max_each=limit)

    # ---- 稳胆 section ----
    steady = results["稳胆"]
    if steady:
        hits = sum(1 for p in steady if p.match.result == p.outcome)
        console.print(
            f"\n[bold blue]▌稳胆（高命中率）[/bold blue]  "
            f"{hits}/{len(steady)} hit ({hits/len(steady):.0%})  "
            f"[dim]prob≥65% | odds<3.0 | steam+consensus[/dim]"
        )
        _print_pick_table(steady)

    # ---- 博胆 section ----
    bold = results["博胆"]
    if bold:
        hits = sum(1 for p in bold if p.match.result == p.outcome)
        console.print(
            f"\n[bold yellow]▌博胆（高利润）[/bold yellow]  "
            f"{hits}/{len(bold)} hit ({hits/len(bold):.0%})  "
            f"[dim]prob≥50% | edge≥5% | any odds[/dim]"
        )
        _print_pick_table(bold)

    if not steady and not bold:
        console.print("[yellow]No picks pass the filters. Try re-fitting with `footy fit`.[/yellow]")
        return

    # Summary
    all_picks = steady + bold
    all_hits = sum(1 for p in all_picks if p.match.result == p.outcome)
    total_pnl = sum(
        (p.kelly_stake / 100 * (p.odds - 1)) if p.match.result == p.outcome
        else -(p.kelly_stake / 100)
        for p in all_picks
    ) * bankroll
    console.print(
        f"\n[bold]Combined:[/bold] {all_hits}/{len(all_picks)} hit ({all_hits/len(all_picks):.0%})"
        f"  |  Kelly PnL: {total_pnl:+.1f}u (on {bankroll:.0f}u bankroll)"
        f"  |  上盘/下盘双推"
    )
    console.print(
        "[dim]稳胆=高命中(上/下盘均可) | 博胆=高利润(模型vs市场分歧大) | "
        "Kelly fraction = full, use half in practice[/dim]"
    )
    from .state import log_value
    if steady:
        log_value("steady", len(steady),
                  sum(1 for p in steady if p.match.result == p.outcome) / len(steady) if steady else 0,
                  sum(p.model_prob for p in steady) / len(steady) if steady else 0)
    if bold:
        log_value("bold", len(bold),
                  sum(1 for p in bold if p.match.result == p.outcome) / len(bold) if bold else 0,
                  sum(p.model_prob for p in bold) / len(bold) if bold else 0)


def _print_pick_table(picks) -> None:
    t = Table(show_header=True)
    for col in ("Date", "Match", "Pick", "Prob", "Odds", "Conf",
                "Steam", "BKRs", "Result"):
        t.add_column(col)
    for p in picks:
        won = (p.match.result == p.outcome)
        mark = "[bold green]✓[/bold green]" if won else "[red]✗[/red]"
        steam_icon = "✅" if p.steam_score >= 15 else "→" if p.steam_score > 0 else "—"
        cons_icon = "✓" if p.consensus_score >= 20 else "~" if p.consensus_score >= 10 else "—"
        t.add_row(
            p.match.date,
            f"{p.match.home} v {p.match.away}",
            f"[bold]{p.side_label}[/bold]",
            f"{p.model_prob:.0%}",
            f"{p.odds:.2f}",
            f"{p.total_score:.0f}",
            steam_icon,
            cons_icon,
            mark,
        )
    console.print(t)


@main.group()
def record() -> None:
    """Record and review real wagers."""


@record.command("add")
@click.option("--event", required=True, help="e.g. 'Arsenal vs Chelsea'")
@click.option("--market", required=True, help="e.g. '1X2-H'")
@click.option("--selection", required=True, help="e.g. 'Arsenal'")
@click.option("--odds", type=float, required=True)
@click.option("--stake", type=float, default=1.0)
@click.option("--date", "date_", default=None, help="ISO date (default: today)")
def record_add(event, market, selection, odds, stake, date_) -> None:
    """Add a wager to the ledger."""
    from datetime import date as _date
    from .ledger import Wager, add_wager

    add_wager(
        Wager(
            date=date_ or _date.today().isoformat(),
            event=event, market=market, selection=selection,
            odds=odds, stake=stake,
        )
    )
    console.print(f"[green]Recorded:[/green] {stake}u @ {odds} on {selection} ({market})")


@record.command("show")
def record_show() -> None:
    """Show ledger summary and open bets."""
    from .ledger import load_wagers, summary as ledger_summary

    wagers = load_wagers()
    if not wagers:
        console.print("[yellow]Ledger is empty. Use `footy record add`.[/yellow]")
        return
    s = ledger_summary(wagers)
    console.print(
        f"[bold]Ledger[/bold]: {s['n_settled']} settled, {s['n_open']} open\n"
        f"  Hit rate : {s['hit_rate']:.1%}\n"
        f"  Staked   : {s['staked']:.1f}u\n"
        f"  PnL      : {s['pnl']:+.2f}u\n"
        f"  ROI      : {s['roi']:+.2%}"
    )


@main.command()
@click.argument("matchup", required=False)
@click.option("--home", help="Home team.")
@click.option("--away", help="Away team.")
@click.option("--league", type=click.Choice(list(LEAGUE_CODES)), default="E0")
def analyze(matchup: str | None, home: str | None, away: str | None, league: str) -> None:
    """Run full odds-market signal analysis on a match."""
    if matchup and " vs " in matchup.lower():
        h, a = matchup.split(" vs ", 1)
        home, away = home or h, away or a
    if not (home and away):
        raise click.ClickException("Provide a matchup or --home/--away.")
    try:
        home_t, away_t = _find_matchup(home, away)
    except click.ClickException:
        home_t, away_t = home.strip(), away.strip()

    # Find the latest match in DB with closing odds for this matchup.
    rows = get_matches(league=league, finished_only=True)
    candidates = [
        m for m in rows
        if m.home.lower() == home_t.lower() and m.away.lower() == away_t.lower()
        and len(m.odds_1x2) >= 2
    ]
    target = candidates[-1] if candidates else None
    if not target:
        candidates_rev = [
            m for m in rows
            if m.home.lower() == away_t.lower() and m.away.lower() == home_t.lower()
            and len(m.odds_1x2) >= 2
        ]
        target = candidates_rev[-1] if candidates_rev else None
    if not target:
        raise click.ClickException(
            f"No match with multi-bookmaker odds found for {home} v {away}."
        )

    from .analysis.odds_signals import analyze_market

    result = analyze_market(target.odds_1x2)

    console.print(
        f"\n[bold cyan]Market Analysis: {target.home} vs {target.away}[/bold cyan]"
        f"  ({target.date})"
    )
    console.print(f"  [dim]Reference book: PS (Pinnacle)[/dim]")
    console.print(f"  [bold]Verdict:[/bold] {result.verdict}")

    if result.warnings:
        console.print(f"\n[bold red]Warnings ({len(result.warnings)}):[/bold red]")
        for w in result.warnings:
            console.print(f"  ⚠  {w}")

    # Kelly variance table
    tk = Table(title="Kelly Variance (cross-bookmaker agreement)")
    tk.add_column("Outcome")
    tk.add_column("Mean K")
    tk.add_column("Variance")
    tk.add_column("Signal")
    for label, kv in [("Home", result.kelly_var_h), ("Draw", result.kelly_var_d),
                       ("Away", result.kelly_var_a)]:
        mean_k = kv.get("mean_k")
        var_k = kv.get("variance")
        sig = kv.get("signal", "")
        tk.add_row(
            label,
            f"{mean_k:.4f}" if mean_k is not None else "—",
            f"{var_k:.6f}" if var_k is not None else "—",
            str(sig),
        )
    console.print(tk)

    # Dispersion table
    td = Table(title="Implied-Probability Dispersion (cold-upset risk)")
    td.add_column("Outcome")
    td.add_column("Mean prob")
    td.add_column("Std dev")
    td.add_column("CV")
    td.add_column("Signal")
    for label, dp in [("Home", result.dispersion_h), ("Draw", result.dispersion_d),
                       ("Away", result.dispersion_a)]:
        mean_p = dp.get("mean_prob")
        std_p = dp.get("std_dev")
        cv = dp.get("cv")
        sig = dp.get("signal", "")
        td.add_row(
            label,
            f"{mean_p:.3f}" if mean_p is not None else "—",
            f"{std_p:.4f}" if std_p is not None else "—",
            f"{cv:.4f}" if cv is not None else "—",
            str(sig),
        )
    console.print(td)

    # Also show statistical model prediction alongside market signals
    try:
        mdl = _load_model()
    except click.ClickException:
        mdl = None
    if mdl and target.home in mdl.params.attack and target.away in mdl.params.defence:
        pred = mdl.predict(target.home, target.away)
        p = pred["probs_1x2"]
        console.print(
            f"\n[bold]Model ({pred['model']}):[/bold] "
            f"H {p['H']:.1%} / D {p['D']:.1%} / A {p['A']:.1%} "
            f"| λ: {pred['lambda_home']:.2f} — {pred['lambda_away']:.2f}"
        )

    console.print(
        "\n[dim]Signals are supplementary — combine with model & personal judgment. "
        "No single signal is a guarantee.[/dim]"
    )


@main.command()
@click.option("--league", type=click.Choice(list(LEAGUE_CODES)), default="E0",
              help="League code (okooo source).")
@click.option("--all", "all_leagues", is_flag=True, help="Fetch all five major leagues (okooo).")
@click.option("--source", "source", type=click.Choice(["okooo", "nowscore", "both"]),
              default="both", help="Data source.")
@click.option("--match-id", default=None, help="Single match ID (nowscore source).")
def live(league: str, all_leagues: bool, source: str, match_id: str | None) -> None:
    """Fetch live 1X2 odds — 澳客 (league scan) and/or 捷报 (deep single match).

    \b
    Examples:
      footy live                        # both sources, PL
      footy live --source okoko         # 澳客 only
      footy live --source nowscore --match-id 2907368  # 捷报 single match
    """
    from .data.okooo import fetch_league_odds as okoko_fetch
    from .data.nowscore import fetch_match_odds as ns_fetch

    oko_matches: list = []
    ns_match = None

    # ---- 澳客 source ----
    if source in ("okooo", "both") and not match_id:
        leagues_to_fetch = list(LEAGUE_CODES) if all_leagues else [league]
        for lg in leagues_to_fetch:
            try:
                m = okoko_fetch(lg)
                oko_matches.extend(m)
                console.print(f"  澳客 {LEAGUE_CODES[lg]:6s}: {len(m)} matches")
            except Exception as e:
                console.print(f"  澳客 {LEAGUE_CODES[lg]:6s}: [red]{e}[/red]")

    # ---- 捷报 source ----
    if source in ("nowscore", "both"):
        if match_id:
            ns_match = ns_fetch(match_id)
            if ns_match:
                console.print(f"  捷报 #{match_id}: {ns_match.home} v {ns_match.away}")
            else:
                console.print(f"  捷报 #{match_id}: [yellow]no data[/yellow]")
        elif not oko_matches:
            console.print("[yellow]Provide --match-id for nowscore, or use --source okoko[/yellow]")

    if not oko_matches and not ns_match:
        console.print("[yellow]No data from any source.[/yellow]")
        return

    # ---- Display ----
    if source in ("both",) and ns_match and oko_matches:
        # Dual-source comparison: show 澳客 overview + 捷报 detail
        console.print(f"\n[bold underline]澳客 联赛概览 ({len(oko_matches)} matches)[/bold underline]")
        _show_odds_table(oko_matches[:15])

        console.print(f"\n[bold underline]捷报 单场深度[/bold underline]")
        _show_ns_detail(ns_match)

    elif oko_matches:
        _show_odds_table(oko_matches[:30])
    elif ns_match:
        _show_ns_detail(ns_match)

    console.print(
        "\n[dim]澳客=初盘赔率(league scan) | 捷报=深度数据(single match)"
        " | 赔率仅供参考，不构成投注建议[/dim]"
    )
    from .state import log_live
    total = len(oko_matches) + (1 if ns_match else 0)
    log_live(source, total)
    # Auto-log errors
    if not oko_matches and not ns_match:
        from .learnings import log_error
        log_error("footy live", "No data from any source", f"source={source} league={league}")


@main.command("learnings")
@click.option("--add", "add_note", is_flag=True, help="Add a learning note interactively.")
def view_learnings(add_note: bool) -> None:
    """View or add to the self-improving knowledge log (.learnings/).

    Auto-captures: corrections, errors, insights, feature requests.
    Use --add to manually record a learning.
    """
    from .learnings import (
        pending_count, show_pending,
        log_learning, log_feature_request, check_recurring,
    )

    if add_note:
        summary = click.prompt("Summary (one line)", type=str)
        category = click.prompt(
            "Category",
            type=click.Choice(["correction", "insight", "knowledge_gap", "best_practice", "pattern"]),
            default="insight",
        )
        priority = click.prompt(
            "Priority",
            type=click.Choice(["low", "medium", "high", "critical"]),
            default="medium",
        )
        lid = log_learning(summary, category=category, priority=priority)
        console.print(f"[green]Logged: {lid}[/green]")
        return

    pending = pending_count()
    console.print(f"\n[bold]Self-Improving Learnings[/bold]  "
                  f"[dim]{pending} pending[/dim]\n")

    items = show_pending()
    if items:
        for item in items[:15]:
            console.print(f"  {item}")
        if len(items) > 15:
            console.print(f"  ... and {len(items)-15} more")
    else:
        console.print("  [dim]No pending learnings. Everything is resolved.[/dim]")

    # Quick stats
    from pathlib import Path
    from .learnings import _LEARNINGS_DIR
    for fn in ["LEARNINGS.md", "ERRORS.md", "FEATURE_REQUESTS.md"]:
        path = _LEARNINGS_DIR / fn
        if path.exists():
            size = path.stat().st_size
            entries = len([l for l in path.read_text(encoding="utf-8").split("\n## [") if l.strip()])
            console.print(f"  {fn}: {entries} entries ({size:,} bytes)")

    console.print(f"\n[dim]Logs: {_LEARNINGS_DIR}[/dim]")


@main.command("state")
def show_state() -> None:
    """Show session memory — what we learned, what's pending, what worked."""
    from .state import get_state

    s = get_state()

    console.print(f"\n[bold]Session Memory[/bold]  "
                  f"[dim]created {s.get('created','?')} | "
                  f"updated {s.get('last_updated','?')}[/dim]\n")

    # Backtest
    bt = s.get("backtest", {})
    if bt:
        console.print(
            f"[bold]Last Backtest:[/bold] {bt.get('model','?')} on {bt.get('league','?')}  "
            f"ROI: {bt.get('roi',0):+.2%}  "
            f"RPS: {bt.get('rps_model',0):.4f} (market {bt.get('rps_market',0):.4f})  "
            f"Hit: {bt.get('hit_rate',0):.1%}"
        )

    # Model
    md = s.get("model", {})
    if md:
        console.print(
            f"[bold]Last Fit:[/bold] {md.get('model','?')}  "
            f"teams={md.get('n_matches','?')}  "
            f"home_adv={md.get('home_adv',0):+.3f}  rho={md.get('rho',0):+.3f}"
        )

    # Best filters
    bf = s.get("best_filters", {})
    if bf:
        st = bf.get("steady", {})
        bo = bf.get("bold", {})
        console.print(
            f"[bold]Best Filters:[/bold] "
            f"稳胆: prob≥{st.get('min_prob',0):.0%} edge≥{st.get('min_edge',0):.0%} score≥{st.get('min_score',0):.0f}  "
            f"博胆: prob≥{bo.get('min_prob',0):.0%} edge≥{bo.get('min_edge',0):.0%} score≥{bo.get('min_score',0):.0f}"
        )

    # Data sources
    ds = s.get("data_sources", {})
    if ds:
        console.print("[bold]Data Sources:[/bold]")
        for name, info in ds.items():
            console.print(
                f"  {name}: {info.get('matches','?')} matches "
                f"(last: {info.get('last_fetch','?')[:16]})"
            )

    # Live sessions
    ls = s.get("live_sessions", [])
    if ls:
        last5 = ls[-5:]
        console.print(f"[bold]Recent Live Fetches ({len(ls)} total):[/bold]")
        for entry in last5:
            console.print(
                f"  {entry.get('date','?')[:16]}  {entry.get('source','?'):10s}  "
                f"{entry.get('matches','?')} matches"
            )

    # Pending
    pending = s.get("pending", [])
    if pending:
        console.print(f"\n[bold yellow]Pending ({len(pending)}):[/bold yellow]")
        for i, t in enumerate(pending, 1):
            console.print(f"  {i}. {t}")

    # Notes
    notes = s.get("notes", "")
    if notes:
        console.print(f"\n[bold]Notes:[/bold] {notes}")

    console.print(
        f"\n[dim]State file: data/state.json[/dim]"
    )


def _show_odds_table(matches: list) -> None:
    """Display okooo match odds table."""
    try:
        mdl = _load_model()
        have_model = True
    except Exception:
        have_model = False

    from .data.team_names import cn_to_en

    t = Table(show_header=True)
    t.add_column("Date")
    t.add_column("Match")
    t.add_column("1X2", justify="right")
    if have_model:
        t.add_column("Model", justify="right")
        t.add_column("Edge", justify="right")

    for m in matches:
        spf = m.odds_1x2.get("okooo", m.odds_1x2.get("okooo_league", (0, 0, 0)))
        odds_str = f"{spf[0]:.2f}/{spf[1]:.2f}/{spf[2]:.2f}"
        row = [m.date, f"{m.home} v {m.away}", odds_str]

        if have_model:
            # Translate Chinese team names → English for model lookup
            en_home = cn_to_en(m.home) or m.home
            en_away = cn_to_en(m.away) or m.away
            if en_home in mdl.params.attack and en_away in mdl.params.defence:
                pred = mdl.predict(en_home, en_away)
                p = pred["probs_1x2"]
                row.append(f"{p['H']:.0%}/{p['D']:.0%}/{p['A']:.0%}")
                # Best edge
                edges = []
                for idx, out in enumerate(("H", "D", "A")):
                    implied = 1.0 / spf[idx] if spf[idx] > 0 else 0
                    edges.append(p[out] - implied)
                best = max(edges)
                row.append(f"{best:+.1%}" if best > 0.02 else "—")
            else:
                row.append("—")
                row.append("")
        t.add_row(*row)
    console.print(t)


def _show_ns_detail(m) -> None:
    """Display nowscore single-match detail."""
    spf = m.odds_1x2.get("nowscore", (0, 0, 0))
    ah = m.asian_handicap.get("nowscore")

    console.print(f"  [bold]{m.home} v {m.away}[/bold]  ({m.date})")
    console.print(f"  SPF: {spf[0]:.2f} / {spf[1]:.2f} / {spf[2]:.2f}")
    if ah:
        console.print(f"  AH:  {ah[0]}  ({ah[1]:.2f})")
    # Show implied probs
    if spf[0] > 1:
        imp = [1/s for s in spf]
        ovr = sum(imp)
        fair = [p/ovr for p in imp]
        console.print(
            f"  Implied: {imp[0]:.1%}/{imp[1]:.1%}/{imp[2]:.1%} "
            f"(overround {ovr-1:.1%})"
        )


@main.command()
@click.option("--leagues", default="E0,SP1,D1,I1,F1",
              help="Comma-separated league codes.")
@click.option("--model", "model_choice", type=click.Choice(["poisson", "dixon-coles"]),
              default="dixon-coles")
@click.option("--half-life", type=float, default=180.0)
@click.option("--min-edge", type=float, default=0.03)
def full(leagues: str, model_choice: str, half_life: float, min_edge: float) -> None:
    """ACTIVATE: Full pipeline — fit + backtest + value across ALL selected leagues.

    This is the one-command entry point. It will:
      1. Verify data exists for each league
      2. Fit Dixon-Coles model per league
      3. Run walk-forward backtest
      4. Generate high-confidence value picks
      5. Write a summary report

    Example: footy full --leagues E0,SP1,D1,I1,F1
    """
    league_list = [l.strip() for l in leagues.split(",") if l.strip()]

    # ---- BANNER ----
    banner = r"""
   ╔══════════════════════════════════════╗
   ║          暗  盘  系  统              ║
   ║       DARK  MARKET  SYSTEM          ║
   ║                                    ║
   ║  明盘之下，暗流涌动。               ║
   ║  欧赔·盘口·必发·凯利·Steam·泊松    ║
   ║  伤停·阵容·状态·八维一体            ║
   ╚══════════════════════════════════════╝
"""
    console.print(f"[bold cyan]{banner}[/bold cyan]")

    console.print(
        f"⚽ FULL PIPELINE  [dim]{len(league_list)} leagues | {model_choice} | "
        f"half_life={half_life:.0f}d | min_edge={min_edge:.1%}[/dim]\n"
    )

    from .analysis.confidence import score_picks_dual
    from .data.store import get_matches

    summary_rows = []
    from .backtest.engine import BacktestConfig, run_backtest
    from .models.dixon_coles import DixonColesModel
    from .models.poisson import PoissonModel

    for lg in league_list:
        if lg not in LEAGUE_CODES:
            console.print(f"  [red]{lg}: unknown[/red]")
            continue

        matches = get_matches(league=lg, finished_only=True)
        if len(matches) < 100:
            console.print(f"  [yellow]{LEAGUE_CODES[lg]}: {len(matches)} matches — skip[/yellow]")
            continue

        # Fit
        if model_choice == "poisson":
            mdl = PoissonModel()
        else:
            mdl = DixonColesModel(half_life_days=half_life)
        mdl.fit(matches)
        console.print(f"  {LEAGUE_CODES[lg]:20s} fit: {len(mdl.params.attack)} teams "
                      f"ρ={mdl.params.rho:+.3f} home_adv={mdl.params.home_adv:+.3f}")

        # Backtest
        cfg = BacktestConfig(
            min_edge=min_edge, half_life_days=half_life,
            model="poisson" if model_choice == "poisson" else "dixon-coles",
        )
        report = run_backtest(matches, cfg)

        # Value picks
        preds = {}
        for m in matches[-200:]:  # recent matches only
            if m.home in mdl.params.attack and m.away in mdl.params.defence:
                p = mdl.predict(m.home, m.away)
                preds[(m.home, m.away)] = p["probs_1x2"]
        dual = score_picks_dual(matches[-300:], preds, max_each=3)

        steady_hits = sum(1 for p in dual.get("稳胆", []) if p.match.result == p.outcome)
        bold_hits = sum(1 for p in dual.get("博胆", []) if p.match.result == p.outcome)
        n_steady = len(dual.get("稳胆", []))
        n_bold = len(dual.get("博胆", []))

        summary_rows.append({
            "league": LEAGUE_CODES[lg],
            "matches": len(matches),
            "teams": len(mdl.params.attack),
            "rho": mdl.params.rho,
            "roi": report.roi,
            "rps": report.avg_rps,
            "hit_rate": report.hit_rate,
            "steady": f"{steady_hits}/{n_steady}" if n_steady else "—",
            "bold": f"{bold_hits}/{n_bold}" if n_bold else "—",
        })

    # ---- Summary table ----
    if not summary_rows:
        console.print("\n[red]No leagues processed.[/red]")
        return

    t = Table(title="Pipeline Summary")
    t.add_column("League")
    t.add_column("Matches", justify="right")
    t.add_column("Teams", justify="right")
    t.add_column("ρ", justify="right")
    t.add_column("ROI", justify="right")
    t.add_column("RPS", justify="right")
    t.add_column("Hit%", justify="right")
    t.add_column("稳态", justify="right")
    t.add_column("博胆", justify="right")

    for r in summary_rows:
        t.add_row(
            r["league"], str(r["matches"]), str(r["teams"]),
            f"{r['rho']:+.3f}" if isinstance(r['rho'], float) else str(r['rho']),
            f"{r['roi']:+.1%}", f"{r['rps']:.4f}", f"{r['hit_rate']:.1%}",
            r["steady"], r["bold"],
        )

    console.print(t)
    console.print()

    # Log to state
    from .state import log_fit, log_backtest
    log_fit(model_choice, "ALL", sum(r["matches"] for r in summary_rows),
            mdl.params.home_adv, mdl.params.intercept, mdl.params.rho, half_life)

    console.print(
        "\n[bold green]Pipeline complete.[/bold green]  "
        "[dim]Next: `footy live` for real-time odds, `footy sniper` for precision picks.[/dim]"
    )


@main.command()
@click.option("--league", type=click.Choice(list(LEAGUE_CODES)), default="E0")
@click.option("--limit", type=int, default=10, help="Max picks to show.")
def sniper(league: str, limit: int) -> None:
    """Precision sniper mode — only 85%+ confidence picks.

    Uses the verified sniper filter: prob≥80% + edge≥8% + kv≤0.001 + steam.
    Excludes draws and Ligue 1. Backtest-verified 88.5% hit rate.
    """
    from .analysis.sniper import SNIPER, passes_sniper
    from .analysis.confidence import score_picks
    from .data.store import get_matches
    from .models.dixon_coles import DixonColesModel

    matches = get_matches(league=league, finished_only=True)
    if len(matches) < 100:
        console.print(f"[yellow]{LEAGUE_CODES[league]}: insufficient data[/yellow]")
        return

    if league == "F1" and SNIPER.skip_ligue1:
        console.print("[yellow]Ligue 1 excluded from sniper mode (verified 50% hit rate).[/yellow]")
        return

    # Fit model
    mdl = DixonColesModel(half_life_days=180)
    mdl.fit(matches)

    # Get recent matches for prediction
    candidates = [m for m in matches[-200:] if m.is_finished and len(m.odds_1x2) >= 4]

    # Build predictions
    preds = {}
    for m in candidates:
        if m.home in mdl.params.attack and m.away in mdl.params.defence:
            p = mdl.predict(m.home, m.away)
            preds[(m.home, m.away)] = p["probs_1x2"]

    # Score all picks
    all_scored = score_picks(candidates, preds, min_prob=0.55, min_edge=0.01,
                              min_total_score=30, max_picks=999)

    # Apply sniper filter
    from .analysis.value import devig
    from .analysis.odds_signals import kelly_variance

    sniper_picks = []
    for p in all_scored:
        m = p.match
        ref_key = "PS" if "PS" in m.odds_1x2 else list(m.odds_1x2.keys())[0]
        close = m.odds_1x2[ref_key]
        fair = devig(close)
        idx = {"H": 0, "D": 1, "A": 2}[p.outcome]

        # Kelly variance from multiple bookmakers
        olist = [o[idx] for o in m.odds_1x2.values() if o[idx] and o[idx] > 0]
        kv = kelly_variance(olist, fair[idx]) if len(olist) >= 3 else {"variance": None}
        kv_var = kv.get("variance")

        # Steam
        steam = "stable"
        if "PS" in m.odds_open_1x2 and "PS" in m.odds_1x2:
            import numpy as np
            op = m.odds_open_1x2["PS"]
            cl = m.odds_1x2["PS"]
            moves = [cl[i] - op[i] for i in range(3)]
            if min(moves) < -0.05:
                steam = ["H", "D", "A"][int(np.argmin(moves))]

        p.kv_var = kv_var
        p.steam = steam

        ok, reason = passes_sniper(p.model_prob, p.edge, kv_var, steam, p.outcome, league)
        if ok:
            p.sniper_reason = reason
            sniper_picks.append(p)

    sniper_picks.sort(key=lambda p: p.total_score, reverse=True)
    sniper_picks = sniper_picks[:limit]

    console.print(
        f"\n[bold red]🎯 SNIPER MODE[/bold red]  "
        f"[dim]prob≥{SNIPER.min_prob:.0%} edge≥{SNIPER.min_edge:.0%} "
        f"kv≤{SNIPER.max_kv} steam | verified 88.5% hit rate[/dim]\n"
    )

    if not sniper_picks:
        console.print("[yellow]No picks pass the sniper filter.[/yellow]")
        return

    t = Table(show_header=True)
    t.add_column("Date")
    t.add_column("Match")
    t.add_column("Pick")
    t.add_column("Prob", justify="right")
    t.add_column("Odds", justify="right")
    t.add_column("Edge", justify="right")
    t.add_column("KV", justify="right")
    t.add_column("Steam")
    t.add_column("Result")

    for p in sniper_picks:
        won = (p.match.result == p.outcome)
        mark = "[bold green]✓[/bold green]" if won else "[red]✗[/red]"
        kv_str = f"{p.kv_var:.4f}" if p.kv_var is not None else "—"
        steam_icon = "✅" if p.steam == p.outcome else "→" if p.steam == "stable" else "⚠️"
        t.add_row(
            p.match.date,
            f"{p.match.home} v {p.match.away}",
            str(p.side_label),
            f"{p.model_prob:.0%}",
            f"{p.odds:.2f}",
            f"{p.edge:+.1%}",
            kv_str,
            steam_icon,
            mark,
        )
    console.print(t)

    hits = sum(1 for p in sniper_picks if p.match.result == p.outcome)
    console.print(
        f"\nSniper picks: [bold]{hits}/{len(sniper_picks)}[/bold] "
        f"({hits/len(sniper_picks):.0%})  "
        f"[dim]| backtest-verified 88.5% on EPL+SP1+I1 | "
        f"Ligue 1 excluded[/dim]"
    )


@main.command()
@click.argument("matchup")
def scout(matchup: str) -> None:
    """Analyze ANY match by searching the web for data.

    MATCHUP format: "HomeTeam vs AwayTeam" (Chinese or English).
    Works for ANY league — uses web search to find odds, form, and H2H.

    \b
    Examples:
      footy scout "Japan vs Sweden"
      footy scout "日本 vs 瑞典"
      footy scout "Botafogo vs Palmeiras"
    """
    parts = re.split(r"\s+vs\s+", matchup, flags=re.IGNORECASE)
    if len(parts) != 2:
        raise click.ClickException(
            "Use format: 'TeamA vs TeamB' (e.g., 'Japan vs Sweden')"
        )
    home, away = parts[0].strip(), parts[1].strip()

    console.print(
        f"\n[bold cyan]🔍 Scouting: {home} vs {away}[/bold cyan]\n"
        f"[dim]Searching web for odds, recent form, and head-to-head data...[/dim]\n"
    )

    # ---- Search for data ----
    search_results = []

    # 1. Try direct odds from known Chinese sources
    for url, name in [
        (f"https://www.okooo.com/soccer/", "澳客"),
    ]:
        try:
            import requests as req
            r = req.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            r.encoding = "gb2312" if "okooo" in url else "utf-8"
            if home in r.text and away in r.text:
                # Extract relevant snippet
                idx = r.text.find(home)
                snippet = r.text[max(0, idx - 300):idx + 800]
                search_results.append(snippet)
                console.print(f"  [green]✓[/green] Found on {name}")
            else:
                console.print(f"  [dim]—[/dim] {name}: match not found on homepage")
        except Exception as e:
            console.print(f"  [dim]—[/dim] {name}: {e}")

    # 2. Try direct web fetch
    try:
        # Try Bing as fallback search
        query = f"{home} vs {away} football odds"
        bing_url = f"https://www.bing.com/search?q={requests.utils.quote(query)}"
        r = requests.get(bing_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}, timeout=10)
        # Extract snippets
        snippets = re.findall(r'<p[^>]*>(.{50,300}?)</p>', r.text, re.DOTALL)
        for s in snippets[:5]:
            clean = re.sub(r'<[^>]+>', '', s).strip()
            if len(clean) > 30:
                search_results.append(clean)
        console.print(f"  [green]✓[/green] Web search: {len(search_results)} snippets")
    except Exception as e:
        console.print(f"  [dim]—[/dim] Web search: {type(e).__name__}")

    if not search_results:
        console.print(
            "\n[yellow]No data found from automated search.[/yellow]\n"
            "[dim]Try searching manually and re-run, or use:\n"
            f"  https://www.google.com/search?q={requests.utils.quote(home + '+' + away + '+odds')}[/dim]"
        )
        return

    # ---- Run analysis ----
    from .scout import analyze_scout_data
    report = analyze_scout_data(home, away, search_results)

    # ---- Display report ----
    console.print(f"\n[bold underline]Scout Report: {home} vs {away}[/bold underline]")
    if report.competition:
        console.print(f"  Competition: {report.competition}")
    if report.kickoff:
        console.print(f"  Kickoff: {report.kickoff}")

    # Odds
    if report.odds_1x2[0] > 0:
        o = report.odds_1x2
        ip = report.implied_probs
        console.print(
            f"\n  [bold]Odds:[/bold] {o[0]:.2f} / {o[1]:.2f} / {o[2]:.2f}  "
            f"(source: {report.odds_source})"
        )
        console.print(
            f"  [bold]Market:[/bold] H {ip[0]:.1%} / D {ip[1]:.1%} / A {ip[2]:.1%}"
        )

    # Form
    if report.home_form or report.away_form:
        console.print(
            f"\n  [bold]Form:[/bold] "
            f"{home}: {''.join(report.home_form) if report.home_form else '?'}  "
            f"({report.home_strength})  |  "
            f"{away}: {''.join(report.away_form) if report.away_form else '?'}  "
            f"({report.away_strength})"
        )
        console.print(f"  [bold]Form edge:[/bold] {report.form_edge}")

    # H2H
    if report.h2h:
        console.print(f"\n  [bold]H2H:[/bold] {', '.join(report.h2h[:6])}")
        console.print(f"  [bold]H2H edge:[/bold] {report.h2h_edge}")

    # Verdict
    verdict_color = {"home": "green", "away": "red", "draw": "yellow", "too close": "dim"}
    console.print(
        f"\n[bold]Prediction:[/bold] "
        f"[{verdict_color.get(report.prediction, 'white')}]{report.prediction.upper()}[/]  "
        f"(confidence: [bold]{report.confidence}[/bold])"
    )

    if report.reasoning:
        for r in report.reasoning:
            console.print(f"  • {r}")

    if report.warnings:
        console.print("")
        for w in report.warnings:
            console.print(f"  [yellow]{w}[/yellow]")

    console.print(
        "\n[dim]Scout uses public web data only. "
        "Supplement with your own research before wagering.[/dim]"
    )


if __name__ == "__main__":
    main()