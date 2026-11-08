## Description:

Access OurFamilyWizard (OFW) — messages, calendar, expenses, journal — from a shell with the fpx CLI (@fetchproxy/cli) instead of running the ofw-mcp server: capture the signed-in web app's Bearer token once via the browser bridge, then curl the REST API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OurFamilyWizard account can use shell commands to access messages, calendar events, expenses, journal entries, and files without installing the ofw-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send or delete messages, change calendar events and expenses, upload files, and add journal entries to a shared family-court record.

Mitigation: Review the exact action and target before running commands, and require human approval before each write or delete. Confirm message sends by fetching the message again as the skill instructs.

Risk: The skill captures and uses the signed-in account's bearer token for API requests.

Mitigation: Keep the token and shell output private, and capture a fresh token only from the signed-in OurFamilyWizard browser session when needed.

Risk: The security scan was partial because some referenced paths were missing, so it cannot provide complete assurance.

Mitigation: Review the skill instructions and request examples before installation; install only if these actions are needed and acceptable.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ofw-fpx on ClawHub](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy extension reference](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance]

**Output Format:** [Markdown instructions with shell commands and JSON request/response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes direct reads and writes to OurFamilyWizard; writes affect the shared account record.]

## Skill Version(s):

2.27.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
