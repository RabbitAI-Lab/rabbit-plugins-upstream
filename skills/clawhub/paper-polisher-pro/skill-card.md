## Description:

Paper Polisher Pro audits academic writing for AI-writing signals, terminology issues, translation smell, metaphor quality, paragraph-level attribution, AIGC labeling, and journal precheck workflows using local scripts and bundled reference data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, editors, and developers use this skill to review Chinese and English academic drafts for AI-writing indicators, terminology consistency, compliance labels, and manuscript-quality issues before submission or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill explicitly supports reducing or hiding AI-writing signals in academic papers, which can conflict with journal, school, employer, or disclosure rules.

Mitigation: Use it for transparent quality review and compliant disclosure workflows, and do not use detector or de-AI outputs to misrepresent AI assistance.

Risk: AI-writing detector scores can be unreliable in known boundary cases such as short text, English text, mixed human-AI documents, and medical-register text without the optional supervised layer.

Mitigation: Treat scores as advisory, review degraded-mode notices, avoid verdicts on short passages, and prefer paragraph-level attribution plus human review for consequential decisions.

Risk: Some supervised-layer performance figures are author-side held-out measurements and the optional model files are not bundled.

Mitigation: Verify the active engine mode, run the bundled evaluation or self-check scripts in the target environment, and avoid substituting unverified model exports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article Review Workflow](references/article-review-workflow.md)
- [AI Pattern Library (English)](references/ai_patterns_en.json)
- [AI Pattern Library (Chinese)](references/ai_patterns_zh.json)
- [Model Fingerprints](references/model_fingerprints.json)
- [Fusion Configuration](references/fusion_config.json)
- [Release Evaluation Results](eval/results/v350_release.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands plus local JSON, HTML, and text reports from the bundled scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with no reported upload or credential requirement; detector scores are advisory and may include degraded-mode notices when optional model support is unavailable.]

## Skill Version(s):

3.5.0 (source: SKILL.md frontmatter, skill.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
