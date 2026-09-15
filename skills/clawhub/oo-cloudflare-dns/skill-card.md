## Description:

Cloudflare DNS helps agents read, create, update, and delete Cloudflare DNS data through OOMOL's oo CLI and server-managed Cloudflare credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage Cloudflare DNS accounts, zones, and DNS records through an OOMOL-connected account. It supports read operations directly and requires confirmation before create, update, or delete DNS actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts that are run directly in a shell.

Mitigation: Review the OOMOL CLI installation method before use and prefer a signed, pinned, or package-manager-based install when available.

Risk: Cloudflare DNS create, update, and delete actions can change or remove live DNS records.

Mitigation: Use a Cloudflare credential with the narrowest DNS permissions needed and require explicit user confirmation before any state-changing DNS action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cloudflare-dns)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cloudflare](https://www.cloudflare.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce JSON command responses from the oo CLI when connector actions are run.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
