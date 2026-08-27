# /// script
# requires-python = ">=3.10"
# dependencies = ["garminconnect>=0.2.38"]
# ///
"""Sync daily health data from Garmin Connect into markdown files."""

import argparse
import os
import sys
import time
from datetime import date, timedelta
from getpass import getpass
from pathlib import Path

from garminconnect import Garmin


TOKEN_DIR = Path.home() / ".garminconnect"
VERBOSE = False


def default_output_dir() -> Path:
    """Health files live OUTSIDE the skill install dir so registry updates
    never see local changes: $GARMIN_PULSE_HEALTH_DIR, else XDG data dir.
    A legacy in-package health/ dir with existing files keeps working."""
    env = os.environ.get("GARMIN_PULSE_HEALTH_DIR")
    if env:
        return Path(env)
    legacy = Path(__file__).resolve().parent.parent / "health"
    if any(legacy.glob("*.md")):
        return legacy
    xdg = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local/share")
    return xdg / "garmin-pulse" / "health"


def setup(email: str) -> None:
    """One-time interactive setup: authenticate with email/password and cache tokens."""
    password = getpass("Garmin Connect password: ")
    if not password:
        print("Error: Password cannot be empty.", file=sys.stderr)
        sys.exit(1)

    TOKEN_DIR.mkdir(parents=True, exist_ok=True)
    tokenstore = str(TOKEN_DIR)

    def prompt_mfa() -> str:
        return input("Garmin MFA code: ").strip()

    client = Garmin(email, password, prompt_mfa=prompt_mfa)

    last_exc: Exception | None = None
    for attempt in range(3):
        try:
            client.login(tokenstore)
            last_exc = None
            break
        except Exception as e:
            last_exc = e
            if attempt < 2 and "no profile" in str(e).lower():
                time.sleep(2**attempt)
                continue
            break

    if last_exc is not None:
        msg = str(last_exc).lower()
        print(f"Error: Authentication failed — {last_exc}", file=sys.stderr)
        if "no profile" in msg or "connectapi" in msg:
            print(
                "\nThis usually means Garmin's servers are temporarily blocking requests.\n"
                "Try again in a few minutes. If it persists, double-check your password.",
                file=sys.stderr,
            )
        elif "401" in msg or "unauthorized" in msg or "credentials" in msg:
            print(
                "\nDouble-check your email and password. If you have two-factor\n"
                "authentication (2FA) enabled on your Garmin account, you may need\n"
                "to disable it — the garminconnect library does not support 2FA.",
                file=sys.stderr,
            )
        elif "cloudflare" in msg or "captcha" in msg or "403" in msg:
            print(
                "\nGarmin's Cloudflare protection may be blocking this request.\n"
                "Wait a few minutes and try again.",
                file=sys.stderr,
            )
        sys.exit(1)

    print(f"Success! Tokens cached in {TOKEN_DIR}")
    print("You can now run the sync command without credentials.")


def authenticate() -> Garmin:
    """Authenticate with Garmin Connect using cached tokens only."""
    client = Garmin()

    TOKEN_DIR.mkdir(parents=True, exist_ok=True)
    tokenstore = str(TOKEN_DIR)
    if not any(TOKEN_DIR.iterdir()):
        print(
            "Error: No cached tokens found.\n"
            "Run setup first:\n\n"
            "  uv run skills/garmin-pulse/scripts/sync_garmin.py --setup --email you@example.com\n",
            file=sys.stderr,
        )
        sys.exit(1)

    last_exc: Exception | None = None
    for attempt in range(3):
        try:
            client.login(tokenstore)
            return client
        except FileNotFoundError:
            print(
                "Error: No cached tokens found.\n"
                "Run setup first:\n\n"
                "  uv run scripts/sync_garmin.py --setup --email you@example.com\n",
                file=sys.stderr,
            )
            sys.exit(1)
        except Exception as e:
            last_exc = e
            if attempt < 2 and "no profile" in str(e).lower():
                time.sleep(2**attempt)
                continue
            break

    msg = str(last_exc).lower()
    if "no profile" in msg or "connectapi" in msg:
        print(
            "Error: Garmin's servers returned 'No profile'. This is usually\n"
            "temporary — wait a few minutes and try again. If it persists,\n"
            "re-run setup:\n\n"
            "  uv run scripts/sync_garmin.py --setup --email you@example.com\n",
            file=sys.stderr,
        )
    else:
        print(
            f"Error: Authentication failed — {last_exc}\n"
            "Your cached tokens may have expired. Re-run setup:\n\n"
            "  uv run scripts/sync_garmin.py --setup --email you@example.com\n",
            file=sys.stderr,
        )
    sys.exit(1)


