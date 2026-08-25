## Description:

AI-powered plant root health analysis from transparent pots or smart seedling boxes that evaluates visible root color, hair density, branching, and root rot signs, then returns a health score, vitality grade, care guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and plant-care operators use this skill to analyze transparent-pot, seedling-box, hydroponic, or plant-factory root images and videos for early signs of weak roots or root rot. It supports structured health reporting and history lookup for care adjustment, not definitive agronomic diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected plant images, videos, or supplied URLs may be uploaded to remote API endpoints.

Mitigation: Review endpoint configuration and obtain user or organizational approval before running analysis on sensitive media.

Risk: The skill can silently create or reuse a cloud identity and store service tokens locally.

Mitigation: Run in an isolated workspace, restrict access to local data directories, and rotate or remove generated tokens after evaluation.

Risk: Default development or private HTTP endpoints may be present in shipped configuration.

Mitigation: Replace defaults with approved production endpoints and block private or unencrypted endpoints unless explicitly authorized.

Risk: Historical report lookup can be triggered by matching phrases and may retrieve prior cloud reports without a separate confirmation.

Mitigation: Limit use to trusted sessions and verify that report access policies match the intended user identity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-root-health-transparent-pot-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a root health score from 0 to 100, vitality grade, care recommendations, historical report table, and report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
