## Description: <br>
Gainsight NXT (gainsight.com). Use this skill for Gainsight NXT requests including reading, creating, updating, and deleting data through the OOMOL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate their connected Gainsight NXT account through OOMOL, including querying Company records and performing approved insert, update, and delete actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can insert, update, or delete Gainsight NXT Company records. <br>
Mitigation: Approve exact payloads, target records, and intended effects before allowing write or destructive actions. <br>
Risk: The skill depends on a connected OOMOL Gainsight NXT account with valid credentials and scopes. <br>
Mitigation: Install only when the agent is intended to operate that account, and resolve authentication or connection failures before retrying actions. <br>


## Reference(s): <br>
- [Gainsight NXT homepage](https://www.gainsight.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs through the OOMOL oo CLI and returns connector JSON responses that include data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
