## Description:

Scans local npm, Python, and Maven dependency files for supply-chain warning signs and generates a lightweight software bill of materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill before builds, releases, or CI runs to review dependency-confusion indicators, lockfile consistency, and unpinned dependencies, or to generate a lightweight SBOM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A requirements-file include can read dependency metadata outside the selected scan folder.

Mitigation: Scan untrusted repositories only in a sandbox or restricted workspace without access to private dependency files outside the repository.

Risk: Global installation can update more agent skill directories than intended.

Mitigation: Install with --agent or --dir to limit changes to the intended directory.

Risk: Offline dependency checks cannot confirm vulnerabilities or whether suspected package impersonation is real.

Mitigation: Treat findings as triage signals and verify them manually before taking action.

## Reference(s):

- [Detection rules and remediation guidance](references/rules.md)
- [Project homepage](https://github.com/YottaMeta/yotta-chain)
- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-chain)

## Skill Output:

**Output Type(s):** [Analysis, Files, Guidance]

**Output Format:** [Text, JSON, or CSV findings; CycloneDX 1.5 subset JSON for SBOM-lite]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity and fix hints; scan exit codes support CI gating. Findings require human review.]

## Skill Version(s):

0.1.5 (source: ClawHub release, SKILL.md frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
