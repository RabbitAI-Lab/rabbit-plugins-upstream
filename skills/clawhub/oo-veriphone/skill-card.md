## Description:

Veriphone helps agents verify phone numbers and retrieve account credit summaries through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Veriphone through an OOMOL-connected account for phone number validity checks, carrier and region lookup, and account credit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote installer scripts executed directly in a shell.

Mitigation: Install the oo CLI only from a verified, versioned source with checksum or signature validation, and do not let an agent run the remote installer automatically.

Risk: Connector calls rely on a correctly installed, authenticated, and connected OOMOL account.

Mitigation: Use setup commands only after an auth or connection failure, and keep routine Veriphone reads limited to an already installed and connected oo CLI.

## Reference(s):

- [ClawHub Veriphone Skill](https://clawhub.ai/oomol/skills/oo-veriphone)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Veriphone Connection Setup](https://console.oomol.com/app-connections?provider=veriphone)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Veriphone connector responses containing data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
