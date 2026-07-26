from types import SimpleNamespace

import player_goal_value as pgv


def test_combo_leg_question_converts_title_to_will_score_market():
    leg = {
        "display": {
            "marketTitle": "Vinícius Júnior: 1+ goals",
            "eventTitle": "Brazil vs. Japan",
        }
    }

    assert pgv.combo_leg_question(leg) == "Will Vinícius Júnior score at least one goal in Brazil vs. Japan?"
    assert pgv.is_player_goal_market(pgv.combo_leg_question(leg))
    assert pgv.extract_player_name(pgv.combo_leg_question(leg)) == "Vinícius Júnior"


def test_fetch_premade_combo_player_goal_markets(monkeypatch):
    def fake_gamma_json(path, params=None):
        assert path == "/events/slug/fifwc-bra-jpn-2026-06-29/premade-combos"
        assert params == {"placement": "event_under_chart"}
        return {
            "shelves": [
                {
                    "combos": [
                        {
                            "legs": [
                                {
                                    "marketId": "2696247",
                                    "marketSlug": "fifwc-bra-jpn-2026-06-29-goals-vinicius-junior-gte1",
                                    "eventSlug": "fifwc-bra-jpn-2026-06-29",
                                    "sportsMarketType": "soccer_player_goals",
                                    "display": {
                                        "marketTitle": "Vinícius Júnior: 1+ goals",
                                        "eventTitle": "Brazil vs. Japan",
                                    },
                                    "prices": {"yes": 0.385, "no": 0.615},
                                },
                                {
                                    "marketId": "2690979",
                                    "sportsMarketType": "moneyline",
                                    "display": {"marketTitle": "Will Brazil win on 2026-06-29?"},
                                    "prices": {"yes": 0.575, "no": 0.425},
                                },
                            ]
                        }
                    ]
                }
            ]
        }

    monkeypatch.setattr(pgv, "gamma_json", fake_gamma_json)

    markets = pgv.fetch_premade_combo_player_goal_markets("fifwc-bra-jpn-2026-06-29")

    assert len(markets) == 1
    market = markets[0]
    assert market.id == "2696247"
    assert market.event_slug == "fifwc-bra-jpn-2026-06-29"
    assert market.yes_ask == 0.385
    assert market.import_source == "gamma_premade_combo"
    assert market.question == "Will Vinícius Júnior score at least one goal in Brazil vs. Japan?"


def test_discover_markets_includes_combo_player_goal_markets(monkeypatch):
    fake_client = SimpleNamespace(get_markets=lambda **kwargs: [])
    monkeypatch.setattr(pgv, "api_market_search", lambda query, limit: [])
    monkeypatch.setattr(pgv, "discover_combo_player_goal_markets", lambda: [
        SimpleNamespace(id="2696226", question="Will Ayase Ueda score at least one goal in Brazil vs. Japan?")
    ])

    markets = pgv.discover_markets(fake_client)

    assert [m.id for m in markets] == ["2696226"]
    assert pgv.is_player_goal_market(markets[0].question)
