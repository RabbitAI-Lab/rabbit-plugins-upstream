# Debugging Checklist (closed-loop thinking mode)

This checklist is a **prompt scaffold for the LLM's internal loop** during debugging.
Work top to bottom; do not skip steps. If you find yourself on step 4 without a clear x
and u, return to step 1.

## 1. Identify (state & control)
- [ ] **Controlled variable x**: what must stay correct? Name it concretely, with a target/units.
- [ ] **Control variable u**: what lever will I actually change? (Not "rewrite"; the smallest editable thing.)
- [ ] **Observability**: do I have a sensor (log/test/metric) that reveals x? If not → add it first.
- [ ] **Bounds**: what are the limits on u and x? Size, rate, time, memory, retries, context.

## 2. Analyze (current behavior)
- [ ] Reproduced the fault deterministically? (Not "sometimes".)
- [ ] Measured the deviation ε = x* − x? Stated the mental model of the plant and where it breaks.
- [ ] Located the fault to a subsystem (not guessed).

## 3. Stabilize (before any feature)
- [ ] Tested with perturbations: empty / huge / null / concurrent / dependency-down / load spike.
- [ ] No unbounded growth, oscillation, or limit cycle?
- [ ] If unstable → fixed stability before adding anything.

## 4. Synthesize (minimal control action)
- [ ] Change is the smallest u that moves x to target. No speculative extras.
- [ ] Decoupled harmful coupling; kept beneficial coupling (coordination, not over-decoupling).

## 5. Close the loop (observe & correct)
- [ ] Ran the actual code; read the actual sensor output — did NOT assume u worked.
- [ ] Corrections are getting smaller, not larger.
- [ ] Reached target within stated bounds.

## 6. Compensate & clamp
- [ ] Measurable disturbances handled by feedforward where possible; feedback the rest.
- [ ] Control magnitude clamped (max retries/depth/rate). Graceful degradation at the bound.

## 7. Optimize (last)
- [ ] Only now tuning speed/cost/elegance. Stability and correctness already proven.

---
Anti-patterns (stop if you catch yourself):
- Adding retries without a bound → retry storm (unstable delay loop)
- Cranking gain on a delayed system → oscillation
- Optimizing before stabilizing → divergence on perturbation
- Guessing cause without reproduction → open-loop patch
