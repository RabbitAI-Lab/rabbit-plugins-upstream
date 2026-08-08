## Description: <br>
Comprehensive Checkly CLI command reference and Monitoring as Code workflows for authentication, configuration, checks, monitors, testing, deployment, imports, constructs, and advanced Checkly patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to create, test, deploy, import, and troubleshoot Checkly Monitoring as Code resources through the Checkly CLI and related TypeScript configuration patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Checkly API keys, account IDs, logs, or downloaded assets may expose sensitive account or application data. <br>
Mitigation: Keep credentials in environment variables or CI secrets, sanitize verbose logs and assets before sharing, and avoid embedding secrets in generated check code. <br>
Risk: Deploy, destroy, member-management, delete, import commit, and forceful commands can change live Checkly account resources. <br>
Mitigation: Review proposed changes before approval, prefer preview or dry-run flows when available, and run returned confirmation commands only after explicit user approval. <br>
Risk: Bypassing authentication checks can hide configuration problems or run commands against an unintended context. <br>
Mitigation: Do not use CHECKLY_SKIP_AUTH outside tightly controlled local debugging, and verify the active account before deployment or account-management actions. <br>


## Reference(s): <br>
- [Checkly CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills) <br>
- [Checkly CLI Best Practices](artifact/references/best-practices.md) <br>
- [Common Issues and Solutions](artifact/references/troubleshooting.md) <br>
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, TypeScript examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Checkly CLI commands, Checkly configuration files, monitoring definitions, troubleshooting steps, and review-before-execution guidance for account-changing actions.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence and artifact/VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
