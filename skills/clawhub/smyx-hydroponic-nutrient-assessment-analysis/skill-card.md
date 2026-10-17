## Description:

Assesses hydroponic nutrient concentration from root and leaf images or video and suggests qualitative adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Hydroponic growers and developers use this skill to assess visible root and leaf stress, receive directional nutrient adjustments, and retrieve past assessment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or videos are uploaded to the publisher's remote service.

Mitigation: Get informed consent and review the content before submitting it.

Risk: The skill may create or reuse a local identity and store authentication tokens in workspace data.

Mitigation: Review account creation and access scope; protect and periodically clear stored credentials.

Risk: Cloud-stored report history may be queried under the reused identity.

Mitigation: Confirm the intended account and user authorization before retrieving reports.

Risk: Visual observations alone may misstate nutrient concentration.

Mitigation: Treat adjustments as directional guidance and verify consequential changes with independent measurements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [JSON or Markdown report with assessment, adjustment advice, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Qualitative assessment only; no EC or ppm measurements.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
