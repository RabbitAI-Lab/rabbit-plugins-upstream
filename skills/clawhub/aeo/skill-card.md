## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and marketing engineers use this skill to audit answer-engine optimization signals, compare preview or branch changes against production, validate schema, generate AI-readable site files, and apply site fixes after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill executes an npm CLI that fetches and analyzes websites.

Mitigation: Run audits only against intended targets, quote validated arguments, and review generated commands before execution.

Risk: Local or private audit flags can access localhost, private IPs, or staging systems.

Mitigation: Use local/private flags only for systems the user controls and only after explicit opt-in.

Risk: Fix and llms.txt workflows may generate or change site files.

Mitigation: Review proposed edits before applying them and verify changes with a follow-up audit when practical.

Risk: Optional Lighthouse/PageSpeed checks can use a PageSpeed API key.

Mitigation: Provide API keys only when intentionally enabling those checks and avoid exposing secrets in shared logs or prompts.

## Reference(s):

- [AEO ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)
- [Canonry homepage](https://canonry.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON audit reports, and optional generated or modified site files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce audit scores, prioritized fixes, regression verdicts, schema guidance, llms.txt content, robots.txt updates, and code or configuration edits when the user asks for fixes.]

## Skill Version(s):

6.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
