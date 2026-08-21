## Description:

Automates Fanqie Novel author-console workflows for logging in, listing works, uploading single or batch chapters, publishing chapters, and saving chapters as drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and publishing operators use this skill to automate Fanqie Novel chapter management, including QR-code login, work lookup, Markdown chapter extraction, direct publishing, draft saving, and batch submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can directly publish or bulk-save account content in the Fanqie Novel author console.

Mitigation: Prefer draft mode first, verify the selected work and chapter list before running, and manually review chapter content before direct publishing.

Risk: The skill stores login cookies locally after QR-code login.

Mitigation: Use only accounts where local cookie storage is acceptable, keep the workspace access-controlled, and clear saved cookies with logout when finished.

Risk: The skill uses browser automation and clipboard-based content entry.

Mitigation: Run it in a visible browser session, avoid keeping unrelated sensitive content on the clipboard, and watch for unexpected page changes before confirming publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/fanqie-publisher-skill)
- [Fanqie Novel writer console](https://fanqienovel.com/writer/zone/)
- [Fanqie Novel book management](https://fanqienovel.com/main/writer/book-manage)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cause browser-side account actions such as draft saves or chapter submissions when the generated commands or code are executed.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
