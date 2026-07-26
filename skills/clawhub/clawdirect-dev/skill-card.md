## Description: <br>
Build agent-facing web experiences with ATXP-based authentication, following the ClawDirect pattern. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[napoleond](https://clawhub.ai/user/napoleond) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to build agent-facing Node.js web apps with MCP endpoints, ATXP authentication and payments, cookie-based browser authentication, and agent skill publication guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The sample authentication flow places bearer cookie values in URLs and should not be deployed unchanged. <br>
Mitigation: Use short-lived one-time exchange codes or direct cookie-setting support, then redirect to a clean URL. <br>
Risk: The sample auth storage and cookie lifecycle need production hardening. <br>
Mitigation: Add token expiry, revocation, HTTPS-only cookies, logging controls, and dependency review before production use. <br>


## Reference(s): <br>
- [ClawDirect reference implementation](https://github.com/napoleond/clawdirect) <br>
- [ATXP developer documentation](https://skills.sh/atxp-dev/cli/atxp) <br>
- [ClawDirect directory](https://claw.direct) <br>
- [ClawHub skill page](https://clawhub.ai/napoleond/skills/clawdirect-dev) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with TypeScript, JSON, environment configuration, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes templates for Express, SQLite, MCP tools, ATXP authentication, and agent skill creation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
