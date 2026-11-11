## Description:

Build agent product UIs with Candor UI, a shadcn/ui registry of React components for agents that do real work - chat, tool calls, plans, approvals, diffs, run logs, traces, evals, admin and the app shell around them. Use when building or changing a React or Next.js interface for an AI agent, when the project's components.json lists the @candor registry, or when the user mentions Candor. Covers installing components, choosing the right one, wiring the Vercel AI SDK, Claude Agent SDK or AG-UI adapter, and the honesty rules every Candor screen follows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arunk3](https://clawhub.ai/user/arunk3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to design and build React or Next.js interfaces for AI agents, including conversations, approvals, plans, run activity, and administration. It guides component selection, installation, and connections to supported agent SDKs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions can download and run unpinned CLI package versions.

Mitigation: Review the commands and package sources before running them, and pin versions when reproducible or trusted installs are required.

Risk: The supplied security guidance flags sending a local CSS file to an external service as a consideration.

Mitigation: Check the destination and the CSS contents before sending any local file to an external service.

Risk: The security evidence says the scan was partial because several referenced paths were missing.

Mitigation: Review referenced files that were not included before relying on the scan as a complete assessment.

## Reference(s):

- [Candor component documentation index](https://candor.themethodic.com/llms.txt)
- [Candor principles](https://candor.themethodic.com/principles)
- [Component catalogue](artifact/references/components.md)
- [Design reference](artifact/references/design.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and TypeScript/TSX code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and setup guidance are tailored to the selected component and agent SDK.]

## Skill Version(s):

3.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
