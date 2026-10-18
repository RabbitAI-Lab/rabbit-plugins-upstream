## Description:

Finds listed model API and relay prices, free credits, and guidance for connecting a chosen provider to an app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanzohanzhe](https://clawhub.ai/user/hanzohanzhe)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other API users compare listed model prices and free-credit offers, then optionally configure a chosen provider in their app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a provider can persistently change the agent's model API and where it spends credits.

Mitigation: Review the proposed configuration change, confirm before applying it, and retain the backup for undo.

Risk: The WorkBuddy/CodeBuddy credential path may store an API key with unsafe inherited file permissions.

Mitigation: Avoid that path unless the configuration file is owner-only; keep credentials out of shared files.

## Reference(s):

- [Grandet homepage](https://grandet.ai)
- [Published skill](https://clawhub.ai/hanzohanzhe/skills/grandet-api-price-finder)
- [Free credits](references/free-credits.md)
- [Connection guidance](references/host-setup.md)
- [Quality evidence](references/quality-evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with price comparisons, links, and optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Price and free-credit lookups are read-only; connecting a provider requires user confirmation.]

## Skill Version(s):

0.3.0-build.20261018.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
