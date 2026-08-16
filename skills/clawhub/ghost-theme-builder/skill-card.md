## Description:

Build, customize, review, debug, migrate, and optimize Ghost CMS Handlebars themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frontendweb](https://clawhub.ai/user/frontendweb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, customize, review, debug, migrate, and optimize Ghost CMS themes with Ghost Handlebars templates, routes, custom settings, memberships, search, sharing, and GScan validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose changes to Ghost theme files, membership signup flows, newsletter behavior, routes.yaml, scripts, or code-injection areas that affect a live site.

Mitigation: Review generated theme, membership, newsletter, routes.yaml, script, and code-injection changes before publishing; prefer visible newsletter choices and audit anything rendered through Ghost Code Injection.

Risk: Theme changes can introduce rendering, accessibility, SEO, or validation regressions.

Mitigation: Run GScan and any available theme build or lint command separately, and manually review accessibility, metadata, member-state UI, and responsive behavior before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/frontendweb/skills/ghost-theme-builder)
- [Ghost CMS](https://ghost.org)
- [Theme Structure Reference](artifact/docs/structure.md)
- [GScan Reference](artifact/docs/gscan.md)
- [Ghost Theme Contexts Reference](artifact/reference/contexts.md)
- [Ghost Helpers Reference](artifact/reference/helpers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, configuration snippets, file-change summaries, and review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Ghost theme template code, routes.yaml/package.json guidance, GScan commands, and issue-focused review notes.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
