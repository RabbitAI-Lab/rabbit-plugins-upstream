## Description:

Local agent identity - wallet, secrets, optional email. Use when asked to initialize or hand off an identity, use its wallet or secrets, connect email, or process mail. Prefer --json and open the matching reference for multi-step work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mbilenko03](https://clawhub.ai/user/mbilenko03)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to initialize or inspect a local agent identity, manage handoff context, work with stored secrets, connect optional email, and authorize wallet activity through the agentself CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through commands that touch local identity files, secrets, optional email setup, and wallet authorization.

Mitigation: Install only when this local identity workflow is intended, check the agentself CLI version and executable path first, and avoid exposing secret values in logs, arguments, or chat.

Risk: The documented default Base wallet is live and wallet send actions can move real funds.

Mitigation: Inspect wallet backends and review wallet actions manually before authorizing signing or transfers.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON-oriented CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers --json CLI output and requires agentself cli schema 1.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
