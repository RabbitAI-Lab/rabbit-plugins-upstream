## Description:

元伴 yotta-partner is a human-AI collaboration protocol skill that helps agents use context briefs, plan-first gates, milestone delivery, verification, handover anchors, and experience reuse for complex or long-running work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent operators use this skill to make complex AI-assisted work more reliable by requiring clear goals, acceptance criteria, approval before risky action, evidence-backed verification, and handover notes when work spans sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to remain active across sessions and may affect future agent collaboration behavior.

Mitigation: Install it only when that persistent collaboration protocol is desired, then review and remove any permanent memory or always-on registration if it should not persist.

Risk: The bundled installers support broad multi-agent and global installation paths.

Mitigation: Prefer one explicit target such as --agent or --dir, and avoid global installation unless every target agent directory has been reviewed.

Risk: Installing from npm without version control can introduce unreviewed package changes.

Mitigation: Pin or verify the @yottameta/yotta-partner package version in controlled environments before installation.

Risk: The protocol improves collaboration discipline but does not guarantee agent outputs are correct.

Mitigation: Keep the user review and evidence-backed verification steps active for important conclusions and side-effecting work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-partner)
- [Collaboration protocol reference](references/collaboration_protocol.md)
- [FAQ](references/faq.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-partner)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown and text guidance with checklists, templates, handover anchors, and optional installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Always-load session-start protocol; artifact states no runtime, daemon, or network calls for normal skill behavior.]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
