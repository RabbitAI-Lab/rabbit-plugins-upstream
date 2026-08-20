## Description:

爆款拆解师 helps agents analyze Chinese viral marketing content across six viral-content elements and eleven dimensions, then produce scores, reusable content formulas, and differentiated creation suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, independent developers, and business teams use this skill to turn Chinese viral posts or competitor content into structured analysis, scoring, reusable templates, and originality-focused recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad command, file-write, and file-search permissions are requested for a skill whose primary behavior is text analysis.

Mitigation: Install or run the skill with minimum permissions; avoid enabling command execution, filesystem write access, or broad file search unless those capabilities are explicitly needed for a controlled workflow.

Risk: User-provided marketing content or competitor examples may contain sensitive or proprietary text.

Mitigation: Review inputs before use and remove confidential data, credentials, or private customer information from content submitted for analysis.

Risk: Generated scoring and content recommendations may be inaccurate or may encourage close imitation of source content.

Mitigation: Treat the report as drafting guidance, review factual claims and brand fit manually, and use the differentiated suggestions to avoid copying protected or proprietary expression.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/viral-decoder)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [analysis, json, markdown, guidance]

**Output Format:** [Structured JSON reports with Markdown-readable analysis sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include decode_result, score, formula, suggestions, warnings, and error fields; the skill is intended for Chinese text content and may truncate inputs above 10000 characters.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
