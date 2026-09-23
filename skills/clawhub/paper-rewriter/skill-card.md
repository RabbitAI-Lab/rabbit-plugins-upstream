## Description:

A bilingual CN/EN academic writing toolkit that helps agents run local style self-checks, deterministic cleanup, rewrite guidance, and integrity checks for clearer scholarly prose.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, scholars, ESL authors, and writing-support agents use this skill to check academic drafts for stiff or templated phrasing, clean mechanical artifacts, guide section-by-section revision, and verify that numbers, citations, and terminology remain intact. It is intended for legitimate writing-quality improvement with required AI-use disclosure, not for concealing authorship or defeating integrity review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may try to use rewriting to hide required AI disclosure or misrepresent authorship.

Mitigation: Refuse concealment or integrity-evasion requests, point users to the bundled compliance guidance, and offer only legitimate quality-editing assistance.

Risk: Academic facts, statistics, citations, or terminology could be altered during revision.

Mitigation: Run the bundled integrity guard after revision and fix the rewrite if numbers, DOIs, PMIDs, years, abbreviations, or user-provided terms are lost or changed.

Risk: Local heuristic style scores may be mistaken for official authorship or AI-detection evidence.

Mitigation: Present reports as writing-pattern self-checks only, review outputs before use, and keep drafts and version history as process evidence.

Risk: Sensitive technical terminology may be damaged if it is not protected.

Mitigation: Provide a terms file for drug names, gene symbols, scale names, instruments, and custom abbreviations before running the pipeline.

## Reference(s):

- [End-to-End Examples](references/examples.md)
- [FAQ](references/faq.md)
- [English Academic Style Manual](references/style_guide_en.md)
- [Chinese Academic Style Manual](references/style_guide_zh.md)
- [Compliance and Integrity Guardrails](references/compliance.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports, plain-text rewrites, JSON reports when requested, and shell commands for local scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided text files; supports CN/EN style reports, deterministic cleanup output, rewrite briefs, and integrity-verification summaries.]

## Skill Version(s):

1.2.0 (source: server release metadata and hxt_core.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
