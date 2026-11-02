## Description:

Analyzes dog toilet or outdoor walking images and video for stool color, form, and visible blood or mucus, returning structured observations without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care teams use the skill to review stool appearance from images or video and consult structured observation reports or report history. The observations support monitoring and do not diagnose disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and URLs are sent to Life Emergence services, while account isolation and report deletion are not explained.

Mitigation: Avoid sensitive footage and shared workspaces until the publisher explains account isolation and report deletion.

Risk: Stored tokens and account identifiers may not be adequately separated or protected.

Mitigation: Ask the publisher to separate API secrets from account identifiers and protect stored tokens before installation.

Risk: The documented export-only mode does not work as intended.

Mitigation: Ask the publisher to fix export-only mode before relying on it.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-pet-stool-morphology-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis results, Text, Markdown, JSON]

**Output Format:** [Structured stool observation report in text, Markdown, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports describe visible stool features and may include abnormal observation flags, suggestions, and report links; they are not diagnoses.]

## Skill Version(s):

1.0.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
