## Description:

Use this skill for Webflow requests to read, create, update, publish, and delete data through the OOMOL-connected Webflow connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Webflow sites and CMS collections, then create, update, publish, or delete CMS and site content through an authenticated OOMOL Webflow connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts for the oo CLI.

Mitigation: Review the setup path before installation and prefer a verified or package-manager installation of the oo CLI instead of piping remote scripts directly into a shell.

Risk: Write, publish, and delete actions can change Webflow CMS items or site publication state.

Mitigation: Require an exact payload and effect summary before approval, and use only Webflow accounts whose sites are intended to be managed by this skill.

## Reference(s):

- [Webflow](https://webflow.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Webflow Skill](https://clawhub.ai/oomol/skills/oo-webflow)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill routes Webflow actions through the oo CLI and may produce read results, write confirmations, publish results, or setup guidance.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
