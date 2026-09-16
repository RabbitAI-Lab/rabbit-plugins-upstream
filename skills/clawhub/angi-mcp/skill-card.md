## Description:

Read angi.com from a shell with the fpx CLI to find home-service pros by trade and city, inspect profiles, ratings breakdowns and reviews, and list trade/city taxonomy without running the angi-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve and analyze Angi public directory data through command-line workflows, including provider search, profile review extraction, ratings analysis, and taxonomy lookup. Users can optionally read their own signed-in Angi account data when they intentionally pair a my.angi.com browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser-tab bridge can fetch through the user's browser context, including signed-in Angi account pages if my.angi.com is paired.

Mitigation: Pair only www.angi.com for public directory use, and pair my.angi.com only when the user intentionally wants account data read.

Risk: The setup uses a global npm install for @fetchproxy/cli, which can introduce version drift or supply-chain exposure.

Mitigation: Pin the fpx CLI version or install it locally for controlled execution.

Risk: Angi page data is extracted from undocumented page payloads and may duplicate records or omit expected fields.

Mitigation: Use the documented dedupe option, resolve trade and city slugs from sitemaps before fetching, and validate extracted fields before acting on them.

## Reference(s):

- [Angi page shapes and recipes](artifact/references/angi-pages.md)
- [Angi RSC flight extractor](artifact/references/rsc.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi trade sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)
- [Angi plumbing geo sitemap](https://www.angi.com/sitemap/angi-geocat-plumbing.xml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command pipelines and JSON-processing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include fpx, curl, node, jq, sed, and grep command examples plus JSON records extracted from Angi pages.]

## Skill Version(s):

0.3.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
