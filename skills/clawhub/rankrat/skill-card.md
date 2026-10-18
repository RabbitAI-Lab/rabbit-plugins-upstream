## Description:

Rankrat helps agents inspect SEO, search traffic, indexing, site performance, and managed website settings through a self-hosted server for sites their operators control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners, SEO practitioners, and developers use this skill to analyze their own search and analytics data, audit website health, and, when authorized, manage tags, redirects, indexing submissions, and monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider credentials grant broad access, and account-changing tools are enabled by default.

Mitigation: Grant only needed provider permissions and use RANKRAT_READ_ONLY=true for agents that should not make changes.

Risk: An exposed HTTP endpoint could allow unauthorized access to connected accounts.

Mitigation: Bind HTTP to loopback or a private network and require a bearer token when others can reach it.

Risk: Installer and container image references may change between reviews.

Mitigation: Review the installer and pin and verify the exact release or image digest before use.

## Reference(s):

- [ClawHub rankrat release](https://clawhub.ai/psyb0t/skills/rankrat)
- [Setup and credentials](references/setup.md)
- [Rankrat documentation](https://github.com/psyb0t/rankrat/tree/main/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with reports, recommendations, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports depend on configured provider accounts; account changes require write access.]

## Skill Version(s):

0.20.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
