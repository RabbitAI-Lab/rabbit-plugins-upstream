## Description:

Turns workflows, analysis notes, dashboards, frameworks, and summaries into validated infographic plans, self-contained HTML visuals, optional PNG share images, and adapter drafts for SVG, whiteboard, and document workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, designers, product teams, growth teams, and knowledge workers use this skill to compress complex information into a single editable overview visual. It is best suited for explainers, summaries, comparisons, diagnostics, roadmaps, dashboards, and office-native handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted plan content or poorly reviewed source material can produce incorrect or misleading visuals.

Mitigation: Use trusted or reviewed plan content, validate plans before rendering, and review generated visuals before sharing.

Risk: Local scripts read plan JSON and write generated HTML, PNG, adapter, and document files to user-selected paths.

Mitigation: Choose output directories deliberately and inspect generated files before embedding them in downstream tools.

Risk: PNG export launches a local Chrome or Chromium process through the Chrome DevTools Protocol.

Mitigation: Run PNG export only in trusted local environments, set CHROME_PATH deliberately when needed, and review future API or credential-bearing integrations before granting access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/bonniegeng-max/skills/text-to-infographic)
- [README](README.md)
- [Infographic Plan Schema](schemas/infographic-plan.schema.json)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Infographic plan JSON, self-contained HTML, optional PNG, and adapter draft JSON/Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [HTML is the primary deliverable; PNG export requires local Chrome or Chromium; adapter drafts can produce SVG, whiteboard, and document structures.]

## Skill Version(s):

0.2.1 (source: server evidence, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
