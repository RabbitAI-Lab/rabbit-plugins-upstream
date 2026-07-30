## Description: <br>
Credential Exposure Map audits the credentials an OpenClaw agent can access by scanning environment variables, configuration, memory, installed skills, MCP servers, and git history, then generating a risk-scored exposure report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, security reviewers, and OpenClaw users use this skill to understand which credentials an agent can access at runtime and prioritize cleanup for exposed tokens, memory entries, environment variables, MCP configuration, and git history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs a broad local credential exposure audit across sensitive sources including environment variables, OpenClaw configuration, memory files, MCP server configuration, installed skills, and recent git history. <br>
Mitigation: Run it only when intentionally performing a credential audit and only in a trusted environment. <br>
Risk: The scanner saves a persistent report that may reveal sensitive credential locations and masked credential previews. <br>
Mitigation: Review or delete ~/.openclaw/credential-exposure-report.json after use and avoid sharing the report outside the trusted review context. <br>
Risk: The scan has broad local scope and does not provide clear scan scoping or opt-in controls in the evidence provided. <br>
Mitigation: Confirm the workspace and OpenClaw configuration being audited before execution, and rotate or remove exposed credentials identified by the report. <br>


## Reference(s): <br>
- [Credential Exposure Map ClawHub Listing](https://clawhub.ai/thomaszhou22/skills/credential-exposure-map) <br>
- [OpenClaw Documentation](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown summary with tables, shell command output, and a JSON report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Masks credential values in displayed output and writes ~/.openclaw/credential-exposure-report.json with 600 permissions when run.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
