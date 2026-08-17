## Description:

Helps AI-agent users, skill authors, maintainers, and teams adapt AdMapix-style software and data workflows into practical support for bug fixing, setup hardening, reliability improvements, and adjacent skill development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and teams use this skill to turn demand for AdMapix-style software and data workflows into practical guidance, checklists, implementation plans, code-change support, and verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may cause the skill to be used for ordinary software or data questions where AdMapix-style guidance is not a good fit.

Mitigation: Prefer explicit invocation by skill name and review whether the generated guidance matches the task before applying it.

Risk: The skill can propose code changes, workflow changes, or setup-hardening steps that may be incorrect for a specific environment.

Mitigation: Review suggested changes, run the included verification commands when provided, and apply changes incrementally.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/software-data-admapix-raw-developer-helper)
- [AdMapix Demand Signal](https://clawhub.ai/skills/admapix)
- [Ontology Demand Signal](https://clawhub.ai/skills/ontology)
- [Agent Browser Demand Signal](https://clawhub.ai/skills/agent-browser-clawdbot)
- [Ask HN Marketing Discussion](https://news.ycombinator.com/item?id=49316403)
- [DevLake Plugin Article](https://segmentfault.com/a/1190000042069896)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code blocks, shell commands, checklists, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, remaining risks, and follow-up work when relevant]

## Skill Version(s):

0.20260817.40422 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
