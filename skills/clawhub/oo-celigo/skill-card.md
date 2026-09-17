## Description:

Provides agent guidance for operating Celigo through an OOMOL-connected oo CLI account, including schema inspection, read and list actions, and guarded state-changing requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Celigo through an OOMOL-connected account, inspect live connector schemas, list or retrieve Celigo resources, and confirm payloads for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer instructions include remote pipe-to-shell commands that may run unverified code on the user's machine.

Mitigation: Review the installer path before use, prefer verified release or package-manager installation, and avoid running remote installer commands from an elevated shell.

Risk: Celigo actions can change state when tagged as write or destructive.

Mitigation: Fetch the live action schema, confirm the exact payload and expected effect with the user, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Celigo skill page](https://clawhub.ai/oomol/skills/oo-celigo)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Celigo homepage](https://www.celigo.com)
- [Celigo skill icon](https://static.oomol.com/logo/third-party/Celigo.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live oo connector schema output before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
