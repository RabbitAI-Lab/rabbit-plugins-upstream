## Description:

Operate Sendspark through an OOMOL-connected account to read, create, and update Sendspark data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Sendspark through an OOMOL-connected account, including creating and managing dynamic video campaigns, adding prospects, and retrieving prospect data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Prefer an official package-manager or signed release path, or inspect a pinned installer with checksum or signature verification before execution.

Risk: Write actions can modify Sendspark campaigns or prospects.

Mitigation: Confirm the exact payload and expected effect with the user before running state-changing actions.

## Reference(s):

- [Sendspark homepage](https://sendspark.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sendspark)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue oo CLI connector calls that return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