def fmt_duration(seconds: float | int | None) -> str:
    """Format seconds into 'Xh Ym' string."""
    if seconds is None:
        return "—"
    total_minutes = int(seconds) // 60
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours}h {minutes:02d}m"


def fmt_duration_mmss(seconds: float | int | None) -> str:
    """Format seconds into 'MM:SS' string."""
    if seconds is None:
        return "—"
    total_seconds = int(seconds)
    minutes = total_seconds // 60
    secs = total_seconds % 60
    return f"{minutes}:{secs:02d}"


def fetch_sleep(client: Garmin, day: str) -> str | None:
    """Fetch and format sleep data."""
    try:
        data = client.get_sleep_data(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Sleep fetch failed: {e}", file=sys.stderr)
        return None

    daily = data.get("dailySleepDTO", {})
    if not daily or not daily.get("sleepTimeSeconds"):
        return None

    total = fmt_duration(daily.get("sleepTimeSeconds"))
    deep = fmt_duration(daily.get("deepSleepSeconds"))
    light = fmt_duration(daily.get("lightSleepSeconds"))
    rem = fmt_duration(daily.get("remSleepSeconds"))
    awake = fmt_duration(daily.get("awakeSleepSeconds"))

    score = daily.get("sleepScores", {}).get("overall", {}).get("value")
    qualifier = daily.get("sleepScores", {}).get("overall", {}).get("qualifierKey", "")
    # Clean up qualifier like "GOOD" -> "Good"
    qualifier_str = qualifier.replace("_", " ").title() if qualifier else ""

    header = f"## Sleep: {total}"
    if qualifier_str:
        header += f" ({qualifier_str})"

    lines = [header]
    lines.append(f"Deep: {deep} | Light: {light} | REM: {rem} | Awake: {awake}")
    if score is not None:
        lines.append(f"Sleep Score: {score}")

    return "\n".join(lines)


def fetch_body(client: Garmin, day: str) -> str | None:
    """Fetch and format body/activity summary data."""
    parts = []

    # User summary (steps, calories, distance, floors, active minutes)
    summary = None
    try:
        summary = client.get_user_summary(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] User summary fetch failed: {e}", file=sys.stderr)

    # Heart rates
    hr_data = None
    try:
        hr_data = client.get_heart_rates(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Heart rate fetch failed: {e}", file=sys.stderr)

    # Body Battery. Garmin returns a list of day records with
    # bodyBatteryValuesArray = [[timestamp_ms, level], ...]. Older versions of
    # this skill looked for a non-existent chargedValue field, so Body Battery
    # was silently omitted even though Garmin returned it.
    battery = None
    battery_charged = None
    battery_drained = None
    try:
        bb_data = client.get_body_battery(day, day)
        if bb_data and isinstance(bb_data, list) and len(bb_data) > 0:
            record = bb_data[-1] or {}
            battery_charged = record.get("charged")
            battery_drained = record.get("drained")
            values = [
                row[1]
                for row in record.get("bodyBatteryValuesArray", [])
                if isinstance(row, list) and len(row) > 1 and row[1] is not None
            ]
            if values:
                battery = values[-1]
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Body battery fetch failed: {e}", file=sys.stderr)

    # HRV
    hrv = None
    try:
        hrv_data = client.get_hrv_data(day)
        if hrv_data:
            summary_hrv = hrv_data.get("hrvSummary", {})
            if summary_hrv:
                hrv = summary_hrv.get("weeklyAvg") or summary_hrv.get("lastNightAvg")
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] HRV fetch failed: {e}", file=sys.stderr)

    # SpO2
    spo2 = None
    try:
        spo2_data = client.get_spo2_data(day)
        if spo2_data:
            spo2 = spo2_data.get("averageSpO2")
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] SpO2 fetch failed: {e}", file=sys.stderr)

    # Weight
    weight = None
    try:
        weight_data = client.get_daily_weigh_ins(day)
        if weight_data:
            entries = weight_data.get("dateWeightList", [])
            if entries:
                grams = entries[0].get("weight")
                if grams:
                    weight = round(grams / 1000, 1)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Weight fetch failed: {e}", file=sys.stderr)

    if not summary and not hr_data and battery is None and hrv is None:
        return None

    # Build header line
    steps = summary.get("totalSteps") if summary else None
    calories = summary.get("totalKilocalories") if summary else None

    header_parts = []
    if steps is not None:
        header_parts.append(f"{steps:,} steps")
    if calories is not None:
        header_parts.append(f"{int(calories):,} cal")

    header = "## Body"
    if header_parts:
        header += ": " + " | ".join(header_parts)

    lines = [header]

    # Distance and floors
    detail_parts = []
    if summary:
        distance_m = summary.get("totalDistanceMeters")
        if distance_m is not None:
            detail_parts.append(f"Distance: {distance_m / 1000:.1f} km")
        floors = summary.get("floorsAscended")
        if floors is not None:
            detail_parts.append(f"Floors: {int(floors)}")
    if detail_parts:
        lines.append(" | ".join(detail_parts))

    # HR line
    hr_parts = []
    if hr_data:
        resting = hr_data.get("restingHeartRate")
        if resting:
            hr_parts.append(f"Resting HR: {resting} bpm")
        max_hr = hr_data.get("maxHeartRate")
        if max_hr:
            hr_parts.append(f"Max HR: {max_hr} bpm")
    if hr_parts:
        lines.append(" | ".join(hr_parts))

    # Battery, HRV, SpO2, Weight
    extra_parts = []
    if battery is not None:
        battery_str = f"Body Battery: {battery}"
        battery_delta = []
        if battery_charged is not None:
            battery_delta.append(f"+{battery_charged}")
        if battery_drained is not None:
            battery_delta.append(f"-{battery_drained}")
        if battery_delta:
            battery_str += " (" + " / ".join(battery_delta) + ")"
        extra_parts.append(battery_str)
    if hrv is not None:
        extra_parts.append(f"HRV: {hrv} ms")
    if extra_parts:
        lines.append(" | ".join(extra_parts))

    if spo2 is not None:
        lines.append(f"SpO2: {spo2}%")

    if weight is not None:
        lines.append(f"Weight: {weight} kg")

    return "\n".join(lines)


