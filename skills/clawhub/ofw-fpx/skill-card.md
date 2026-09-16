## Description:

Access OurFamilyWizard (OFW) messages, calendar, expenses, and journal from a shell with the fpx CLI by capturing the signed-in web app's bearer token once, then calling the OFW REST API directly with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient OFW users use this skill to retrieve OFW data and prepare direct curl calls for OFW messages, calendar, expenses, journal, and attachments without running the ofw-mcp server. It is intended for use where the user already has an authenticated OFW browser session and understands that write and delete commands affect shared family-court records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill workflow uses a browser-derived bearer token to access sensitive OFW data and can make permanent write or delete changes to shared family-court records.

Mitigation: Run it only from a trusted personal machine, treat the bearer token like a password, and require explicit human confirmation before any send, upload, create, update, or delete command.

Risk: The workflow relies on a globally installed token-access tool and an active signed-in browser session.

Mitigation: Prefer a pinned, reviewed @fetchproxy/cli version, avoid shared terminals or shell tracing, and invalidate the OFW session if the token may have been exposed.

## Reference(s):

- [OurFamilyWizard requests for fpx + curl](references/requests.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown with inline shell commands and JSON-oriented curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that read from or write to OFW using a browser-derived bearer token; users should review and confirm write/delete operations before execution.]

## Skill Version(s):

2.16.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
