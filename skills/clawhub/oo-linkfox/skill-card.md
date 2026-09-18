## Description:

LinkFox helps agents operate LinkFox through OOMOL's oo CLI connector for ecommerce intelligence, product research, marketplace analytics, account reports, and IP or compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run LinkFox connector actions for marketplace product discovery, ecommerce analytics, shop and seller research, advertising reports, and IP or policy risk checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote installer commands for the oo CLI.

Mitigation: Review and install the oo CLI through a trusted, verified method before using the skill; avoid running pipe-to-shell installers blindly.

Risk: Write actions can change LinkFox state or create authorization, report, upload, or policy-update resources.

Mitigation: Inspect the live action schema and confirm the exact payload, target account, and intended effect before running write actions.

## Reference(s):

- [LinkFox skill page](https://clawhub.ai/oomol/skills/oo-linkfox)
- [LinkFox homepage](https://www.linkfox.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses that include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
