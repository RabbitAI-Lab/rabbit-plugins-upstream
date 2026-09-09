## Description:

Natural language task and list management for MyLister through its public API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mgoettel13](https://clawhub.ai/user/mgoettel13)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage MyLister task lists through conversational commands, including creating, viewing, updating, moving, completing, sharing, exporting, emailing, and deleting list items. It also supports reminders, comments, project metadata, attachments, media uploads, and API health checks when configured with a MyLister API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags chat commands that can set API keys or custom API base URLs.

Mitigation: Configure credentials through a dedicated low-privilege environment key and avoid chat commands that set API keys or change the API base URL.

Risk: The security summary flags high-impact actions such as deletes, email sends, sharing, and permission changes without clear safety gates.

Mitigation: Run the skill in a host that requires confirmation before deletes, outbound emails, sharing, permission changes, and other mutating operations.

Risk: The security guidance warns against untrusted text that could trigger uploads or destructive actions.

Mitigation: Do not pass untrusted natural-language input directly to the skill; review parsed commands before execution in automated workflows.

Risk: The skill supports local file upload commands for attachments, images, and voice files.

Mitigation: Require explicit user confirmation for file paths and limit the runtime account to files intended for MyLister upload.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/mgoettel13/myLister-Skill)
- [ClawHub skill page](https://clawhub.ai/mgoettel13/skills/mylister-skill)
- [MyLister API documentation](https://api.mylister.dev/docs)
- [MyLister application](https://app.mylister.dev)
- [Agent Skills compatibility reference](https://agentskills.io/)
- [OpenClaw skills documentation](https://github.com/openclaw/openclaw/blob/main/docs/tools/skills.md)
- [Hermes skills guide](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
- [Claude Code skills documentation](https://code.claude.com/docs/en/slash-commands)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, configuration guidance]

**Output Format:** [Formatted text and Markdown responses, with JSON or HTML returned for export commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a MyLister API key; some commands perform network API calls, file uploads, emails, sharing, permission updates, and destructive changes.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact package.json reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
