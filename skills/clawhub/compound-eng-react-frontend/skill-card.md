## Description:

Provides React architecture, TypeScript, Next.js, hooks, and testing guidance for agents working on component structure, state management, routing, Vitest, React Testing Library, or React code review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide React and TypeScript implementation or review, including component structure, state management, Next.js routing, hooks, and test coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: E2E testing guidance can lead agents to persist reusable login state or credentials in project files.

Mitigation: Treat Playwright storage-state files as secrets, keep e2e/.auth/ out of version control and release artifacts, use environment or CI secret stores for credentials, and use dedicated low-privilege test accounts.

## Reference(s):

- [Components, State, and Interaction](references/components-and-state.md)
- [E2E Testing with Playwright](references/e2e-testing.md)
- [Rendering and Framework Patterns](references/rendering-and-frameworks.md)
- [Test Selection](references/test-selection.md)
- [Testing React (Vitest + RTL)](references/testing.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with TypeScript, TSX, configuration, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include React, Next.js, Vitest, React Testing Library, and Playwright patterns.]

## Skill Version(s):

4.5.2 (source: server release evidence, changelog v4.5.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
