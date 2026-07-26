import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.safety_circuit_breaker import SafetyCircuitBreaker


@pytest.fixture
def breaker():
    return SafetyCircuitBreaker()


TEST_CASES = [
    pytest.param(4200, 1, True, "理塘", None, "critical", id="high_altitude+low_acclimatization"),
    pytest.param(3000, 1, True, "林芝", None, "none", id="safe_altitude"),
    pytest.param(4700, 2, True, "那曲", None, "critical", id="very_high_altitude"),
    pytest.param(4000, 5, True, None, None, "none", id="acclimatized"),
    pytest.param(4200, 1, False, None, None, "none", id="no_overnight"),
    pytest.param(3500, 1, True, None, "暴雪红色预警", "warning", id="weather_trigger"),
    pytest.param(5200, 7, True, "珠峰大本营", None, "extreme", id="extreme_altitude"),
    pytest.param(4200, 0, True, "理塘", None, "critical", id="days_zero"),
    pytest.param(3800, 1, True, "拉萨", None, "none", id="boundary_3800m"),
    pytest.param(4500, 5, True, "纳木错", None, "none", id="acclimatized_at_4500"),
    pytest.param(5000, 10, True, "阿里", None, "extreme", id="boundary_5000m"),
    pytest.param(5000, 10, False, "阿里", None, "none", id="boundary_5000m_no_overnight"),
    pytest.param(0, 3, True, "成都", None, "none", id="zero_altitude"),
    pytest.param(4200, 1, True, None, "暴雨橙色预警+山洪预警", "critical", id="multi_weather_keywords"),
]


class TestSafetyCircuitBreaker:
    def test_evaluate(self, breaker):
        r = breaker.evaluate(target_altitude=4200, days_in_plateau=1,
                             stay_overnight=True, location_name="理塘")
        assert r["severity"] == "critical"
        assert r["triggered"] is True

    def test_safe_scenario(self, breaker):
        r = breaker.evaluate(target_altitude=3000, days_in_plateau=1,
                             stay_overnight=True, location_name="林芝")
        assert r["severity"] == "none"
        assert r["triggered"] is False

    def test_extreme_altitude(self, breaker):
        r = breaker.evaluate(target_altitude=5200, days_in_plateau=7,
                             stay_overnight=True, location_name="珠峰大本营")
        assert r["severity"] == "extreme"
        assert r["triggered"] is True

    def test_days_zero(self, breaker):
        r = breaker.evaluate(target_altitude=4200, days_in_plateau=0,
                             stay_overnight=True, location_name="理塘")
        assert r["severity"] == "critical"
        assert r["triggered"] is True

    def test_weather_trigger_only(self, breaker):
        r = breaker.evaluate(target_altitude=3500, days_in_plateau=1,
                             stay_overnight=True, weather_warning="暴雪红色预警")
        assert r["severity"] == "warning"
        assert r["triggered"] is True

    def test_multi_weather_keywords(self, breaker):
        r = breaker.evaluate(target_altitude=4200, days_in_plateau=1,
                             stay_overnight=True, weather_warning="暴雨橙色预警+山洪预警")
        assert r["severity"] == "critical"
        assert r["triggered"] is True

    def test_evaluate_from_json(self, breaker):
        json_input = '{"target_altitude": 4200, "days_in_plateau": 1, "stay_overnight": true}'
        result = breaker.evaluate_from_json(json_input)
        import json
        r = json.loads(result)
        assert r["severity"] == "critical"
        assert r["triggered"] is True

    def test_bad_json(self, breaker):
        result = breaker.evaluate_from_json("not json")
        import json
        r = json.loads(result)
        assert "error" in r

    def test_output_structure(self, breaker):
        r = breaker.evaluate(target_altitude=4200, days_in_plateau=1,
                             stay_overnight=True, location_name="那曲")
        assert all(k in r for k in ("triggered", "severity", "warning_text", "suggestion"))

    def test_severity_values(self, breaker):
        valid = {"extreme", "critical", "warning", "info", "none"}
        for alt, days, overnight, loc, weather, expected in [
            (4200, 1, True, "理塘", None, "critical"),
            (3000, 1, True, "林芝", None, "none"),
            (5200, 7, True, "珠峰", None, "extreme"),
        ]:
            r = breaker.evaluate(target_altitude=alt, days_in_plateau=days,
                                 stay_overnight=overnight, location_name=loc,
                                 weather_warning=weather)
            assert r["severity"] in valid


@pytest.mark.parametrize("altitude,days,overnight,location,weather,expected", TEST_CASES)
def test_parametrized(breaker, altitude, days, overnight, location, weather, expected):
    r = breaker.evaluate(target_altitude=altitude, days_in_plateau=days,
                         stay_overnight=overnight, location_name=location,
                         weather_warning=weather)
    assert r["severity"] == expected, (
        f"alt={altitude}, days={days}, overnight={overnight}: "
        f"got {r['severity']}, expected {expected}"
    )
