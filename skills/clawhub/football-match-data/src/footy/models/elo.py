"""Elo rating system for football teams — 《足球财富》《足彩310实战指南》.

Provides a baseline team strength rating that can be used to:
  1. Detect 蛊惑盘 (suspicious handicap): actual handicap mismatches Elo expectation
  2. Detect 赶盘 (chase-away): bookmaker makes favorite look weak
  3. Cross-validate Dixon-Coles Poisson predictions

Formula (standard Elo):
  Expected = 1 / (1 + 10^((rating_opponent - rating_team) / 400))
  New = Old + K * (Result - Expected)

K-factor: 30 for league matches (balanced), 50 for cup/tournament.
Home advantage: +100 points.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Optional

log = logging.getLogger(__name__)

# Default ratings for major teams (seeded from historical data)
DEFAULT_RATINGS = {
    # EPL
    "Man City": 1950, "Arsenal": 1880, "Liverpool": 1920, "Chelsea": 1820,
    "Man United": 1800, "Tottenham": 1780, "Newcastle": 1760, "Aston Villa": 1720,
    "Brighton": 1700, "West Ham": 1680, "Crystal Palace": 1660, "Fulham": 1640,
    "Brentford": 1630, "Everton": 1620, "Wolves": 1610, "Bournemouth": 1600,
    "Nott'm Forest": 1590, "Leicester": 1650, "Leeds": 1640, "Southampton": 1580,
    # La Liga
    "Real Madrid": 1950, "Barcelona": 1920, "Ath Madrid": 1850, "Real Sociedad": 1780,
    "Betis": 1720, "Villarreal": 1740, "Ath Bilbao": 1730, "Sevilla": 1700,
    "Valencia": 1680, "Osasuna": 1640, "Celta": 1630, "Mallorca": 1610,
    "Girona": 1670, "Rayo Vallecano": 1620, "Getafe": 1600, "Alaves": 1590,
    "Granada": 1570, "Cadiz": 1560, "Almeria": 1550, "Las Palmas": 1530,
    # Bundesliga
    "Bayern Munich": 1970, "Dortmund": 1850, "RB Leipzig": 1830, "Leverkusen": 1880,
    "Ein Frankfurt": 1740, "Freiburg": 1720, "Wolfsburg": 1710, "Hoffenheim": 1700,
    "B. M'gladbach": 1690, "Mainz": 1660, "Werder Bremen": 1650, "Augsburg": 1630,
    "Stuttgart": 1700, "Union Berlin": 1670, "Bochum": 1600, "Heidenheim": 1580,
    "Darmstadt": 1560, "FC Koln": 1620,
    # Serie A
    "Inter": 1900, "AC Milan": 1860, "Juventus": 1840, "Napoli": 1830,
    "Atalanta": 1810, "Roma": 1800, "Lazio": 1780, "Fiorentina": 1760,
    "Bologna": 1750, "Torino": 1710, "Monza": 1680, "Genoa": 1670,
    "Udinese": 1660, "Lecce": 1620, "Cagliari": 1610, "Empoli": 1600,
    "Verona": 1590, "Salernitana": 1570, "Frosinone": 1560, "Sassuolo": 1680,
    # Ligue 1
    "Paris SG": 1950, "Marseille": 1780, "Lens": 1760, "Lyon": 1750,
    "Monaco": 1770, "Lille": 1740, "Rennes": 1730, "Nice": 1700,
    "Strasbourg": 1670, "Reims": 1660, "Toulouse": 1640, "Nantes": 1630,
    "Montpellier": 1630, "Brest": 1650, "Le Havre": 1590, "Metz": 1580,
    "Clermont": 1570, "Lorient": 1590,
    # World Cup national teams
    "Argentina": 2200, "France": 2180, "Brazil": 2150, "England": 2120,
    "Spain": 2100, "Germany": 2080, "Portugal": 2060, "Netherlands": 2040,
    "Italy": 2020, "Belgium": 2000, "Uruguay": 1980, "Croatia": 1960,
    "Morocco": 1880, "Colombia": 1900, "Mexico": 1860, "USA": 1840,
    "Japan": 1820, "South Korea": 1800, "Senegal": 1800, "Serbia": 1780,
    "Switzerland": 1780, "Denmark": 1820, "Sweden": 1770, "Norway": 1760,
    "Austria": 1760, "Poland": 1740, "Egypt": 1700, "Ghana": 1680,
    "Cameroon": 1700, "Nigeria": 1720, "Ivory Coast": 1700, "Tunisia": 1660,
    "Algeria": 1660, "Canada": 1700, "Costa Rica": 1640, "Panama": 1580,
    "Saudi Arabia": 1560, "Qatar": 1550, "Iran": 1620, "Australia": 1700,
    "Paraguay": 1640, "Chile": 1720, "Ecuador": 1680, "Peru": 1660,
    # Swedish Allsvenskan
    "Malmo FF": 1780, "Djurgarden": 1720, "Hacken": 1700, "Elfsborg": 1680,
    "Hammarby": 1670, "GAIS": 1580, "Brommapojkarna": 1530, "Sirius": 1550,
    "Mjallby": 1520,
}


# Chinese → English team name mapping (for titan007 / 500.com data)
_CN_TO_EN: dict[str, str] = {
    # World Cup
    "阿根廷": "Argentina", "法国": "France", "巴西": "Brazil", "英格兰": "England",
    "西班牙": "Spain", "德国": "Germany", "葡萄牙": "Portugal", "荷兰": "Netherlands",
    "意大利": "Italy", "比利时": "Belgium", "乌拉圭": "Uruguay", "克罗地亚": "Croatia",
    "摩洛哥": "Morocco", "哥伦比亚": "Colombia", "墨西哥": "Mexico", "美国": "USA",
    "日本": "Japan", "韩国": "South Korea", "塞内加尔": "Senegal",
    "瑞士": "Switzerland", "丹麦": "Denmark", "瑞典": "Sweden", "挪威": "Norway",
    "奥地利": "Austria", "波兰": "Poland", "埃及": "Egypt", "加纳": "Ghana",
    "喀麦隆": "Cameroon", "尼日利亚": "Nigeria", "突尼斯": "Tunisia",
    "阿尔及利亚": "Algeria", "加拿大": "Canada", "哥斯达黎加": "Costa Rica",
    "沙特": "Saudi Arabia", "卡塔尔": "Qatar", "伊朗": "Iran", "澳大利亚": "Australia",
    "巴拉圭": "Paraguay", "智利": "Chile", "厄瓜多尔": "Ecuador", "秘鲁": "Peru",
    "佛得角": "Cape Verde", "新西兰": "New Zealand", "俄罗斯": "Russia",
    # Club teams (common Chinese names)
    "曼城": "Man City", "阿森纳": "Arsenal", "利物浦": "Liverpool", "切尔西": "Chelsea",
    "曼联": "Man United", "热刺": "Tottenham", "纽卡": "Newcastle",
    "皇马": "Real Madrid", "巴萨": "Barcelona", "马竞": "Ath Madrid",
    "拜仁": "Bayern Munich", "多特": "Dortmund", "莱比锡": "RB Leipzig",
    "巴黎": "Paris SG", "马赛": "Marseille", "里昂": "Lyon", "摩纳哥": "Monaco",
    "尤文": "Juventus", "国米": "Inter", "AC米兰": "AC Milan", "那不勒斯": "Napoli",
    "马尔默": "Malmo FF",
    # Swedish teams  
    "布洛马波卡纳": "Brommapojkarna",
    "加尔斯": "GAIS",
    "赫根": "Hacken",
    "佐加顿斯": "Djurgarden",
    "埃尔夫斯堡": "Elfsborg",
    "哈马比": "Hammarby",
    "天狼星": "Sirius",
    "米亚尔比": "Mjallby",
}


class EloSystem:
    """Team strength ratings with Elo updating and handicap estimation."""

    HOME_ADVANTAGE = 100  # Home team gets +100 Elo

    def __init__(self, k_league: int = 30, k_cup: int = 50):
        self.k_league = k_league
        self.k_cup = k_cup
        self.ratings: dict[str, float] = dict(DEFAULT_RATINGS)

    def get(self, team: str) -> float:
        """Get a team's rating, or a sensible default."""
        # Try direct lookup first, then Chinese→English mapping
        if team in self.ratings:
            return self.ratings[team]
        mapped = _CN_TO_EN.get(team, team)
        return self.ratings.get(mapped, 1500.0)

    def expected(self, team_a: str, team_b: str, home_is_a: bool = True) -> float:
        """Expected win probability for team_a (0-1)."""
        ra = self.get(team_a)
        rb = self.get(team_b)
        if home_is_a:
            ra += self.HOME_ADVANTAGE
        return 1.0 / (1.0 + 10.0 ** ((rb - ra) / 400.0))

    def update(self, team_a: str, team_b: str, goals_a: int, goals_b: int,
               is_cup: bool = False) -> None:
        """Update ratings based on match result."""
        k = self.k_cup if is_cup else self.k_league
        # Result from team_a's perspective: 1=win, 0.5=draw, 0=loss
        if goals_a > goals_b:
            result_a = 1.0
        elif goals_a == goals_b:
            result_a = 0.5
        else:
            result_a = 0.0

        expected_a = self.expected(team_a, team_b, home_is_a=True)
        delta = k * (result_a - expected_a)

        # Ensure both teams exist in ratings
        if team_a not in self.ratings:
            self.ratings[team_a] = 1500.0
        if team_b not in self.ratings:
            self.ratings[team_b] = 1500.0

        self.ratings[team_a] += delta
        self.ratings[team_b] -= delta

    def expected_handicap(self, home: str, away: str) -> float:
        """Estimate fair Asian handicap based on Elo difference."""
        diff = self.get(home) + self.HOME_ADVANTAGE - self.get(away)
        # Rough conversion: 100 Elo ≈ 0.25 goals
        return diff / 100.0 * 0.25

    def is_suspicious_handicap(self, home: str, away: str,
                                actual_handicap: float,
                                threshold: float = 0.50) -> bool:
        """Check for 蛊惑盘/赶盘: actual handicap depth deviates from Elo fair."""
        fair_depth = abs(self.expected_handicap(home, away))
        return abs(abs(actual_handicap) - fair_depth) > threshold

    def handicap_signal(self, home: str, away: str,
                         actual_handicap: float) -> str:
        """Interpret handicap vs Elo expectation. Returns signal string.
        
        Compares absolute handicap depth: deeper = more goals favorite must give.
        """
        fair_depth = abs(self.expected_handicap(home, away))
        actual_depth = abs(actual_handicap)
        diff = actual_depth - fair_depth

        if abs(diff) < 0.25:
            return "合理"
        elif diff > 0.50:
            return "🔴 蛊惑盘: 实际盘远深于实力→诱上盘"
        elif diff < -0.50:
            return "🔴 浅开陷阱: 实际盘远浅于实力→冷门风险"
        elif diff > 0.25:
            return "⚠️ 深开: 庄家强推上盘"
        else:
            return "⚠️ 浅开: 庄家看低上盘"

    def load_db_matches(self, db_path: str) -> int:
        """Load all matches from SQLite DB to initialize ratings."""
        import sqlite3
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cur = conn.execute(
                "SELECT home, away, home_goals, away_goals FROM matches "
                "WHERE home_goals IS NOT NULL ORDER BY date"
            )
            count = 0
            for row in cur:
                self.update(row["home"], row["away"],
                           row["home_goals"], row["away_goals"])
                count += 1
            conn.close()
            log.info("Elo loaded %d matches from DB", count)
            return count
        except Exception as e:
            log.warning("Elo DB load failed: %s", e)
            return 0


# Singleton
_elo: Optional[EloSystem] = None


def get_elo() -> EloSystem:
    global _elo
    if _elo is None:
        _elo = EloSystem()
        # Load from DB to train ratings
        db_paths = []
        for base in [Path(__file__).resolve().parent.parent.parent.parent,
                     Path.cwd()]:
            dbp = base / "data" / "footy.db"
            if dbp.exists():
                db_paths.append(str(dbp))
        for dbp in db_paths:
            n = _elo.load_db_matches(dbp)
            if n > 0:
                log.info("Elo trained on %d matches from %s", n, dbp)
                break
        else:
            log.warning("Elo: no DB found, using default ratings only")
    return _elo
