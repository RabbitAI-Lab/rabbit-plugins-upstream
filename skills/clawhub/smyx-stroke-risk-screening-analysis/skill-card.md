## Description:

Analyzes face images or videos with optional physiological indicators to generate stroke risk screening reports, early warnings, lifestyle suggestions, and medical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and health-oriented application developers use this skill to run cloud-backed stroke risk screening from face media and optional blood pressure, blood sugar, and blood lipid values. The skill returns structured risk information, health warnings, lifestyle suggestions, medical guidance, and historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles facial media and health indicators through cloud services.

Mitigation: Use only with clear privacy terms, informed consent, and production HTTPS-only service configuration.

Risk: The skill silently creates or reuses an internal identity and associates historical reports with that identity.

Mitigation: Confirm identity handling, retention, and access controls before deployment, and avoid exposing internal identity values to users.

Risk: The security evidence reports local token storage and shipped development HTTP configuration.

Mitigation: Require protected credential storage and verified production endpoints before normal use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports and JSON analysis output, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links returned by the cloud service; supports basic, standard, and json detail levels.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
