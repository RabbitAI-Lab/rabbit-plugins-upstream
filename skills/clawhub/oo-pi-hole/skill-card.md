## Description:

Pi-hole (pi-hole.net). Use this skill for Pi-hole requests that read, create, update, or delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and administrators use this skill to operate Pi-hole through the OOMOL connector, including monitoring DNS activity, managing domains, lists, groups, clients, configuration, backups, gravity updates, and DNS blocking state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from external URLs if used without independent verification.

Mitigation: Install the oo CLI only from a trusted and verified source, and avoid running pasted remote installer commands unless the source has been reviewed.

Risk: Broad oo CLI access can operate the user's connected Pi-hole account, including write and destructive actions.

Mitigation: Review the live action schema, exact payload, and expected effect before approving state-changing actions; require explicit approval for destructive deletes or restores.

## Reference(s):

- [Pi-hole homepage](https://pi-hole.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pi-hole)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and an execution id when actions are run with JSON output.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
