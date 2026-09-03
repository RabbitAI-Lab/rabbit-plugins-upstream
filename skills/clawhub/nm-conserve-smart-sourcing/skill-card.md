## Description:

Selects optimal sources for tool calls, balancing accuracy with token cost before research tasks or when deciding whether a claim needs verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to decide when web search, citations, or uncertainty markers are worth the cost for factual claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may influence when an agent chooses to search and cite sources, which can under-verify high-stakes claims if applied too broadly.

Mitigation: Require full verification standards for legal, compliance, security, medical, and formal research work.

Risk: Citation cost heuristics may lead the agent to use an uncertainty marker instead of a source for claims that still need verification.

Mitigation: Use the skill as lightweight sourcing guidance and escalate to comprehensive sourcing when accuracy or auditability matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-smart-sourcing)
- [Conserve plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown guidance with decision criteria and citation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution; helps the agent decide whether to search, cite, or state uncertainty.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
