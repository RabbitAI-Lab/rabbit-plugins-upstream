## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and marketing engineers use this skill to audit and improve answer-engine optimization, schema quality, AI-readable site files, preview deployments, and regression checks for websites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audits fetch user-provided URLs and the skill runs the published @ainyc/aeo-audit npm package.

Mitigation: Use the skill only for URLs or static outputs you intend to audit, and review the package execution context before running commands.

Risk: Local or private preview audits can expose a local development server to the audit workflow when explicitly enabled.

Mitigation: Use local/private URL auditing only when intended, and require explicit opt-in before passing local/private access flags.

Risk: Fix mode can make scoped website file changes.

Mitigation: Review proposed changes and approve them before editing files, then inspect the resulting diff.

## Reference(s):

- [AEO homepage](https://ainyc.ai)
- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)
- [Publisher profile](https://clawhub.ai/user/arberx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON audit reports, code/configuration changes, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce llms.txt, llms-full.txt, robots.txt, JSON-LD examples, audit summaries, regression reports, and scoped website file changes after user confirmation.]

## Skill Version(s):

4.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
