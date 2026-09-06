## Description:

Comprehensive Checkly CLI command reference and Monitoring as Code workflows for authoring, testing, importing, and deploying Checkly synthetic monitoring resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site reliability engineers use this skill to configure Checkly projects, create API, browser, and infrastructure checks, test locally, import existing resources, and deploy Monitoring as Code through reviewable CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact deployment, destruction, member-management, check-delete, import, and live-run workflows can change or remove Checkly resources or account access.

Mitigation: Require preview or dry-run output and explicit confirmation of the exact target resources before executing these workflows.

Risk: Included helper scripts and follow-up guidance can use force deployment without first showing a detailed deploy diff.

Mitigation: Review and adjust scripts to show a deploy preview or diff before applying changes; avoid force flags except after explicit approval.

Risk: Checkly API keys, account IDs, verbose logs, and downloaded result assets may expose sensitive operational data.

Mitigation: Store credentials in protected secrets, avoid printing or committing them, and treat logs, traces, videos, screenshots, pcap captures, and downloaded assets as sensitive.

Risk: Floating package versions can shift CLI behavior in automated environments.

Mitigation: Prefer pinned or locked Checkly CLI and dependency versions in CI and agent-run workflows.

## Reference(s):

- [Checkly CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills)
- [Checkly CLI Best Practices](artifact/references/best-practices.md)
- [Common Issues and Solutions](artifact/references/troubleshooting.md)
- [Checkly Documentation](https://www.checklyhq.com/docs/)
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and TypeScript or JavaScript configuration and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local files, Checkly account resources, CLI output, and downloaded result assets depending on the workflow.]

## Skill Version(s):

1.0.17 (source: server release evidence and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
