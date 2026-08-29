## Description:

Access AlphaPortal school-bus data from shell workflows by capturing a browser refresh token, minting access tokens, and calling the AlphaRoute REST API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized users and developers use this skill to retrieve AlphaPortal student transportation data, live bus location, notifications, and related endpoint responses without running the MCP server. It is intended for scripting and shell-based inspection when the user already has legitimate AlphaPortal account access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refresh tokens can enable access to sensitive student transportation records and live bus location data.

Mitigation: Use only with explicit authorization for the AlphaPortal account and students involved, and avoid storing tokens in shared shells, scripts, logs, or long-lived environment files.

Risk: Documented write endpoints can permanently change transportation-related settings.

Mitigation: Require strict user confirmation before issuing write calls and avoid using write endpoints for casual exploration.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [AlphaRoute API base](https://api.alpharoute.app)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl and jq recipes, token handling steps, endpoint examples, and cautions for live write calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
