## Description:

Analyzes cat climbing-frame or cat-tree video input through a configured external service to produce dwell-time, transition-count, and 2D activity heatmap observations without providing disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze cat-tree or climbing-frame videos, review structured activity observations, and retrieve prior analysis reports. It is intended for pet behavior monitoring and enrichment assessment, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, video URLs, and identity-linked request metadata may be sent to configured external services.

Mitigation: Review privacy disclosures and obtain appropriate user permission before submitting media or URLs for analysis.

Risk: The skill may silently create or reuse an identity and store tokens in a local SQLite database.

Mitigation: Run only in trusted workspaces, review local data handling before installation, and clear or rotate stored tokens when they are no longer needed.

Risk: Activity and wellbeing observations could be mistaken for medical advice.

Mitigation: Present results as behavior and enrichment observations only, and route veterinary diagnosis or treatment questions to qualified professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Climbing Frame API Documentation](artifact/references/api_doc.md)
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown-style status text with structured JSON analysis content, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the configured external analysis service and may include historical report listings.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
