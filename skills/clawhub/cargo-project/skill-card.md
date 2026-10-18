## Description:

Helps developers define a Cargo workspace in TypeScript and plan or deploy its resources with the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scaffold, review, and manage version-controlled Cargo workspace resources across environments or from CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deploy, destroy, or pruning can change or remove live workspace resources.

Mitigation: Review each project plan before deploying; avoid destroy, --prune, --force, or CI --yes unless the scope is clear.

Risk: Credentials can be exposed if placed in tracked configuration.

Mitigation: Store tokens and other sensitive values as secrets rather than in committed files.

Risk: Unpinned npm or npx installs can fetch unexpected tooling versions.

Mitigation: Pin package versions where possible and review tooling changes before deployment.

## Reference(s):

- [Cargo Project on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-project)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Deploy and state guide](artifact/guides/deploy-and-state.md)
- [Project command reference](artifact/references/commands.md)
- [CI deployment recipe](artifact/recipes/deploy-from-ci.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with TypeScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes resource definitions and deployment plans for user review.]

## Skill Version(s):

3.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
