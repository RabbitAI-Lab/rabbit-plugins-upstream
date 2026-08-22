## Description:

AI通识课资深专家 helps educators design AI literacy lessons, analyze course materials locally with OpenVINO, compose Markdown assessments and interactive p5.js courseware, and apply edge-cloud privacy, cost, and interaction quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linix-2026](https://clawhub.ai/user/linix-2026)

### License/Terms of Use:

MIT-0

## Use Case:

Educators and course developers use this skill to prepare AI literacy courses, generate lesson materials, assessments, and p5.js interactive courseware, and compare local OpenVINO work with configured cloud model assistance. It is intended for AI PC and edge-cloud teaching workflows where privacy, cost monitoring, and interaction testing matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provisions a Python environment and downloads AI resources.

Mitigation: Review the environment setup scripts and dependencies before installation, and run the skill in an isolated workspace.

Risk: The skill stores local logs and cache that may reflect teaching materials or workflow metadata.

Mitigation: Configure retention and access controls for local logs and cache, and clear them before handling different privacy contexts.

Risk: Configured cloud model exchange can send redacted abstract metadata outside the local machine.

Mitigation: Confirm provider configuration, redaction behavior, and privacy requirements before enabling cloud exchange.

Risk: Generated HTML and deployment guidance may be used in privacy-sensitive or public-network settings.

Mitigation: Review generated HTML, referenced assets, and deployment settings before publishing or sharing externally.

## Reference(s):

- [Skill release page](https://clawhub.ai/linix-2026/skills/ai-literacy-expert-v8-1-0-aipc)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [VERSION.txt](artifact/VERSION.txt)
- [edge-cloud-architecture.md](artifact/references/edge-cloud-architecture.md)
- [zero-upload-privacy.md](artifact/references/zero-upload-privacy.md)
- [edge-cloud-protocol.md](artifact/references/edge-cloud-protocol.md)
- [edge-cloud-protocol-schema.json](artifact/references/edge-cloud-protocol-schema.json)
- [p5js-courseware-guide.md](artifact/references/p5js-courseware-guide.md)
- [p5js-game-design-guide.md](artifact/references/p5js-game-design-guide.md)
- [local-ai-quality-gate.md](artifact/references/local-ai-quality-gate.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include lesson plans, assessment.json, p5.js courseware, local/cloud comparison summaries, cost and privacy checks, and interaction gate results.]

## Skill Version(s):

8.1.0 (source: server release metadata; artifact metadata uses 8.1.0-aipc)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
