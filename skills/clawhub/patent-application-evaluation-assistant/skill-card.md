## Description:

Assists corporate IPR teams, patent engineers, and patent attorneys with preliminary patent application evaluations by checking disclosure completeness, searching patent and non-patent references, assessing China, U.S., and European grant feasibility, and producing ratings, score rationales, risks, and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Corporate IPR teams, patent engineers, and patent attorneys use this agent to triage invention disclosures before filing. It structures technical materials, requests missing information, performs patentability-oriented searches, and prepares a preliminary A/B/C application rating with jurisdiction-specific risk analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may process confidential invention disclosures, trade secrets, personal data, export-controlled details, or business strategy.

Mitigation: Review deployment before use and redact sensitive material that is not required for the evaluation.

Risk: Patent and web-search workflows may send invention details to external search services.

Mitigation: Confirm that PatSnap and web-search use is approved for the specific materials before running searches.

Risk: Optional HTML reports can preserve sensitive evaluation content in the local session.

Mitigation: Export HTML reports only when local session persistence is acceptable and handle exported files under the organization's confidentiality controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-application-evaluation-assistant)
- [Opening Message](references/opening-message.md)
- [User Input Template](references/user-input-template.md)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code]

**Output Format:** [Markdown analysis with structured tables, cited reference links, recommendations, and optional self-contained HTML export code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs preliminary patent evaluation guidance, not formal legal advice or a substitute for patent counsel review.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
