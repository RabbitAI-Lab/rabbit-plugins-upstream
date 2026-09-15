## Description:

ZeroBounce helps agents validate email addresses, inspect account and usage data, and manage custom allow/block filter rules through an OOMOL-connected ZeroBounce account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate ZeroBounce through an OOMOL-connected account for email validation, account usage checks, activity lookups, credit balance checks, and filter-rule management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes shell commands that execute unpinned remote installer scripts.

Mitigation: Review the installer path and install the oo CLI from a trusted, versioned source with checksum or signature verification; do not allow the agent to run the remote installer automatically.

Risk: The skill can create or update ZeroBounce custom filter rules.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ZeroBounce homepage](https://www.zerobounce.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before running ZeroBounce actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
