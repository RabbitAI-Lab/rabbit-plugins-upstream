## Description:

Voiceflow lets agents operate a connected Voiceflow account through OOMOL, including conversation sessions, environment listing, and knowledge base queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Voiceflow connector actions from an agent, including starting sessions, sending non-streaming interaction actions, listing environments, and querying the knowledge base. It is intended for users who have an OOMOL account connected to Voiceflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer execution for the OOMOL CLI without an embedded verification step.

Mitigation: Review the installer source and prefer a verified package or signed release before installing the CLI.

Risk: Write actions can change Voiceflow conversation state through the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Voiceflow Skill](https://clawhub.ai/oomol/skills/oo-voiceflow)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Voiceflow Homepage](https://www.voiceflow.com)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require payload and effect confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
