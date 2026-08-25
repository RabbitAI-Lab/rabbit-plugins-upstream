## Description:

Argus Design Review helps agents audit frontend code for design token use, hardcoded values, dark mode coverage, accessibility, CSS/HTML quality, and stack-aware framework API usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review frontend components, pages, pull requests, and design systems for design consistency, accessibility gaps, dark mode issues, and framework-specific API problems. The skill returns severity-grouped findings with copy-ready fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be mistaken for a full security audit because some metadata mentions security review.

Mitigation: Use it for frontend design, accessibility, design-token, CSS, and framework API review; perform a separate security audit for security assurance.

Risk: Suggested fixes or automated PR comments could introduce incorrect or misleading guidance if applied without review.

Mitigation: Review proposed fixes and comments before applying them automatically or merging changes.

## Reference(s):

- [Argus Design Review on ClawHub](https://clawhub.ai/cgartlab/skills/argus)
- [React Reference](https://react.dev/reference)
- [Vue Essentials Guide](https://vuejs.org/guide/essentials)
- [Angular Guide](https://angular.dev/guide)
- [Svelte Documentation](https://svelte.dev/docs)
- [Astro Documentation](https://docs.astro.build)
- [Lit Documentation](https://lit.dev/docs)
- [MDN CSS Documentation](https://developer.mozilla.org/docs/Web/CSS)

## Skill Output:

**Output Type(s):** [markdown, code, guidance]

**Output Format:** [Markdown review report with severity-grouped issues, found-versus-expected snippets, references, and copy-ready code fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review output is organized by P0 through P3 severity and includes official documentation links for framework API findings.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
