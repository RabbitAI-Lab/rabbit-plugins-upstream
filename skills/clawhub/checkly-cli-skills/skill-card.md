## Description:

Comprehensive Checkly CLI command reference and Monitoring as Code workflows for authoring, testing, importing, deploying, and operating Checkly synthetic monitoring resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill pack to generate Checkly CLI guidance, commands, and configuration examples for Monitoring as Code workflows, including checks, monitors, authentication, testing, deployment, imports, account usage, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes high-impact production and account operations.

Mitigation: Use least-privilege Checkly keys, confirm the active account before writes, and require explicit review before role, deployment, import, delete, or destroy operations.

Risk: Force-deploy guidance can skip detailed review of destructive changes.

Mitigation: Run deploy previews, review deletions before approval, and avoid force-deploy helper scripts unless CI has a separate approval gate.

Risk: Local config files or CI logs may contain Checkly credentials.

Mitigation: Protect local Checkly config files and CI logs, and avoid printing or committing API keys or account credentials.

Risk: Unpinned Checkly package resolution can change CLI behavior over time.

Mitigation: Pin Checkly package versions where possible and validate commands against the intended Checkly account before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills)
- [Checkly CLI best practices](artifact/references/best-practices.md)
- [Checkly CLI troubleshooting](artifact/references/troubleshooting.md)
- [Checkly documentation](https://www.checklyhq.com/docs/)
- [Checkly runtimes](https://www.checklyhq.com/docs/runtimes/)
- [Playwright documentation](https://playwright.dev/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and TypeScript or JavaScript configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Checkly CLI commands that read or modify a live Checkly account; credentials, account selection, deploy previews, and explicit approval gates should be reviewed before write operations.]

## Skill Version(s):

1.0.18 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
