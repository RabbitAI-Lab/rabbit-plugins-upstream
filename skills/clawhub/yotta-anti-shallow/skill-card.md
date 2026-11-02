## Description:

元谨 is a quality-discipline skill that prompts agents to analyze complex tasks before acting, check their work, and report uncertainty without taking over execution or tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users apply this skill to complex analysis, coding, writing, and verification tasks to reduce unsupported guesses and shallow completion. It scales review depth to task complexity and leaves task choices under the user's explicit instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The FAQ and main skill file differ on which rules users can disable, which may lead to inconsistent handling of override requests.

Mitigation: Review the main SKILL.md sections R007 and R008 as the intended behavior before rollout.

Risk: Installing the package can affect files in an agent's selected skill directory, including local customizations.

Mitigation: Choose one explicit installation directory, back up customizations, and use a reviewed, pinned package version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [Project homepage](https://github.com/YottaMeta/yotta-anti-shallow)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-anti-shallow)
- [FAQ](references/faq.md)
- [Walkthroughs](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Natural-language guidance with analysis, verification, and self-check sections when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts depth to task complexity; does not execute code or call external tools.]

## Skill Version(s):

1.4.3 (source: frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
