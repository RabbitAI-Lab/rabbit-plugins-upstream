## Description:

Kustomer helps agents read, create, and update Kustomer customer data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support operators use this skill to retrieve, list, search, create, and update Kustomer customer records through the oo CLI. The skill is intended for Kustomer account workflows where credentials are managed by OOMOL rather than handled directly by the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions tell users to execute a remote installer script without verification.

Mitigation: Review the installer path before installing; prefer a verified, pinned oo CLI release or a trusted package manager.

Risk: Write actions can create or update Kustomer customer records.

Mitigation: Confirm the exact payload and expected effect before allowing create_customer or update_customer actions.

## Reference(s):

- [ClawHub Kustomer skill page](https://clawhub.ai/oomol/skills/oo-kustomer)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Kustomer homepage](https://www.kustomer.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector commands that return JSON responses containing Kustomer data and execution metadata.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
