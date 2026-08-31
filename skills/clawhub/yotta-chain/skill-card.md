## Description:

Yotta-chain is a local, offline supply-chain dependency validation skill that scans npm, Python, and Maven manifests and lockfiles for dependency confusion, lockfile inconsistencies, missing lockfiles, unpinned versions, typosquatting signals, and SBOM-lite generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill before build, release, or CI workflows to check project dependencies for supply-chain risk signals, compare lockfiles with manifests, assess dependency-confusion exposure, and generate SBOM-lite output for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers can persistently copy the skill into multiple agent environments without confirmation.

Mitigation: Review the installer before use, pass an explicit --agent value or a verified --dir for the intended skills directory, avoid global installation unless intended, and manually remove unintended copies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-chain)
- [Detection rules reference](references/rules.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-chain)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, plus scanner output in text, JSON, CSV, or SBOM-lite JSON when invoked.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are local review signals and may require human verification.]

## Skill Version(s):

0.1.2 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
