## Description: <br>
Scan, fix, and remediate security vulnerabilities in a local code repository using Mobb MCP/CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathansantilli](https://clawhub.ai/user/jonathansantilli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security engineers use this skill to scan local repositories for vulnerabilities, fetch Mobb remediation guidance, and apply approved fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The monitoring workflow can trigger background scans and automatic code changes without a fresh confirmation step. <br>
Mitigation: Use a trusted, user-managed Mobb MCP server and disable or avoid auto-fix unless local code changes will be reviewed and recoverable. <br>
Risk: Repository security remediation requires Mobb authentication and scans of local repository contents. <br>
Mitigation: Confirm the repository path before scanning and use scoped, revocable API keys for Mobb access. <br>


## Reference(s): <br>
- [MCP Tools for Mobb Fixes](artifact/references/mcp-scan-fix.md) <br>
- [Mobb Authentication and Login Flow](artifact/references/mobb-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline tool parameters and patch-application guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize vulnerability fixes, request user confirmation, and apply approved patches returned by Mobb MCP.] <br>

## Skill Version(s): <br>
0.1.2 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
