## Description:

Codegen (codegen.com). Use this skill for Codegen requests that search or read Codegen data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Codegen connector schemas and run read-only Codegen actions for agent runs, users, organizations, and repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users or agents to execute an unverified remote installer script for the oo CLI.

Mitigation: Review the setup path before installing; use a trusted OOMOL CLI distribution, prefer a manually downloaded or package-manager install, avoid elevated shells, and require explicit approval before running a remote installer.

## Reference(s):

- [Codegen homepage](https://codegen.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Codegen connector actions return structured JSON with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
