## Description:

KlickTipp enables agents to manage KlickTipp subscriber and tag workflows through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect KlickTipp action schemas and run subscriber sign-in, sign-off, and tag-removal actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote install commands that execute scripts directly in a shell.

Mitigation: Review the official oo CLI installation instructions and install the CLI yourself before using the skill.

Risk: The skill can create or update subscribers, unsubscribe contacts, and remove tags from subscribers.

Mitigation: Confirm the exact action, target email address, payload, and expected effect before running any write or destructive action.

Risk: The OOMOL CLI and KlickTipp connector may receive account access needed to perform requested actions.

Mitigation: Install and use the skill only when that access level is acceptable for the connected OOMOL and KlickTipp accounts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-klicktipp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL KlickTipp App Connection](https://console.oomol.com/app-connections?provider=klicktipp)
- [KlickTipp Homepage](https://www.klicktipp.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
