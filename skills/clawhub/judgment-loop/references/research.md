# Research mode

Use for papers, reports, data claims, causal claims, and judgments that depend on current facts. Verify primary material first. If critical material is unavailable, mark it unverified instead of filling gaps from model memory.

## X-ray review

1. **Problem**: What problem is actually solved, for whom, and against what baseline?
2. **Mechanism**: Through what testable mechanism should the method produce the result? Do not merely restate component names.
3. **Increment**: What is genuinely new relative to existing approaches? Separate new packaging, engineering gain, and knowledge gain.
4. **Evidence**: Evaluate sample, controls, metrics, statistical uncertainty, replication, and source quality separately.
5. **Argument**: Which assumptions carry the conclusion? Where does evidence stop and extrapolation begin?
6. **Boundary**: Population, environment, time, cost, failure cases, and uncovered conditions.
7. **Strongest failure reason**: Look first for leakage, selection bias, proxy metrics, unfair baselines, confounding, failed replication, or temporal drift.
8. **Cheapest falsification**: Design a small test that separates the leading explanations. State expected, contrary, and stopping outcomes.

## Black boxes and updates

Input-output experiments can support local prediction when internals are hidden. Keep separate:

- behavioral regularity and internal causality;
- one hit and a stable relationship;
- in-sample explanation and out-of-sample prediction;
- descriptive result and deployable value.

Record the current judgment, confidence, supporting evidence, opposing evidence, and what would change the conclusion. When new evidence arrives, state which assumptions changed rather than merely saying confidence increased.

## Output

Lead with the research conclusion and evidence strength, then the strongest counterevidence and next test. Place citations next to the claims they support. If the user requested review or explanation only, do not run experiments or modify systems without authorization.
