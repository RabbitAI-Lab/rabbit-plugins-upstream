## Description:

Analyzes local WeChat chat records to produce relationship/personality assessments, conversation-status summaries, issue diagnosis, and next-reply suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiqingge](https://clawhub.ai/user/haiqingge)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect local WeChat chats, identify active sessions, summarize relationship dynamics, and draft context-aware reply suggestions. It is intended for personal chat analysis workflows where the user explicitly selects the contact or scan mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access local WeChat chats, contacts, recent sessions, unread status, and relationship-related message content.

Mitigation: Install and run it only after explicit user approval, and require confirmation for each contact or session scan.

Risk: Bundled data files and generated caches can contain raw chat transcripts, contact identifiers, feedback, and analysis history.

Mitigation: Delete bundled data files before use and clear cache, history, and feedback files after analysis when retention is not needed.

Risk: Raw transcript output may expose sensitive personal conversations in generated reports.

Mitigation: Disable or remove raw transcript sections before sharing reports, and limit generated reports to necessary summaries.

## Reference(s):

- [Analysis Framework](artifact/references/analysis_framework.md)
- [Response Templates](artifact/references/response_templates.md)
- [ClawHub skill page](https://clawhub.ai/haiqingge/skills/wechat-chat-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline command guidance and reply suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include chat statistics, trend comparisons, active-session lists, and raw transcript excerpts unless disabled by the user.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
