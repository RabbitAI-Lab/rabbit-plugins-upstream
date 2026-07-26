#!/usr/bin/env python3
"""Gate tests. No network, no API key, no SDK required.

Each test names the behaviour it protects. The interesting ones are the
abstentions: this skill's value is in the trades it refuses.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sizing_guard import (  # noqa: E402
    MAX_KELLY_MULTIPLIER,
    MAX_LAMBDA,
    Decision,
    decide,
    lambda_from_accuracy,
    shrink_probability,
)


class TestLambda(unittest.TestCase):
    def test_matches_closed_form(self):
        # sigma_est=0.06, sigma_mkt=0.03 -> 0.0009/(0.0009+0.0036) = 0.2
        # Simulation put the empirical optimum at exactly 0.20.
        self.assertAlmostEqual(lambda_from_accuracy(0.06, 0.03), 0.2, places=6)

    def test_equal_accuracy_halves_the_edge(self):
        self.assertAlmostEqual(lambda_from_accuracy(0.05, 0.05), 0.5, places=6)

    def test_worse_than_market_shrinks_hard(self):
        self.assertLess(lambda_from_accuracy(0.20, 0.03), 0.03)

    def test_perfect_forecaster_trusts_itself(self):
        self.assertAlmostEqual(lambda_from_accuracy(0.0, 0.03), 1.0, places=6)

    def test_monotonic_in_own_error(self):
        prev = 1.1
        for s in [0.01, 0.02, 0.05, 0.10, 0.20]:
            cur = lambda_from_accuracy(s, 0.03)
            self.assertLess(cur, prev)
            prev = cur

    def test_rejects_negative_and_degenerate(self):
        with self.assertRaises(ValueError):
            lambda_from_accuracy(-0.1, 0.03)
        with self.assertRaises(ValueError):
            lambda_from_accuracy(0.0, 0.0)


class TestShrink(unittest.TestCase):
    def test_lambda_zero_is_the_market(self):
        self.assertAlmostEqual(shrink_probability(0.9, 0.55, 0.0), 0.55)

    def test_lambda_one_is_untouched(self):
        self.assertAlmostEqual(shrink_probability(0.9, 0.55, 1.0), 0.9)

    def test_pulls_toward_market(self):
        self.assertAlmostEqual(shrink_probability(0.75, 0.55, 0.5), 0.65)

    def test_works_downward_too(self):
        self.assertAlmostEqual(shrink_probability(0.35, 0.55, 0.5), 0.45)

    def test_rejects_lambda_out_of_range(self):
        with self.assertRaises(ValueError):
            shrink_probability(0.9, 0.55, 1.5)


class TestGates(unittest.TestCase):
    """Every one of these must return stake=0."""

    def test_lambda_cap_blocks_full_trust(self):
        # The setting that wiped out 96% of overconfident runs.
        d = decide(0.90, 0.55, 1000, lam=1.0)
        self.assertTrue(d.abstained)
        self.assertEqual(d.stake, 0.0)
        self.assertIn("exceeds cap", d.reasons[0])

    def test_sigma_implying_high_lambda_is_capped(self):
        # Claiming near-perfect accuracy must not buy a big stake.
        d = decide(0.90, 0.55, 1000, sigma_est=0.001)
        self.assertTrue(d.abstained)

    def test_kelly_multiplier_cap(self):
        d = decide(0.90, 0.55, 1000, sigma_est=0.03,
                   kelly_multiplier=MAX_KELLY_MULTIPLIER + 0.01)
        self.assertTrue(d.abstained)

    def test_marginal_edge_dies_after_shrinkage(self):
        # Raw edge +0.05 looks tradeable; at lambda=0.2 only +0.01 survives,
        # which is under min_ev. This is the single most common real case.
        d = decide(0.60, 0.55, 1000, sigma_est=0.06, min_ev=0.02)
        self.assertTrue(d.abstained)
        self.assertGreater(d.edge_raw, 0.02)
        self.assertLess(d.edge_shrunk, 0.02)

    def test_exposure_cap_blocks(self):
        d = decide(0.90, 0.55, 1000, sigma_est=0.03,
                   current_exposure_usd=100.0, exposure_cap_usd=100.0)
        self.assertTrue(d.abstained)

    def test_invalid_probabilities(self):
        for bad in (0.0, 1.0, -0.2, 1.4):
            self.assertTrue(decide(bad, 0.55, 1000).abstained)
            self.assertTrue(decide(0.7, bad, 1000).abstained)

    def test_zero_bankroll(self):
        self.assertTrue(decide(0.90, 0.55, 0).abstained)

    def test_no_edge_at_market_price(self):
        self.assertTrue(decide(0.55, 0.55, 1000, sigma_est=0.03).abstained)

    def test_unmeasured_default_is_pessimistic(self):
        # Default sigma_est=0.10 -> lambda ~0.08. A +0.15 raw edge shrinks to
        # ~0.012, below the 0.02 floor. Unmeasured forecasters mostly abstain.
        d = decide(0.70, 0.55, 1000)
        self.assertTrue(d.abstained)


class TestSizing(unittest.TestCase):
    def test_strong_measured_edge_trades(self):
        d = decide(0.90, 0.55, 1000, sigma_est=0.03, max_trade_usd=100.0)
        self.assertFalse(d.abstained)
        self.assertGreater(d.stake, 0)
        self.assertEqual(d.side, "yes")

    def test_shrunk_stake_is_smaller_than_raw(self):
        shrunk = decide(0.90, 0.55, 1000, sigma_est=0.03, max_trade_usd=1e9)
        raw = decide(0.90, 0.55, 1000, lam=MAX_LAMBDA, max_trade_usd=1e9)
        self.assertLess(shrunk.stake, raw.stake)

    def test_max_trade_cap_binds(self):
        # sigma_est must stay at or above sigma_mkt or the lambda cap fires
        # first and this asserts nothing.
        d = decide(0.95, 0.30, 100000, sigma_est=0.03, max_trade_usd=10.0)
        self.assertFalse(d.abstained)
        self.assertLessEqual(d.stake, 10.0)

    def test_exposure_headroom_clamps_stake(self):
        d = decide(0.95, 0.30, 100000, sigma_est=0.03, max_trade_usd=1000.0,
                   current_exposure_usd=95.0, exposure_cap_usd=100.0)
        self.assertFalse(d.abstained)
        self.assertLessEqual(d.stake, 5.0)

    def test_no_side_is_taken_when_market_too_high(self):
        d = decide(0.10, 0.60, 1000, sigma_est=0.03, max_trade_usd=100.0)
        self.assertFalse(d.abstained)
        self.assertEqual(d.side, "no")
        self.assertAlmostEqual(d.price, 0.40)

    def test_stake_never_exceeds_bankroll(self):
        d = decide(0.99, 0.02, 5.0, sigma_est=0.03, max_trade_usd=1e9,
                   exposure_cap_usd=1e9)
        self.assertFalse(d.abstained)
        self.assertLessEqual(d.stake, 5.0)

    def test_shrinkage_can_flip_a_marginal_side(self):
        # Believing 0.52 against a 0.55 market is a NO on the raw number, but
        # the shrunk estimate stays on the market's side and abstains.
        d = decide(0.52, 0.55, 1000, sigma_est=0.10, min_ev=0.02)
        self.assertTrue(d.abstained)


class TestDecisionShape(unittest.TestCase):
    def test_abstain_default(self):
        self.assertTrue(Decision().abstained)
        self.assertEqual(Decision().stake, 0.0)

    def test_explain_mentions_abstention(self):
        self.assertIn("ABSTAIN", decide(0.55, 0.55, 1000).explain())

    def test_explain_reports_both_edges(self):
        self.assertIn("raw=", decide(0.90, 0.55, 1000, sigma_est=0.03).explain())


if __name__ == "__main__":
    unittest.main(verbosity=2)
