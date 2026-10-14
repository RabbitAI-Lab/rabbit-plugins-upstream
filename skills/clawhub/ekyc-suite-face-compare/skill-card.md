## Description:

Compares two consented face images through a configured eKYC backend and returns a structured similarity score for human-reviewed KYC checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

KYC teams and developers compare an authorized selfie with a reference face image during human-reviewed onboarding and identity checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images are sent to the configured eKYC backend for processing.

Mitigation: Process only authorized images and establish a retention and deletion policy with the backend before use.

Risk: A similarity score alone can lead to incorrect identity decisions.

Mitigation: Keep a human in the KYC review loop; do not use this skill for liveness, OCR, broad face recognition, or fully automated identity decisions.

## Reference(s):

- [eKYC Suite Face Compare on ClawHub](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)
- [eKYC Suite Face Compare MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-face-compare-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown instructions and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Similarity score on a 0–100 scale; report errors rather than guessing.]

## Skill Version(s):

1.0.20 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
