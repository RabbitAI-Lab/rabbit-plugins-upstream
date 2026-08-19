## Description:

Identifies common abnormal pet behaviors such as scratching, biting, destructive chewing, jumping, digging, chasing, and separation anxiety, helping owners understand their pet's habits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents assisting them use this skill to submit pet monitoring videos or video URLs for behavior recognition, receive structured behavior reports, and retrieve cloud report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or home video data and report-history queries are sent to the provider API.

Mitigation: Use only with user consent and after reviewing the provider's data handling, retention, and endpoint security commitments.

Risk: The skill silently creates or reuses an internal identity and stores authentication tokens in the workspace data database.

Mitigation: Approve installation only after the publisher clarifies identity creation, token retention, and token removal practices; restrict access to workspace data.

Risk: Behavior analysis output may be mistaken for health diagnosis or professional pet care advice.

Mitigation: Treat reports as informational behavior references and consult a qualified pet trainer or veterinarian for corrective action or medical concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Interface Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown text or JSON, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local mp4, avi, or mov videos up to 10 MB or public video URLs; can query cloud report history through the provider API.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
