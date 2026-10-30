## Description:

Provides local AI-writing self-checks and academic-writing polish guidance, including consistency, translation-style, paragraph attribution, journal prechecks, style conventions, quality and AIGC-label checks, and sentence-level revision suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Academic writers use the skill locally to review manuscript drafts for AI-writing signals and identify writing-quality, consistency, and terminology issues. It offers suggestions rather than automatically rewriting text; use it for self-checking, not ghostwriting or institutional plagiarism checking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crafted report files may insert browser code into generated HTML reports.

Mitigation: Prefer text or JSON output, and avoid rendering reports received from others until HTML escaping and validation are fixed.

Risk: The built-in verifier and AI scores are limited checks and should not be treated as conclusive judgments.

Mitigation: Treat scores as advisory and review the results in context.

Risk: Terminology replacements may need editorial review, and workflows can temporarily store manuscript text on disk.

Mitigation: Review proposed replacements before using corrected copy, and account for local manuscript files when handling sensitive drafts.

## Reference(s):

- [Paper Polisher Pro on ClawHub](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Project repository](https://github.com/docsor1212/paper-polisher-pro)
- [Documentation site](https://docsor.cn)
- [ModelScope skill page](https://modelscope.cn/skills/Docsor/paper-polisher-pro)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML]

**Output Format:** [Text and structured JSON reports, Markdown guidance, and self-contained HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally; sentence-level revision output is advisory rather than an automatic rewrite, and AI-writing scores should be treated as limited checks.]

## Skill Version(s):

6.4.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
