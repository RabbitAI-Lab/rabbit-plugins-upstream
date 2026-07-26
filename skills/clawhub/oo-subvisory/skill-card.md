## Description: <br>
Subvisory helps agents read, create, update, and delete Subvisory data through an OOMOL-connected account using the oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to manage Subvisory categories, payment methods, and subscriptions from Codex through the OOMOL oo CLI. It is intended for Subvisory read and account-management workflows, with confirmation before write or destructive actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Subvisory categories, payment methods, or subscriptions. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged [write]. <br>
Risk: Destructive actions can delete Subvisory records. <br>
Mitigation: Get explicit approval for the target record before running actions tagged [destructive]. <br>
Risk: The skill depends on the OOMOL oo CLI and a connected Subvisory account. <br>
Mitigation: Run install, login, or connection steps only after an auth or connection failure and only when the user intends to connect Subvisory. <br>


## Reference(s): <br>
- [Subvisory homepage](https://www.subvisory.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-subvisory) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use oo connector schema and oo connector run; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
