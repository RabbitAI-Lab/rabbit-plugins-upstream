## Description:

Laposta (laposta.nl). Use this skill for ANY Laposta request: reading, creating, and updating data through the OOMOL-connected Laposta connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Laposta mailing lists and members through an authenticated OOMOL-connected account. It supports listing, retrieving, creating, and updating Laposta data while requiring schema inspection before payload construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Install the oo CLI only from a trusted, verified, versioned, or signed distribution path before using the skill.

Risk: Write actions can create or update Laposta mailing lists and members.

Mitigation: Review the live action schema and confirm the exact payload and expected effect before running any write action.

## Reference(s):

- [Laposta homepage](https://laposta.nl/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-laposta)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and metadata when actions are run.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
