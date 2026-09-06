## Description:

ClawVision Lite exports an OpenClaw session into a lightweight, English-only, self-contained HTML summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to turn a selected chat session into a simple local HTML summary for review or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads selected session history, which may include sensitive conversation content.

Mitigation: Confirm intent and avoid running it on sessions that may contain secrets or private data unless the user confirms it is safe.

Risk: The generated HTML summary may contain conversation details that are not suitable for wider sharing.

Mitigation: Review the generated HTML before sharing it outside the local workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision-lite)
- [Publisher profile](https://clawhub.ai/user/monaxamo)
- [Project homepage from metadata](https://github.com/monaxamo/clawvision)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance, files]

**Output Format:** [JSON summary input and a self-contained HTML file, with the agent response providing the generated file path in text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [English-only HTML with inline CSS and JavaScript; no external assets, CDN, analytics, PowerPoint, or Markdown export.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
