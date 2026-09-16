## Description:

This skill lets agents search and read Slickdeals data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to search and read Slickdeals data through an OOMOL-connected Slickdeals account, including deals, coupons, articles, stores, brands, categories, and supported deal or coupon types.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may run a remote installer and create local OOMOL authentication state.

Mitigation: Install only if OOMOL is an acceptable connector provider, and inspect or verify the installer before execution.

## Reference(s):

- [Slickdeals homepage](https://slickdeals.net/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-slickdeals)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Slickdeals connector requests.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
