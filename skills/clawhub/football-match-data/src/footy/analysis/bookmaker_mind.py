"""庄家意图解析器 — reverse-engineer the bookmaker's real intent.

Core principle: every odds line, handicap, and movement is a DELIBERATE choice.
Don't just analyze the match — analyze what the BOOKMAKER is doing.

Three questions for every match:
  1. 开盘意图: What was the bookmaker trying to achieve?
  2. 真实保护: Which side are they ACTUALLY protecting?
  3. 散户流向: Where will public money go vs where it SHOULD go?
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BookmakerIntent:
    """Reverse-engineered bookmaker strategy for a match."""

    match: str = ""
    favorite: str = ""
    underdog: str = ""

    # ---- What the bookmaker DID ----
    open_line: float = 0.0      # opening handicap
    close_line: float = 0.0     # current handicap
    fav_odds: float = 0.0       # favorite's decimal odds

    # ---- What we INFER ----
    intent_type: str = ""       # "诱杀" / "阻上" / "平衡" / "失控"
    protected_side: str = ""    # which side the bookmaker is protecting
    public_trap: str = ""       # which side is the trap
    depth_analysis: str = ""    # handicap depth analysis

    # ---- Risk assessment ----
    bookmaker_fear: str = ""    # which outcome hurts them most
    public_flow_prediction: str = ""  # where will public money go
    profit_strategy: str = ""   # how the bookmaker plans to profit

    # ---- Signal for our betting ----
    our_action: str = ""        # what WE should do based on this
    confidence: str = ""        # "high" / "medium" / "low"


def analyze_intent(
    home: str, away: str,
    home_odds: float, draw_odds: float, away_odds: float,
    open_ah: float, close_ah: float,
    public_bias: str = "",       # "home" / "away" / "balanced" — where public naturally leans
    sharp_money_on: str = "",    # from 必发: where smart money is
    steam_direction: str = "",   # from Steam analysis
    host_advantage: bool = False,
    injuries_fav: int = 0,
    injuries_dog: int = 0,
    favorite_must_win: bool = False,
    underdog_must_win: bool = False,
) -> BookmakerIntent:
    """Reverse-engineer bookmaker intent from odds and fundamentals."""

    fav_is_home = home_odds < away_odds
    fav = home if fav_is_home else away
    dog = away if fav_is_home else home
    fav_odds = min(home_odds, away_odds)
    dog_odds = max(home_odds, away_odds)

    intent = BookmakerIntent(
        match=f"{home} v {away}",
        favorite=fav, underdog=dog,
        open_line=open_ah, close_line=close_ah, fav_odds=fav_odds,
    )

    # ---- Step 1: Determine opening intent ----
    abs_line = abs(close_ah)
    odds_ratio = fav_odds / dog_odds if dog_odds > 0 else 1.0
    line_moved_deeper = abs(close_ah) > abs(open_ah)
    line_moved_shallower = abs(close_ah) < abs(open_ah)

    # ---- Step 2: Classify the bookmaker's strategy ----
    if abs_line >= 1.25 and odds_ratio < 0.12:
        # Super deep handicap + massive gap = genuine strength
        intent.intent_type = "实力碾压(少操盘)"
        intent.protected_side = fav
        intent.depth_analysis = f"深盘{abs_line:.1f}是真实力，非诱。散户会觉得'太深'而去{dog}。"
        intent.public_trap = dog
    elif abs_line >= 1.0 and odds_ratio > 0.18:
        # Deep but gap not that big — bookmaker stretching
        intent.intent_type = "深盘诱杀"
        intent.protected_side = fav
        intent.depth_analysis = (
            f"盘口{abs_line:.1f}偏深但实力差有限(ratio={odds_ratio:.2f})。"
            f"庄家利用深盘吓散户去{dog}。真实意图：{fav}穿盘，吃{dog}方向。"
        )
        intent.public_trap = dog
    elif abs_line <= 0.50 and host_advantage and not fav_is_home:
        # Shallow handicap + dog is host — bookmaker subtle trap
        intent.intent_type = "东道主逆开盘"
        intent.protected_side = dog
        intent.depth_analysis = (
            f"{dog}是东道主，但庄家开{fav}让球({abs_line:.1f})。"
            f"逆势开盘→制造{fav}优势假象→引诱散户去{fav}。"
            f"真实保护：{dog}。东道主难输。"
        )
        intent.public_trap = fav
    elif abs_line <= 0.50 and odds_ratio > 0.35 and host_advantage:
        # Shallow handicap + close odds + host — balanced trap
        intent.intent_type = "东道主诱盘"
        intent.protected_side = dog
        intent.depth_analysis = (
            f"浅盘{abs_line:.1f}看似{fav}便宜+{dog}东道主。"
            f"散户双面纠结→庄家小幅调整引导流向。"
        )
        intent.public_trap = fav
    elif abs_line <= 0.50 and odds_ratio < 0.18:
        # Shallow but big gap — bookmaker blocking
        intent.intent_type = "浅盘阻上"
        intent.protected_side = fav
        intent.depth_analysis = f"盘口偏浅({abs_line:.1f})但实力差大(ratio={odds_ratio:.2f})。庄家制造{fav}不稳假象，阻挡资金。"
        intent.public_trap = fav
    elif abs_line <= 0.50 and odds_ratio > 0.40:
        # Shallow and close — genuine balance
        intent.intent_type = "均衡观望"
        intent.protected_side = "难判断"
        intent.depth_analysis = "盘口合理，无明显操盘意图。庄家自己也没把握。"
        intent.public_trap = "无明显陷阱"
    elif line_moved_shallower and abs_line >= 0.75:
        # Line dropping on deep handicap — bookmaker cooling
        intent.intent_type = "退盘散热"
        intent.protected_side = fav
        intent.depth_analysis = f"深盘退至{abs_line:.1f}→庄家主动降热度。{fav}仍可信但可能只赢1球。"
        intent.public_trap = "无明显陷阱"
    else:
        intent.intent_type = "标准开盘"
        intent.protected_side = fav
        intent.depth_analysis = "无显著异常操盘信号。"
        intent.public_trap = "无明显陷阱"

    # ---- Step 3: Public flow prediction ----
    public_reasons = []
    if host_advantage and not fav_is_home:
        public_reasons.append(f"{dog}是东道主")
    if underdog_must_win:
        public_reasons.append(f"{dog}必须赢")
    if injuries_fav >= 2:
        public_reasons.append(f"{fav}伤停{injuries_fav}人")
    if abs_line >= 1.5:
        public_reasons.append(f"深盘{dog}太便宜")

    if public_reasons:
        intent.public_flow_prediction = f"散户会押{dog}——" + "，".join(public_reasons)
    elif public_bias:
        intent.public_flow_prediction = f"散户倾向于{public_bias}"
    else:
        intent.public_flow_prediction = "散户无明显倾向"

    # ---- Step 4: Bookmaker's profit strategy ----
    if intent.intent_type == "深盘诱杀":
        intent.profit_strategy = f"引诱散户押{dog}+{abs_line:.1f}→{fav}穿盘→庄家通吃散户"
    elif intent.intent_type == "浅盘阻上":
        intent.profit_strategy = f"制造{fav}不稳假象→散户去{dog}→{fav}打出→庄家吃{dog}方向"
    elif intent.intent_type == "实力碾压(少操盘)":
        intent.profit_strategy = f"不操盘，用实力差自然吃{dog}方向。散户天然喜欢高赔。"
    else:
        intent.profit_strategy = "标准操盘，吃抽水为主"

    # ---- Step 5: Bookmaker's fear ----
    if intent.protected_side == fav:
        intent.bookmaker_fear = f"最怕{dog}爆冷。{fav}方向注码重。"
    elif intent.protected_side == dog:
        intent.bookmaker_fear = f"最怕{fav}穿盘。{dog}方向散户多。"
    else:
        intent.bookmaker_fear = "风险分散，无特别暴露"

    # ---- Step 6: Our action ----
    if intent.intent_type == "东道主逆开盘" or intent.intent_type == "东道主诱盘":
        intent.our_action = f"庄家逆势开盘保护{dog}（东道主）。{dog}不败，考虑{dog}+AH。避开{fav}。"
        intent.confidence = "high"
    elif intent.intent_type == "深盘诱杀":
        intent.our_action = f"庄家深盘吓散户去{dog}，真实保护{fav}。{fav}1X2可信，但穿盘需看基本面。"
        intent.confidence = "high"
    elif intent.intent_type == "浅盘阻上":
        intent.our_action = f"庄家制造{fav}不稳假象。跟庄家，{fav}方向可信。不追穿盘。"
        intent.confidence = "medium"
    elif intent.intent_type == "实力碾压(少操盘)":
        intent.our_action = f"{fav}实力碾压，庄家不操盘=信心足。1X2稳。"
        intent.confidence = "high"
    elif intent.intent_type == "退盘散热":
        intent.our_action = f"庄家主动降盘散热→{fav}仍可信但可能只赢1球。小注1X2，不追穿盘。"
        intent.confidence = "medium"
    elif intent.intent_type == "均衡观望":
        intent.our_action = "庄家也没把握，轻仓或不碰。"
        intent.confidence = "low"
    else:
        intent.our_action = "按基本面正常分析。"
        intent.confidence = "medium"

    return intent
