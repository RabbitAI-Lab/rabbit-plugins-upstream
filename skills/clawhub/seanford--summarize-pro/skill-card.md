## Description:

Summarize Pro helps agents summarize long content into formats such as TL;DRs, bullet points, key takeaways, action items, executive summaries, meeting notes, email summaries, comparisons, translated summaries, and custom-length summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to convert long text, documents, meetings, emails, reports, conversations, and transcripts into concise summaries and task-oriented extracts. It is suited for local summarization workflows where retaining user preferences, summary history, saved summaries, and templates on the local machine is acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically keeps local usage history, settings, saved summaries, templates, and summary statistics under ~/.openclaw/summarize-pro/.

Mitigation: Avoid using the skill on highly sensitive text when retained local metadata is unacceptable, and periodically review or delete the local history, saved summaries, settings, and templates files.

Risk: Summaries may omit nuance or introduce misleading emphasis when condensing long or complex source material.

Mitigation: Review summaries against the original source before using them for decisions, publication, compliance, or external communication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seanford/skills/summarize-pro)
- [Publisher profile](https://clawhub.ai/user/seanford)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and plain text summaries, with local JSON settings and history when management features are used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multiple summary styles, language-directed summaries, saved summaries, summary history, usage stats, and custom templates.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
