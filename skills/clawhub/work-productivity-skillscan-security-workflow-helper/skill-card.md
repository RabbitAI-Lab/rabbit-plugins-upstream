## Description:

Helps AI-agent users and skill maintainers create practical SkillScan-style workflows for bug fixing, setup hardening, safety checks, reliability improvements, and adjacent skill planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and teams use this skill to turn security-gate and SkillScan-style needs into local-friendly plans, checklists, workflows, code changes, and validation notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic activation triggers could steer unrelated chats toward SkillScan-style security workflow advice.

Mitigation: Narrow activation to explicit SkillScan or security-workflow requests, or disable implicit invocation before broad installation.

Risk: Workflow, checklist, or code-change guidance may be incorrect for a user's local environment if applied without review.

Mitigation: Review proposed outputs against local success criteria and scan skills before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper)
- [Requirement plan](references/requirement-plan.md)
- [Demand evidence: SkillScan](https://clawhub.ai/skills/skillscan)
- [Demand evidence: Skill Vetter](https://clawhub.ai/skills/skill-vetter)
- [Demand evidence: gate engine issue](https://github.com/prokopto-dev/dragonkillparty/issues/173)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code, shell-command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, and follow-up risks.]

## Skill Version(s):

0.20260812.40408 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
