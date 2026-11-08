## Description:

Coordinates user-authorized cloud-drive downloads across macOS, Windows, and Linux through Agent/MCP/CLI, a Web UI, or browser link handoff, with local use as the default and NAS or server deployment as an option.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Developers and users can ask an agent to route authorized cloud-drive links into local downloads, inspect a proposed plan, and manage tasks through supported command-line, MCP, or Web UI entry points. Use the setup guidance to choose a supported drive and deployment mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with high confidence, citing an exposed Web API token, automatic handling of clipboard and browser download links, and capabilities beyond its stated download purpose.

Mitigation: Avoid installation unless these features are needed and the risks have been reviewed. Do not expose the Web UI to a network; review clipboard or browser-link capture, credential access, and any synchronization that can upload or delete files. Scanning was partial, so unreported behavior is not established as safe.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/cloud-drive-downloader)
- [Skill instructions](SKILL.md)
- [MCP and agent interface](references/23-MCP与Agent接口.md)
- [Agent use and privacy](references/20-Agent调用与隐私.md)
- [Supported drive matrix](references/40-网盘支持矩阵.md)
- [Cross-platform setup and use](references/44-三系统安装与用法.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON task status, Download plans, Guidance]

**Output Format:** [Commands, configuration examples, and text or JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the user-provided link, destination, and selected engine; secrets should remain in the system credential store.]

## Skill Version(s):

0.20.1 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
