## Description:

Pod AI enables an agent to inspect connector schemas and create outbound phone calls with a Pod AI voice agent through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Pod AI through an OOMOL-connected account, inspect live connector schemas, and create outbound phone calls with a Pod AI voice agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags setup instructions that run an unverified remote installer script directly in a shell.

Mitigation: Review or verify the oo CLI installation path manually before using the skill; do not have an agent run the remote installer automatically.

Risk: The available Pod AI action can create outbound phone calls, which changes external state.

Mitigation: Fetch the live connector schema and confirm the exact call payload and user-visible effect before running create_outbound_call.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pod-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Pod AI Homepage](https://callpod.ai/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing Pod AI action payloads.]

## Skill Version(s):

1.0.2 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
