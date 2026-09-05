## Description:

Comprehensive Checkly CLI command reference and Monitoring as Code workflows for Checkly authentication, configuration, checks, monitors, testing, deployment, imports, constructs, and advanced patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to author, test, import, deploy, and troubleshoot Checkly Monitoring as Code projects through the Checkly CLI. It helps agents produce project configuration, TypeScript check definitions, Playwright check guidance, and reviewed CLI workflows for live Checkly accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help perform live Checkly account actions such as deploying monitoring resources, deleting checks, or changing members.

Mitigation: Review the target account with whoami and use dry-run, preview, or explicit confirmation flows before deploy, delete, import commit, cancel, destroy, or member changes.

Risk: Checkly API keys, account IDs, and user-defined test secrets may be used during CLI workflows.

Mitigation: Keep CHECKLY_API_KEY and other tokens in environment variables or CI secrets, and avoid printing or storing secret values in generated code, logs, or shared artifacts.

Risk: Downloaded failure assets such as logs, traces, screenshots, videos, pcap files, and reports may contain application data.

Mitigation: Download only the assets needed for investigation, store them in an approved location, and review contents before sharing or attaching them to reports.

## Reference(s):

- [Checkly CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills)
- [Checkly Documentation](https://www.checklyhq.com/docs/)
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/)
- [Playwright Documentation](https://playwright.dev/)
- [Best Practices](references/best-practices.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash and TypeScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Checkly CLI commands, TypeScript monitoring constructs, Playwright examples, configuration snippets, and review steps before live account changes.]

## Skill Version(s):

1.0.16 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
