## Description:

Guides agents through DreamLayer workflows to create, edit, and download image assets, including product imagery, transparent cutouts, campaign variations, and sprite sheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thedesignfounder](https://clawhub.ai/user/thedesignfounder)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and developers use this skill to generate and edit visual assets inside an agent run, then save and review the results locally. It also guides reference-based sprite creation and game-engine import workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DreamLayer API key could be exposed through prompts or checked-in configuration.

Mitigation: Pass the key through the host secret mechanism and never include it in prompts, commits, or skill files.

Risk: Paid image generation or reference uploads may incur charges or send user images to DreamLayer.

Mitigation: Confirm the brief, upload, destination, output count, and credit budget with the user before starting; check capabilities and balance first.

Risk: Installing the MCP package requires trusting DreamLayer and its npm distribution.

Mitigation: Review the publisher and pinned package version before installation.

Risk: Generated product images, logos, or print artwork may be inaccurate or unsuitable for publication.

Mitigation: Inspect downloaded assets for fidelity, text, transparency, and production needs; seek independent clearance where required.

## Reference(s):

- [DreamLayer image workflows on ClawHub](https://clawhub.ai/thedesignfounder/skills/dreamlayer-image-workflows)
- [DreamLayer agent overview](https://dreamlayer.io/agent?utm_source=clawhub&utm_medium=agent_distribution&utm_campaign=agent_launch_202609)
- [DreamLayer agent API reference](https://docs.dreamlayer.io/agent-api)
- [DreamLayer canonical workflow instructions](https://github.com/TheDesignFounder/dreamlayer-agent-plugin/blob/main/docs/workflow-contract.md)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Code, Configuration]

**Output Format:** [Downloaded image files and Markdown guidance, with JSON configuration and importer code where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are downloaded to a new local path; users should inspect the resulting assets before use.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
