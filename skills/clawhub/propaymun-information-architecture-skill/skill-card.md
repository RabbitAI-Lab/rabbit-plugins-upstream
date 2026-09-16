## Description:

Shape, review, and validate end-to-end product information architecture, product/UX sitemaps, and stateful user flows when users need clearer structure, labels, relationships, access, findability, destinations, or task paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kamroncorp](https://clawhub.ai/user/kamroncorp)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams, designers, content strategists, and builders use this skill to reason through product information architecture, product/UX sitemaps, and stateful user flows. It helps turn product evidence into clear structures, labels, relationships, access decisions, findability guidance, and human or technical handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional helpers can create local HTML or Markdown files when explicitly run.

Mitigation: Run helper scripts only after the user has requested the output and supplied approved local paths; preserve existing files.

Risk: Builder handoffs may contain structured product information from user briefs.

Mitigation: Avoid including confidential briefs unless the target environment is approved for that information.

## Reference(s):

- [Capability-aware execution and output routing](references/capability-routing.md)
- [IA deliverables and semantic model](references/deliverables.md)
- [Optional IA diagramming](references/diagramming.md)
- [Discovery and low-effort interaction](references/discovery.md)
- [Evidence and uncertainty](references/evidence.md)
- [IA foundations and decision rules](references/ia-foundations.md)
- [Contextual localization](references/localization.md)
- [Modeling and option generation](references/modeling.md)
- [Product and UX sitemap](references/sitemap.md)
- [Stateful user flow](references/user-flow.md)
- [IA validation and measurement](references/validation.md)
- [Visual Builder Handoff](references/visual-builder-handoff.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, standalone HTML, and shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional standard-library helpers can validate IA models, validate companion models, render IA HTML, or export visual-builder handoffs when explicitly requested with paths.]

## Skill Version(s):

1.0.4 (source: evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
