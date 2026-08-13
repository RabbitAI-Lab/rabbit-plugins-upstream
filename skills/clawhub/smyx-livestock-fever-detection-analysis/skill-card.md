## Description:

Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and farm operations teams use this skill to screen livestock and poultry images or videos for body-temperature anomalies, including fever, hypothermia, borderline cases, affected individual locations, and report links. Results are intended for early screening and monitoring, not for veterinary diagnosis or treatment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock images, videos, or supplied URLs are processed by the publisher's cloud service.

Mitigation: Use only inputs that are acceptable to send to the publisher-operated service, and avoid submitting unrelated sensitive content.

Risk: The skill silently creates or reuses an internal identity and stores returned session tokens or profile fields locally.

Mitigation: Review local data and token storage before and after use, and remove stored local data if the skill is no longer needed.

Risk: Historical cloud reports may be listed using the locally associated identity.

Mitigation: Confirm the local identity context before querying history and avoid shared execution environments when report separation matters.

Risk: Temperature-anomaly outputs can be mistaken for disease diagnosis.

Mitigation: Use results only for screening and monitoring, and rely on qualified veterinary and laboratory assessment for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include abnormal-temperature levels, individual locations, estimated temperature ranges, historical report listings, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; SKILL.md frontmatter says 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
