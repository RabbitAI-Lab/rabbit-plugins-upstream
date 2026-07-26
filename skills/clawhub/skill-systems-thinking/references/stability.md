# Reference: Stability

Book anchors: §1.1 (constant-coefficient linear systems), §4.1 (Lyapunov stability definition
and direct method), §1.3 (nonlinear systems have multiple equilibria).

## Stability is the first requirement

(§1.1) For a control system, stability is demanded *before* anything else. A program that
gives the right answer *sometimes* but diverges, hangs, leaks, or corrupts state under
perturbation is **unstable** — and therefore useless, however clever.

### Lyapunov definition (§4.1), in plain terms

A motion is *stable* if: for any tolerated deviation ε > 0, there exists a δ > 0 such that,
whenever the initial state starts within δ of the target, the trajectory stays within ε of the
target for all t ≥ t₀. *Asymptotically stable* if it also converges back to the target.

- Translate: **small perturbations must produce bounded deviation, not runaway.**
- "For all t" matters. A system that looks fine for 5 minutes then explodes is not stable.

## LLM behavior pattern: Stability before everything

> "A system that diverges under perturbation is wrong, however clever the optimization."

The LLM using this skill **must** verify stability before proposing any feature or
optimization. This is not a suggestion; it is the second cognitive law.

- Before generating performance optimizations, the LLM must reason: "Is the base system
  stable under perturbation? If not, I reject the optimization and fix stability first."
- Perturbations to consider: empty input, huge input, null, concurrent calls, network flake,
  dependency down, clock skew.

### Test for stability, not just correctness

- Probe with **perturbations**, not only golden paths: empty input, huge input, null,
  concurrent calls, network flake, one dependency down, clock skew.
- If deviation **grows without bound** under a small kick → unstable. Fix before features.
- Watch the **signatures of instability**:
  - unbounded growth → memory/CPU/disk creep, state explosion;
  - oscillation → retry storms, ping-pong state between two components;
  - limit cycle → two routines mutually undoing each other every tick.

## Local vs global stability (§1.3, §4.1)

- Linear systems are all-or-nothing: either every motion is stable or none is. So "is the
  system stable?" is a meaningful question *only* for linear systems.
- Nonlinear systems (and almost everything real, §1.4) can be stable in one region and
  unstable in another — each equilibrium has its own stability. "Works on my machine / small
  data" is **local stability only**. Probe the edges of the operating envelope.

## LLM behavior pattern: Reject unstable trajectories

> "If you observe a deviation that grows over iterations, you have lost stability. Stop. Do not paper over it with a 'slightly better' patch. Return to step 1 (Identify) and re-analyze the plant."

An LLM must not declare success when a trajectory is unstable. Growing deviation is a
hard-stop signal, not a minor concern.

## Worked example: retry storm → damped

**Before (unstable):**
```python
def fetch(url):
    for attempt in range(999):          # unbounded loop
        try:
            return requests.get(url, timeout=3)
        except requests.Timeout:
            continue                    # high gain, zero damping
```
No backoff, no circuit breaker, no jitter. Under load this oscillates: concurrent
retries amplify the load spike → each times out → more retries. Trajectory diverges.

**After (stable):**
```python
def fetch(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            return requests.get(url, timeout=3)
        except requests.Timeout:
            delay = (2 ** attempt) + random.uniform(0, 0.1)  # exponential + jitter
            time.sleep(delay)           # damping
    raise CircuitBreakerOpen()          # open loop before saturation
```

- Bound on actuator (`max_retries`).
- Backoff = damping; jitter = break synchronization.
- Circuit breaker = open loop when service is unhealthy.

---

## Stabilizing a system

- Linear feedback (§5): `u = −Kx` pulls state back toward target. But simple feedback is not
  always enough (§5, §9.6): near actuator saturation or with bad phase margin, you need
  damping / lead correction, not just gain.
- Adding gain to "fix" a lagging or oscillating system often *destabilizes* it (§11): reduce
  loop gain or add damping instead.
- Keep stability margins explicit: how much worse can the input/get worse before it diverges?
