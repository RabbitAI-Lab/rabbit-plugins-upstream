## Description:

Connects a local LobsterAI desktop agent to an Infinite Canvas instance by preparing the local connector, starting it when needed, and generating an auto-connect canvas URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rainbow-boy-max](https://clawhub.ai/user/rainbow-boy-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers who use LobsterAI with an Infinite Canvas instance can use this skill to prepare the local connector, start it when needed, and open a canvas URL that auto-populates assistant connection details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill downloads and runs unverified connector code.

Mitigation: Review before installing, prefer a version that bundles or verifies the connector, and ask before starting the background service.

Risk: The security evidence says generated output and URLs expose a local connection token.

Mitigation: Use only trusted canvas origins and do not share generated pageUrl or token output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rainbow-boy-max/skills/canvas-connector)
- [LobsterAI desktop app](https://lobsterai.youdao.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the helper script emits single-line JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a generated pageUrl containing local agent connection parameters.]

## Skill Version(s):

1.0.0 (source: server release evidence, VERSION, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
