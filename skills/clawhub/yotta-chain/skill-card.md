## Description:

元链 yotta-chain is a local, offline supply-chain dependency validator that parses npm, Python, and Maven manifests and lockfiles to flag dependency-confusion, lockfile consistency, missing-lockfile, unpinned-version, and typosquatting signals and generate SBOM-lite output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill before build, release, or CI to review local dependency manifests and lockfiles for supply-chain risk signals, verify lockfile consistency, assess dependency-confusion exposure, and generate SBOM-lite records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can persist files into agent skill directories.

Mitigation: Install from a trusted, pinned source when possible and prefer --agent or --dir for the single intended agent directory.

Risk: Scan reports may expose local dependency metadata and registry URLs, especially when written to an output file.

Mitigation: Treat generated reports as project-sensitive artifacts and store or share them only in approved locations.

Risk: The skill reports supply-chain risk signals that may require confirmation outside the local files.

Mitigation: Have a human review findings before acting on dependency-confusion, typosquatting, or lockfile-consistency results.

## Reference(s):

- [yotta-chain rules reference](references/rules.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-chain)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-chain)

## Skill Output:

**Output Type(s):** [text, markdown, json, csv, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; scan and SBOM commands can produce text, JSON, CSV, or CycloneDX-style JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are local risk signals for human review; output may include local dependency metadata and registry URLs.]

## Skill Version(s):

0.1.3 (source: server release metadata; artifact files declare 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
