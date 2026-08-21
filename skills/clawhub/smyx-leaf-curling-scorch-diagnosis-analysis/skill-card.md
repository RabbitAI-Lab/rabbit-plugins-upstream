## Description:

Analyzes plant leaf images, videos, or URLs to detect leaf curling direction and margin scorch patterns, rank likely causes such as drought or disease, and provide diagnostic guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farmers, agronomists, and agriculture IoT developers use this skill to analyze leaf imagery from fields, greenhouses, orchards, UAVs, or agricultural cameras and receive structured guidance on likely causes of leaf curling and margin scorch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media, private URLs, or related inputs may be processed by the LifeEmergence/SMYX backend.

Mitigation: Avoid sensitive images, videos, and URLs unless the publisher clarifies endpoint configuration, retention, and data handling.

Risk: The skill can create or reuse a local identity and store backend tokens in a workspace SQLite database.

Mitigation: Run in an isolated workspace, avoid shared workspaces, and review or remove local identity and token data after use.

Risk: Cloud report history is retrieved under the resolved local identity.

Mitigation: Use history queries only when account isolation and report access behavior are acceptable for the deployment.

Risk: Plant diagnosis results can be incomplete or mistaken because visual symptoms from drought, disease, chemical damage, and fertilizer burn may overlap.

Mitigation: Treat outputs as screening guidance and confirm serious disease or crop-loss cases with field inspection or professional plant-health advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-leaf-curling-scorch-diagnosis-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with structured diagnostic report content, JSON-style fields, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report text to a user-provided output file; history queries return cloud report lists associated with the resolved local identity.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
