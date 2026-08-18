## Description:

Helps developers, analysts, and technical users create practical workflows, artifacts, checklists, analysis, code changes, or decision support for questions about Pi Agent compared with Codex and Claude Code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and technical users use this skill to turn recurring questions about Pi Agent, Codex, Claude Code, and related agent tooling into a repeatable evaluation workflow with concrete outputs and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill name suggests USA business migration, while the artifact instructions and triggers focus on Pi Agent comparisons.

Mitigation: Rename the skill or narrow its triggers before relying on it for routing; enable it only when a Pi Agent versus Codex or Claude Code comparison workflow is intended.

Risk: The skill can produce decision support, code, shell commands, or configuration guidance that may be wrong or unsuitable for the user's environment.

Mitigation: Review generated outputs before acting on them, and run any proposed commands or code changes in a controlled environment with clear success criteria.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub self-improving-agent demand signal](https://clawhub.ai/skills/self-improving-agent)
- [V2EX Pi Agent comparison demand signal](https://www.v2ex.com/t/1235226)
- [Ask HN human code review tools demand signal](https://news.ycombinator.com/item?id=49321400)
- [Ask HN pi harness provider demand signal](https://news.ycombinator.com/item?id=49322689)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown response with optional code blocks, shell commands, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No credential variables, MCP servers, or tool integrations are declared by the artifact.]

## Skill Version(s):

0.20260818.40417 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
