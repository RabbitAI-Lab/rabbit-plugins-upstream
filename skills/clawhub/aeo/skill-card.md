## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site maintainers, and marketing engineering teams use this skill to audit websites or built site output for AI answer readiness, schema quality, auxiliary AI access files, and release regressions. It can guide command execution, summarize audit findings, compare reports, and propose or write targeted site files when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands for fix, llms, monitor, local/private targets, and output-file flags can read project content, write public-facing files, or save comparison results.

Mitigation: Review proposed commands before execution, require explicit opt-in for local/private targets, and confirm file writes or output paths before running those modes.

Risk: Generated llms.txt, llms-full.txt, robots.txt, schema, or site fixes may affect public crawler and AI access behavior.

Mitigation: Inspect generated files and proposed site changes before publishing or deploying them.

## Reference(s):

- [Canonry](https://canonry.ai)
- [AEO audit repository](https://github.com/Canonry/aeo-audit)
- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command snippets, JSON audit summaries, and generated text or configuration files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write llms.txt, llms-full.txt, robots.txt, and comparison or report files when the user requests those modes.]

## Skill Version(s):

5.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
