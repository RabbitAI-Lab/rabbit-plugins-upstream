## Description:

Analyzes crop leaf images and videos for diseases specific to corn, potatoes, peanuts, and tomatoes, and retrieves past analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural advisers can submit crop leaf images or videos for preliminary disease identification and review their analysis history. Results should be checked against field observations and expert advice before making treatment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop images, videos, and report history are processed by an external service.

Mitigation: Use only if you trust the publisher and lifeemergence.com with submitted media and report data.

Risk: The skill silently manages account identity and persists account-linked tokens.

Mitigation: Review or disable identity and token persistence before use in sensitive environments; run in a protected workspace.

Risk: A risky Python import setup can load code from shared writable locations.

Mitigation: Avoid shared writable install paths and review the installation before executing it.

Risk: Image-based disease identification may be incorrect or incomplete.

Mitigation: Treat results as preliminary and confirm diagnoses with field observations and an agricultural expert.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)
- [Crop disease analysis API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis reports; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes disease labels, confidence scores, symptom descriptions, and report links when available.]

## Skill Version(s):

1.0.14 (source: ClawHub release; bundled frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
