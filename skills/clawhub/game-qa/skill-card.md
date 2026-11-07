## Description:

Verifies a game build on its target runtime and records evidence for launch, rendering, input, core gameplay, a designed outcome, and restart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Game developers use this skill to verify that a build completes a minimal playable loop on its selected runtime. It records the run, evidence, results, and limitations in a structured QA record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run the game's verification command and make targeted project fixes.

Mitigation: Review the command before execution and inspect resulting changes and saved evidence.

## Reference(s):

- [QA contract](artifact/references/qa-contract.md)
- [Test design method](artifact/references/test-design-method.md)
- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/game-qa)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, QA guidance]

**Output Format:** [A structured QA verification record with evidence references, results, and limitations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence is tied to one complete run; unverified checks and runtime limitations remain explicit.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
