## Description: <br>
Guides an agent to choose between Claude Haiku, Sonnet, and Opus based on task complexity and cost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[victorking2005](https://clawhub.ai/user/victorking2005) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to route Claude-only agent work to Haiku, Sonnet, or Opus according to complexity, quality needs, and cost. It is intended for model-selection guidance rather than execution, data access, or tool orchestration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad escalation rules may increase Sonnet or Opus usage and raise costs. <br>
Mitigation: Review the routing thresholds before deployment and monitor model selection and spend after installation. <br>
Risk: Incorrect routing guidance may place a complex task on a cheaper model that gives incomplete or lower-quality results. <br>
Mitigation: Keep the skill's escalation rule active: move from Haiku to Sonnet when focused reasoning is needed, and move to Opus for architecture, critical decisions, or deep debugging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/victorking2005/skills/opus) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown with inline code and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only output for Claude model-routing decisions; no hidden execution or data-access behavior is identified in server security evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
