## Description:

Provides schema-first read access to Gitee through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the authenticated Gitee user, fetch repository details, and list repositories visible to the connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad oo CLI authority for a Gitee-read workflow.

Mitigation: Review the skill before installation and narrow allowed commands to Gitee connector schema and read actions where the host policy supports it.

Risk: The first-time setup instructions include remote installer one-liners.

Mitigation: Verify the installer source and publisher before running installer commands, or install the CLI through an already trusted process.

Risk: Gitee access is mediated through an OOMOL-connected account.

Mitigation: Use a least-privileged connected account or scopes, and review action payloads before executing any command that could expose account or repository data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gitee)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Gitee](https://gitee.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
