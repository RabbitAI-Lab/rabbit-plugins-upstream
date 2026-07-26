# Reference: Closed-Loop Workflow & Analysis-before-Synthesis

Book anchors: §1.5 (analysis vs synthesis), §3.7 (feedback), §4 (control-system analysis).

## Why closed loop

An open-loop program — "write it once, hope it works" — has no path to recover from error. A
closed-loop program *acts → observes → corrects*, and therefore converges (§3.7: feedback
raises both accuracy and speed of response).

Operational rules:
- After every non-trivial change, **observe the actual state** before declaring success:
  run it, read output, check tests. Do not assume `u` produced the intended `x`.
- Prefer mechanisms that **measure** outcomes over mechanisms that **assert** they happened.
- If you cannot observe a quantity, you cannot control it (§1.5): a controlled quantity is
  steered only through a control quantity you are free to change.

## Analysis before synthesis (§1.5, §4)

> Analysis is understanding the motion of a given system; synthesis is changing that motion to
> meet a need. Analysis is the foundation; synthesis is the goal — and the higher stage.

- **Never skip analysis.** Before fixing or refactoring, characterize current behavior:
  reproduce, measure, locate the fault. You cannot steer what you have not measured.
- Then synthesize the *minimal* control action that moves state to the target.
- A change whose effect you cannot predict from analysis is an open-loop guess. Make the
  prediction explicit, then verify it.

## The loop, made concrete

| Step | Control term | What you actually do |
|------|--------------|----------------------|
| Identify | define `x`, `u`, sensors, bounds | Write down what must be correct and what lever you'll pull |
| Analyze | measure current trajectory | Reproduce the bug / profile the baseline |
| Stabilize | drive poles to stable region | Stop the divergence/leak/oscillation |
| Synthesize | choose control law `u = f(ε)` | Make the smallest change that moves `x` to target |
| Observe | read sensors | Run tests, read logs, check metrics |
| Correct | update `u` from error `ε = x* − x` | Iterate until `‖ε‖` is bounded and small |
| Compensate | feedforward + clamp | Pre-handle measurable disturbances; bound the actuator |
| Optimize | secondary criteria | Only now tune speed/cost/elegance |

## How to know the loop converged

- Deviation `ε` is **bounded** for the largest perturbation you can throw at it (stability, §4.1).
- Corrections get **smaller**, not larger, over iterations (no limit cycle, no retry storm).
- The setpoint is reached within the stated bounds (memory, time, rate limit).

## Worked example: analysis before synthesis — cache stampede

**Symptom:** under sudden traffic spike, database CPU spikes to 100%, API returns 503.

**Open-loop (skip analysis):**
```python
@app.get("/data/{id}")
def get_data(id):
    data = cache.get(id) or db.query(f"SELECT * FROM t WHERE id={id}")
    return data
```
Naive fix (synthesis without analysis): "just add a cache"

**Closed-loop (analysis first):**
```
Analyze:
  x = db CPU utilization; target < 70%
  u = cache TTL + eviction policy
  Model: thundering-herd on cache miss → spike proportional to missing-key rate
  Validity: model holds for any cache with TTL; breaks for in-process unbounded cache
```

**Stabilize first:**
```python
@app.get("/data/{id}")
def get_data(id):
    data = cache.get(id)
    if data is None:
        with lock:                    # serialize misses per key
            data = cache.get(id) or db.query(...)
            cache.set(id, data, ttl=60)
    return data
```
- Lock prevents thundering herd (damps the oscillation).
- TTL bounds memory.

**Then optimize:**
- Only after CPU is bounded <70%, consider increasing TTL or adding tiered caching.

Key point: adding a cache *without* the lock in the first patch would have shifted but not
eliminated the oscillation. Analysis → stabilize → then synthesize = closed loop.

