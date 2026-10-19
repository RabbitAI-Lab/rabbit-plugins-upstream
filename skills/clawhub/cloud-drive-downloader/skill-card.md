## Description:

Routes authorized cloud-drive downloads through an agent, CLI, web interface, or browser extension to local or optional remote engines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users route links they are authorized to download to local or optional NAS/server download engines, with CLI, MCP, web, and browser-extension entry points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Web UI or API may expose unauthenticated download controls on a reachable network.

Mitigation: Keep the service on localhost or behind strong network access controls; do not expose its API or Docker port to untrusted networks.

Risk: A configured completion hook can run a local command after downloads finish.

Mitigation: Leave http.on_complete_hook empty unless a trusted local administrator configures it.

Risk: The browser extension has broad permissions and can forward copied, selected, or newly downloaded URLs.

Mitigation: Review extension permissions and configure it only for a trusted local service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cloud-drive-downloader)
- [Usage guide](artifact/references/00-使用说明.md)
- [Supported cloud drives](artifact/references/40-网盘支持矩阵.md)
- [Docker deployment](artifact/references/33-Docker部署与一键搜索.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Text or JSON responses, with commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate downloads and report progress or errors.]

## Skill Version(s):

0.18.3 (source: ClawHub release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
