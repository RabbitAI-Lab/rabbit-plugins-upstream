## Description:

AI writing detection for author self-check, academic polishing guidance, terminology and translation-smell review, metaphor audit, quality reporting, AIGC compliance label checks, paragraph-level attribution, journal precheck, and local fingerprint attribution for CN/EN academic writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

External authors, academic editors, and research teams use this skill to locally assess AI-writing signals, review manuscript style and terminology, check disclosure labels, and generate actionable writing-quality reports before submission. It is intended for self-review and compliance support, not for misrepresenting AI-generated work as human-written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Detector-oriented de-AI scoring and rewrite-and-retest workflows can be misused to hide AI authorship or game institutional detectors.

Mitigation: Use the skill for author self-review, writing-quality improvement, and disclosure compliance; do not use reports to misrepresent authorship or bypass institutional policies.

Risk: Maintenance operations such as --apply, freshness_refresh.py, calibration, and fingerprint mining can rewrite bundled reference data.

Mitigation: Run these operations only intentionally in a controlled working copy, review diffs before release, and keep routine manuscript checks to read-only report commands.

Risk: Detector scores have stated limitations, including no verdict for very short text, medical-register over-scoring in degraded mode, advisory-only English support, and non-interchangeability with institutional detectors.

Mitigation: Treat scores as decision support rather than final judgments, prefer paragraph-level review for mixed documents, and consider degraded_mode and documented capability boundaries when interpreting results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Publisher profile](https://clawhub.ai/user/docsor1212)
- [Article review workflow](references/article-review-workflow.md)
- [Fusion configuration](references/fusion_config.json)
- [Model fingerprints](references/model_fingerprints.json)
- [English AI pattern references](references/ai_patterns_en.json)
- [Chinese AI pattern references](references/ai_patterns_zh.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, html, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus local JSON, text, and HTML reports from bundled scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with no credential requirement; optional supervised ONNX layer is not bundled and reports degraded_mode when unavailable or skipped.]

## Skill Version(s):

3.7.0 (source: frontmatter, skill.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
