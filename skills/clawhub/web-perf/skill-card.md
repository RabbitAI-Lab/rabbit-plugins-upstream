## Description: <br>
Analyzes web performance using Chrome DevTools MCP, measuring Core Web Vitals and identifying render-blocking resources, network dependency chains, layout shifts, caching issues, and high-level accessibility gaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[elithrar](https://clawhub.ai/user/elithrar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and site owners use this skill to audit, profile, debug, and optimize page-load performance, Lighthouse scores, and site speed. It guides agents through Chrome DevTools MCP traces, network analysis, accessibility snapshots, and optional codebase inspection when source code is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP setup example uses an unpinned `npx -y chrome-devtools-mcp@latest` command. <br>
Mitigation: Review or pin the Chrome DevTools MCP package before using it in sensitive environments. <br>
Risk: The skill can inspect local project configuration and browser sessions during performance analysis. <br>
Mitigation: Run it only in repositories and browser sessions that are approved for analysis. <br>


## Reference(s): <br>
- [Web Perf on ClawHub](https://clawhub.ai/elithrar/skills/web-perf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with tables, prioritized findings, recommendations, code snippets, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Core Web Vitals ratings, estimated impact, framework or bundler findings, and omitted codebase findings when source access is unavailable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
