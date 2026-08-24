## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical Skill Vetter-style workflows for bug fixing, setup hardening, reliability improvement, and adjacent skill creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and AI-agent teams use this skill to turn requests about vetting, hardening, bug fixing, and reliability into concise plans, checklists, artifacts, analysis, or implementation support. It is intended to make repeatable work-productivity and skill-vetting tasks easier to act on without requiring readers to inspect the original demand sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers may activate the skill for unrelated security, GitHub, or bug-fix prompts.

Mitigation: Narrow invocation triggers or disable implicit invocation when the workflow should only run on explicit Skill Vetter-style requests.

Risk: The skill can produce guidance, code changes, shell commands, or configuration snippets that may be unsuitable for a specific repository or environment.

Mitigation: Review generated outputs against the stated success criteria and run normal project validation before applying recommendations.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper)
- [Popular ClawHub Skill Demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter)
- [Popular ClawHub Skill Demand: SkillScan](https://clawhub.ai/skills/skillscan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with optional checklists, code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and follow-up work when helpful.]

## Skill Version(s):

0.20260823.40325 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
