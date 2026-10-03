## Description:

Analyzes plant leaf images or videos for disease symptoms and returns a likely diagnosis, confidence information, and general care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, gardeners, and agricultural teams use the skill to assess plant leaf disease symptoms from images or video and review prior analysis reports. Its findings are preliminary guidance rather than a definitive diagnosis or chemical treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, video, or supplied URLs may be sent to a remote analysis service, including private media or internal URLs.

Mitigation: Use only media and URLs approved for remote processing; confirm the publisher's data handling before sharing private content.

Risk: The skill may silently create or reuse an internal identity and store authentication tokens in a local SQLite database.

Mitigation: Review account linkage and protect local token storage before installation or use.

Risk: Cloud report-history queries may reveal reports linked to the internally managed identity.

Mitigation: Use history queries only in an appropriate account context and review report access before sharing results.

## Reference(s):

- [Plant leaf analysis API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include disease likelihood, confidence, general recommendations, and report links; results can be saved as JSON.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
