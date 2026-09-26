## Description:

Read angi.com home-services directory data from a shell with the fpx CLI, including providers by trade and city, provider profiles, ratings, reviews, and trade/city taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch and analyze Angi public directory pages from a browser-backed shell workflow when direct curl or Node requests cannot access the content. It also documents optional signed-in account reads when the user deliberately pairs a my.angi.com tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing my.angi.com lets the agent read signed-in Angi account pages such as projects or reviews.

Mitigation: Pair my.angi.com only when private account reads are intended, and review outputs for personal data before sharing or storing them.

Risk: Browser-backed fetching depends on an open, cleared Angi tab and may return login, challenge, or non-content pages if the tab state is wrong.

Mitigation: Keep the intended host tab open, use the documented fpx health and exit-code checks, and verify that fetched content is an Angi data page before parsing it.

Risk: Search pages can duplicate providers and include sponsored placements, which can mislead rankings or counts.

Mitigation: Use the documented dedupe key, keep sponsored placement flags visible, and rank with the unrounded rating fields when comparing providers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC flight extractor](references/rsc.mjs)
- [Angi](https://angi.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with shell, jq, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow guidance; optional signed-in account examples may expose private account data when the user pairs my.angi.com.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
