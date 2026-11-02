## Description:

Locally checks npm, Python, and Maven dependency manifests and lockfiles for supply-chain risk signals, and can generate an SBOM-lite inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use the skill to review local project dependencies before a build, release, or CI run, check whether lockfiles match manifests, and produce an SBOM-lite inventory for audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project files can cause reads outside the selected folder.

Mitigation: Until include paths are confined, scan trusted projects in an isolated environment without access to personal secrets.

Risk: Reports can expose secrets.

Mitigation: Keep credentials out of registry URLs and .npmrc files, and inspect reports before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-chain)
- [Project homepage](https://github.com/YottaMeta/yotta-chain)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Text findings or JSON scan output; SBOM-lite as CycloneDX 1.5 subset JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, explanations, and remediation hints.]

## Skill Version(s):

0.1.6 (source: release evidence, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
