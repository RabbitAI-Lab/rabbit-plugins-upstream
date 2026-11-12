## Description:

Provides Rotifer Gene guidance for building and testing Genes, auditing them before publication, and migrating fidelity between Wrapped, Hybrid, and Native.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers use this skill to create, test, audit, publish, and upgrade Rotifer Protocol Genes with the Rotifer CLI. Its procedures apply to Rotifer Genes and their phenotype schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports out-of-scope behavior and an incomplete review, including an external request and a migration example.

Mitigation: Clarify those behaviors and review the partially inspected material before installing or using the skill.

Risk: The audit module includes instructions for rewriting manifests in bulk, which could affect multiple Gene files.

Mitigation: Review the target set and proposed changes, and keep a recoverable copy before applying a bulk rewrite.

Risk: The reported publish-before-audit sequence could leave a Gene published before its checks are complete.

Mitigation: Complete the four-layer audit before publishing, then verify the published records as the audit guidance describes.

## Reference(s):

- [Rotifer Protocol Documentation](https://rotifer.dev/docs)
- [Rotifer Protocol Specification](https://github.com/rotifer-protocol/rotifer-spec)
- [Rotifer Playground CLI Repository (declared in package metadata)](https://github.com/rotifer-protocol/rotifer-playground)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with shell commands and JSON or TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference material is organized into development, security audit, and migration modules.]

## Skill Version(s):

1.0.7 (source: frontmatter; server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
