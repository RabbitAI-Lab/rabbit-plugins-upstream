## Description: <br>
Operate OpenStatus through an OOMOL-connected account for reading, creating, updating, triggering, and deleting monitors via the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage OpenStatus monitors and inspect monitor status, summaries, and HTTP response logs from an OOMOL-connected OpenStatus account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, trigger, and delete OpenStatus monitors in the connected account. <br>
Mitigation: Review exact write or destructive payloads with the user and require explicit approval before executing state-changing actions. <br>
Risk: The connected OpenStatus API key determines what account data and actions the agent can access. <br>
Mitigation: Connect only an OpenStatus API key with the access level the user is comfortable granting. <br>


## Reference(s): <br>
- [OpenStatus homepage](https://www.openstatus.dev) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub OpenStatus skill](https://clawhub.ai/oomol/skills/oo-openstatus) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI action results are JSON responses containing data and meta.executionId; state-changing actions require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
