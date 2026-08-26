## Description:

EasyEDA API Skill helps AI agents work with EasyEDA Pro projects by consulting API and source-format documentation and, when configured, executing JavaScript through a local bridge into a running EasyEDA client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to look up EasyEDA Pro APIs, generate extension or automation code, inspect EasyEDA document source formats, and debug actions against a live EasyEDA session when the bridge is intentionally enabled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can execute code in a live EasyEDA session.

Mitigation: Run the bridge only on trusted local machines, stop it when finished, and require explicit user confirmation before write operations.

Risk: Automation can modify, delete, or switch design projects.

Mitigation: Duplicate or back up EasyEDA projects before use and review generated commands before execution.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [EasyEDA bridge extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)
- [API reference index](artifact/references/_index.md)
- [API quick reference](artifact/references/_quick-reference.md)
- [Getting started guide](artifact/guide/how-to-start.md)
- [API invocation guide](artifact/guide/invoke-apis.md)
- [Document source format overview](artifact/format/index.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JavaScript, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include EasyEDA API calls, local bridge commands, extension configuration steps, and document-format guidance.]

## Skill Version(s):

1.1.21 (source: ClawHub release evidence; artifact metadata reports 1.1.26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
