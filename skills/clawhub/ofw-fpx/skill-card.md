## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal records from a shell by using fpx to capture a signed-in browser token and curl to call OFW endpoints directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient OFW users use this skill to read, write, upload, and delete OurFamilyWizard records from shell scripts when an MCP server is unavailable or undesired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured signed-in OFW browser session token can expose sensitive family-court records to direct shell access.

Mitigation: Install only when this access is intentional, keep browser extension site access scoped to OFW, and revoke pairing or sign out when work is complete.

Risk: Write, upload, and delete commands can permanently change records visible in OFW.

Mitigation: Verify IDs and record details before running write or delete commands, and export or archive important records first.

## Reference(s):

- [OurFamilyWizard requests for fpx + curl](references/requests.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read and write request examples for OFW endpoints; no local cache is provided.]

## Skill Version(s):

2.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
