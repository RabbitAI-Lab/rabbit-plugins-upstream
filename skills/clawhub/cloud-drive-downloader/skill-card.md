## Description:

Helps users download supported cloud-drive shares and direct links to local devices or private storage through a unified workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and developers use this skill to identify cloud-drive links, plan and manage downloads, and save authorized files to their own computers, NAS devices, or private storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Web and Feishu controls can initiate downloads or alter tasks without authentication if exposed beyond localhost.

Mitigation: Keep the services bound to localhost or behind authenticated access; avoid remote web control without access controls and quotas.

Risk: Browser extension and clipboard monitoring can forward copied or selected links and trigger downloads.

Mitigation: Enable these automations only when needed and review forwarded links before downloading.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cloud-drive-downloader)
- [Usage guide](references/00-使用说明.md)
- [Agent interface and privacy](references/20-Agent调用与隐私.md)
- [MCP and agent interface](references/23-MCP与Agent接口.md)
- [Remote NAS and private storage](references/21-远程NAS与私有存储.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON download plans and status]

**Output Format:** [Text or Markdown guidance, CLI commands, and optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads can create files on local or private storage when explicitly initiated.]

## Skill Version(s):

0.7.1 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
