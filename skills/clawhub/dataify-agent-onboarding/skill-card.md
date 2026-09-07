## Description:

Set up and verify a first Dataify workflow, then route the user to MCP, local skills, or REST without losing their original task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to configure Dataify access, validate account readiness, choose MCP, local skill, or REST integration, and continue the original Dataify task after setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Dataify API token and can send search terms, URLs, and task data to Dataify services.

Mitigation: Use it only for data you are permitted to send to Dataify, avoid sensitive or internal targets, and keep the token in environment variables rather than chat.

Risk: The bundled workflows can perform broader scraping and reporting actions beyond first-time onboarding.

Mitigation: Review the workflow scripts and requested scope before executing high-volume, multi-page, media-download, or cost-impacting tasks.

Risk: Task-status URLs or logs could expose enough context to justify token rotation if mishandled.

Mitigation: Avoid sharing logs that contain task-status URLs, keep diagnostics local, and rotate the Dataify token if exposure is suspected.

## Reference(s):

- [Dataify Documentation](https://doc.dataify.com)
- [Dataify Support](https://www.dataify.com/)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-agent-onboarding)
- [Access Paths](references/access-paths.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON status or report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON and Markdown report files when broader Dataify workflows are executed.]

## Skill Version(s):

1.1.1 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
