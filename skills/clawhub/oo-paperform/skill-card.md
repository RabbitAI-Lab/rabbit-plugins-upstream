## Description:

Paperform enables agents to read Paperform forms, fields, products, coupons, submissions, and partial submissions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Paperform account data through the OOMOL oo CLI without handling raw Paperform credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill permits broad oo CLI shell commands for the connected Paperform account.

Mitigation: Keep agent approval scoped to Paperform connector schema and run commands rather than arbitrary oo subcommands.

Risk: The first-time setup section includes remote installer commands.

Mitigation: Install the oo CLI through a verified, reviewed method before allowing the agent to use the connector.

## Reference(s):

- [ClawHub Paperform skill](https://clawhub.ai/oomol/skills/oo-paperform)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Paperform homepage](https://paperform.co)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
