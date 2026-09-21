## Description:

YuanCe is an authorization-first web security testing methodology skill that guides agents through reconnaissance, discovery, verification, and reporting for authorized targets while enforcing scope checks and avoiding executable payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External developers, security engineers, and authorized testing teams use this skill to structure web vulnerability assessment, bug bounty/SRC, CTF/lab, and penetration-test reporting workflows for targets they are authorized to test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables security-testing workflows that could be misused if applied to targets without documented authorization.

Mitigation: Install and use it only for assets the user owns, lab or CTF systems, bug bounty/SRC scopes, or other targets with documented authorization.

Risk: Installing the package broadly can enable the workflow in more agents than intended.

Mitigation: Prefer explicit --agent or --dir installation, avoid global or no-argument auto-detection unless multi-agent installation is intended, and pin or verify the package version before running npx.

Risk: Local scope and audit records may be created during use.

Mitigation: Account for ~/.yottasec scope and audit files in local data-retention and review practices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-security-testing)
- [Project homepage](https://github.com/YottaMeta/yotta-security-testing)
- [Methodology playbook](playbooks/00-methodology.md)
- [Tutorial](references/tutorial.md)
- [Report template](references/report-template.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with inline shell commands; generated reports can be Markdown or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses explicit authorization scope and audit records; generated reports redact sensitive credentials.]

## Skill Version(s):

0.3.1 (source: SKILL.md frontmatter, package.json, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
