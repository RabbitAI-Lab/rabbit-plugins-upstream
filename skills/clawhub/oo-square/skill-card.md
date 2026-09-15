## Description:

Square integration for reading, creating, searching, listing, and updating customer and location data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Square through an OOMOL-connected account, including customer creation, retrieval, listing, searching, updates, and seller location listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote install scripts that could execute arbitrary local code if the source is compromised or unverified.

Mitigation: Install the oo CLI from a verified, versioned, checksum- or signature-checked source, and avoid running curl-to-bash or irm-to-iex commands as an administrator.

Risk: Square write actions can create or update customer records in the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before allowing create or update actions.

## Reference(s):

- [Square homepage](https://squareup.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-square)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Square connector schemas before action execution and returns structured JSON responses with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
