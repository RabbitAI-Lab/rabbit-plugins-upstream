## Description:

Assesses hydroponic nutrient concentration from plant root and leaf images and provides a qualitative status with directional adjustment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External hydroponic growers use the skill to review root and leaf images for visible stress signs and receive a qualitative nutrient-concentration assessment and adjustment suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media may still be uploaded when using the documented no-analysis or export-only option.

Mitigation: Do not rely on export-only to prevent uploads; wait for the export-only issue to be corrected before using private media.

Risk: Account setup handles credentials unsafely, and remote account creation, charges, media retention, and token removal are not verified.

Mitigation: Wait for credential-handling fixes before using real credentials, and confirm account creation, possible charges, media retention, and token removal behavior.

Risk: The documented command needs correction.

Mitigation: Confirm the corrected command before running the skill.

## Reference(s):

- [Hydroponic assessment API reference](artifact/references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON, Markdown]

**Output Format:** [Structured analysis report with observations, qualitative nutrient status, adjustment guidance, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual assessment is qualitative and does not provide EC or ppm values.]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
