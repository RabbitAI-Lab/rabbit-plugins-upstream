## Description:

Analyzes face images or videos to identify nine traditional Chinese medicine constitution types and return structured wellness suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit facial media or media URLs for cloud-based TCM constitution analysis, receive structured reports and wellness suggestions, and query prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, and related wellness analysis are sent to the publisher's cloud service.

Mitigation: Use only with clear consent from the person shown and avoid private health media unless the user accepts cloud processing.

Risk: The skill may create or reuse a local identity and store service tokens in a workspace SQLite database.

Mitigation: Protect the workspace data directory, review retention expectations, and remove local identity or token data when it is no longer needed.

Risk: Prior reports can be fetched automatically when report-list prompts are used.

Mitigation: Run report queries only in the intended workspace/account context and review report content before sharing it.

Risk: TCM constitution output is wellness-oriented and may be mistaken for medical diagnosis.

Mitigation: Present results as informational wellness guidance and direct users with symptoms or health concerns to qualified clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands]

**Output Format:** [Markdown text containing structured JSON analysis or report-list output, with optional file output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report export URL; accepts local media paths or public media URLs and supports basic, standard, or json detail levels.]

## Skill Version(s):

1.0.11 (source: server release metadata; SKILL.md frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
