## Description:

Analyzes dog stool images or videos from local files or URLs for color, consistency, and visible abnormalities, producing observational reports rather than diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care teams use the skill to review dog stool imagery from toilets or outdoor paths, identify observable changes, and retrieve prior reports. Results support monitoring, not veterinary diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-health images or videos are sent to a remote service for analysis.

Mitigation: Use only non-sensitive media and confirm that remote processing is acceptable before uploading.

Risk: The skill can silently create or reuse an identity, register or log in remotely, and retrieve identity-linked cloud report history.

Mitigation: Use an account and identity you control, and review access to stored reports before running the skill.

Risk: Local tokens and a generated user record may persist in the workspace data directory.

Mitigation: Protect the workspace data directory and remove saved credentials and records when no longer needed.

## Reference(s):

- [Pet stool analysis API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-stool-morphology-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured observations and optional report links or saved results; not a diagnosis.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
