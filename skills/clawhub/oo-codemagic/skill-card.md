## Description:

Use this skill to operate Codemagic through an OOMOL-connected account for reading Codemagic data, starting builds, and canceling builds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to inspect Codemagic teams, apps, users, and builds, and to start or cancel Codemagic builds after confirming state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes pipe-to-shell installer commands that are not pinned or verified.

Mitigation: Review the installer before execution, prefer an official pinned package when available, and use least-privileged Codemagic credentials.

Risk: Write actions can start or cancel Codemagic builds.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write.

## Reference(s):

- [Codemagic homepage](https://codemagic.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-codemagic)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Codemagic connector responses are returned as JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
