## Description:

eKYC Suite Face Compare compares two consented face images for KYC onboarding or selfie verification and returns a structured 0-100 similarity score through a configured eKYC Suite Cloud backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

External agent developers, fintech onboarding teams, compliance engineers, and identity-verification builders use this skill to compare a consented selfie with a reference face image during human-reviewed KYC or eKYC onboarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive face images and sends them to the operator-configured HTTPS eKYC backend.

Mitigation: Install and run it only with authorization to process the submitted images, an appropriate retention policy, and a trusted HTTPS backend configured.

Risk: A face-comparison score can be overused as standalone identity proof.

Mitigation: Treat the score as one review signal and apply business thresholds, retry rules, and human review appropriate to the deployment.

Risk: Privacy guidance may be incomplete if reviewers rely only on the short Chinese README.

Mitigation: Use the main documentation and server security guidance when reviewing consent, data flow, retention, and deployment requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)
- [npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-face-compare-mcp)
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [eKYC Suite AI Guardian](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [eKYC Suite Document OCR](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [JSON response from the face comparison command, with human-facing Markdown guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns similarity scoring and backend response metadata from the configured deployment; local image files are encoded before transmission.]

## Skill Version(s):

1.0.18 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
