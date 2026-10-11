## Description:

Converts a WeChat Channels ID beginning with sph into a finder username for use in later queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users with a WeChat Channels short ID use this skill to obtain the finder username needed for follow-on queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions can install unpinned Node tooling globally and change the local runtime environment.

Mitigation: Review the dependency and install a pinned version manually or in an isolated environment.

Risk: Token setup can store a persistent API credential on the user's machine.

Mitigation: Prefer a temporary token environment variable and keep credentials out of shared logs or files.

Risk: A conversion request can incur paid credits.

Mitigation: Check the current estimate and obtain user approval before calling the paid tool.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-id-convert)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Plain text or Markdown with the finder username and, when applicable, credits used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Channels ID beginning with sph; paid queries require prior user approval.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
