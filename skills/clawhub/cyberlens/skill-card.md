## Description:

Scan websites, GitHub repositories, and Claw Hub skills for practical security issues using a local quick website scan and CyberLens cloud analysis when connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shadoprizm](https://clawhub.ai/user/shadoprizm)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security reviewers use this skill to assess websites, GitHub repositories, and Claw Hub skill packages before installing, shipping, or trusting them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make network requests and process untrusted skill archives from the agent host.

Mitigation: Install only if this access is acceptable, and avoid scanning internal, localhost, cloud-metadata, or private-network URLs.

Risk: Direct skill download URLs may be less trustworthy than Claw Hub skill pages.

Mitigation: Prefer Claw Hub URLs over arbitrary direct ZIP links when scanning skills.

Risk: A CyberLens API key may be stored locally when connecting an account.

Mitigation: Use CYBERLENS_API_KEY when you do not want the key stored in the skill configuration.

Risk: Generated reports may include CyberLens branding or context that is not appropriate for every audience.

Mitigation: Review generated reports before sharing them outside the agent session.

## Reference(s):

- [CyberLens Security Scanner on ClawHub](https://clawhub.ai/shadoprizm/skills/cyberlens)
- [CyberLens homepage](https://cyberlensai.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Structured scan results, Markdown security reports, and optional PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes security scores, letter grades, findings, and remediation guidance; PDF export requires reportlab.]

## Skill Version(s):

1.2.2 (source: server release metadata and skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
