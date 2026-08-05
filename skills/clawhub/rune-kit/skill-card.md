## Description: <br>
Rune is a 66-skill mesh for AI coding assistants that routes coding, review, deployment, rescue, research, and domain-extension workflows through connected specialist skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nhadaututtheky](https://clawhub.ai/user/nhadaututtheky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use Rune to coordinate AI coding assistants across implementation, review, debugging, deployment, legacy rescue, documentation, and domain-specific workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundle has broad coding authority and includes automation modes with inconsistent or weak guardrails. <br>
Mitigation: Review or disable automatic and fast execution modes, and require explicit confirmation before high-impact actions. <br>
Risk: Persistent project memory and cross-project memory writes can retain or propagate sensitive project context. <br>
Mitigation: Review or disable automatic Neural Memory capture and require explicit approval before cross-project memory writes. <br>
Risk: External CLI dispatch can send task context outside the current agent runtime. <br>
Mitigation: Review or disable external CLI dispatch and require confirmation before external repository analysis or multi-agent fanout. <br>
Risk: Messaging tools can send communications through Zalo workflows. <br>
Mitigation: Require explicit confirmation before any messaging action, especially sends, broadcasts, or personal-account automation. <br>
Risk: Git rollback, commit, and broad staging workflows can make irreversible or hard-to-review repository changes. <br>
Mitigation: Require explicit confirmation for commits, rollbacks, git reset workflows, and git add -A usage. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/nhadaututtheky/skills/rune-kit) <br>
- [Rune Documentation](https://rune-kit.github.io/rune) <br>
- [Rune Guides](https://rune-kit.github.io/rune/guides) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code blocks, shell commands, checklists, tables, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May coordinate multi-step workflows, persistent project memory, external CLI dispatch, browser automation, git operations, and domain-specific integration guidance depending on the invoked Rune skill.] <br>

## Skill Version(s): <br>
2.31.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
