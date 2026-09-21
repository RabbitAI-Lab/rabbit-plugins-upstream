## Description:

Connects agents to WeCom Bot through OOMOL's oo CLI to read, create, update, delete, and send WeCom Bot data and messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers can use this skill to operate WeCom Bot through an OOMOL-connected account, including messaging, chat and media retrieval, meetings, schedules, todos, documents, online sheets, smart pages, and smart sheets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to install the oo CLI by executing a remote shell script.

Mitigation: Review the setup section before installing and prefer an official, pinned, or otherwise verifiable oo CLI release.

Risk: Write and destructive actions can send messages, modify schedules, meetings, todos, documents, sheets, smart pages, or smart sheets in a WeCom workspace.

Mitigation: Require explicit user approval for write, delete, message-send, and dynamic call_tool actions, including confirmation of the exact payload and target.

Risk: Connector actions depend on live schemas and credentials managed through the OOMOL connection.

Mitigation: Inspect the action schema before constructing payloads and reroute authentication or connection failures to the documented one-time setup flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wecom-bot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [WeCom Bot homepage](https://work.weixin.qq.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger connector API calls that read or change WeCom workspace data after user approval.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
