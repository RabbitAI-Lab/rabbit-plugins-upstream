## Description:

Analyzes a brand's presence and sentiment in LLM-generated industry recommendations, extracting mention context and competitor comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ljseeking](https://clawhub.ai/user/ljseeking)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing analysts use this skill to test whether a target brand appears in model-generated recommendations for a category, then review sentiment, mention context, competitor mentions, and a short GEO analysis report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand name, category keyword, and generated analysis text are sent to DeepSeek under the user's API key.

Mitigation: Use only when that data can be shared with DeepSeek under the applicable account terms and data handling requirements.

Risk: LLM-based GEO conclusions can be influenced by crafted inputs and should not be treated as definitive market evidence.

Mitigation: Treat the report as advisory and review important conclusions before using them for business decisions.

Risk: Dependencies are declared with minimum versions rather than pinned versions.

Mitigation: Use pinned dependencies or a reviewed lockfile before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ljseeking/skills/geo-analyzer)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [JSON containing structured brand mention data and a human-readable GEO analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DEEPSEEK_API_KEY and sends brand name, category keyword, and generated analysis text to the DeepSeek API.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
