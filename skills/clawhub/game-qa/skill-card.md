## Description:

Verify a game with evidence on its selected target runtime. Launch the actual build and prove real rendering, input, the core loop, at least one designed outcome, restart, and explicit limitations without dressing subjective fun up as a certain verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers and QA engineers use this skill to verify a candidate build's playable loop on its selected runtime, preserve concrete run evidence, and report limitations without treating gameplay checks as proof of subjective quality or release readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification executes the candidate game and may include targeted fixes.

Mitigation: Use a game project you trust, review the verification command before running it, and inspect any proposed changes.

Risk: A passing gameplay verification could be mistaken for a security or release-readiness certification.

Mitigation: Treat PASS as evidence for the documented gameplay checks only; assess security and release readiness separately.

## Reference(s):

- [QA Contract](references/qa-contract.md)
- [Test Design Method](references/test-design-method.md)
- [ClawHub release](https://clawhub.ai/worldwonderer/skills/game-qa)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [JSON verification report with references to run evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports launch, rendering, input, core-loop, outcome, and restart checks, with limitations and evidence references.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
