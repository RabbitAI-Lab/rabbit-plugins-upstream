## Description:

Identifies diseases affecting economic crops such as corn, potatoes, peanuts, and tomatoes from leaf images or videos and returns structured findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and other agricultural users can submit crop-leaf images or videos for preliminary visual disease identification, or request their prior analysis reports. The results describe likely disease findings and are not treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the release suspicious with high confidence because reported account, identity, video-analysis, and report-management behavior does not clearly match its crop-disease purpose.

Mitigation: Before installing, clarify the skill's purpose and verify the provider and identity-handling flow against trusted information.

Risk: Use involves sending crop images or videos for analysis and accessing stored reports, while the security guidance says these data and access details need clarification.

Mitigation: Confirm what media and identifiers are sent, how reports are protected and accessed, and avoid uploading sensitive material until those details are clear.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured disease analysis report and report-history records, with report links or Markdown tables where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include disease type, confidence, symptom description, and report links; does not provide treatment advice.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
