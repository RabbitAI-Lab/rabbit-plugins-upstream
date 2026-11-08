## Description:

Analyzes submitted pet stool images or videos and returns structured observations about color, shape, blood, or mucus without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caretakers can submit an image, video, or media URL from a pet's toileting area to get structured stool appearance observations and review past reports. The results are an observation aid and do not provide a veterinary diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images, videos, or media URLs may be processed by a remote service.

Mitigation: Submit only media and URLs you are comfortable sharing with that service.

Risk: The security review reports account and credential handling and access to historical records.

Mitigation: Review the service's account and credential practices, keep credentials private, and use only an account you trust.

Risk: The export-only option's behavior was not fully verified and may still submit media for remote analysis.

Mitigation: Do not rely on export-only to prevent remote submission; verify its behavior before using it with sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-stool-morphology-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis observations in JSON or text, with Markdown-formatted history lists and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observations cover stool color, shape, and visible blood or mucus; results are not a diagnosis.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
