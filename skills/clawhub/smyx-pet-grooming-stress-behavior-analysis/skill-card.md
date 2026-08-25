## Description:

Analyzes pet grooming videos or video URLs for stress behaviors such as struggling, panting, and tail tucking, then returns a structured stress-level report to help grooming or veterinary staff decide when to pause or intervene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet care staff, groomers, and veterinary clinic teams can use the skill to submit grooming-session media and receive behavior observations, stress-level grading, and report links. It is intended as behavioral observation support, not disease diagnosis or behavior-correction advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, video URLs, and report data may be sent to vendor remote services.

Mitigation: Use only with media approved for vendor processing, and avoid submitting sensitive or restricted grooming footage.

Risk: The skill can silently create or reuse an identity and may store authentication tokens locally.

Mitigation: Review workspace identity and token state before installation, avoid workspaces containing sensitive smyx-api-key.txt values unless intended, and clear local credentials when decommissioning.

Risk: Stress-level output could be mistaken for medical diagnosis or prescriptive behavior correction.

Mitigation: Present results as behavioral observations only, and have qualified staff review severe stress indicators before deciding whether to pause grooming or seek veterinary input.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and JSON analysis results from remote API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and historical report tables; analysis depends on remote service availability and submitted media quality.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
