## Description: <br>
FDE Agent guides enterprise AI deployment planning by mapping workflows, identifying AI-ready nodes, estimating annual savings, and producing enterprise profiles, node plans, deployment checklists, and handoff manuals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business leaders, consultants, and implementation teams use this skill to turn enterprise AI deployment discussions into structured deliverables covering workflow discovery, AI-node triage, ROI estimates, deployment plans, and handoff materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent beyond chat-only planning into file creation, deployment tooling, persistent automation, or business knowledge storage. <br>
Mitigation: Require explicit user confirmation before file writes, shell commands, runtime media creation, daemon or cron configuration, or storing business knowledge. <br>
Risk: Enterprise deployment conversations can contain sensitive customer, financial, credential, or internal-system details. <br>
Mitigation: Keep generated repositories private and avoid entering sensitive business details unless a retention and sanitization process is in place. <br>


## Reference(s): <br>
- [FDE Agent ClawHub listing](https://clawhub.ai/kongfangxun/skills/sofagent) <br>
- [README](artifact/README.md) <br>
- [FDE capability model](artifact/FDE.md) <br>
- [Quick start](artifact/quick-start.md) <br>
- [Deliverable templates](artifact/templates/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown documents and conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce enterprise profiles, workflow node plans, deployment checklists, and handoff manuals; require explicit user approval before writing files or storing business knowledge.] <br>

## Skill Version(s): <br>
1.3.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
