## Description:

Checks vulnerabilities in a specified package and version, repository, container image, or SBOM, and can inspect a specified CVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use the skill to check a requested software package, repository, container image, SBOM, or CVE for known vulnerabilities. Specify the target before scanning and use offline mode when online sharing of private package identifiers is not authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online vulnerability checks send package identifiers, versions, and advisory IDs to external providers, which may expose private package information.

Mitigation: Obtain authorization before querying private identifiers; use offline mode when external sharing is not authorized and report resulting coverage gaps.

Risk: The external scanner's implementation and redaction behavior are not verified by the supplied evidence.

Mitigation: Pin and review the external scanner version before use; do not assume sensitive configuration values are fully redacted.

## Reference(s):

- [ClawHub release](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Agent BOM project information](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Text, Markdown, or JSON vulnerability-scan summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and coverage depend on the selected target, data sources, and whether online checks are enabled.]

## Skill Version(s):

0.110.0 (source: server-resolved release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
