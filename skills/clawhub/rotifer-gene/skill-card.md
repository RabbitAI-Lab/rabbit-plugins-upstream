## Description:

Guides developers through building, auditing, and upgrading Rotifer Genes, including phenotype schemas, fidelity changes, testing, and publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers use this reference to create and test Rotifer Genes, audit them before publishing, and migrate Genes between Wrapped, Hybrid, and Native fidelity levels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The manuals contain a workflow ordering inconsistency around final artifact review.

Mitigation: Follow the security guidance and audit final artifacts before approving publication.

Risk: Bulk manifest edits can affect unintended paths.

Mitigation: Preview edits, back up manifests, and verify target paths before applying changes.

Risk: Hybrid examples send input text to the selected provider.

Mitigation: Use appropriate data and credentials when running those examples.

Risk: CLI setup contacts package registries, and this review does not verify a separately downloaded CLI.

Mitigation: Keep the CLI version pinned and verify the package before use; use a lockfile and npm ci in automation.

## Reference(s):

- [Rotifer Protocol documentation](https://rotifer.dev/docs)
- [Rotifer Protocol specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground repository](https://github.com/rotifer-protocol/rotifer-playground)

## Skill Output:

**Output Type(s):** [Markdown guidance, Shell commands, Configuration examples]

**Output Format:** [Markdown reference with tables and inline shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Three task-specific manuals for development, security audits, and fidelity migration]

## Skill Version(s):

1.0.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
