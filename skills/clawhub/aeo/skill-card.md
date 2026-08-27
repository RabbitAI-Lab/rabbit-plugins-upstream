## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site teams, and agents use this skill to audit websites for answer-engine readiness, review preview or static builds, compare regressions, validate schema, and generate AI-readable site metadata files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates website audits to the third-party npm package @canonry/aeo-audit via npx.

Mitigation: Review the command before execution and use the disclosed package invocation from the skill.

Risk: Local or private audits can target non-public systems.

Mitigation: Run local/private audits only for systems the user controls and only with explicit opt-in.

Risk: Proposed site fixes can affect public metadata, schema, or crawler access files.

Mitigation: Review proposed changes before approval and rerun the audit to confirm the intended effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)
- [Publisher profile](https://clawhub.ai/user/arberx)
- [Canonry website](https://canonry.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON audit summaries, inline shell commands, and generated site metadata files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update llms.txt, llms-full.txt, and robots.txt when the user requests file generation.]

## Skill Version(s):

7.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
