## Description:

Apple Ads helps agents operate Apple Ads through OOMOL-connected credentials using the oo CLI for reading, creating, updating, and deleting advertising resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Apple Ads connector schemas, run Apple Ads actions through connected OOMOL credentials, and manage campaigns, ad groups, ads, creatives, keywords, reporting, recommendations, and related account resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can install the oo CLI by running remote installer scripts on the host.

Mitigation: Review the CLI installation path first and prefer a verified package or manually reviewed installer before using the skill.

Risk: Write and destructive Apple Ads actions can change budgets, campaigns, ads, keywords, creatives, and related account resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub Apple Ads Skill](https://clawhub.ai/oomol/skills/oo-apple-ads)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Apple Ads](https://ads.apple.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; read, write, and destructive actions are labeled in the skill guidance.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
