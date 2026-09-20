## Description:

OpenHands lets an agent operate OpenHands Cloud through an OOMOL-connected account using the oo CLI for reading conversations, starting repository tasks, and sending follow-up messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage OpenHands Cloud conversations and repository task workflows from an agent session. It supports read-only conversation inspection and write actions for starting conversations or sending follow-up messages when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote installer commands that could install the oo CLI without verification.

Mitigation: Do not let an agent run remote installer commands automatically; install the oo CLI only from trusted OOMOL documentation and prefer a pinned or verifiable installer when available.

Risk: The skill can trigger OpenHands write actions such as starting a conversation or sending a follow-up message.

Mitigation: Require explicit user approval for the exact payload and intended effect before running write actions.

Risk: OpenHands access depends on an OOMOL account connection, available scopes, valid credentials, and billing status.

Mitigation: Use the documented setup and recovery steps only after command failures indicate missing authentication, connection scope, expired credentials, app readiness, or insufficient credit.

## Reference(s):

- [OpenHands skill page](https://clawhub.ai/oomol/skills/oo-open-hands)
- [OpenHands homepage](https://www.all-hands.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
