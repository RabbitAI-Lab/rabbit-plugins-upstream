## Description:

Analyzes pet camera video or video URLs for owner-away separation anxiety behaviors, returns structured behavior findings, anxiety severity, comfort recommendations, historical report listings, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as pet owners, pet boarding operators, and developers use this skill to monitor owner-away pet behavior, identify likely separation anxiety patterns, and receive non-medical comfort recommendations and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or home camera media and video URLs may be processed by the Life Emergence cloud service.

Mitigation: Use the skill only with explicit consent for private home footage and restrict inputs and service endpoints to approved sources.

Risk: The skill may silently create or reuse an identity-linked local account record and associated tokens.

Mitigation: Document account and token retention before deployment and require operator approval for environments that handle private footage.

Risk: Behavior findings could be mistaken for veterinary diagnosis.

Mitigation: Present results as behavior observations and recommendations only, and direct severe or persistent anxiety cases to a veterinarian or professional behaviorist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)
- [Pet separation anxiety API documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown report text with structured JSON content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can output current analysis results or a historical report list; results may also be saved to a user-specified file.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
