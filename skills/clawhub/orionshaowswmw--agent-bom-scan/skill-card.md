## Description:

Deep vulnerability scanning for software bills of materials that detects CVEs, analyzes dependencies, assesses supply chain risks, and generates security reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to scan authorized projects or SBOMs for vulnerable dependencies, CVE matches, and supply chain risk signals before acting on the generated findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's privacy and network behavior are inconsistent in the evidence.

Mitigation: Verify whether the selected workflow is offline or network-assisted before use.

Risk: Dependency names or hashes may be sent to public vulnerability databases.

Mitigation: Install and run the skill only when that data sharing is acceptable for the assessed project.

Risk: Generated scan reports may expose sensitive dependency details.

Mitigation: Scope scans to projects you are authorized to assess and store reports securely.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/agent-bom-scan)
- [ClawHub publisher profile](https://clawhub.ai/user/orionshaowswmw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and security report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan reports may include sensitive dependency details and should be reviewed before relying on them.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
