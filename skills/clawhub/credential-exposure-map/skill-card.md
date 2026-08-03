## Description: <br>
Map all credentials your OpenClaw agent can access, including environment variables, config, memory, installed skills, MCP servers, and recent git history, then generate a risk-scored exposure report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaszhou22](https://clawhub.ai/user/thomaszhou22) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit credential exposure in an OpenClaw environment and identify where secrets may be visible to agents, skills, MCP servers, memory files, or git history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill broadly scans sensitive local sources, including OpenClaw configuration, memory files, environment files, installed skills, MCP server configuration, and recent git history. <br>
Mitigation: Use it only for intentional credential audits in an appropriate workspace, and review the scope before running the scanner. <br>
Risk: The scanner uses a hard-coded workspace path, which may not match the user's intended project. <br>
Mitigation: Confirm or adjust the workspace path before running the scan. <br>
Risk: The skill automatically saves a credential exposure report that may reveal sensitive locations and masked secret previews. <br>
Mitigation: Protect the saved report, keep its restrictive file permissions, and delete it after review if it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thomaszhou22/skills/credential-exposure-map) <br>
- [Publisher profile](https://clawhub.ai/user/thomaszhou22) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [scan_exposure.py](artifact/scripts/scan_exposure.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown summary with tables, masked credential previews, and a JSON report file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The scanner masks credential values in displayed findings and saves a local report with file permissions set to 600.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
