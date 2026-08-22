## Description:

Generates English or French opening hooks and post titles for long-form articles, proposes distinct psychological angles, and asks the user to choose before continuing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, editors, marketers, and developers using an agent harness use this skill to draft opening hooks or post titles for long-form English or French articles while preserving article-type fit and avoiding common copywriting anti-patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may trigger on broad hook, intro, headline, or title requests that overlap with adjacent copywriting workflows.

Mitigation: Confirm publication context before use and keep it scoped to long-form article hooks or post titles, excluding social posts, email subjects, ads, landing-page headlines, press releases, SEO metadata, fiction, scripts, and body rewrites.

Risk: Generated persuasive copy can become misleading if it overpromises, uses unsupported statistics, or opens a curiosity gap the article does not close.

Mitigation: Review candidates against the article's evidence, payoff, audience, and the bundled anti-pattern guidance before using them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/copywriting-hooks)
- [cc-skills repository](https://github.com/samber/cc-skills)
- [Anglophone vs Francophone Traditions](references/anglophone-vs-francophone.md)
- [Hook Anti-Patterns](references/anti-patterns.md)
- [30 Hook Formulas: EN and FR Templates](references/formulas.md)
- [Post Title Formula Catalog](references/title-formulas.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown option sets with labeled candidates and follow-up selection prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 3-4 hook options with two candidates each, or 3-5 title candidates, then waits for user selection.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
