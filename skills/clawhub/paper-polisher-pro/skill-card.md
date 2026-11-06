## Description:

Provides academic writers with AI-writing self-checks, terminology and style checks, journal prechecks, and sentence-level revision guidance that does not rewrite text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic writers use the skill to review drafts for AI-like signals, terminology consistency, translation artifacts, style conventions, and journal requirements, then assess suggested changes themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional local HTTP server lacks caller authentication and browser-origin checks.

Mitigation: Prefer the CLI or default stdio integration; keep HTTP mode disabled until authentication and origin checks are added.

Risk: Workflow reports can retain manuscript excerpts in temporary directories.

Mitigation: Remove temporary report files when finished.

Risk: Terminology changes may introduce errors, especially for medical terminology.

Mitigation: Review terminology changes on copies of the source text.

Risk: AI-writing scores can be misleading and do not establish authorship; short texts have no verdict.

Mitigation: Treat scores as advisory and follow the relevant institution's AI-use and disclosure policy.

Risk: The separately supplied optional model has not been reviewed.

Mitigation: Treat the model as unreviewed and verify its source before installing or using it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Publisher profile](https://clawhub.ai/user/docsor1212)
- [Usage FAQ](references/faq.md)
- [Writing best practices](references/best-practices.md)
- [Documentation site](https://docsor.cn)
- [Project issue and model request page (linked from README)](https://github.com/docsor1212/paper-polisher-pro)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, HTML reports, CSV summaries, Writing guidance]

**Output Format:** [JSON, Markdown, HTML, and CSV reports with sentence-level writing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores are advisory; texts under 100 characters receive no verdict.]

## Skill Version(s):

7.5.0 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
