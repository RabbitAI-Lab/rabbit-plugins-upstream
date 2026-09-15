## Description:

Scan websites, GitHub repositories, and Claw Hub skills for practical security issues using a local quick website scan and CyberLens cloud analysis when connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shadoprizm](https://clawhub.ai/user/shadoprizm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers, security reviewers, and operators use this skill to assess websites, GitHub repositories, and Claw Hub skills before installation, deployment, or report sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential and network controls may be broader than users expect.

Mitigation: Review the skill before installing, especially on shared machines or hosts with access to private networks.

Risk: A saved CyberLens API key may persist on disk.

Mitigation: Use CYBERLENS_API_KEY from a managed environment variable when a persistent local key is not desired.

Risk: Changing CYBERLENS_API_BASE_URL can redirect scan traffic away from the default CyberLens API.

Mitigation: Keep the default endpoint unless the replacement HTTPS endpoint is fully trusted.

Risk: Scanning private or internal URLs can send intentional requests into sensitive network locations.

Mitigation: Scan private or internal targets only when the operator intends that network activity.

Risk: Direct skill download URLs from untrusted sources may point to risky packages.

Mitigation: Prefer server-resolved ClawHub skill pages and review direct download sources before scanning or installing.

## Reference(s):

- [CyberLens Security Scanner on ClawHub](https://clawhub.ai/shadoprizm/skills/cyberlens)
- [CyberLens homepage](https://cyberlensai.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Structured scan results, markdown reports, and PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns security scores, letter grades, findings, remediation advice, optional AI analysis, and PDF report paths.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence and skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
