## Description:

Databar.ai lets agents read, create, and update Databar.ai data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Databar.ai schemas, read account, table, row, enrichment, and task data, and submit table or enrichment operations through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that would execute code on the user's machine.

Mitigation: Do not let an agent run installer commands automatically; review the installer path and prefer official versioned documentation with checksum or signature verification where available.

Risk: Write actions can create tables, insert rows, or submit enrichment and waterfall tasks in Databar.ai.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-databar-ai)
- [Databar.ai homepage](https://databar.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Databar.ai action schemas before execution; write actions require confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
