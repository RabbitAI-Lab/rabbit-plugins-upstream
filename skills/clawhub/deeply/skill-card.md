## Description:

deeply helps an agent retrieve first-hand, dated quotes and source-backed viewpoints from selected interviews, articles, podcast transcripts, and research reports for judgment-oriented questions in finance, technology, business, and ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[komako-workshop](https://clawhub.ai/user/komako-workshop)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to support analysis, comparison, and decision-making questions with attributed expert evidence before composing an answer. It is intended for judgment-oriented research questions, not current prices, breaking news, health, metaphysics, or relationship advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send broad judgment and research questions to deeply.dev for retrieval without a clear user-facing consent step.

Mitigation: Install and use it only for queries suitable for third-party processing; avoid confidential business plans, personal financial details, secrets, or regulated data unless intentionally sharing that text with the service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/komako-workshop/skills/deeply)
- [Deeply token setup](https://deeply.dev)
- [Deeply evidence search API](https://api.deeply.dev/v2/evidence/search)
- [Deeply unit retrieval API](https://api.deeply.dev/api/unit)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a DEEPLY_TOKEN bearer token; search responses include coverage status, source metadata, claims, and verbatim quotes.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
