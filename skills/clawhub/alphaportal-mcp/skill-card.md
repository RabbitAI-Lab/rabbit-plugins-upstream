## Description:

Access AlphaPortal (AlphaRoute) school-bus data such as students, stops, live bus GPS location, and arrival notifications from a shell with curl by using a captured web-app refresh token to mint access tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized AlphaPortal users use this skill to query school transportation data from shells or scripts without running the alphaportal-mcp server. It also documents write calls for transportation settings, which should only be used with explicit authorization and intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived browser refresh tokens can expose AlphaPortal account access and sensitive school transportation data.

Mitigation: Install and use the skill only with explicit authorization; avoid shared shells, logs, shell history, and scripts that store tokens or API responses, and prefer an official or vendor-approved API/auth flow where available.

Risk: The skill includes curl examples for write endpoints that can permanently change real transportation settings.

Mitigation: Use write examples only when you intend to make the documented change, confirm the target student and request body before execution, and avoid unattended automation for these calls.

Risk: Student records, notification data, and live bus location data are sensitive and may be exposed through command output or saved responses.

Mitigation: Minimize displayed fields, redact outputs before sharing, and avoid persisting response payloads unless required by an authorized workflow.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell, JavaScript, curl, and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Handles browser refresh tokens, bearer access tokens, student transportation records, live vehicle location, notifications, and write examples for real transportation settings.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
