## Description:

A toolkit for academic writing self-review that checks AI-writing signals, style, and terminology, and offers sentence-level revision guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Authors use it to self-review academic drafts, especially Chinese prose, for AI-writing signals, terminology, style, and consistency, then use reports and suggestions to guide their own revisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some editing or verdict behavior may differ from guidance-only expectations.

Mitigation: Review scores and suggestions before use, and keep final interpretation and revision decisions with the author.

Risk: The optional local HTTP service, dependencies, and incomplete scan coverage may not fit every installation environment.

Mitigation: Review dependencies and scan coverage, and decide whether the optional local service fits your environment before installing or enabling it.

Risk: Evaluation reliability is flagged as a concern, so results may be less dependable outside documented use limits.

Mitigation: Use results for author self-review and treat scores as advisory, following the documented short-text, language, mixed-document, and degraded-mode limits.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Best practices](artifact/references/best-practices.md)
- [FAQ and usage limits](artifact/references/faq.md)
- [Architecture reference](artifact/references/architecture.md)
- [Project documentation site](https://docsor.cn)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON, HTML reports]

**Output Format:** [Markdown and JSON reports, optional HTML summaries, and sentence-level revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected check and include advisory scores, findings, or author-reviewed suggestions.]

## Skill Version(s):

7.8.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
