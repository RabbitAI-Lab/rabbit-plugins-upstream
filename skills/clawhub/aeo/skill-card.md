## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and marketing engineers use this skill to audit and improve how websites expose content to answer engines, crawlers, schema validators, and AI-readable files. It supports deployed sites, preview branches, local builds with explicit private-target opt-in, static HTML output, regression checks, and guided fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a dynamically resolved npm CLI with the agent's normal file, environment, and network permissions.

Mitigation: Run it in a sandbox with minimal environment variables, and pin or preinstall a reviewed exact package version before use in sensitive repositories or CI.

Risk: Local or private preview audits can reach internal targets when the user explicitly opts in.

Mitigation: Use local/private audit flags only for targets the user controls, keep the scope to the named host, and review any sitemap origin rewriting before crawling.

Risk: Fix and llms.txt workflows may modify site files or AI-readable public metadata.

Mitigation: Require user confirmation before edits, review generated diffs, and rerun the relevant audit or validation mode after changes.

## Reference(s):

- [Canonry AEO Homepage](https://canonry.ai)
- [ClawHub Skill Page](https://clawhub.ai/arberx/skills/aeo)
- [Publisher Profile](https://clawhub.ai/user/arberx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON or agent-format audit reports, and file edits for approved fixes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate or update llms.txt, llms-full.txt, robots.txt, structured data, and comparison summaries when the selected workflow calls for those outputs.]

## Skill Version(s):

7.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
