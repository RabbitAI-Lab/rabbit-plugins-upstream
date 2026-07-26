## Description: <br>
Give AI agents hands to control macOS apps by discovering installed applications, generating CLI wrappers, and returning structured JSON for automation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mileszhang001-boom](https://clawhub.ai/user/mileszhang001-boom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to let AI agents discover controllable macOS applications, install app-specific CLI wrappers, and execute supported app actions through shell commands with structured JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an AI agent broad control over local macOS applications. <br>
Mitigation: Install it only when that control is intended, and use an app/action allowlist where possible. <br>
Risk: Automation or Accessibility permissions may allow sensitive app, file, browser, messaging, email, or system-setting changes. <br>
Mitigation: Grant macOS permissions narrowly and require human confirmation before high-impact actions. <br>
Risk: Generated wrappers and granted permissions can remain after the workflow is complete. <br>
Mitigation: Remove generated wrappers and revoke macOS Automation and Accessibility permissions when finished. <br>
Risk: Package substitution or drift could change the behavior of the installed automation tool. <br>
Mitigation: Pin and verify the clam-mac package before use. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/mileszhang001-boom/agent-tool-scout) <br>
- [Project homepage](https://github.com/mileszhang001-boom/cli-on-mac) <br>
- [CLAM CLI / MCP / Lobster Reference](docs/README-AI.md) <br>
- [PyPI package](https://pypi.org/project/clam-mac/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash, YAML, Python, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated app wrappers can emit structured JSON with the --json flag.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata, SKILL.md frontmatter, pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
