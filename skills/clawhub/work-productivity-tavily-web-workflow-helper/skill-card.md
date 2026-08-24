## Description:

Helps agent users, skill authors, maintainers, and teams create practical Tavily-style web search workflows, fix related issues, harden setup, improve reliability, and build adjacent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and AI-agent users use this skill to turn Tavily-style web search workflow demand into actionable plans, checklists, code changes, or decision support. It is intended for practical workflow help around setup hardening, reliability improvements, bug fixes, and related skill creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to activate for ordinary web, search, or workflow requests when Tavily-specific help was not intended.

Mitigation: Prefer explicit invocation for Tavily workflow help, or narrow the trigger keywords and examples before publishing in environments where accidental activation matters.

Risk: The skill can propose workflow, code, shell, or configuration changes that may be incomplete or mismatched to a user's environment.

Mitigation: Review generated artifacts before use, validate them against the stated success criteria, and test commands or configuration changes in a controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper)
- [Requirement Plan](references/requirement-plan.md)
- [Tavily search demand signal](https://clawhub.ai/skills/openclaw-tavily-search)
- [Alternative to Internet Archive demand signal](https://news.ycombinator.com/item?id=49309061)
- [V2EX workflow demand signal](https://www.v2ex.com/t/1234656)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with optional code, shell command, and configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tailored workflow artifacts, reusable checklists, implementation notes, and verification notes.]

## Skill Version(s):

0.20260816.40342 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
