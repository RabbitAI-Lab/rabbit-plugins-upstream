## Description:

Slickdeals helps agents search and read Slickdeals deals, coupons, shopping articles, stores, brands, categories, and supported type data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Slickdeals deal, coupon, store, brand, category, article, and type data through an OOMOL-connected Slickdeals account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer scripts that could be unsafe if run without review.

Mitigation: Install the oo CLI through a verified, versioned, or package-manager path when possible, and review setup commands before execution.

Risk: The skill depends on the OOMOL connector and server-side credential model.

Mitigation: Install only when the OOMOL connector model is acceptable for the deployment, and keep Slickdeals credentials managed through the connected account.

## Reference(s):

- [Slickdeals homepage](https://slickdeals.net/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and return Slickdeals connector responses as JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
