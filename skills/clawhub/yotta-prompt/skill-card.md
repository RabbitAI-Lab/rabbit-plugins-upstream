## Description:

Turns vague user requests into clear tasks by offering candidate directions, asking focused follow-up questions, and producing ready-to-run prompts that can route to related skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

External users who are unsure how to prompt an AI use the skill to clarify goals, scope, output, and constraints, then receive a self-contained prompt and an optional route to a related skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may remove files through loosely checked folder links.

Mitigation: Choose one agent or an exact destination, avoid linked destinations, review the resolved target, use dry-run when available, and back up existing files before updating.

Risk: Generated instructions can expand installation or persistent-storage scope.

Mitigation: Review each generated command and storage instruction; approve only the specific destination and behavior wanted, and remove the memory clause unless lasting storage is intended.

Risk: Recommended packages and future npm releases are not verified by the supplied evidence.

Mitigation: Use reviewed local files or an exact reviewed npm version.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-prompt)
- [Project homepage](https://github.com/YottaMeta/yotta-prompt)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-prompt)
- [FAQ](references/faq.md)
- [Scenario examples](references/scenarios.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Text or JSON CLI output, with Markdown examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate directions, follow-up questions, clarified task descriptions, ready-to-run prompts, and optional skill installation commands.]

## Skill Version(s):

0.2.5 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
