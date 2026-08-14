## Description:

Generates accessible, TypeScript-typed React components that match a project's detected design system and UI library conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to generate new React UI components, stories, and tests that follow an existing project's component, styling, TypeScript, and accessibility patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect nearby project files to detect design-system and component patterns.

Mitigation: Run it in the intended project context and review generated code, imports, stories, and tests before committing.

Risk: Generated UI code may not fully match local accessibility, dependency, or design-system requirements.

Mitigation: Validate the output with the project's normal type checks, tests, accessibility review, and design-system review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/react-component-generator)
- [ClawHub publisher profile](https://clawhub.ai/user/heroinyan-stack)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with TypeScript, TSX, and test code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include component variants, Storybook stories, tests, dependency notes, and accessibility guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
