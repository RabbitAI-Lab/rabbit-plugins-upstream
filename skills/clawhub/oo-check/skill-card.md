## Description:

Use this skill to inspect Check action schemas and run Check tax-agency lookup, agency listing, and US address-validation actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to work with Check data via the OOMOL `oo` CLI. It supports reading Check tax agencies, listing agencies with filters and pagination, and validating US addresses after inspecting each action's live schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup section includes remote installer pipeline commands that execute downloaded code without integrity verification.

Mitigation: Install the oo CLI only from trusted OOMOL sources and prefer official installation documentation, a package manager, or a downloaded installer whose source and integrity can be verified before execution.

Risk: The skill depends on an OOMOL-connected account and the oo CLI for Check access.

Mitigation: Use the skill only when the user trusts OOMOL, has intentionally connected Check, and accepts the oo CLI dependency.

## Reference(s):

- [Check homepage](https://www.checkhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-check)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses `oo connector schema` before constructing action payloads and `oo connector run --json` for execution responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
