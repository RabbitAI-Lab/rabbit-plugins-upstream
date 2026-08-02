## Description: <br>
Assesses decision reversibility and risk at critical checkpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill during issue work, pull request review, architecture review, and PR fixes to decide whether a high-stakes branch can proceed with a quick recommendation or should escalate to War Room deliberation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local audit files may include file paths, issue numbers, decisions, and rationale under ~/.claude. <br>
Mitigation: Confirm this logging is acceptable before installation and narrow, disable, or redirect audit logging in sensitive repositories when the surrounding plugin supports it. <br>
Risk: Overbroad triggers may invoke the checkpoint in workflows where escalation assessment is unnecessary. <br>
Mitigation: Review trigger configuration and keep checkpoint use limited to high-stakes branches, dependency conflicts, architecture changes, or similarly consequential decisions. <br>
Risk: The skill's recommendations can influence automated workflow control flow. <br>
Mitigation: Require human confirmation when confidence is low or when the response marks requires_user_confirmation as true. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-war-room-checkpoint) <br>
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Markdown, Configuration] <br>
**Output Format:** [Markdown with structured response fields and YAML-style examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a reversibility score, selected escalation mode, recommendation or orders, confidence, and user-confirmation status.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
