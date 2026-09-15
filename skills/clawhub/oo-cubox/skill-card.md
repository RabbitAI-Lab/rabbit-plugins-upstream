## Description:

This skill guides an agent to use the OOMOL oo CLI to operate Cubox through a connected account, including saving URLs for Cubox parsing and snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to operate a connected Cubox account through OOMOL. The documented action saves a web page URL to Cubox after the agent checks the live action schema and confirms write payloads with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Prefer installing the oo CLI from a signed or verified release and review installation instructions before use.

Risk: The documented Cubox action can change user data by saving a URL to Cubox.

Mitigation: Confirm the exact URL, action name, and payload with the user before running the write action.

## Reference(s):

- [ClawHub Cubox skill page](https://clawhub.ai/oomol/skills/oo-cubox)
- [Cubox homepage](https://cubox.pro)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to fetch the live Cubox action schema before constructing an action payload.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
