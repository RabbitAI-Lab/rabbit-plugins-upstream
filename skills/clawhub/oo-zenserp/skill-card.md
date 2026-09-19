## Description:

Operate Zenserp through an OOMOL-connected account to run Google Search, Image Search, Maps local search, and News search actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Zenserp search surfaces through the OOMOL oo CLI after the user has installed the CLI, signed in, and connected Zenserp.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can run an unverified remote installer on the user's machine without an explicit approval step.

Mitigation: Do not allow an agent to run the remote installer automatically; install the CLI from a verified, versioned release or package manager, or inspect and verify the installer before execution.

Risk: Zenserp actions depend on an authenticated OOMOL oo CLI connection and may fail when credentials, scopes, app readiness, or credits are missing.

Mitigation: Run normal searches only after the CLI is installed, the user is signed in, and Zenserp is connected; use the documented setup steps only after matching auth, connection, or billing failures.

## Reference(s):

- [Zenserp homepage](https://zenserp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zenserp)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before constructing JSON payloads; connector runs return data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
