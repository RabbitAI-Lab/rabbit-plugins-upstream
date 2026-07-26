## Description: <br>
A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuzhuhai](https://clawhub.ai/user/wuzhuhai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and AI agents use AgentBrowser to automate browser workflows, inspect page structure, interact with elements, test web UIs, collect page data, and capture screenshots, PDFs, traces, or recordings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can create screenshots, videos, traces, PDFs, and saved auth state that contain sensitive page or account data. <br>
Mitigation: Store captures and state files only in trusted locations, keep them out of shared folders and repositories, and delete them when they are no longer needed. <br>
Risk: The skill depends on a third-party browser automation CLI and local Node/npm installation. <br>
Mitigation: Install only from trusted sources, review the CLI source and version before use, and avoid running it against authenticated or sensitive sites unless that trust decision is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wuzhuhai/skills/agentbrowser) <br>
- [agent-browser CLI repository](https://github.com/vercel-labs/agent-browser) <br>
- [AgentBrowser skill issue repository](https://github.com/TheSethRose/Agent-Browser-CLI) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, JSON, files] <br>
**Output Format:** [Markdown guidance with inline shell command examples; CLI commands can return text, JSON snapshots, screenshots, PDFs, videos, traces, and saved browser state files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npm, plus an installed agent-browser CLI and browser runtime.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
