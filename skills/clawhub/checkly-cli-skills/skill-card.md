## Description: <br>
Comprehensive Checkly CLI command reference and Monitoring as Code workflows for authentication, configuration, checks, monitors, testing, deployment, imports, constructs, and advanced Checkly CLI patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and DevOps engineers use this skill to ask an agent for Checkly CLI guidance while creating, testing, importing, deploying, and investigating Monitoring as Code checks and monitors. It is intended for Checkly workflows that may involve account credentials, cloud deployments, live check runs, and account-member operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may help an agent propose Checkly operations that deploy, destroy, import, cancel, run live checks, change members, or use --force with account credentials. <br>
Mitigation: Require explicit user confirmation before those operations, preview or dry-run when available, and review returned changes or target selectors before execution. <br>
Risk: Checkly API keys, account IDs, .env files, verbose logs, and downloaded result assets may contain sensitive account, application, or customer data. <br>
Mitigation: Keep credentials in secret stores, avoid committing .env files, limit verbose/debug output, and review downloaded assets before sharing or storing them. <br>
Risk: CHECKLY_SKIP_AUTH and broad live-run selectors can bypass normal expectations or affect many deployed checks. <br>
Mitigation: Use authentication bypass only for deliberate debugging, and require specific check IDs or tags before live check runs. <br>


## Reference(s): <br>
- [Checkly CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills) <br>
- [Checkly CLI Best Practices](artifact/references/best-practices.md) <br>
- [Checkly CLI Troubleshooting](artifact/references/troubleshooting.md) <br>
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/) <br>
- [Checkly Documentation](https://www.checklyhq.com/docs/) <br>
- [Playwright Documentation](https://playwright.dev/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, TypeScript examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Checkly CLI commands and code snippets; high-impact commands should be reviewed and explicitly approved before execution.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence and artifact/VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
