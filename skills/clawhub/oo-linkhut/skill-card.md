## Description:

Linkhut (ln.ht) enables an agent to read, create, update, and delete Linkhut bookmarks through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Linkhut bookmarks from an agent session through OOMOL's oo CLI. It supports listing bookmarks and tags, creating or updating bookmarks, and deleting bookmarks after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly by the shell.

Mitigation: Prefer an official package or downloaded installer that can be inspected and verified before execution.

Risk: Create, update, and delete actions can change or remove Linkhut account data.

Mitigation: Confirm the exact payload, target URL, and intended effect with the user before running write or destructive actions.

Risk: The skill depends on OOMOL's oo CLI and an OOMOL-connected Linkhut account.

Mitigation: Install and use the skill only when the user is comfortable connecting Linkhut through OOMOL and using the oo CLI in the active environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-linkhut)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Linkhut Homepage](https://ln.ht)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON connector responses.]

## Skill Version(s):

1.0.3 (source: evidence release version and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
