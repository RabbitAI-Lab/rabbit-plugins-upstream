## Description:

Deep vulnerability scanning for software bills of materials, including CVE detection, dependency analysis, supply-chain risk assessment, and security report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to inspect project dependency manifests or software bills of materials for known vulnerabilities and supply-chain risks, then produce actionable scan findings or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy expectations may be unclear because SKILL.md describes offline-only scanning while README and security evidence note possible network CVE or OSV database lookups.

Mitigation: Review the scanner configuration before use and assume dependency names or hashes may be sent to public vulnerability services when network-backed lookups are enabled.

Risk: Scan reports can reveal sensitive dependency and vulnerability details about a project.

Mitigation: Store generated reports securely and limit report sharing to the teams that need the vulnerability information.

Risk: The release evidence describes this as a lightweight scanner-description skill rather than a complete scanner implementation.

Mitigation: Validate any proposed scanner commands, installed tools, and findings before relying on the results for security decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/agent-bom-scan)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with scan findings and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize CVE, dependency, and supply-chain risk information from local manifests and vulnerability database lookups.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
