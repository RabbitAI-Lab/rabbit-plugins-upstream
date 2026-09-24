## Description:

Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, veterinarians, and developers use this skill to analyze thermal or visible-light livestock and poultry images or videos for early fever/hypothermia screening and historical report review. It supports screening workflows only and does not provide disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security verdict is suspicious because the skill silently manages identities and tokens and defaults to insecure plaintext service endpoints.

Mitigation: Review carefully before installing, run in a contained environment, require HTTPS endpoints, and confirm identity creation, token storage, and retention behavior before use.

Risk: The skill sends farm media to cloud analysis services and can query historical reports.

Mitigation: Avoid submitting sensitive farm media until data handling is approved, and limit report access to the intended authenticated identity.

Risk: The skill produces screening warnings that could be mistaken for veterinary diagnosis.

Mitigation: Use results only as body-temperature screening support and require professional veterinary and laboratory confirmation for disease diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown status text and tables, with JSON-oriented analysis details and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include abnormality level, individual locations, estimated temperature ranges, affected-individual list, analysis time, and report links.]

## Skill Version(s):

1.0.11 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
