## Description:

Helps an agent search and read Snipcart customer and order data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Snipcart connector schemas and perform read-only customer and completed-order lookups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may install the OOMOL CLI from a remote script.

Mitigation: Install the CLI manually from a trusted source and verify the installer where possible before using the skill.

Risk: Future connector artifacts may disclose write actions beyond the read-only customer and order lookups in this release.

Mitigation: Use this release only for read-only Snipcart customer and order lookups, and re-review future artifacts before enabling write actions.

## Reference(s):

- [ClawHub Snipcart skill page](https://clawhub.ai/oomol/skills/oo-snipcart)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Snipcart homepage](https://snipcart.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses for Snipcart customer and order reads.]

## Skill Version(s):

1.0.4 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
