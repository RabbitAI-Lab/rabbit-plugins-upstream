## Description:

Guides agents to access an authorized SimplePractice Client Portal from a shell with curl, using passwordless sign-in or optional fpx cookie capture to read appointments, billing, documents, announcements, and practice or clinician information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and authorized portal users use this skill to script read-only retrieval of their own SimplePractice Client Portal data without running the SimplePractice MCP server. It is intended for authorized access to appointment, billing, document, announcement, practice, and clinician information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive health data and session cookies.

Mitigation: Use it only for authorized access to your own portal data, protect the cookie jar like a password, keep credentials out of git, and avoid shared machines.

Risk: Browser-cookie extraction can grant portal access without a fresh sign-in flow.

Mitigation: Prefer the magic-link flow unless browser-cookie access through fpx is intentional, and grant only the scopes needed for the session.

Risk: Repeated failed sign-in requests can trigger email or IP rate limits.

Mitigation: Do not retry failed sign-ins aggressively; wait out rate limits before requesting another link or PIN.

## Reference(s):

- [SimplePractice Client Portal request reference](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused instructions for authorized portal access; no write operations are covered.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
