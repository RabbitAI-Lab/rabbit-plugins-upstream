## Description:

Access SignUpGenius (sign-ups, groups, RSVPs) from a shell with curl instead of running the signupgenius-mcp server -- server-side email/password login to a JWT + cfid/cftoken cookies, then curl the v3 API and legacy /SUGboxAPI.cfm dispatcher directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access authorized SignUpGenius account, group, sign-up, slot, participant, and RSVP data from shell workflows without installing the signupgenius-mcp server. It also provides request patterns for carefully confirmed RSVP, slot-claim, group-member, and withdrawal actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches SignUpGenius email/password login and session-token handling, so exposed passwords, JWTs, cookies, or refresh tokens could compromise an account.

Mitigation: Use only authorized accounts, store secrets in a secrets manager, avoid logging or pasting raw tokens, and clean up temporary cookie and header files after use.

Risk: The skill describes unauthenticated lookup endpoints that can return participant names, quantities, and related public sign-up details.

Mitigation: Avoid bulk collection of public participant data and only access sign-up pages and participant details for which the operator has authorization and a legitimate need.

Risk: Several documented flows perform writes, including RSVP submission, slot claims, group-member creation, and withdrawal actions.

Mitigation: Require explicit user confirmation before any write or withdrawal action, verify the target sign-up and member identity, and re-read the affected slot or record after the request.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is documentation-only and does not execute code by itself.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
