## Description:

Wanx lets agents operate Tongyi Wanxiang through OOMOL's Wanx connector for image generation, image editing, and asynchronous video generation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Wanx action schemas, run Wanx connector actions, submit image or video generation requests, and retrieve video generation results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path recommends installing the oo CLI by piping a remote script directly into a shell.

Mitigation: Install the oo CLI manually from official documentation with version and integrity checks before using the skill.

Risk: Wanx image generation and video submission actions change service state and may incur account usage or billing effects.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and resolve billing or connection errors before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wanx)
- [Wanx homepage](https://tongyi.aliyun.com/wanxiang/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
