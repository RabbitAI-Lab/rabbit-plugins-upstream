## Description: <br>
邮件日报免费版 helps personal users use browser automation with an authenticated mailbox session to collect recent messages and generate a daily email statistics and summary report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users, independent developers, and small teams can use this skill to review a live mailbox, count unread and visible messages, capture inbox screenshots, and produce a daily digest for faster triage. It is intended for mailbox summarization and notification workflows, not bulk or spam messaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates an authenticated browser mailbox session. <br>
Mitigation: Use an already logged-in browser session, avoid entering passwords through agent commands, and supervise the session when accessing live mail. <br>
Risk: Inbox screenshots and summary reports may contain sensitive personal or business information. <br>
Mitigation: Store generated outputs in a private directory, limit sharing, and delete screenshots and reports when they are no longer needed. <br>
Risk: Browser automation over mailbox pages may select the wrong elements or expose more messages than intended. <br>
Mitigation: Review proposed commands before execution, keep the workflow scoped to read-only summarization, and verify mailbox-specific selectors before relying on extracted data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/email-digest-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown and text reports with optional JSON, CSV, bash snippets, and PNG screenshots] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write inbox screenshots and local digest files that contain sensitive mailbox information.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
