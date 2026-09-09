## Description:

Yotta Anti-Shallow is a rule-only agent skill that prompts agents to analyze before acting, state uncertainty, seek confirmation on complex tasks, and self-check their work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to add a persistent quality discipline to complex agent tasks such as development, bug fixing, architecture review, data analysis, documentation, and open-ended Q&A. It is intended to improve reasoning transparency and completion checks, not to replace tests or human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently changes agent behavior on complex tasks.

Mitigation: Install it only when the extra analysis, confirmation, and self-check steps are desired; uninstall it if those behaviors appear where they are not wanted.

Risk: Installers can write the skill into many agent skill directories.

Mitigation: Prefer a pinned package version, avoid sudo or administrator execution, and use --agent or a carefully checked --dir target instead of global installation.

## Reference(s):

- [Skill README](README.md)
- [FAQ](references/faq.md)
- [Complex Scenario Walkthroughs](references/walkthroughs.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-anti-shallow)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text responses with analysis, confidence, and self-check sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill shapes agent responses; it does not execute code, call external tools, or replace tests and human review.]

## Skill Version(s):

1.4.0 (source: frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
