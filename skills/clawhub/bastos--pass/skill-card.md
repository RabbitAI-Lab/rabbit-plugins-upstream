## Description:

Complete guide for using pass, the standard Unix password manager, including terminal password management, GPG-encrypted stores, git synchronization, TOTP, imports, and common CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bastos](https://clawhub.ai/user/bastos)

### License/Terms of Use:


## Use Case:

Developers, engineers, and terminal users use this skill to set up and operate pass for GPG-backed password storage, password generation, retrieval, organization, git synchronization, and related extensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands may create, overwrite, move, or recursively remove password-store entries.

Mitigation: Review each command before execution and use destructive options such as -f and -r only when the target path is correct.

Risk: The workflow handles private GPG keys, TOTP seeds, clipboard contents, and password-manager export files.

Mitigation: Protect private keys and exports, avoid exposing clipboard or terminal output, and clear or delete sensitive files after use.

Risk: Extension installation can execute third-party code in the user's password-store environment.

Mitigation: Install extensions only from trusted sources and prefer verified or pinned versions where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bastos/skills/pass)
- [pass-update extension](https://github.com/roddhjav/pass-update)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include commands that manipulate password-store entries, GPG keys, git remotes, clipboard behavior, and third-party pass extensions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
