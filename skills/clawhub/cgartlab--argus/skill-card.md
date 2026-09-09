## Description:

Argus Design Review audits frontend code for design token usage, hardcoded values, dark mode coverage, accessibility, CSS consistency, semantic HTML, and stack-aware framework API usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review frontend components, pages, and design systems for design quality, accessibility gaps, CSS issues, semantic HTML problems, and framework API mistakes. It returns prioritized findings with copy-ready fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated review fixes may be incorrect, incomplete, or inconsistent with a repository's design system.

Mitigation: Review proposed fixes before merging and run the repository's lint, type-check, accessibility, and visual regression checks where available.

Risk: Separate GitHub App or composite action usage can read pull request code and post comments.

Mitigation: Review and pin that external automation separately before enabling it in repositories.

## Reference(s):

- [Argus Skill Page](https://clawhub.ai/cgartlab/skills/argus)
- [React Documentation](https://react.dev)
- [Vue Guide](https://vuejs.org/guide)
- [Svelte Documentation](https://svelte.dev/docs)
- [Angular API](https://angular.dev/api)
- [Astro Documentation](https://docs.astro.build)
- [Lit Documentation](https://lit.dev/docs)
- [UnoCSS Documentation](https://uno.antfu.me/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [MDN CSS Documentation](https://developer.mozilla.org/docs/Web/CSS)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Guidance]

**Output Format:** [Markdown with prioritized issue blocks and copy-ready code fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are grouped by P0 through P3 severity and include file:line prefixes when issues are found.]

## Skill Version(s):

0.4.1 (source: frontmatter, manifest.yaml, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
