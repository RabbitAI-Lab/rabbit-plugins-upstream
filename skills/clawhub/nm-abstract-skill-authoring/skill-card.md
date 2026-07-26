## Description: <br>
Guide creating Claude Code skills with TDD and persuasion principles. Use for new skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to create, validate, troubleshoot, and deploy Claude Code skills using a test-driven authoring workflow, progressive disclosure, and anti-rationalization patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally changes authoring behavior by loading a skill-writing methodology into the agent. <br>
Mitigation: Install it only when that methodology is desired for skill authoring and testing work. <br>
Risk: Deployment checklist examples include environment-changing commands such as tagging, pushing to git, and copying files into a live skills directory. <br>
Mitigation: Treat those commands as manual examples and confirm repository remotes, tag names, and destination paths before running them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-skill-authoring) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>
- [Deployment checklist module](artifact/modules/deployment-checklist.md) <br>
- [Validation module](artifact/modules/validation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with examples, checklists, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; command examples are intended for manual review before execution.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
