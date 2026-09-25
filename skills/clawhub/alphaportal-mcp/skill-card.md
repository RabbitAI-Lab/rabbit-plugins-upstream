## Description:

Access AlphaPortal (AlphaRoute) school-bus data such as students, stops, live bus location, and arrival notifications from a shell using curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized AlphaPortal users use this skill to retrieve school transportation information and run documented AlphaRoute API calls from scripts or a shell without running the alphaportal-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copied AlphaPortal refresh tokens act like durable account secrets and can expose sensitive student transportation data.

Mitigation: Use the skill only with authorized accounts, keep tokens out of shell history, logs, scripts, and shared terminals, and rotate or recapture tokens when needed.

Risk: Documented write endpoints can change real transportation settings without a preview or confirmation step.

Mitigation: Do not run write endpoint commands unless explicit permission and an independent confirmation process are in place.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [AlphaPortal API base URL](https://api.alpharoute.app)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alphaportal-mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands that can read sensitive transportation data and call write endpoints when supplied with valid AlphaPortal tokens.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
