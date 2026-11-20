## Description:

Edits an existing skill without scoring it, using bundled criteria to propose one evidence-based change for confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yumingtao](https://clawhub.ai/user/yumingtao)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to maintain existing agent skills from scoring bands, evaluation comments, recurring retrospectives, or structure checks. It drafts one proposed change at a time and applies edits only after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A proposed edit could introduce incorrect or misleading guidance into a maintained skill.

Mitigation: Review the proposal before confirming changes. The supplied security assessment found no issues but reports medium confidence because some local references could not be fully resolved.

## Reference(s):

- [TRACE self-check bands](references/trace-items.en.md)
- [Signal rules](references/signal-rules.en.md)
- [Proposal template and examples](references/proposal-template.en.md)
- [Upstream TRACE reference materials](https://github.com/Tencent/skillhub/tree/main/skills/skillhub-trace-evaluator/references)
- [ClawHub skill release](https://clawhub.ai/yumingtao/skills/skill-maintainer)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files]

**Output Format:** [Markdown proposal followed by targeted skill file edits after confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposes one gap per round; does not score skills or run a security scan.]

## Skill Version(s):

1.0.6 (source: SKILL.md frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
