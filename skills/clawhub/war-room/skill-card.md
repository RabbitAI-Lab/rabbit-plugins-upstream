## Description: <br>
War Room runs structured multi-agent brainstorming, design, review, and strategy sessions with specialist roles and an adversarial CHAOS reviewer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maxkle1nz](https://clawhub.ai/user/maxkle1nz) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, product teams, and operators use War Room to turn complex software, business, or creative problems into decision logs, specialist analyses, consolidated blueprints, and post-mortems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow creates and updates local project files. <br>
Mitigation: Run it in a dedicated workspace and review generated files before using them as project direction. <br>
Risk: Follow-up scheduling can continue a session after agents finish or remain pending. <br>
Mitigation: Require explicit approval before scheduling follow-ups and confirm how to view and cancel scheduled jobs. <br>
Risk: The workflow may open generated artifacts with the operating system's default viewer. <br>
Mitigation: Ask for operator consent before opening local viewers and keep artifact paths scoped to the war-room workspace. <br>
Risk: Briefs, DNA files, and agent outputs may contain sensitive project information. <br>
Mitigation: Do not put secrets or confidential credentials in war-room briefs, DNA files, communications, or generated artifacts. <br>


## Reference(s): <br>
- [Agent Roles Reference](references/agent-roles.md) <br>
- [WAR ROOM Agent DNA v3](references/dna-template.md) <br>
- [Wave Protocol Detailed Reference](references/wave-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files, workspace folders, terminal-oriented status text, and optional project scaffolding outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a war-rooms/<project>/ workspace with briefs, decisions, status, blockers, communications, agent outputs, artifacts, and lessons.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
