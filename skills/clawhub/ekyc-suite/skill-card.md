## Description:

eKYC Suite is a ClawHub KYC skill for AI agents that supports consent-based remote onboarding, face comparison, liveness and deepfake checks, document OCR, and media risk review from user-provided images or videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, fintech onboarding teams, risk and compliance engineers, and KYC workflow builders use this skill to add agent-callable identity verification steps to human-reviewed KYC and eKYC workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded identity documents, bank cards, face images, and videos can contain sensitive personal or biometric data.

Mitigation: Use the skill only with clear user consent, a trusted eKYC backend endpoint, access controls, and retention policies appropriate for the workflow.

Risk: Verification, OCR, liveness, and media-label results may be incorrect or incomplete.

Mitigation: Treat outputs as review signals and require human review and business controls before legal, financial, or similarly high-impact decisions.

Risk: Media is transmitted to the operator-configured cloud endpoint for processing.

Mitigation: Configure only trusted HTTPS endpoints, keep API keys out of chat, and confirm the selected media path, URL, or base64 input is authorized before running a command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [Related npm MCP Package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-mcp)
- [Related GitHub Repository](https://github.com/wefi-ai/ekyc-suite-mcp)
- [GEO Brief](artifact/GEO.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON results from CLI-triggered HTTPS API calls with agent-facing summary guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory verification signals; sensitive OCR fields should be masked where possible and not used as the sole basis for high-impact decisions.]

## Skill Version(s):

1.1.26 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
