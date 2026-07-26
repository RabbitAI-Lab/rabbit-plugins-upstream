## Description: <br>
Shorten.REST helps an agent create, inspect, update, and delete Shorten.REST aliases through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage Shorten.REST links, aliases, and click records from an agent through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write or destructive actions can change or remove live Shorten.REST aliases and affect click data. <br>
Mitigation: Confirm the exact payload, alias, domain, and intended effect with the user before running create, update, or delete actions. <br>
Risk: Authentication, connection, or billing failures can interrupt connector execution. <br>
Mitigation: Run first-time setup only after a matching error and retry only after the user resolves the reported account, connection, or billing issue. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shorten-rest) <br>
- [Shorten.REST Homepage](https://shorten.rest) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write and destructive actions require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
