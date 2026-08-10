## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site operators, and SEO/AEO teams use this skill to audit websites for AI discoverability, compare production and preview changes, validate structured data, generate llms.txt assets, and guide targeted site fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a published npm audit package that fetches target websites, including local or private targets when explicitly allowed.

Mitigation: Confirm the target is owned or authorized for audit, use local/private auditing only with explicit intent, and review command arguments before execution.

Risk: Fix and llms.txt workflows can write AEO-related site files such as llms.txt, llms-full.txt, and robots.txt.

Mitigation: Review proposed file changes before approval and verify generated content against the site's intended crawler and AI-access policy.

## Reference(s):

- [Canonry homepage](https://canonry.ai)
- [ClawHub skill listing](https://clawhub.ai/arberx/skills/aeo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON summaries, inline shell commands, and generated or edited site files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce audit scores, factor breakdowns, prioritized fixes, regression comparisons, schema examples, and llms.txt or robots.txt file content.]

## Skill Version(s):

4.6.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
