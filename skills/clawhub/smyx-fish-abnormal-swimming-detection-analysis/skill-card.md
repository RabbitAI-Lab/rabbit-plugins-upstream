## Description:

Analyzes fixed-camera aquarium videos to flag fish swimming postures such as side-swimming or upside-down swimming and summarize observed abnormal duration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists, aquarium staff, and ornamental fish keepers can use the skill to review fixed-camera fish videos, summarize visible swimming-posture abnormalities, and retrieve analysis reports. Its results describe visual observations and should not be treated as a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says videos may still be uploaded when the no-analysis option is used, and remote retention and sharing terms were not verified.

Mitigation: Verify no-analysis behavior and the provider's retention and sharing controls before sending recordings; avoid uploading sensitive footage until those controls are confirmed.

Risk: The security review says account setup can send access keys as user identifiers, while account tokens persist locally.

Mitigation: Keep access keys separate from identity fields, restrict access to the local token store, and rotate any key already submitted as an account identifier.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis)
- [Skill API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis results and Markdown report summaries with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes observed posture events and abnormal-duration ratios; does not provide veterinary diagnoses.]

## Skill Version(s):

1.0.14 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
