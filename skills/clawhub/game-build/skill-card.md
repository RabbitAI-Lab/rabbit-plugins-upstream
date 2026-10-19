## Description:

Turns approved game designs into a playable whitebox or production candidate, with a concise build brief and reproducible checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Game developers and designers use this skill to turn an approved game design into a runnable prototype or production candidate, then check the intended gameplay against reproducible evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Building and testing a game may execute project code or unreviewed downloaded assets.

Mitigation: Review the approved project brief and external assets before execution; keep local services private.

Risk: Optional media generation can expose sensitive content or service credentials.

Mitigation: Use only approved services and necessary inputs; keep credentials out of client code, repositories, logs, and evidence.

## Reference(s):

- [ClawHub game-build release](https://clawhub.ai/worldwonderer/skills/game-build)
- [Build brief contract](references/build-brief-contract.md)
- [Playable model contract](references/playable-model-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration]

**Output Format:** [A Markdown build brief and runnable game files, with build and verification commands when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The production path includes a verification entry point; unavailable tools may limit delivery to the build brief.]

## Skill Version(s):

1.2.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
