## Description:

Records browser sessions via Playwright and converts video to GIF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create browser-based UI demo recordings, documentation clips, and tutorial GIFs from Playwright specs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser recordings can capture credentials, private production content, or other sensitive on-screen data.

Mitigation: Use test accounts and sanitized demo data, and avoid recording credentials or private production content.

Risk: Generated videos and GIFs may preserve sensitive visual details after capture.

Mitigation: Review videos and GIFs before sharing, and delete sensitive artifacts when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-scry-browser-recording)
- [Publisher Profile](https://clawhub.ai/user/athola)
- [Clawdis Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scry)
- [Spec Execution Module](artifact/modules/spec-execution.md)
- [Video Capture Module](artifact/modules/video-capture.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline TypeScript configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce Playwright WebM recordings and optional GIF outputs.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter version is 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
