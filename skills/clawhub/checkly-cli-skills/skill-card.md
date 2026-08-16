## Description:

Comprehensive Checkly CLI command reference and Monitoring as Code workflows for Checkly CLI, synthetic monitoring, API checks, browser checks, Playwright testing, monitor deployment, imports, constructs, and advanced patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site reliability engineers use this skill to author, test, import, inspect, and deploy Checkly Monitoring as Code resources with the Checkly CLI. It helps agents choose safe CLI workflows for authentication, configuration, checks, monitors, Playwright suites, deployment, account members, imports, and result-asset investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checkly CLI write actions can deploy, destroy, import, cancel, update members, delete members, or trigger live checks against a real account.

Mitigation: Review proposed changes and require explicit approval before deploy, destroy, import commit/cancel, member update/delete, or live check run commands.

Risk: Checkly API keys and account IDs are required for authenticated workflows and can expose account access if mishandled.

Mitigation: Use least-privilege Checkly API keys, keep credentials in environment variables or the CLI config, and avoid committing secrets.

Risk: Verbose logs in shared terminals or CI can expose sensitive request, response, or environment details.

Mitigation: Use verbose output only for targeted debugging and ensure shared terminals and CI logs mask secrets.

Risk: The `CHECKLY_SKIP_AUTH` debug variable can bypass normal authentication checks in inappropriate workflows.

Mitigation: Do not set `CHECKLY_SKIP_AUTH` in normal local or CI workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills)
- [Checkly CLI Best Practices](references/best-practices.md)
- [Checkly CLI Troubleshooting](references/troubleshooting.md)
- [Checkly Documentation](https://www.checklyhq.com/docs/)
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/)
- [Playwright Documentation](https://playwright.dev/)
- [Checkly App](https://app.checklyhq.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Checkly CLI commands and Monitoring as Code files that require user review before live account changes.]

## Skill Version(s):

1.0.13 (source: server release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
