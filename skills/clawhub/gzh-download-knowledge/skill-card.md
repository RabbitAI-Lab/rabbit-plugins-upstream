## Description:

Exports the user's own WeChat Official Account article history from the official published-records page into local Markdown archives using the currently logged-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content owners use this skill to archive articles from their own WeChat Official Account into a local Markdown knowledge base. It is intended for accounts where the browser is already logged into the official WeChat admin backend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the currently logged-in WeChat Official Account admin browser session and can export account article contents to local files.

Mitigation: Run it only while logged into the account intended for archiving, and choose an output directory appropriate for article titles, URLs, authors, dates, and full article text.

Risk: Using the skill outside the documented boundary could create copyright or account-use issues.

Mitigation: Use it only for articles from the user's own official account through the official published-records page.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fatmind/skills/gzh-download-knowledge)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Text]

**Output Format:** [Local Markdown article files, index JSON, result JSON, data Markdown, and one-line JSON stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an active WeChat Official Account admin browser session and writes article titles, URLs, authors, dates, and full article text to the selected local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
