## Description:

Operate TinyURL through an OOMOL-connected account to create short links, list account URLs, and inspect live action schemas before running connector actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate TinyURL from an OOMOL-connected account, including creating short links and listing account URLs while checking action schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified internet installer commands that can execute code on the user's machine.

Mitigation: Review the setup path before installing the oo CLI; verify the installer script or use a safer package-manager or signed-release installation method.

Risk: Creating a short URL changes TinyURL account state.

Mitigation: Inspect the live schema and confirm the exact destination URL and JSON payload with the user before running the write action.

## Reference(s):

- [ClawHub TinyURL Skill](https://clawhub.ai/oomol/skills/oo-tinyurl)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [TinyURL Homepage](https://tinyurl.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Confirms write payloads before execution and uses live action schemas before sending JSON.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
