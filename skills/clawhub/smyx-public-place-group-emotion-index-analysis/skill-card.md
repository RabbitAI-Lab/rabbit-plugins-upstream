## Description:

Analyzes group-level facial-expression trends in public-place camera footage and provides emotion summaries and operational guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Operators of malls, exhibition halls, scenic areas, and similar public venues use the skill to review aggregate emotion trends and receive service or safety guidance from camera footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports that camera footage may be sent for remote analysis without clear disclosure.

Mitigation: Use only after reviewing and accepting how footage is processed and disclosed; avoid submitting footage you are not comfortable sending for remote analysis.

Risk: The security assessment reports identity and credential handling beyond the stated group-emotion purpose.

Mitigation: Review the identity and credential handling before use, and do not provide sensitive credentials unless their handling is understood and trusted.

Risk: The security assessment says scanner analysis was partial because a referenced local path was missing.

Mitigation: Review the complete release behavior before deployment; the available scan does not establish complete behavior.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured group-emotion summaries and historical report listings, presented as JSON or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include aggregate emotion categories, an overall index, operational suggestions, and report links; detail varies by selected output level.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
