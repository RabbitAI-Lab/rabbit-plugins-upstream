## Description:

YuanYin yotta-prompt helps agents turn vague user requests into clarified tasks by offering candidate intent directions, asking for goal, scope, output, and constraints, and producing ready-to-run prompts that can route to YottaMeta skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users, employees, developers, and agent operators use this skill when a request is too vague to execute directly. It helps the agent present candidate directions, ask targeted clarification questions, and return a runnable prompt or optional YottaMeta skill routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-start activation and persistence can influence future agent behavior beyond a single task.

Mitigation: Install only when this always-active clarification behavior is intended, and do not allow permanent memory, startup prompt, or long-term configuration changes unless reviewed and approved.

Risk: Multi-agent or global installation can spread the skill across agents more broadly than intended.

Mitigation: Prefer a single-agent or explicit directory install with --agent or --dir, and avoid -g or --global unless broad deployment is intentional.

## Reference(s):

- [Scenario library](references/scenarios.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-prompt)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-prompt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown-style conversational guidance, optional CLI text or JSON output, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask two to three clarification questions at a time; CLI commands can emit text or JSON.]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
