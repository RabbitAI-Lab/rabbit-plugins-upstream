## Description:

Orchestrates the adaptation of a novel into a playable game through source analysis, game design, target-platform building, and evidence-based QA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Authors and game developers use this skill to turn novels into playable games, coordinating adaptation decisions, design, building, and verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The complete workflow relies on separately installed companion skills whose behavior is not covered by this release's security assessment.

Mitigation: Review the six companion skills and their permissions separately before running the full pipeline.

Risk: Adapting a novel or incorporating reference assets without permission can create rights issues.

Mitigation: Confirm adaptation and asset rights during intake before committing to production or release.

Risk: An untested prototype could be presented as a verified, release-ready game.

Mitigation: Check launch, rendering, input, core loop, outcome, and restart against actual runtime evidence; leave untested checks unverified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/novel-to-game)
- [Intake method](references/intake-method.md)
- [Pipeline contract](references/pipeline-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Code]

**Output Format:** [Project documents, game build files, and JSON verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source-backed adaptation decisions and runtime QA evidence.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
