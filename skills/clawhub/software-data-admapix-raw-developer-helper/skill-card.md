## Description:

Helps agent users, skill authors, maintainers, and teams create practical AdMapix-style raw-data workflows for bug fixing, safer setup, reliability improvements, and adjacent skill development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent users, skill authors, maintainers, and teams use this skill to turn AdMapix-style raw-data workflow demand into concrete implementation plans, checklists, analysis, code changes, and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad activation wording and may be invoked when a more specific skill would better match the user's intent.

Mitigation: Require explicit AdMapix or raw-data workflow intent in usage, tighten description and trigger examples, or disable implicit invocation.

Risk: The skill provides workflow and implementation guidance that could be incorrect or incomplete for a user's codebase or data context.

Mitigation: Review proposed changes before use, run relevant tests or validation commands, and confirm assumptions against the target project.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [Popular Clawhub skill demand: ontology](https://clawhub.ai/skills/ontology)
- [Popular Clawhub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot)
- [Popular Clawhub skill demand: AdMapix](https://clawhub.ai/skills/admapix)
- [Ask HN: If you write release notes, what stops you from being specific?](https://news.ycombinator.com/item?id=49367131)
- [Is this AWS RI/SP simulation engine interesting / valuable?](https://news.ycombinator.com/item?id=49374412)
- [How to Implement a DevLake plugin?](https://segmentfault.com/a/1190000042069896)
- [Ask: mysql raw data](https://segmentfault.com/q/1010000012550302)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and remaining risks when helpful.]

## Skill Version(s):

0.20260821.52309 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
