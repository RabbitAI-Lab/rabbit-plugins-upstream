## Description:

Helps agents build or update React and Next.js interfaces for AI agents using Candor UI components, SDK adapters, installation guidance, and patterns for transparent, user-controlled interactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arunk3](https://clawhub.ai/user/arunk3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to choose and install Candor UI components, connect an agent SDK, and build React or Next.js screens for agent conversations, approvals, work tracking, and operations. It guides interface behavior that keeps agent actions and decisions clear to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious and notes unpinned command-line packages and a workflow that sends local CSS to a third-party service.

Mitigation: Review package commands before running them, prefer pinned versions where practical, and inspect CSS contents before sending them to an external service.

Risk: The scan was partial and several referenced paths or files were missing, so it does not establish that the artifact is safe.

Mitigation: Review the missing files and the complete skill contents before relying on the scan as a safety assessment.

## Reference(s):

- [Candor UI component reference](references/components.md)
- [Candor UI design system](references/design.md)
- [Candor UI documentation index](https://candor.themethodic.com/llms.txt)
- [Candor UI 4.0 token upgrade guide](https://candor.themethodic.com/upgrading-to-4#tokens-cd-prefix)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and implementation guidance for React and Next.js agent interfaces.]

## Skill Version(s):

4.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
