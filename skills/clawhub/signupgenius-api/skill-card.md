## Description:

Provides curl-based guidance for logging in to SignUpGenius session mode and calling its v3 API and legacy SUGboxAPI endpoints for profiles, groups, sign-ups, RSVPs, slot reads, claims, and releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access SignUpGenius account and public sign-up data from shell scripts when the MCP server is unavailable or unnecessary. It also guides careful RSVP, slot claim, release, and group-member changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented endpoints can expose privacy-sensitive participant names, identifiers, contact details, and quantities, including through unauthenticated public sign-up reads.

Mitigation: Use the skill only for sign-ups and accounts the operator is authorized to manage, and avoid collecting participant names or identifiers unless clearly necessary and permitted.

Risk: The workflow handles SignUpGenius passwords, JWTs, and ColdFusion cookies that function as bearer secrets.

Mitigation: Use a secret manager or interactive prompt for credentials, keep temporary cookie and header files private, and clean them up after use.

Risk: Some examples perform state-changing operations such as RSVP submission, slot claim or release, and group-member changes.

Mitigation: Confirm the target account, sign-up, slot, participant, and intended action before running any write command, then re-read the relevant record to verify the result.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes SignUpGenius API request patterns, jq parsing examples, session handling notes, and write-action cautions.]

## Skill Version(s):

1.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
