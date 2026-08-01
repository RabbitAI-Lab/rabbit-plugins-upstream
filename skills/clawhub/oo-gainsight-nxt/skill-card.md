## Description: <br>
Gainsight NXT (gainsight.com). Use this skill for ANY Gainsight NXT request: reading, creating, updating, and deleting data through the OOMOL `gainsight_nxt` connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and developers use this skill to query, insert, update, and delete Gainsight NXT Company records through an OOMOL-connected account. It is suited for account operations where the agent should inspect the live action schema before running read, write, or destructive connector actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update Gainsight NXT Company records when explicitly authorized. <br>
Mitigation: Review the live schema-derived payload and confirm the intended record changes before approving write actions. <br>
Risk: The skill can delete a Gainsight NXT Company record by GSID. <br>
Mitigation: Confirm the target GSID and require explicit approval before running destructive deletion. <br>
Risk: The skill operates a connected Gainsight NXT account through OOMOL. <br>
Mitigation: Install and use it only for accounts where agent-mediated Gainsight NXT operations are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gainsight-nxt) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Gainsight NXT homepage](https://www.gainsight.com) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown text with inline shell commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs the agent to fetch the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
