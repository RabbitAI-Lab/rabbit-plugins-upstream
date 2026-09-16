## Description:

Wanx lets an agent operate the Wanx connector through an OOMOL-connected account to generate or edit images, submit video generation tasks, and retrieve video task results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Wanx through OOMOL's CLI-based connector for image generation, image editing, asynchronous video generation, and video task retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands for the oo CLI.

Mitigation: Do not allow the agent to run those installer commands automatically; install the CLI through a verified release path and inspect or verify installer integrity first.

Risk: Image and video generation can create stored outputs, change account state, or consume credits.

Mitigation: Confirm the exact generation request, payload, and expected credit or account impact before execution.

## Reference(s):

- [Wanx ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wanx)
- [Wanx Homepage](https://tongyi.aliyun.com/wanxiang/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include JSON data and execution metadata; image and video generation may create stored outputs or consume account credits.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
