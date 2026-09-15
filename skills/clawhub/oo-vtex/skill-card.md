## Description:

VTEX helps agents search and read VTEX catalog data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect VTEX storefront and catalog data, including product lookup, brand lists, category trees, product and SKU IDs, and product search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance can lead to running remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, reviewed, versioned method and avoid elevated shells.

Risk: The skill depends on OOMOL account login, VTEX connection setup, and billing status.

Mitigation: Confirm account, connector, and billing readiness before relying on the skill for operational VTEX access.

## Reference(s):

- [VTEX homepage](https://vtex.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vtex)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
