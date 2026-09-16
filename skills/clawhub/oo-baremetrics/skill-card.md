## Description:

Use this Baremetrics skill for reading, creating, and updating Baremetrics data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to inspect Baremetrics schemas and run Baremetrics connector actions for sources, customers, plans, subscriptions, and charges. It supports both read workflows and confirmed write workflows such as creating or updating customers, plans, and subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags the first-time setup instructions for an unverified one-line remote installer script.

Mitigation: Prefer an official package or a downloaded installer whose source and integrity can be verified before execution.

Risk: The skill can run Baremetrics write actions that create, update, or cancel business data.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged [write] or [destructive].

## Reference(s):

- [Baremetrics Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-baremetrics)
- [Baremetrics Homepage](https://baremetrics.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command output may include JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
