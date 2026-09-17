## Description:

Zigpoll support for searching and reading data through OOMOL's oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Zigpoll users, accounts, polls, slides, participants, responses, and unique survey links through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer commands.

Mitigation: Review the installer before execution and prefer an official, versioned installer with checksum or signature verification.

Risk: The skill routes Zigpoll account access through OOMOL credential handling.

Mitigation: Install only when the user is comfortable with OOMOL acting as an intermediary for the connected Zigpoll account.

## Reference(s):

- [Zigpoll homepage](https://www.zigpoll.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Zigpoll connection setup](https://console.oomol.com/app-connections?provider=zigpoll)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Zigpoll account for live actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
