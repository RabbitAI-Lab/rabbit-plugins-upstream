## Description:

Comprehensive Checkly CLI command reference and Monitoring as Code workflows for creating, testing, importing, deploying, and operating synthetic monitoring resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and platform engineers use this skill to guide Checkly CLI workflows for Monitoring as Code, including authentication, configuration, checks, monitors, testing, deployment, imports, usage reporting, and account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to use Checkly credentials for production monitoring or account access.

Mitigation: Use least-privilege service keys, verify the target Checkly account, and require operator review before account or production monitoring changes.

Risk: Some workflows use unpinned npm or npx execution.

Mitigation: Prefer pinned, project-local Checkly CLI versions and review package provenance before running generated install or execution commands.

Risk: The included deployment helper can run a forced deploy that may change production monitoring without showing the full change set.

Mitigation: Avoid the forced-deploy helper unless the exact changes have already been reviewed and approved; prefer reviewed deployment previews.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills)
- [Checkly CLI Best Practices](artifact/references/best-practices.md)
- [Checkly CLI Troubleshooting](artifact/references/troubleshooting.md)
- [Checkly Documentation](https://www.checklyhq.com/docs/)
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/)
- [Playwright Documentation](https://playwright.dev/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Checkly CLI commands, TypeScript configuration examples, monitoring definitions, and operational guidance.]

## Skill Version(s):

1.0.18 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
