## Description:

Read angi.com from a shell with the fpx CLI to find home-service professionals by trade and city, inspect profiles, ratings and reviews, and list trade/city taxonomy without running the angi-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch and parse Angi public directory pages from a browser-backed fpx session, producing shell workflows and JSON extraction patterns for provider search, profile review analysis, and taxonomy lookup. Users may also read their own signed-in Angi account pages when intentionally paired with my.angi.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-backed fetching through fpx and the Transporter extension can access pages available to the paired browser tab.

Mitigation: Pair only the www.angi.com subdomain for public directory lookups and pair my.angi.com only when the user intentionally wants account data read.

Risk: Optional signed-in account reads may expose the user's own Angi projects or reviews to the agent session.

Mitigation: Keep signed-in account reads disabled unless needed, verify the paired host before fetching, and review outputs before sharing them.

Risk: Angi page structures and undocumented record fields may change or be incomplete.

Mitigation: Use the documented sitemap checks and parser recipes, validate extracted fields before relying on them, and do not assume unknown account fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC flight extractor](references/rsc.mjs)
- [Angi state/category sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)
- [Angi geo/category sitemap](https://www.angi.com/sitemap/angi-geocat-plumbing.xml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript parser usage, and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the fpx CLI, the Transporter browser extension, and an open paired Angi tab for page reads; optional my.angi.com pairing can read the user's own signed-in account pages.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
