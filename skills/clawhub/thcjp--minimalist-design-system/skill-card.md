## Description:

极简设计系统 helps front-end developers integrate a minimalist design system into React, Vue, Svelte, and Tailwind CSS projects by producing design tokens, reusable component guidance, and configuration snippets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and front-end engineers use this skill to audit an application's current UI stack, centralize design tokens, and generate implementation guidance for minimalist component systems. It is suited for new design-system initialization, style refactoring, component customization, and cross-framework adaptation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent that has exec access to install packages or run build commands while modifying front-end assets.

Mitigation: Approve package installs and build commands only when they directly match the visible project task, and review generated diffs before merging.

Risk: Generated UI code or design-system guidance can introduce unsafe DOM rendering, CSS injection paths, dependency exposure, or performance regressions if accepted without review.

Mitigation: Review generated code for unsafe HTML insertion, unsanitized class construction, dependency changes, and motion or shadow effects that may harm low-end device performance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/minimalist-design-system)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with CSS, JSON, TypeScript, Tailwind, and shell command snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CSS variables, Tailwind configuration fragments, component specifications, migration guidance, and troubleshooting steps.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
