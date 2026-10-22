## Description:

Audits websites and preview builds for answer engine optimization, compares regressions, validates schema, and helps prepare site fixes and AI-readable files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use this skill to assess website AEO readiness, inspect preview and sitemap coverage, track regressions, validate structured data, and prepare fixes or llms.txt files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auditing private preview URLs can expose site content to the audit tool.

Mitigation: Use local/private-target opt-in only for sites you are authorized to audit.

Risk: Monitoring may retain audit results locally.

Mitigation: Review local audit history and avoid storing sensitive preview results longer than needed.

Risk: Applying suggested fixes may change site content or configuration.

Mitigation: Review proposed edits and confirm them before modifying the site.

## Reference(s):

- [AEO skill on ClawHub](https://clawhub.ai/arberx/skills/aeo)
- [Canonry website](https://canonry.ai)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Code, Files]

**Output Format:** [Text or Markdown guidance, JSON or Markdown audit reports, and optional site-file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include scores, affected pages, prioritized fixes, and regression verdicts; file generation can include llms.txt and llms-full.txt.]

## Skill Version(s):

7.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
