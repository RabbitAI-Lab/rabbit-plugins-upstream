## Description:

Gem (gem.com). Use this skill for Gem requests that search and read data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Gem CRM data, including candidates, projects, sequences, users, custom fields, and project memberships. It is intended for read-oriented Gem workflows through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly.

Mitigation: Use an official, verifiable installation path and inspect installer contents before running them.

Risk: Gem access is mediated through OOMOL-connected credentials.

Mitigation: Install only when use of OOMOL as the intermediary for Gem access is acceptable for the workspace.

## Reference(s):

- [Gem homepage](https://www.gem.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-gem)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
