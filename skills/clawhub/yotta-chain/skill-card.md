## Description:

元链 yotta-chain is a local, offline supply-chain dependency validation skill for agents that parses npm, Python, and Maven manifests and lockfiles to flag dependency confusion, lockfile inconsistency, missing lockfiles, unpinned versions, typosquatting, and to generate SBOM-lite output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill before build, release, or CI to inspect authorized local projects for dependency supply-chain signals, verify lockfiles against manifests, assess dependency-confusion exposure, and produce SBOM-lite records for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads dependency manifests, lockfiles, and package metadata from the project path supplied by the user.

Mitigation: Run it only on projects and assets the user is authorized to inspect, and avoid pointing it at unrelated personal or sensitive directories.

Risk: Generated findings are heuristic review signals and can be false positives or incomplete because the skill does not perform online registry or CVE lookups.

Mitigation: Have a human reviewer confirm flagged package names, registries, lockfile changes, and remediation before treating a finding as confirmed compromise.

Risk: Installer scripts copy the skill into selected agent skill directories, including global locations when requested.

Mitigation: Install only into intended agent environments and review the target directory before using global or multi-agent installation modes.

## Reference(s):

- [Yotta-chain rule reference](references/rules.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-chain)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-chain)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; scan output can be text, JSON, or CSV, and SBOM output can be CycloneDX 1.5 subset JSON or text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, explanation, and fix hints; scan exit codes support CI gating.]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
