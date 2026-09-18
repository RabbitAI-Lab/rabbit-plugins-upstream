## Description:

SignPath (signpath.io) skill for SignPath requests through the OOMOL oo CLI, including hash-signing requests, signing request status checks, and signing policy listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to operate SignPath through an OOMOL-connected account, including submitting hash-signing requests, checking signing request status, and listing signing policies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fast_sign_hash action can create signing results for artifacts and should not be treated as a routine read-only action.

Mitigation: Require explicit approval before signing, and verify the exact hash, project, policy, and intended artifact before any fast_sign_hash call.

Risk: The setup guidance includes remote installer commands that execute downloaded shell or PowerShell content.

Mitigation: Avoid pipe-to-shell installation unless the installer source has been independently trusted and verified.

## Reference(s):

- [SignPath homepage](https://signpath.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [SignPath connection setup](https://console.oomol.com/app-connections?provider=signpath)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
