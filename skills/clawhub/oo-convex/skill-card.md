## Description:

Operate Convex through an OOMOL-connected account using the oo CLI to inspect schemas and run Convex project, deployment, query, mutation, action, domain, and deploy-key operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage Convex projects and deployments, inspect live action schemas, and run Convex queries, mutations, actions, functions, and batch operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions execute remote installer scripts directly.

Mitigation: Review the installer source first and prefer a verified, version-pinned, or package-manager installation method when available.

Risk: The skill can perform high-impact Convex mutations and deletions.

Mitigation: Require explicit user confirmation for every write or destructive action, and verify the live schema, exact target, and payload before execution.

## Reference(s):

- [Convex homepage](https://www.convex.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-convex)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from oo CLI Convex connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
