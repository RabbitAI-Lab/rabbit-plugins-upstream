## Description:

Tailwind CSS v4 patterns: CSS-first config, utility classes, component variants, v3 migration, theme tokens, dark mode, and style fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when styling Tailwind CSS v4 projects, configuring CSS-first theme tokens, building component variants, migrating from Tailwind v3, or resolving missing styles and dark mode behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tailwind CSS v4 syntax and migration guidance can become stale or be misapplied to a project's actual configuration.

Mitigation: Verify current Tailwind v4 documentation for version-specific syntax, then review generated changes against the project configuration.

Risk: Agent-suggested style changes may silently fail when utilities are not scanned or generated.

Mitigation: Run the project build or Tailwind generation step and inspect compiled CSS for expected utilities when class names, tokens, or source paths change.

Risk: Layout guidance can affect scrolling, overlays, focus rings, or visibility behavior in ways unit tests may not catch.

Mitigation: Validate affected layout, overlay, focus, and visibility behavior in a browser before release.

## Reference(s):

- [Component Patterns](artifact/references/component-patterns.md)
- [Layout Patterns](artifact/references/layout-patterns.md)
- [Configuration and Migration](artifact/references/configuration-and-migration.md)
- [Class Generation and Composition](artifact/references/class-generation-and-composition.md)
- [v3 to v4 Breaking Changes](artifact/references/v3-to-v4-migration.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance for Tailwind CSS v4 implementation, migration, class composition, and validation.]

## Skill Version(s):

4.5.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
