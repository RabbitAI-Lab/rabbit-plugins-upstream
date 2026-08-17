## Description:

Read angi.com public home-services directory data from a shell with the fpx CLI, including pros by trade and city, profiles, ratings, reviews, and trade/city taxonomy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Angi public directory data and produce shell pipelines for extracting provider, rating, review, and taxonomy information. It can also guide optional authenticated reads of the user's own Angi account data when explicitly intended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent browser-tab fetch bridge can expose data available through the user's Angi browser session.

Mitigation: Install only when comfortable granting that bridge, keep pairing limited to intended Angi hosts, and avoid widening browser scope beyond fetch access.

Risk: Signed-in my.angi.com examples can read private account data through the user's own session.

Mitigation: Run signed-in examples only when the user explicitly intends to expose their own Angi account data to the agent, and review outputs before sharing or storing them.

## Reference(s):

- [Angi page shapes and recipes](artifact/references/angi-pages.md)
- [Angi RSC flight extractor](artifact/references/rsc.mjs)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi trade sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript extractor usage, and JSON/jq recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented Angi data extraction guidance; optional signed-in account examples depend on the user's active browser session.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
