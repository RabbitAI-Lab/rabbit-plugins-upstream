## Description: <br>
Namely (namely.com). Use this skill for ANY Namely request: searching and reading data through an OOMOL-connected Namely account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and operators use this skill to read Namely employee profiles and company profile-field metadata visible to their connected account. It helps agents inspect the live connector schema before making Namely read requests through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connected Namely account may expose employee profile information visible to that account. <br>
Mitigation: Use the least-privileged Namely account or scopes that still support the intended read-only profile tasks, and review retrieved employee data before sharing it. <br>
Risk: First-time setup can require installing or authenticating the oo CLI and connecting Namely credentials through OOMOL. <br>
Mitigation: Run setup only after an auth, connection, or missing-CLI error, and review installation and authentication steps before executing them. <br>


## Reference(s): <br>
- [Namely homepage](https://www.namely.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-namely) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; action responses are JSON objects with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: artifact frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
