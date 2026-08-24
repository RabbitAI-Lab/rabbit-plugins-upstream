## Description:

Comprehensive Checkly CLI command reference and Monitoring as Code workflows for authentication, configuration, checks, monitors, testing, deployment, imports, constructs, Playwright, assets, members, and advanced patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to create, test, import, inspect, and deploy Checkly Monitoring as Code resources through the Checkly CLI. It helps agents choose safe CLI workflows, generate Checkly configuration and check definitions, and review account-changing actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions that change Checkly account resources, including deploys, deletes, imports, and member changes.

Mitigation: Confirm the active account with whoami, review previews and dry-runs, and require explicit approval before running account-changing commands.

Risk: Checkly API keys, account IDs, verbose logs, and downloaded result assets can expose sensitive operational data.

Mitigation: Use scoped credentials, keep credentials in environment variables or approved local config, and avoid sharing verbose logs or result assets in public channels.

Risk: Using --force or bypassing CLI confirmation can skip review of destructive or broad changes.

Mitigation: Avoid --force unless the change has already been approved and run returned confirmCommand values verbatim only after explicit approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills)
- [Checkly CLI Best Practices](references/best-practices.md)
- [Common Issues and Solutions](references/troubleshooting.md)
- [Checkly Documentation](https://www.checklyhq.com/docs/)
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/)
- [Playwright Documentation](https://playwright.dev/)
- [Checkly CI Examples](https://github.com/checkly/checkly-ci-examples)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, TypeScript examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Checkly CLI commands and generated Monitoring as Code files; account-changing commands should be reviewed before execution.]

## Skill Version(s):

1.0.14 (source: release evidence and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
