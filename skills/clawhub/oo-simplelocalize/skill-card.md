## Description:

This skill helps agents read, create, update, and delete SimpleLocalize data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and localization teams use this skill to inspect and manage SimpleLocalize projects through an OOMOL-connected account, including languages, translation keys, translations, and project statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes a remote shell installer for the oo CLI without pinning or verification.

Mitigation: Review the installer or use a pinned, verifiable package before installing the CLI.

Risk: Write and destructive SimpleLocalize actions can change or delete localization data.

Mitigation: Confirm the exact action, target, and payload with the user before approving write or delete commands.

## Reference(s):

- [SimpleLocalize homepage](https://simplelocalize.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that call the oo CLI connector and may propose JSON payloads for SimpleLocalize actions.]

## Skill Version(s):

1.0.2 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
