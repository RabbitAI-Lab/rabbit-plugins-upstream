## Description:

Checks reasoning outputs by extracting claims, looking for contradictions, evaluating coverage, and optionally grounding statements against provided facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to review an answer or reasoning trace for internal contradictions, missing coverage, and unsupported claims before relying on it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may overstate the dependability of its reasoning-verification results.

Mitigation: Treat outputs as heuristic review signals and require human review before using them for correctness decisions.

Risk: The artifact includes self-evolution metadata that could expand its role if enabled globally.

Mitigation: Avoid enabling self-evolving or global capability registration behavior without a separate review gate.

Risk: The documented placeholder runner provides only a lightweight smoke path rather than the fuller verifier behavior.

Mitigation: Use scripts/verify.py for evaluation and testing rather than relying on the placeholder run script alone.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [JSON report and concise command-line text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write a structured report file when invoked through scripts/verify.py.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
