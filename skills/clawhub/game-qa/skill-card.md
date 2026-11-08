## Description:

Verify a game's actual runtime rendering, input, core loop, at least one designed outcome, and restart with evidence, while recording limitations and avoiding unsupported claims about subjective quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers and QA practitioners use this skill to verify that a game build runs on its selected target runtime and completes a basic playable loop. It records the run evidence, designed outcome, restart behavior, and untested limitations without treating runtime checks as a verdict on fun, balance, or release readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because some local references could not be resolved, leaving part of the available context unreviewed.

Mitigation: Confirm the project runtime briefs and any other required linked materials are available before relying on a verification run.

## Reference(s):

- [QA contract](references/qa-contract.md)
- [Test design method](references/test-design-method.md)
- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/game-qa)

## Skill Output:

**Output Type(s):** [JSON, Test evidence, QA findings and limitations]

**Output Format:** [Structured JSON verification record with linked observations and concise findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The six required checks are supported by the same continuous clean-start-to-restart run; uncovered test gaps are recorded as limitations.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
