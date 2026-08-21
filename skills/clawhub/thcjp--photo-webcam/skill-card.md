## Description:

照片 helps an agent list network webcams and retrieve webcam snapshots, with emphasis on foto-webcam.eu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users can use this skill to collect webcam listings and snapshots for monitoring or data-gathering workflows. Use should be limited to webcams and images the operator is authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill as suspicious because it asks for broad command and file access while its operating scope is incomplete.

Mitigation: Review before installing, run only where command execution and file writes are acceptable, and prefer a revision with a narrower trigger and explicit allowed commands or safer APIs.

Risk: Webcam snapshots can expose sensitive or private visual information.

Mitigation: Use the skill only with authorized webcam sources, avoid collecting private images, and apply retention and access controls to any saved snapshots.

Risk: The artifact makes sandbox or allowlist-style safety claims that are not supported by the server security evidence.

Mitigation: Validate the actual execution controls in the target agent environment before deployment and remove unsupported safety claims from release-facing documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/photo-webcam)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON result examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve network access, command execution, and file writes depending on the agent environment.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
