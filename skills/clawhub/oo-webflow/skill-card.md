## Description: <br>
Webflow (webflow.com). Use this skill for Webflow requests involving reading, creating, updating, and deleting data through the OOMOL Webflow connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect and manage Webflow sites, CMS collections, and CMS items through an OOMOL-connected Webflow account. It supports read operations plus confirmed create, update, publish, and delete workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and publish actions can change Webflow CMS items or site state. <br>
Mitigation: Confirm the exact action, target site, collection or item, and payload with the user before running write or publish actions. <br>
Risk: The delete action can remove a draft CMS item. <br>
Mitigation: Require explicit approval for the specific item before destructive actions and verify the target with a read operation first when practical. <br>
Risk: The skill operates through a connected Webflow account. <br>
Mitigation: Install and use it only for intended Webflow accounts, and resolve authentication, scope, or billing errors through the documented first-time setup flow. <br>


## Reference(s): <br>
- [Webflow homepage](https://webflow.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-webflow) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector responses in JSON format when actions are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
