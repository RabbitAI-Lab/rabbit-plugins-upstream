## Description:

A cross-agent human–AI collaboration protocol for context briefs, plan-first execution, milestone delivery, verification, and session handovers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to guide AI agents through complex or cross-session work: preparing a brief, agreeing on a plan, delivering checkable steps, verifying outcomes, and leaving a handover note.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence how agents plan and carry out complex tasks.

Mitigation: Review proposed guidance, approve work with side effects, and verify outcomes against the task's acceptance criteria.

Risk: Reinstalling can affect customized skill copies.

Mitigation: Choose a specific installation destination and back up customized copies before reinstalling.

Risk: The security review covers the supplied files, not future npm releases.

Mitigation: Verify the exact npm version before executing an installation command.

Risk: Permanent activation or sensitive memory entries can persist information.

Mitigation: Require user consent before enabling permanent activation or saving sensitive memory.

## Reference(s):

- [Collaboration protocol](references/collaboration_protocol.md)
- [Exception playbook](references/exception_playbook.md)
- [Walkthroughs](references/walkthroughs.md)
- [FAQ](references/faq.md)
- [Project homepage](https://github.com/YottaMeta/yotta-partner)
- [ClawHub release page](https://clawhub.ai/yottameta/skills/yotta-partner)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-partner)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Checklists, Handover notes]

**Output Format:** [Markdown with reusable templates and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-sized guidance; no runtime required.]

## Skill Version(s):

0.2.3 (source: SKILL.md frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
