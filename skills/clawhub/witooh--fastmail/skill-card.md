## Description: <br>
Manages Fastmail email and calendar via JMAP and CalDAV APIs. Use for emails (read, send, reply, search, organize, bulk operations, threads) or calendar (events, reminders, RSVP invitations). Timezone auto-detected from system. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[witooh](https://clawhub.ai/user/witooh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Fastmail account users use this skill to let an agent inspect, search, send, organize, and delete Fastmail email and create or manage calendar events, reminders, and invitations through JMAP and CalDAV. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants an agent broad access to private Fastmail email and calendar data. <br>
Mitigation: Install it only in trusted agent environments, use revocable app-specific credentials, keep .env files out of source control, and rotate credentials if they are exposed. <br>
Risk: Destructive or externally visible operations can send email, reply-all, delete or bulk-modify mail, update or delete calendar items, remove reminders, or RSVP to invitations. <br>
Mitigation: Require explicit manual approval before executing those operations. <br>


## Reference(s): <br>
- [Fastmail skill page](https://clawhub.ai/witooh/skills/fastmail) <br>
- [Fastmail Tools Reference](references/TOOLS.md) <br>
- [Fastmail API Documentation](https://www.fastmail.com/dev/) <br>
- [JMAP Specification](https://jmap.io/spec.html) <br>
- [CalDAV RFC](https://datatracker.ietf.org/doc/html/rfc4791) <br>
- [iCalendar Format](https://icalendar.org/) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON tool responses from CLI/API operations, with Markdown setup and usage guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Fastmail credentials in environment variables; calendar timezone can be configured with FASTMAIL_TIMEZONE.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
