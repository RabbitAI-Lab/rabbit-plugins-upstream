## Description:

Read angi.com home-services directory pages from a shell with the fpx CLI to find providers by trade and city, inspect provider profiles, ratings, reviews, and list the trade and city taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Angi directory information, extract provider and review records from fetched pages, and receive command recipes for taxonomy, search, profile, and review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent browser bridge can let the agent fetch pages through the user's open Angi browser tab.

Mitigation: Pair only the required Angi host, keep browser site access scoped to angi.com, and review the skill before installation.

Risk: Optional my.angi.com workflows can expose signed-in account pages beyond public directory lookup.

Mitigation: Do not pair my.angi.com unless account-page access is intended, and treat returned account data as user-private.

Risk: Installing @fetchproxy/cli globally may use a mutable package version.

Mitigation: Prefer a pinned or local fpx CLI installation for controlled environments.

Risk: Angi page structures are undocumented and can drift, which can produce incomplete or misleading extracted records.

Mitigation: Validate city and trade slugs through sitemaps, use the documented dedupe option on search pages, and re-fetch pages when unresolved row references appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](artifact/references/angi-pages.md)
- [Angi RSC flight extractor](artifact/references/rsc.mjs)
- [Angi website](https://angi.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, jq, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only command guidance and extraction recipes; optional signed-in account examples require an already signed-in Angi browser tab.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
