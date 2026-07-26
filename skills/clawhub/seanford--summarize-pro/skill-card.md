## Description: <br>
Summarize Pro helps agents turn long text, articles, documents, meetings, emails, transcripts, books, PDFs, reports, and conversations into concise summaries in formats such as TL;DRs, bullet points, key takeaways, action items, executive summaries, comparisons, translations, and custom-length summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to summarize long or complex content into readable formats for review, decisions, follow-up tasks, and saved reference. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local summary history, saved summaries, templates, and usage stats may contain sensitive details from user-provided documents. <br>
Mitigation: Review or delete ~/.openclaw/summarize-pro/ when clearing local data or before using the skill on shared systems. <br>
Risk: Summaries can omit context or misstate details if source material is ambiguous, incomplete, or too long for the active model context. <br>
Mitigation: Review important summaries against the source text before relying on them for decisions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/seanford/skills/summarize-pro) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration] <br>
**Output Format:** [Markdown-style text with headings, lists, tables, action items, and word-count statistics; local JSON files for settings, history, saved summaries, and templates when persistence features are used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Keeps summary history and preferences locally under ~/.openclaw/summarize-pro/.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
