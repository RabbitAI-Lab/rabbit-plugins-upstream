## Description:

AnyDB (anydb.com). Use this skill for ANY AnyDB request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect AnyDB connector schemas and operate AnyDB records through an OOMOL-connected account. It supports listing, searching, reading, creating, and updating structured records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create and update actions can change AnyDB records.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: First-time setup can install the oo CLI or connect an OOMOL account to AnyDB.

Mitigation: Use setup steps only when the user intends the agent to operate AnyDB through OOMOL and trusts the oo CLI.

## Reference(s):

- [AnyDB homepage](https://www.anydb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-anydb)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema checks before building AnyDB action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
