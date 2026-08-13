## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and marketing engineers use this skill to evaluate whether a website is ready for AI answer engines, diagnose structured data and AI-access issues, compare preview or branch changes, and generate practical remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run an npm audit tool against public URLs or explicitly allowed local/private sites.

Mitigation: Confirm the target is in scope before running audits, and require explicit user intent before using local or private target options.

Risk: The skill can generate or update llms.txt, llms-full.txt, and robots.txt, which may change crawler or AI access policy.

Mitigation: Review proposed file edits before approval, especially changes that affect crawler access, AI indexing, or site visibility.

## Reference(s):

- [Canonry homepage](https://canonry.ai)
- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with inline shell commands; audit reports may be JSON, agent JSON, or Markdown depending on the selected command flags.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or write llms.txt, llms-full.txt, and robots.txt when the user asks for site fixes or AI-access file generation.]

## Skill Version(s):

4.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
