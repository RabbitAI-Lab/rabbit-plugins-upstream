## Description:

Netlify helps agents read, create, update, and delete Netlify resources through an OOMOL-connected Netlify account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Netlify action schemas and manage accounts, users, sites, deploys, builds, forms, and submissions from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly.

Mitigation: Review the skill before installing and prefer a verified, pinned, or package-manager-based oo CLI installation method.

Risk: Write and destructive Netlify actions can change, cancel, delete, lock, unlock, or upload resources in the connected account.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Netlify Skill](https://clawhub.ai/oomol/skills/oo-netlify)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Netlify](https://www.netlify.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect live connector schemas before constructing Netlify action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
