## Description:

Yotta-chain is a local, offline supply-chain dependency validator that checks npm, Python, and Maven manifests and lockfiles for dependency confusion, lockfile consistency issues, missing lockfiles, unpinned versions, typosquatting, and SBOM-lite generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill before build, release, or CI to review local dependency files for supply-chain risk signals, verify manifest and lockfile consistency, and generate a lightweight SBOM for audit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local dependency manifests, lockfiles, and project registry settings as part of its analysis.

Mitigation: Run it only on authorized projects and expect it to inspect files such as package.json, lockfiles, requirements files, pyproject.toml, pom.xml, and project .npmrc settings.

Risk: Installer scripts are present in the release artifact.

Mitigation: Prefer targeted installation with --agent or --dir instead of global installation, and review the release before deployment.

Risk: Findings are supply-chain risk signals rather than proof of exploitability or CVE coverage.

Mitigation: Use the results for human review and follow up with dedicated package, registry, or CVE checks when a finding affects a release decision.

## Reference(s):

- [Yotta-chain homepage](https://github.com/YottaMeta/yotta-chain)
- [Detection rules reference](references/rules.md)
- [npm package @yottameta/yotta-chain](https://www.npmjs.com/package/@yottameta/yotta-chain)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Files, Configuration]

**Output Format:** [Markdown summaries with optional text, JSON, CSV, and CycloneDX 1.5 subset JSON outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local dependency manifests, lockfiles, and project registry configuration; scan findings require human review.]

## Skill Version(s):

0.1.4 (source: server release evidence, SKILL.md frontmatter, package.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
