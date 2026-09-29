## Description:

Verifies claims, statements, statistics, quotes, dates, and other information against reliable sources, then provides evidence-based verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[webguhui](https://clawhub.ai/user/webguhui)

### License/Terms of Use:


## Use Case:

External users, employees, and developers use this skill to fact-check concrete factual claims by identifying the claim, checking reliable sources, cross-referencing evidence, and returning a cited verdict with caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad verification requests can lead to incomplete or misleading conclusions when evidence is weak, stale, or ambiguous.

Mitigation: Use the skill for concrete factual claims, require cited sources, and preserve uncertainty with UNVERIFIABLE or clear caveats when evidence is insufficient.

Risk: Legal, medical, financial, or safety-critical claims may require domain-specific care beyond generic fact-checking.

Mitigation: Supplement the workflow with authoritative specialist sources and appropriate expert review before relying on conclusions in high-impact contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/webguhui/skills/fact-check)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with a claim, verdict, evidence list, and notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts use TRUE, MOSTLY TRUE, UNVERIFIABLE, MOSTLY FALSE, or FALSE and should include cited evidence and caveats.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
