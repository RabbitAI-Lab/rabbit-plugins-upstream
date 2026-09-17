## Description:

Helps agents read CallRail account, call, company, and form submission data through an OOMOL-connected CallRail account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover CallRail accounts and retrieve CallRail calls, companies, and form submissions through OOMOL's connected-account workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified remote installer for the oo CLI.

Mitigation: Install the oo CLI only from a trusted, verified, and versioned source before using the skill.

Risk: The action scope is broader than a strictly read-only skill should be.

Mitigation: Use the skill for the listed get and list actions, inspect the live connector schema first, and avoid unrestricted CallRail changes.

Risk: CallRail data is accessed through an OOMOL-connected account.

Mitigation: Use only when the user trusts OOMOL with the connected CallRail data path and has authorized the relevant account connection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-callrail)
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [CallRail homepage](https://www.callrail.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
