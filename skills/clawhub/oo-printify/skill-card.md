## Description:

Operates Printify through an OOMOL-connected account to inspect schemas and run read-only shop, product, and order actions via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Printify shop, product, and order information from an OOMOL-connected merchant account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access connected Printify merchant account data.

Mitigation: Install and use it only for explicit Printify account read tasks where OOMOL-mediated access is intended.

Risk: The skill documentation includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Review the installer first or use a trusted package-manager or manual installation path before running setup commands.

Risk: The broad activation language could cause the skill to be selected for any Printify-related request.

Mitigation: Confirm the user is asking for Printify account reads before running connector commands.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Printify homepage](https://printify.com/)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-printify)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
