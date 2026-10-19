## Description:

Verifies a game build on its tested runtime with evidence for launch, rendering, input, core gameplay, a designed outcome, and restart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Game developers use this skill to check whether a candidate build completes its core playable path and to document failures or untested behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The project's verification command may execute project code and write QA evidence in the workspace.

Mitigation: Review the command and project before running it, and inspect workspace changes afterward.

Risk: A successful run on the tested runtime can be mistaken for proof of untested target-device behavior.

Mitigation: Record runtime differences as limitations and avoid claiming coverage of untested devices.

## Reference(s):

- [Game QA skill release](https://clawhub.ai/worldwonderer/skills/game-qa)
- [QA contract](references/qa-contract.md)
- [Test design method](references/test-design-method.md)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Workspace QA verification JSON and run evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records six required checks, the verification command, limitations, and evidence from one complete run.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
