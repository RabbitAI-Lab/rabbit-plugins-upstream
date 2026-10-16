## Description:

Guides React and Next.js development with TypeScript architecture, state management, Tailwind styling, testing, and locale synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to implement and review React or Next.js interfaces, choose component and state patterns, write tests, and maintain frontend styling and translations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Playwright authentication state can expose a reusable test session if committed.

Mitigation: Keep e2e/.auth/user.json out of version control and use low-privilege test accounts.

Risk: Running package or test commands may execute repository dependencies.

Mitigation: Run npx and test commands only in repositories whose dependencies you trust.

## Reference(s):

- [Components, state, and interaction](references/components-and-state.md)
- [Rendering and framework patterns](references/rendering-and-frameworks.md)
- [Tailwind CSS guidance](references/tailwind.md)
- [Testing examples](references/testing.md)
- [Test selection](references/test-selection.md)
- [Playwright E2E testing](references/e2e-testing.md)
- [JSON locale synchronization](references/locale-synchronization.md)

## Skill Output:

**Output Type(s):** [Code, Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include focused code changes, tests, and locale diffs.]

## Skill Version(s):

5.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
