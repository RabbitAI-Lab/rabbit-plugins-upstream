## Description:

Uses video and optional audio to classify a child's apparent emotional state and provide soothing prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and teachers can submit a child's video, optionally with audio, for an apparent-emotion summary and soothing prompts, or query earlier reports. Results are described as a communication aid, not a psychological diagnosis or clinical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks this release suspicious, citing account and credential handling beyond the stated analysis purpose and uncertainty about remote processing. The scan was partial, with a missing local reference and some behavior depending on unavailable components.

Mitigation: Avoid installation or sending children's media until the skill's behavior, dependencies, and receiving service have been verified; use non-sensitive test material during review.

Risk: Children's video and audio can expose sensitive personal information.

Mitigation: Obtain guardian consent before use and protect recordings; verify the receiving service's handling before uploading any footage.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Markdown]

**Output Format:** [Structured JSON reports, text summaries, or Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an emotion classification, intensity, alerts, soothing prompts, and report links. Results are informational and are not a psychological diagnosis.]

## Skill Version(s):

1.0.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
