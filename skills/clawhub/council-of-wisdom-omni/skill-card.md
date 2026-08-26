## Description:

A multi-agent deliberation hub with 3 core agents and extensible extended agents. Activates on explicit request, can suggest calling user workspace skills with consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adelpro](https://clawhub.ai/user/adelpro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route deliberate decisions through multiple advisory perspectives, including intent, risk, tone, architecture, complexity, and values checks. It can suggest relevant workspace skills for specialized follow-up, with delegation announced first and explicit consent required for sensitive or high-impact tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose delegating a security, account, or other high-impact task to a downstream workspace skill that is not appropriate for the request.

Mitigation: Approve delegation only when the named downstream skill and the stated reason make sense for the task; deny delegation when the routing is unclear or outside the intended scope.

Risk: Multi-agent advisory output can still contain incomplete assumptions or misleading guidance.

Mitigation: Use the skill as decision support and review its risk, intent, and values conclusions before acting on consequential recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adelpro/skills/council-of-wisdom-omni)
- [ClawHub publisher profile](https://clawhub.ai/user/adelpro)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows consulted agents and reasoning by default; full per-agent analysis is available when explicitly invoked with the council prefix.]

## Skill Version(s):

1.4.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
