## Description:

Yotta-partner is a human-AI collaboration protocol skill that helps agents run complex or cross-session work through context briefs, plan-first approval, milestone delivery, verification, handover anchors, and experience reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and agent users apply this skill to keep complex, long-running, side-effecting, or cross-session work disciplined: define goals and acceptance criteria, require plan-first execution, verify outputs, and leave reusable handover state. The skill is for collaboration productivity and does not provide marketing, operations, trading, or domain-specific decision advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to be always loaded at session start and can shape many agent interactions.

Mitigation: Install it only when a broad collaboration protocol is desired, and rely on its 30-second task gate so simple questions remain lightweight.

Risk: Installer scripts can copy the skill into user-level or multiple agent skill directories.

Mitigation: Prefer pinned package versions or manual review before running npx or install scripts, and avoid global installation unless the skill should apply across all supported agents.

Risk: Handover, state, or memory records could capture sensitive project details if written carelessly.

Mitigation: Require explicit user agreement before persistent memory or host-configuration changes, and inspect any project state or memory entry before it is recorded.

Risk: The protocol improves collaboration discipline but does not guarantee that the agent's substantive output is correct.

Mitigation: Use the skill's acceptance criteria, evidence, dry-run, and user-review checks before treating outputs as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-partner)
- [Project homepage](https://github.com/YottaMeta/yotta-partner)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-partner)
- [Collaboration protocol](references/collaboration_protocol.md)
- [Exception playbook](references/exception_playbook.md)
- [Walkthroughs](references/walkthroughs.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown text with context briefs, plans, checklists, validation notes, and handover anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persistent memory or host-configuration changes require explicit user agreement; records should state where they were written.]

## Skill Version(s):

0.2.1 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
