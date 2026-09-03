## Description:

OOMOL Console (console.oomol.com). Use this skill for ANY OOMOL Console request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and administrators use this skill to inspect and administer OOMOL Console teams, billing, usage, connections, members, and permission groups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make account-impacting OOMOL Console changes, including permission changes, member additions, and group deletion.

Mitigation: Approve write and destructive actions only after reviewing the exact target, action name, and JSON payload.

Risk: Incorrect action payloads can change the wrong OOMOL Console resource or fail against the live connector contract.

Mitigation: Inspect the live connector schema before constructing payloads and match the authoritative input fields.

## Reference(s):

- [OOMOL Console skill page](https://clawhub.ai/oomol/skills/oo-oomol-console)
- [OOMOL Console homepage](https://console.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before actions and returns OOMOL Console action results when commands are executed.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
