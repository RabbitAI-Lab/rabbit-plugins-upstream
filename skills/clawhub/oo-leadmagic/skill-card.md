## Description:

LeadMagic (leadmagic.io) helps agents search and read lead intelligence data through OOMOL's LeadMagic connector instead of calling the LeadMagic API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent enrich companies and profiles, find professional contact details, validate email addresses, and check LeadMagic credit balance through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a trusted, verified method and do not allow an agent to run remote installer commands automatically.

Risk: LeadMagic actions may return personal contact data.

Mitigation: Use retrieved contact data only for authorized workflows and review outputs before sharing or storing them.

Risk: LeadMagic actions may consume account credits.

Mitigation: Check credit balance when needed and confirm credit-sensitive lookups before running them at scale.

## Reference(s):

- [ClawHub LeadMagic skill page](https://clawhub.ai/oomol/skills/oo-leadmagic)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [LeadMagic homepage](https://leadmagic.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke LeadMagic connector actions that return structured JSON data and an execution id.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
