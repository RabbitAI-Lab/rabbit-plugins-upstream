## Description:

Helps agents work with SignPath by submitting hash-signing requests, checking signing request status, and listing visible signing policies through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to request SignPath hash signatures, monitor signing requests, and discover available signing policies from an agent. It is intended for users with an OOMOL-connected SignPath account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit SignPath signing requests through an OOMOL-connected account.

Mitigation: Require explicit user confirmation of the exact payload and effect before any fast_sign_hash or signing action.

Risk: The skill documentation includes remote installer commands for the oo CLI.

Mitigation: Prefer a verified manual or package-manager installation path instead of running pipe-to-shell installer commands.

Risk: Installing the skill gives the agent access to actions available through the user's connected SignPath account.

Mitigation: Review the skill before installation and use it only with SignPath access the user is comfortable delegating to the agent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-signpath)
- [SignPath Homepage](https://signpath.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected SignPath account; action schemas should be fetched before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
