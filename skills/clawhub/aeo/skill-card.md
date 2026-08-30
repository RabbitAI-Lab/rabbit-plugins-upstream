## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and marketing engineers use this skill to audit and improve answer-engine optimization, schema quality, AI-readable files, crawler access, preview deployments, and regressions across public, staging, local, or static site outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a published npm audit CLI against public, local, or private targets and may read project or site content.

Mitigation: Install only if you are comfortable with the Canonry npm audit package, and use local or private audit flags only for systems you own or are authorized to test.

Risk: Requested fix and llms.txt workflows may write site-facing files such as llms.txt, llms-full.txt, and robots.txt.

Mitigation: Review generated changes and scan the site outputs before deployment.

## Reference(s):

- [Canonry homepage](https://canonry.ai)
- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON audit results, and site-facing text or configuration files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write llms.txt, llms-full.txt, and robots.txt during requested generation or fix workflows.]

## Skill Version(s):

7.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
