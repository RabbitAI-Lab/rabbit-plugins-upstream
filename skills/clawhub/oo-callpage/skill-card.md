## Description:

Use CallPage through an OOMOL-connected account to read calls, users, and widgets and to create callback requests without handling raw API tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate CallPage through the OOMOL connector: listing and retrieving calls, users, and widgets, and creating widget callback requests after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, verifiable method; do not allow an agent to run remote installer commands automatically.

Risk: The skill can create CallPage callback requests that change CallPage state.

Mitigation: Confirm the exact payload and expected effect with the user before any write action.

Risk: Authentication and CallPage connection steps affect the user's OOMOL account.

Mitigation: Run login or connection steps only after an action fails for auth or connection reasons and with explicit user approval.

## Reference(s):

- [ClawHub CallPage skill page](https://clawhub.ai/oomol/skills/oo-callpage)
- [CallPage homepage](https://www.callpage.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action execution; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
