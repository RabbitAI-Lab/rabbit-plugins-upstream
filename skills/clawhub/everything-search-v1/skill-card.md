## Description: <br>
Windows 10/11 and WSL2 local file search skill based on the Everything es.exe CLI tool for filename, path, extension, and size searches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1tokener](https://clawhub.ai/user/1tokener) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and local agent users use this skill to search Windows or WSL file names, paths, extensions, and sizes through Everything without performing web search or full-text content search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically start Everything.exe and invoke es.exe for local searches. <br>
Mitigation: Install it only when local filename and path search is intended, and verify the exact Everything.exe and es.exe locations before first use. <br>
Risk: Executable discovery can use path.env, environment variables, and PATH. <br>
Mitigation: Pin trusted executable locations in path.env and avoid untrusted PATH or environment-variable overrides. <br>
Risk: Search output can expose local filenames, paths, extensions, and sizes to the agent. <br>
Mitigation: Use it only in environments where returning local path metadata to the agent is acceptable, and review outputs before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1tokener/skills/everything-search-v1) <br>
- [Server-resolved GitHub provenance](https://github.com/1TOKENer/Everything-Search-Skill) <br>
- [Everything command-line interface help](https://www.voidtools.com/zh-cn/support/everything/command_line_interface/) <br>
- [Everything command-line options help](https://www.voidtools.com/zh-cn/support/everything/command_line_options/) <br>
- [Everything search syntax](https://www.voidtools.com/support/everything/searching/) <br>
- [Everything and es.exe downloads](https://www.voidtools.com/zh-cn/downloads/#cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style text tables with command-line status and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns local file result metadata such as filename, extension, size, and path; default result limit is 100 unless changed by invocation.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata and release changelog; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
