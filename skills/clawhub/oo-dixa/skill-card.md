## Description: <br>
Dixa (dixa.com). Use this skill for ANY Dixa request -- searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Dixa connector schemas and read Dixa agents, conversations, end users, conversation messages, and presence through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions can expose sensitive support data, including customer conversations, end-user records, and agent presence. <br>
Mitigation: Use least-privilege Dixa credentials and avoid retrieving or sharing records beyond the user's stated task. <br>
Risk: Connector contracts can change, which may make stale payload assumptions inaccurate. <br>
Mitigation: Inspect the live action schema before constructing each action payload. <br>
Risk: Authentication, connection, scope, credential, or billing failures can trigger unnecessary setup actions. <br>
Mitigation: Run setup or recovery steps only after the corresponding command failure is observed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dixa) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Dixa Homepage](https://www.dixa.com) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads; read actions may return Dixa support data.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
