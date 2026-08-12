## Description:

Helps agent users, skill authors, maintainers, and teams create practical vetting workflows, checklists, analysis, implementation support, and safer adjacent skill patterns for Skill Vetter-style work on ClawHub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, skill authors, maintainers, and agent users use this helper to turn Skill Vetter-style demand into practical workflows for bug fixing, setup hardening, safety review, reliability improvement, and adjacent skill creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms and implicit invocation may cause the helper to activate during unrelated security, installation, or GitHub conversations.

Mitigation: Narrow or disable implicit invocation and reserve the helper for explicit Skill Vetter, vetting, skill-safety, or reliability workflow requests.

Risk: Workflow guidance can still produce incorrect or incomplete vetting advice for a specific skill or repository.

Mitigation: Review the generated workflow against the user's success criteria, scan the target skill before deployment, and keep assumptions and remaining risks visible.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper)
- [Publisher Profile](https://clawhub.ai/user/kyro-ma)
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter)
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan)
- [GitHub issue: agents directory support](https://github.com/vercel-labs/skills/issues/1929)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are tailored to the user's immediate workflow and should state assumptions, limits, validation steps, and remaining risks when relevant.]

## Skill Version(s):

0.20260812.40408 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
