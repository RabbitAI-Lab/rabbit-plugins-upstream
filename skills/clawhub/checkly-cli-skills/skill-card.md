## Description:

Comprehensive Checkly CLI command reference and Monitoring as Code workflows for authoring, testing, importing, deploying, and inspecting Checkly checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to work with Checkly CLI and Monitoring as Code projects, including authentication, configuration, check creation, local testing, deployment, imports, member administration, and failure investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help operate a real Checkly account, including deploy, import, member, run, and delete workflows.

Mitigation: Use least-privilege Checkly credentials and review CLI previews or confirmation prompts before approving commands that change account state.

Risk: Verbose logs and downloaded result assets can contain production secrets, traces, screenshots, videos, packet captures, or other sensitive data.

Mitigation: Avoid unnecessary verbose logging in production contexts and sanitize downloaded assets before sharing, committing, or attaching them to reports.

Risk: CLI and MCP sessions can refer to different Checkly accounts if account identity is not checked.

Mitigation: Run account identity checks and confirm the same account ID before combining CLI and MCP evidence or using either path for live-account work.

## Reference(s):

- [Checkly CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills)
- [Checkly CLI Best Practices](artifact/references/best-practices.md)
- [Common Issues and Solutions](artifact/references/troubleshooting.md)
- [Checkly Documentation](https://www.checklyhq.com/docs/)
- [Playwright Documentation](https://playwright.dev/)
- [Checkly CLI GitHub Issues](https://github.com/checkly/checkly-cli/issues)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Checkly CLI commands, configuration snippets, and review steps for live account operations.]

## Skill Version(s):

1.0.15 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
