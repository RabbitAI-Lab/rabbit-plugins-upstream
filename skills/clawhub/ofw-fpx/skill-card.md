## Description:

Access OurFamilyWizard (OFW) messages, calendar, expenses, and journal from a shell with the fpx CLI by capturing the signed-in web app's bearer token and using curl against the REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate shell commands and curl request patterns for reading and updating OurFamilyWizard account data without running the ofw-mcp server. It is suited to scripted OFW workflows where the user intentionally handles the browser-derived bearer token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables shell-level access using a browser-derived OurFamilyWizard bearer token.

Mitigation: Install only when intentionally granting shell workflows access to the OFW account, keep tokens out of logs and shared shell history, and re-capture tokens only from a signed-in browser session you control.

Risk: Write and delete commands can immediately modify sensitive shared family-court records without an enforced confirmation step.

Mitigation: Prefer read-only use unless a write is necessary, and manually inspect every recipient, ID, file path, message body, calendar event, expense, and journal entry before running mutation commands.

Risk: Some message POST responses can appear successful before the content is confirmed.

Mitigation: Re-fetch newly created messages or drafts and verify the subject and body match the intended content before treating the write as complete.

## Reference(s):

- [Skill release page](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [OurFamilyWizard request examples](references/requests.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read and write request patterns for OFW API calls; users must supply their own authenticated token and request values.]

## Skill Version(s):

2.19.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
