## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect easyTable restaurant availability, retrieve booking details, and prepare or run fpx shell commands for booking workflows without running the easytable MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can cancel, create, or modify real restaurant bookings.

Mitigation: Require explicit user confirmation before any booking write action and avoid firing create or cancel calls as tests.

Risk: The workflow bridges requests through a signed-in browser session and depends on the Transporter extension.

Mitigation: Pin and verify @fetchproxy/cli, keep browser extension access limited to the easyTable origin, and use fpx health or pairing checks before running commands.

Risk: Create and modify flows may involve manual Turnstile token handling.

Mitigation: Only copy Turnstile tokens for an authorized booking flow, avoid storing tokens or booking payloads persistently, and delete temporary payload files immediately.

Risk: easyTable write endpoints can return HTTP 200 even when a booking action is rejected.

Mitigation: Parse the returned status body and treat Status:0 as failure instead of relying on the HTTP status code or process exit code alone.

## Reference(s):

- [easyTable fpx request recipes](references/easytable-requests.md)
- [easytable-fpx ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command pipelines for parsing HTML fragments and cautions for write actions.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
