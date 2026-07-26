## Description: <br>
PaperPod helps agents use an isolated remote runtime for code execution, live preview URLs, browser automation, command-line tools, AI inference, and persistent memory through CLI or HTTP workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shassingh09](https://clawhub.ai/user/shassingh09) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use PaperPod to run code, manage files and background processes, expose previews, automate browser tasks, call AI endpoints, and persist small state in an isolated PaperPod sandbox. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PaperPod can execute code and shell commands in a remote sandbox and use broad preinstalled tooling. <br>
Mitigation: Use it only for intended sandbox workflows, review commands before running them, and avoid sending secrets or private files unless necessary. <br>
Risk: PaperPod tokens authorize CLI and HTTP access. <br>
Mitigation: Treat PaperPod tokens like passwords, store them in environment variables or secure stores, and re-authenticate or rotate if exposed. <br>
Risk: Port exposure, background processes, browser sessions, and persistent memory can leave accessible or billable resources running. <br>
Mitigation: Expose only services intended for preview, avoid exposing sensitive or unauthenticated apps, and clean up processes, exposed ports, browser sessions, and memory after use. <br>
Risk: CLI workflows depend on the separate @paperpod/cli package. <br>
Mitigation: Review and install the CLI from a trusted package source before global installation, or use documented HTTP endpoints when CLI installation is not appropriate. <br>


## Reference(s): <br>
- [PaperPod homepage](https://paperpod.dev) <br>
- [PaperPod API documentation](https://paperpod.dev/docs) <br>
- [PaperPod ClawHub listing](https://clawhub.ai/shassingh09/skills/paperpod) <br>
- [PaperPod API Reference](references/api-reference.md) <br>
- [Shell Tools Reference](references/shell-tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, HTTP examples, JSON request bodies, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a PaperPod token for authenticated CLI or HTTP use; may start remote processes, expose preview URLs, run browser sessions, call AI endpoints, and use persistent memory.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
