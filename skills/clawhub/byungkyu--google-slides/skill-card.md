## Description:

Google Slides API integration with managed OAuth for creating presentations, adding slides, inserting content, and managing slide formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an authorized Google Slides account through Maton, inspect presentations, create or update slide content, and set up approved automations that act on Google Slides data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a Google Slides connection can expose presentation content available to the connected account.

Mitigation: Use OAuth where possible, select the narrowest available scopes, prefer read-only access, and confirm connection creation with the user before authorizing.

Risk: Write calls and hosted automations can change presentations or continue acting after the initial setup.

Mitigation: Confirm each POST, PUT, PATCH, DELETE, function deployment, trigger, and destination separately with the target resource, payload, and intended effect.

Risk: Trigger destinations can create persistent forwarding of matching events, including sensitive source-system data.

Mitigation: Prefer platform destinations such as api.maton.ai or *.maton.app, and use third-party destinations only after the user approves the exact host and understands what data will be sent.

Risk: API-key based access can expose a long-lived credential if it is printed, logged, committed, or inherited by child processes.

Mitigation: Prefer OAuth; when an API key is unavoidable, keep it out of logs and files, avoid exporting it broadly, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-slides)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Slides API Overview](https://developers.google.com/slides/api/reference/rest)
- [Presentations](https://developers.google.com/slides/api/reference/rest/v1/presentations)
- [Pages](https://developers.google.com/slides/api/reference/rest/v1/presentations.pages)
- [BatchUpdate Requests](https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate)
- [Page Layouts](https://developers.google.com/slides/api/reference/rest/v1/presentations/create#predefinedlayout)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, API paths, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated Maton CLI commands, raw HTTP examples, hosted function snippets, and trigger configuration guidance; writes and automations require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