def fetch_stress(client: Garmin, day: str) -> str | None:
    """Fetch and format stress data."""
    try:
        data = client.get_all_day_stress(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Stress fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None

    # Current garminconnect returns avgStressLevel; older skill expected
    # overallStressLevel, so Stress was silently omitted.
    avg = data.get("avgStressLevel")
    if avg is None:
        avg = data.get("overallStressLevel")
    if avg is None:
        return None

    if avg < 26:
        level = "Rest"
    elif avg < 51:
        level = "Low"
    elif avg < 76:
        level = "Medium"
    else:
        level = "High"

    return f"## Stress: Avg {avg} ({level})"


def fetch_training_readiness(client: Garmin, day: str) -> str | None:
    """Fetch and format training readiness data."""
    try:
        data = client.get_training_readiness(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Training readiness fetch failed: {e}", file=sys.stderr)
        return None

    if not data or not isinstance(data, list) or len(data) == 0:
        return None

    entry = data[0]
    score = entry.get("score")
    if score is None:
        return None

    level = entry.get("level", "").replace("_", " ").title()
    feedback = entry.get("feedbackShort", "").replace("_", " ").title()

    line = f"## Training Readiness: {score}"
    if level:
        line += f" ({level})"
    if feedback:
        line += f" — {feedback}"
    return line


def fetch_training_status(client: Garmin, day: str) -> str | None:
    """Fetch and format training load/status data for recovery context."""
    try:
        data = client.get_training_status(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Training status fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None

    lines = []

    vo2_root = data.get("mostRecentVO2Max") or {}
    vo2 = vo2_root.get("generic") or {}
    vo2_value = vo2.get("vo2MaxPreciseValue") or vo2.get("vo2MaxValue")
    if vo2_value is not None:
        lines.append(f"VO2 Max: {vo2_value:.1f}")

    load_balance_root = data.get("mostRecentTrainingLoadBalance") or {}
    load_balance_map = load_balance_root.get("metricsTrainingLoadBalanceDTOMap") or {}
    if load_balance_map:
        lb = next(iter(load_balance_map.values()))
        load_parts = []
        if lb.get("monthlyLoadAerobicLow") is not None:
            load_parts.append(f"low aerobic {lb.get('monthlyLoadAerobicLow'):.0f}")
        if lb.get("monthlyLoadAerobicHigh") is not None:
            load_parts.append(f"high aerobic {lb.get('monthlyLoadAerobicHigh'):.0f}")
        if lb.get("monthlyLoadAnaerobic") is not None:
            load_parts.append(f"anaerobic {lb.get('monthlyLoadAnaerobic'):.0f}")
        feedback = lb.get("trainingBalanceFeedbackPhrase")
        if load_parts:
            line = "Training Load Balance: " + " | ".join(load_parts)
            if feedback:
                line += f" ({feedback})"
            lines.append(line)

    status_root = data.get("mostRecentTrainingStatus") or {}
    status_map = status_root.get("latestTrainingStatusData") or {}
    if status_map:
        st = next(iter(status_map.values()))
        phrase = st.get("trainingStatusFeedbackPhrase")
        acute = st.get("acuteTrainingLoadDTO") or {}
        acute_parts = []
        if acute.get("dailyTrainingLoadAcute") is not None:
            acute_parts.append(f"acute {acute.get('dailyTrainingLoadAcute')}")
        if acute.get("dailyTrainingLoadChronic") is not None:
            acute_parts.append(f"chronic {acute.get('dailyTrainingLoadChronic')}")
        if acute.get("dailyAcuteChronicWorkloadRatio") is not None:
            acute_parts.append(f"ACWR {acute.get('dailyAcuteChronicWorkloadRatio'):.1f}")
        if acute.get("acwrStatus"):
            acute_parts.append(acute.get("acwrStatus"))
        if acute_parts:
            line = "Acute Load: " + " | ".join(str(x) for x in acute_parts)
            if phrase:
                line += f" ({phrase})"
            lines.append(line)

    accl = vo2_root.get("heatAltitudeAcclimation") or {}
    if accl:
        acc_parts = []
        if accl.get("heatAcclimationPercentage") is not None:
            acc_parts.append(f"heat {accl.get('heatAcclimationPercentage')}%")
        if accl.get("altitudeAcclimation") is not None:
            acc_parts.append(f"altitude {accl.get('altitudeAcclimation')}m")
        if accl.get("acclimationPercentage") is not None:
            acc_parts.append(f"acclimation {accl.get('acclimationPercentage')}%")
        if acc_parts:
            lines.append("Acclimation: " + " | ".join(acc_parts))

    if not lines:
        return None
    return "## Training Status\n" + "\n".join(lines)


def fetch_respiration(client: Garmin, day: str) -> str | None:
    """Fetch and format respiration data."""
    try:
        data = client.get_respiration_data(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Respiration fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None

    parts = []
    avg_waking = data.get("avgWakingRespirationValue")
    if avg_waking:
        parts.append(f"Waking: {avg_waking:.0f} brpm")
    avg_sleeping = data.get("avgSleepRespirationValue")
    if avg_sleeping:
        parts.append(f"Sleeping: {avg_sleeping:.0f} brpm")
    lowest = data.get("lowestRespirationValue")
    highest = data.get("highestRespirationValue")
    if lowest and highest:
        parts.append(f"Range: {lowest:.0f}–{highest:.0f}")

    if not parts:
        return None

    return "## Respiration: " + " | ".join(parts)


def fetch_fitness_age(client: Garmin, day: str) -> str | None:
    """Fetch and format fitness age data."""
    try:
        data = client.get_fitnessage_data(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Fitness age fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None

    fitness_age = data.get("fitnessAge")
    chrono_age = data.get("chronologicalAge")
    if fitness_age is None:
        return None

    line = f"## Fitness Age: {int(fitness_age)}"
    if chrono_age is not None:
        diff = int(fitness_age) - chrono_age
        if diff < 0:
            line += f" ({abs(diff)} years younger)"
        elif diff > 0:
            line += f" ({diff} years older)"
    return line


def fetch_intensity_minutes(client: Garmin, day: str) -> str | None:
    """Fetch and format weekly intensity minutes."""
    try:
        data = client.get_intensity_minutes_data(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Intensity minutes fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None

    moderate = data.get("weeklyModerate")
    vigorous = data.get("weeklyVigorous")
    total = data.get("weeklyTotal")
    goal = data.get("weekGoal")

    if total is None:
        return None

    parts = [f"## Intensity Minutes: {total} weekly"]
    detail = []
    if moderate is not None:
        detail.append(f"Moderate: {moderate}")
    if vigorous is not None:
        detail.append(f"Vigorous: {vigorous}")
    if goal is not None:
        detail.append(f"Goal: {goal}")
    if detail:
        parts.append(" | ".join(detail))

    return "\n".join(parts)


def fmt_race_time(seconds: float | int | None) -> str | None:
    """Format race prediction seconds into 'H:MM:SS' or 'MM:SS'."""
    if not seconds:
        return None
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def fetch_race_predictions(client: Garmin, day: str) -> str | None:
    """Fetch and format race time predictions (5K/10K/half/marathon)."""
    record = None
    try:
        data = client.get_race_predictions(startdate=day, enddate=day, _type="daily")
        if isinstance(data, list) and data:
            record = data[-1]
        elif isinstance(data, dict) and data.get("time5K"):
            record = data
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Race predictions fetch failed: {e}", file=sys.stderr)

    # The dated endpoint has no record for some days; for today the
    # parameterless call returns the current prediction.
    if record is None and day == date.today().isoformat():
        try:
            data = client.get_race_predictions()
            if isinstance(data, dict) and data.get("time5K"):
                record = data
        except Exception as e:
            if VERBOSE:
                print(f"    [verbose] Race predictions (latest) fetch failed: {e}", file=sys.stderr)

    if not record:
        return None

    parts = []
    for key, label in [
        ("time5K", "5K"),
        ("time10K", "10K"),
        ("timeHalfMarathon", "Half"),
        ("timeMarathon", "Marathon"),
    ]:
        formatted = fmt_race_time(record.get(key))
        if formatted:
            parts.append(f"{label} {formatted}")

    if not parts:
        return None
    return "## Race Predictions: " + " | ".join(parts)


def fetch_endurance_score(client: Garmin, day: str) -> str | None:
    """Fetch and format endurance score with classification label."""
    try:
        data = client.get_endurance_score(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Endurance score fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None
    score = data.get("overallScore")
    if score is None:
        return None

    # Classification thresholds ship in the payload; derive the label
    # instead of hardcoding Garmin's classification ids.
    label = "Beginner"
    for name, key in [
        ("Intermediate", "classificationLowerLimitIntermediate"),
        ("Trained", "classificationLowerLimitTrained"),
        ("Well Trained", "classificationLowerLimitWellTrained"),
        ("Expert", "classificationLowerLimitExpert"),
        ("Superior", "classificationLowerLimitSuperior"),
        ("Elite", "classificationLowerLimitElite"),
    ]:
        limit = data.get(key)
        if limit is not None and score >= limit:
            label = name

    return f"## Endurance Score: {score} ({label})"


def fetch_hill_score(client: Garmin, day: str) -> str | None:
    """Fetch and format hill score."""
    try:
        data = client.get_hill_score(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Hill score fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None
    overall = data.get("overallScore")
    if overall is None:
        return None

    line = f"## Hill Score: {overall}"
    detail = []
    if data.get("strengthScore") is not None:
        detail.append(f"Strength: {data.get('strengthScore')}")
    if data.get("enduranceScore") is not None:
        detail.append(f"Endurance: {data.get('enduranceScore')}")
    if detail:
        line += " (" + " | ".join(detail) + ")"
    return line


def fetch_lactate_threshold(client: Garmin, day: str) -> str | None:
    """Fetch and format lactate threshold / FTP. Latest measurement only,
    so it is included only when syncing today to avoid misdating."""
    if day != date.today().isoformat():
        return None
    try:
        data = client.get_lactate_threshold()
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Lactate threshold fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None
    shr = data.get("speed_and_heart_rate") or {}
    power = data.get("power") or {}

    parts = []
    hr = shr.get("heartRate")
    if hr:
        parts.append(f"HR {hr} bpm")
    ftp = power.get("functionalThresholdPower")
    if ftp:
        ftp_str = f"FTP {ftp} W"
        ptw = power.get("powerToWeight")
        if ptw:
            ftp_str += f" ({ptw:.1f} W/kg)"
        parts.append(ftp_str)

    if not parts:
        return None
    return "## Lactate Threshold: " + " | ".join(parts)


def fetch_hydration(client: Garmin, day: str) -> str | None:
    """Fetch and format hydration data (only when something was logged)."""
    try:
        data = client.get_hydration_data(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Hydration fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None
    value = data.get("valueInML")
    sweat = data.get("sweatLossInML")
    if value is None and sweat is None:
        return None

    parts = []
    if value is not None:
        intake = f"{int(value)} ml"
        goal = data.get("goalInML")
        if goal:
            intake += f" / goal {int(goal)} ml"
        parts.append(intake)
    if sweat is not None:
        parts.append(f"Sweat loss: {int(sweat)} ml")

    return "## Hydration: " + " | ".join(parts)


def fetch_nutrition(client: Garmin, day: str) -> str | None:
    """Fetch and format daily nutrition totals.

    Food logging is a Garmin Connect+ (paid) feature; on free accounts or days
    with nothing logged the payload has no dailyNutritionContent and the
    section is silently omitted."""
    try:
        data = client.get_nutrition_daily_food_log(day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Nutrition fetch failed: {e}", file=sys.stderr)
        return None

    if not data:
        return None
    content = data.get("dailyNutritionContent") or {}
    calories = content.get("calories")
    if calories is None:
        return None

    goals = data.get("dailyNutritionGoals") or {}
    goal = goals.get("adjustedCalories") or goals.get("calories")

    header = f"## Nutrition: {int(calories)} kcal"
    if goal:
        header += f" / goal {int(goal)}"
    pct = content.get("caloriesPercentage")
    if pct is not None:
        header += f" ({int(pct)}%)"

    lines = [header]
    macros = []
    for key, label in [("protein", "Protein"), ("fat", "Fat"), ("carbs", "Carbs")]:
        val = content.get(key)
        if val is not None:
            macros.append(f"{label}: {int(val)} g")
    if macros:
        lines.append(" | ".join(macros))

    return "\n".join(lines)


def fetch_activities(client: Garmin, day: str) -> str | None:
    """Fetch and format activities for the day."""
    try:
        activities = client.get_activities_by_date(day, day)
    except Exception as e:
        if VERBOSE:
            print(f"    [verbose] Activities fetch failed: {e}", file=sys.stderr)
        return None

    if not activities:
        return None

    lines = ["## Activities"]
    for act in activities:
        name = act.get("activityName", "Activity")
        duration = fmt_duration_mmss(act.get("duration"))
        header_parts = [f"**{name}** — {duration}"]

        distance = act.get("distance")
        if distance and distance > 0:
            header_parts.append(f"{distance / 1000:.1f} km")

        calories = act.get("calories")
        if calories and calories > 0:
            header_parts.append(f"{int(calories)} cal")

        lines.append("- " + ", ".join(header_parts))

        # Detail lines
        details = []

        avg_hr = act.get("averageHR")
        max_hr = act.get("maxHR")
        if avg_hr and avg_hr > 0:
            hr_str = f"Avg HR {int(avg_hr)}"
            if max_hr and max_hr > 0:
                hr_str += f" / Max {int(max_hr)}"
            details.append(hr_str)

        elev = act.get("elevationGain")
        if elev and elev > 0:
            details.append(f"Elevation: +{int(elev)}m")

        avg_speed = act.get("averageSpeed")
        if avg_speed and avg_speed > 0 and distance and distance > 0:
            pace_sec = 1000 / avg_speed
            pace_min = int(pace_sec) // 60
            pace_s = int(pace_sec) % 60
            details.append(f"Pace: {pace_min}:{pace_s:02d}/km")

        cadence = act.get("averageRunningCadenceInStepsPerMinute")
        if cadence and cadence > 0:
            details.append(f"Cadence: {int(cadence)} spm")

        avg_power = act.get("avgPower")
        if avg_power and avg_power > 0:
            power_str = f"Power: {int(avg_power)}W"
            max_power = act.get("maxPower")
            if max_power and max_power > 0:
                power_str += f" / Max {int(max_power)}W"
            details.append(power_str)

        aero_te = act.get("aerobicTrainingEffect")
        anaero_te = act.get("anaerobicTrainingEffect")
        if aero_te and aero_te > 0:
            te_str = f"Training Effect: {aero_te:.1f} aerobic"
            if anaero_te and anaero_te > 0:
                te_str += f" / {anaero_te:.1f} anaerobic"
            details.append(te_str)

        vo2 = act.get("vO2MaxValue")
        if vo2 and vo2 > 0:
            details.append(f"VO2 Max: {int(vo2)}")

        if details:
            lines.append("  " + " | ".join(details))

    return "\n".join(lines)


def sync_day(client: Garmin, day: date, output_dir: Path) -> None:
    """Sync a single day's data and write the markdown file."""
    day_str = day.isoformat()
    display_date = day.strftime("%B %-d, %Y")

    sections = [f"# Health — {display_date}"]

    sleep = fetch_sleep(client, day_str)
    if sleep:
        sections.append(sleep)

    body = fetch_body(client, day_str)
    if body:
        sections.append(body)

    nutrition = fetch_nutrition(client, day_str)
    if nutrition:
        sections.append(nutrition)

    hydration = fetch_hydration(client, day_str)
    if hydration:
        sections.append(hydration)

    stress = fetch_stress(client, day_str)
    if stress:
        sections.append(stress)

    readiness = fetch_training_readiness(client, day_str)
    if readiness:
        sections.append(readiness)

    training_status = fetch_training_status(client, day_str)
    if training_status:
        sections.append(training_status)

    endurance = fetch_endurance_score(client, day_str)
    if endurance:
        sections.append(endurance)

    hill = fetch_hill_score(client, day_str)
    if hill:
        sections.append(hill)

    race = fetch_race_predictions(client, day_str)
    if race:
        sections.append(race)

    lactate = fetch_lactate_threshold(client, day_str)
    if lactate:
        sections.append(lactate)

    respiration = fetch_respiration(client, day_str)
    if respiration:
        sections.append(respiration)

    fitness_age = fetch_fitness_age(client, day_str)
    if fitness_age:
        sections.append(fitness_age)

    intensity = fetch_intensity_minutes(client, day_str)
    if intensity:
        sections.append(intensity)

    activities = fetch_activities(client, day_str)
    if activities:
        sections.append(activities)

    if len(sections) == 1:
        print(f"  {day_str}: No data available, skipping.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{day_str}.md"
    output_file.write_text("\n\n".join(sections) + "\n")
    print(f"  {day_str}: Written to {output_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync Garmin Connect health data to markdown.")
    parser.add_argument("--setup", action="store_true", help="One-time setup: authenticate and cache tokens.")
    parser.add_argument("--email", type=str, help="Garmin Connect email (used with --setup).")
    parser.add_argument("--date", type=str, help="Specific date to sync (YYYY-MM-DD). Default: today.")
    parser.add_argument("--days", type=int, help="Sync the last N days.")
    parser.add_argument("--verbose", action="store_true", help="Show detailed error info for failed data fetches.")
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Output directory for markdown files (default: $GARMIN_PULSE_HEALTH_DIR "
        "or ~/.local/share/garmin-pulse/health).",
    )
    args = parser.parse_args()

    global VERBOSE
    VERBOSE = args.verbose

    if args.setup:
        if not args.email:
            print("Error: --email is required with --setup.", file=sys.stderr)
            sys.exit(1)
        setup(args.email)
        return

    output_dir = Path(args.output_dir).expanduser() if args.output_dir else default_output_dir()

    # Determine which days to sync
    if args.days:
        today = date.today()
        days = [today - timedelta(days=i) for i in range(args.days)]
    elif args.date:
        try:
            days = [date.fromisoformat(args.date)]
        except ValueError:
            print(f"Error: Invalid date format '{args.date}'. Use YYYY-MM-DD.", file=sys.stderr)
            sys.exit(1)
    else:
        days = [date.today()]

    print("Authenticating with Garmin Connect...")
    client = authenticate()
    print(f"Syncing {len(days)} day(s)...")

    for day in sorted(days):
        sync_day(client, day, output_dir)

    print("Done.")


if __name__ == "__main__":
    main()
