## Description:

Tailwind CSS v4 patterns: CSS-first config, utility classes, component variants, v3 migration, style fixes, and dark mode guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when styling Tailwind CSS projects, configuring v4 theme tokens, composing component variants, migrating v3 projects to v4, or diagnosing missing and conflicting utility classes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tailwind v4 syntax and migration behavior can change, and stale guidance could introduce broken styles.

Mitigation: Check current Tailwind documentation before applying v4-specific syntax and run the project build or generated CSS inspection after changes.

Risk: Dynamically constructed or unscanned utility classes may silently fail to generate CSS.

Mitigation: Keep utility names as complete source literals, confirm source scan paths, and inspect compiled CSS for expected utilities.

Risk: Layout changes involving overflow, hidden visibility, overlays, or focus behavior may appear correct in unit tests but fail in a browser.

Mitigation: Verify affected layouts in a browser and test overlay escape, scrolling, and visibility behavior directly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-tailwind-css)
- [Component Patterns](references/component-patterns.md)
- [Layout Patterns](references/layout-patterns.md)
- [Configuration and Migration](references/configuration-and-migration.md)
- [Class Generation and Composition](references/class-generation-and-composition.md)
- [v3 to v4 Breaking Changes](references/v3-to-v4-migration.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Tailwind CSS snippets, framework component examples, migration checklists, and verification commands.]

## Skill Version(s):

4.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
