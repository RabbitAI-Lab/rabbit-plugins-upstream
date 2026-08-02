## Description: <br>
Ambivo lets an agent operate Ambivo CRM through OOMOL, including listing, creating, updating, and deleting contacts, leads, and tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with Ambivo CRM records through an OOMOL-connected account. It supports routine CRM read workflows plus guarded create, update, and delete actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive actions can create, change, or delete Ambivo CRM records. <br>
Mitigation: Confirm the exact action, target record, payload, and expected effect with the user before running write or delete actions. <br>
Risk: The skill depends on the OOMOL oo CLI and an OOMOL-connected Ambivo account. <br>
Mitigation: Install and use it only when the OOMOL toolchain and account connection are trusted for the intended Ambivo workspace. <br>
Risk: Read actions can expose Ambivo CRM contact, lead, and task data. <br>
Mitigation: Run read actions only for authorized requests and share only the CRM fields needed for the user's task. <br>


## Reference(s): <br>
- [Ambivo homepage](https://www.ambivo.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub listing](https://clawhub.ai/oomol/skills/oo-ambivo) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include returned CRM data and an execution id when actions run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
