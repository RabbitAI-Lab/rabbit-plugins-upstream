## Description:

Creates a local adult health archive from user-provided exam or hospitalization reports, with paid access to advanced formatting and cross-year trend comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[williswu](https://clawhub.ai/user/williswu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to structure their own adult health records and compare trends across reports after consent and payment. It is for record organization and general health information, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backend and deployment materials conflict with the local-only privacy promise for sensitive health data.

Mitigation: Review backend behavior before use, ensure agents never send health reports to the payment endpoint, align deployment docs with the privacy claim, correct the SKILL_ID mismatch, and harden private-key handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/williswu/skills/personal-health-archive-trend-paid)
- [Server-resolved GitHub source](https://github.com/williswu/personal-health-archive-trend-paid)
- [Publisher profile](https://clawhub.ai/user/williswu)
- [Payment verification endpoint](https://mch.1001058.xyz/api/adult/resource)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown health archive with abnormal flags and trend comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill claims local-only handling for health reports; security evidence flags privacy-consistency issues that require review before deployment.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
