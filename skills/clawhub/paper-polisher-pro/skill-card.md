## Description:

Paper Polisher Pro helps agents run local academic-writing self-checks, AI-risk analysis, terminology review, translation-smell checks, paragraph attribution, journal prechecks, and AIGC disclosure-label checks for Chinese and English manuscripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and academic authors use this skill to review manuscripts locally for writing quality, terminology consistency, AI-risk signals, paragraph-level attribution, and disclosure-label readiness before publication or submission. Its detector outputs are advisory and should be reviewed manually against institutional AI-use policies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-risk scores and fingerprint attribution can be mistaken for authoritative publication or compliance decisions.

Mitigation: Treat reports as advisory, review outputs manually, and follow the relevant institution or publisher disclosure policy.

Risk: The tool includes detector-evasion-adjacent functionality and could be misused to hide AI involvement.

Mitigation: Use it for author self-review, writing quality, and disclosure-aware revision rather than misrepresentation of AI-generated or AI-assisted work.

Risk: The optional supervised ONNX layer is not bundled and may affect results if substituted or sourced incorrectly.

Mitigation: Verify the optional model's provenance before placing it in cache and do not substitute unverified model exports.

Risk: Short text, English text, medical register, colloquial prose, and mixed human/AI documents have documented scoring limitations.

Mitigation: Use paragraph-level reports, heed degraded-mode and register warnings, and avoid relying on document-level scores where the skill discloses limitations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-polisher-pro)
- [Article Review Workflow](references/article-review-workflow.md)
- [Fusion Configuration](references/fusion_config.json)
- [Model Fingerprints](references/model_fingerprints.json)
- [English AI Patterns](references/ai_patterns_en.json)
- [Chinese AI Patterns](references/ai_patterns_zh.json)
- [Chinese Sentence Patterns](references/sentence_patterns_zh.json)
- [General Synonyms](references/synonyms_general.json)
- [Chinese Token Spectrum](references/token_spectrum_zh.json)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with optional JSON, text, and HTML reports from bundled local scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are local and advisory; some scripts can write report files to user-specified paths.]

## Skill Version(s):

3.8.0 (source: evidence.release.version, artifact/skill.json, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
