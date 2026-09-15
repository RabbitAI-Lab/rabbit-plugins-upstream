## Description:

Query and act on Evite events, guest lists, RSVPs, messages, invitations, and photos from a shell using curl with authenticated session cookies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to generate shell commands and guidance for reading Evite event data and performing account-authorized Evite actions without installing an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles an Evite password and live session cookies through shell commands.

Mitigation: Use a unique private cookie jar created with mktemp, restrict file permissions, avoid exposing credentials in shell history, and delete the cookie jar after use.

Risk: Generated commands can make real changes to Evite events, guest lists, RSVPs, broadcasts, invitations, cancellations, and photo uploads.

Mitigation: Validate event and guest IDs before execution and test mutating commands only on throwaway events before using them on real invitations.

Risk: Some messaging and send request bodies are documented as assumed rather than fully verified.

Mitigation: Treat those operations as less certain, inspect the generated request body before execution, and prefer a low-impact test event first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)
- [Evite endpoint reference](artifact/references/endpoints.md)
- [Evite](https://www.evite.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and curl code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that read private event data or mutate real Evite events when executed with valid user credentials.]

## Skill Version(s):

0.8.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
