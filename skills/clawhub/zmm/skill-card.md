## Description:

詹明明 routes creators and small-business operators to the right zmm family skill for content workflows, business diagnostics, onboarding, and post-task navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and small-business operators use this entry-point skill to decide which zmm family skill should handle a content or business task, get onboarding guidance, and receive a copy-ready prompt for the next skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can turn corrections and feedback into persistent future rules.

Mitigation: Install it only where this local memory behavior is acceptable, and review feedback before relying on it as a standing rule.

Risk: The skill family may inspect installed zmm skills and expose more local skill information than expected.

Mitigation: Run it in workspaces where local skill discovery is acceptable, and review discovered routing targets before following them.

Risk: The skill may read or write a local vault as part of its workflow.

Mitigation: Use it only with vault contents intended for this workflow, and review generated or updated local files before reuse.

## Reference(s):

- [交互规范](references/交互规范.md)
- [内容理论底座](references/内容理论底座.md)
- [实证规律库](references/实证规律库.md)
- [家族公约](references/家族公约.md)
- [规则卡](references/规则卡.md)
- [认知框架](references/认知框架.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with routing recommendations, numbered next-step options, and copy-ready prompts; may include shell commands for local skill discovery.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No API keys or MCP tool references were detected in the provided evidence.]

## Skill Version(s):

0.2.8 (source: server release metadata; artifact frontmatter reports 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
