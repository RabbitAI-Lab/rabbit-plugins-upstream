## Description:

Analyzes hydroponic root and leaf images for visual signs of nutrient stress, then provides a qualitative assessment and directional dilution or nutrient-addition advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Hydroponic growers use this skill to assess nutrient concentration from plant root and leaf images and receive directional adjustment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account registration, credential use and storage, and external media processing are not clearly explained; some actions may occur without clear user notice.

Mitigation: Review and confirm these data practices before installation or use, and provide only credentials and media whose handling is acceptable.

Risk: The security review is partial because two referenced local files were missing.

Mitigation: Review the missing references and complete a security review of the full package before relying on the skill.

## Reference(s):

- [API interface reference](references/api_doc.md)
- [Analysis API response and error reference](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis, Guidance]

**Output Format:** [Text or JSON assessment report with qualitative findings and directional adjustment advice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Qualitative visual assessment; does not provide EC or ppm values; report links may be included.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
