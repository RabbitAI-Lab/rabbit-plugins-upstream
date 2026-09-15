## Description:

Discourse (discourse.org). Use this skill for ANY Discourse request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read Discourse forum data and, with confirmation for write actions, create topics or replies through an OOMOL-connected Discourse account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the installer before execution, prefer an official package manager when available, or manually download and verify the installer.

Risk: The skill can create Discourse topics and replies that change forum state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Discourse actions depend on OOMOL as an intermediary for authenticated requests.

Mitigation: Install only when the user is comfortable using OOMOL-connected credentials for Discourse operations.

## Reference(s):

- [Discourse homepage](https://www.discourse.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-discourse)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill routes Discourse actions through the oo CLI and expects live schema inspection before action payloads are built.]

## Skill Version(s):

1.0.3 (source: release evidence, SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
