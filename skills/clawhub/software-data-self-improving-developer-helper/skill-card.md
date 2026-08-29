## Description:

Helps AI-agent users, skill authors, maintainers, and teams plan, implement, and verify self-improving agent workflows for bug fixing, setup hardening, reliability improvement, and adjacent skill creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn self-improving agent workflow needs into practical plans, code or configuration changes, checklists, analyses, and verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation may select this skill for ordinary software-help prompts where a narrower skill would fit better.

Mitigation: Confirm the prompt needs a general workflow helper for agent reliability, bug fixes, setup hardening, or adjacent skill creation before relying on this skill.

Risk: The skill produces plans, guidance, code, shell commands, or configuration that may be incomplete or unsuitable for a specific repository or environment.

Mitigation: Review proposed changes against local constraints and run the suggested verification or test commands before applying them.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub self-improving-agent demand signal](https://clawhub.ai/skills/self-improving-agent)
- [ClawHub self-improving demand signal](https://clawhub.ai/skills/self-improving)
- [OpenClaw skill article demand signal](https://segmentfault.com/a/1190000047666647)
- [GitHub issue demand signal](https://github.com/Sayshal/spell-book/issues/228)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional code blocks, command snippets, checklists, and implementation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one tailored response or artifact per user request; no executable runtime is bundled.]

## Skill Version(s):

0.20260829.40354 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
