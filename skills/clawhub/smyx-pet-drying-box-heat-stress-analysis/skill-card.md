## Description:

Analyzes pet drying-box video files or video URLs through a remote service to detect early heat-stress signals such as open-mouth panting intensity, tongue color, and body movement frequency, then returns risk levels, intervention suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet grooming stores, pet hospitals, and operators of pet drying boxes use this skill to review drying-box video and receive structured heat-stress risk observations and safety-oriented intervention suggestions. It is for drying safety support and does not provide disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided videos or URLs are sent to a remote Life Emergence service for analysis.

Mitigation: Use only media that is approved for cloud processing, and avoid sensitive home, people, clinic, or customer footage unless remote processing is acceptable.

Risk: The skill can create or reuse a local backend identity and store reusable tokens in the workspace data directory.

Mitigation: Review the workspace data directory and token retention expectations before installation, and clear stored identity data when shared environments or account changes require it.

Risk: Historical report queries retrieve cloud-stored report records associated with the resolved backend identity.

Mitigation: Install and run the skill only where cloud report history access is expected, and limit use to operators authorized to view those reports.

Risk: Heat-stress output is safety guidance rather than veterinary diagnosis.

Mitigation: Treat high-risk or emergency observations as prompts to stop drying, cool and ventilate the pet, monitor closely, and escalate to veterinary care when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links, risk observations, and intervention guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a user-specified file and may return cloud-hosted report export links.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
