## Description:

Guides agents in reading a user's own SimplePractice Client Portal data from the shell with curl, including sign-in, appointments, billing documents, shared documents, announcements, and practice or clinician information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve their own SimplePractice Client Portal data through documented read-oriented curl commands when they do not want to run the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cookie jar can provide bearer-token access to protected health information.

Mitigation: Keep the cookie jar private, restrict permissions to the account owner, keep it out of source control, and avoid shared machines.

Risk: Using account-changing portal actions from scripts could affect healthcare, billing, signing, cancellation, or other sensitive workflows.

Mitigation: Use the skill's documented read-only examples and perform payments, signing, cancellation, and other account-changing actions in the portal UI.

Risk: Repeated failed sign-in attempts can trigger email or IP rate limits.

Mitigation: Do not retry after rate-limit errors; wait before requesting another passwordless sign-in link or PIN.

Risk: A portal single-page app can return 200 HTML for paths that are not valid JSON:API endpoints.

Mitigation: Check that responses use the expected JSON:API content type and prefer the documented endpoints.

## Reference(s):

- [SimplePractice Client Portal request reference](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON:API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented portal access guidance; no files are produced by the skill itself.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
