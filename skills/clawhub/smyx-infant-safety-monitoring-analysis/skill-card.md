## Description:

Monitors infant behavior via visual AI, automatically identifying high-risk actions like rolling over, mouth/nose obstruction, climbing, or falling from bed, and triggers instant safety warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users can analyze infant activity videos or video URLs for potential safety hazards and receive structured monitoring results, warnings, care suggestions, and report links. The skill can also retrieve account-linked historical infant safety analysis reports from the remote service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child or home media may be uploaded or shared with a remote analysis service.

Mitigation: Obtain clear user consent before processing media, disclose the remote service dependency, and avoid submitting content that users are not authorized to share.

Risk: The skill may silently create or reuse an internal user identity and retrieve account-linked history.

Mitigation: Require explicit user intent before history lookup and clearly disclose identity association behavior before deployment.

Risk: Authentication material may be stored locally or transmitted with weak disclosure and insecure defaults.

Mitigation: Use HTTPS-only production endpoints, protect or avoid local token storage, and review token lifecycle handling before installation.

Risk: Infant safety analysis may be incomplete or affected by video quality and should not replace active supervision.

Mitigation: Present results as advisory only and remind users to maintain real-time caregiver supervision and seek professional guidance when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant Safety Monitoring Analysis API documentation](references/api_doc.md)
- [smyx_analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured JSON or Markdown-formatted text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include safety warnings, care suggestions, historical report records, and exported report image URLs.]

## Skill Version(s):

1.0.14 (source: server release evidence; artifact frontmatter reports 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
