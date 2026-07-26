## Description: <br>
A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cindypapa](https://clawhub.ai/user/cindypapa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and agent builders use this skill to automate browser navigation, interaction, form filling, UI testing, page inspection, screenshots, PDFs, recordings, and structured data extraction through the agent-browser CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can act on authenticated sites or accounts the user has opened. <br>
Mitigation: Use the skill only on sites and accounts the user intends the agent to control, and prefer isolated sessions for important accounts. <br>
Risk: Saved browser state, cookies, storage output, screenshots, PDFs, recordings, and traces can contain sensitive information. <br>
Mitigation: Treat these outputs as sensitive data and avoid committing, sharing, or storing them where unauthorized users can access them. <br>
Risk: The skill depends on installing and running the agent-browser CLI and browser components. <br>
Mitigation: Confirm trust in the npm package or upstream repository before installation and keep Node.js and npm available as required runtime dependencies. <br>


## Reference(s): <br>
- [Agent Browser Skill Page](https://clawhub.ai/cindypapa/skills/agent-browser) <br>
- [agent-browser CLI Repository](https://github.com/vercel-labs/agent-browser) <br>
- [Agent Browser Skill Issue Repository](https://github.com/TheSethRose/Agent-Browser-CLI) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Code, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce screenshots, PDFs, video recordings, traces, saved browser state, cookies, storage data, and structured page snapshots when the documented CLI commands are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
