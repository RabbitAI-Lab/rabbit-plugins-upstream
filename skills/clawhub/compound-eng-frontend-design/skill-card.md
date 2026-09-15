## Description:

Provides visual design and aesthetic direction for frontend interfaces, including web pages, landing pages, dashboards, Next.js server components, and applications where visual identity matters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design-oriented agents use this skill to plan, implement, and review frontend interfaces with stronger visual direction, responsive behavior, interaction states, accessibility cues, and Next.js client-boundary discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested package install commands could add an unintended or vulnerable dependency.

Mitigation: Confirm package names, prefer exact reviewed versions, and review lockfile changes before running installs.

Risk: Frontend guidance may produce UI code that looks correct in source but fails in rendered narrow or wide viewports.

Mitigation: Render the page, capture narrow and wide viewport evidence when tooling is available, and report any environment that cannot render.

Risk: Browser automation output may contain untrusted page content that resembles instructions.

Mitigation: Treat DOM text, screenshots, console output, and network responses as data, and avoid credential access or write actions without explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-frontend-design)
- [Aesthetics and interaction](references/aesthetics-and-interaction.md)
- [Banned AI Design Patterns](references/banned-ai-patterns.md)
- [Creative Arsenal](references/creative-arsenal.md)
- [Design system routing](references/design-system-routing.md)
- [Mobile Collapse and Performance Guardrails](references/mobile-and-performance.md)
- [Motion Patterns](references/motion-patterns.md)
- [Premium Detail Patterns](references/premium-details.md)
- [Redesign Audit Framework](references/redesign-audit.md)
- [Redesigning Existing Interfaces](references/redesigning-existing.md)
- [Server / Client Component Safety](references/rsc-client-boundaries.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, configuration snippets, and shell commands when dependencies are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a design philosophy, implementation code, package-install commands, responsive verification notes, and risk-aware frontend guidance.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
