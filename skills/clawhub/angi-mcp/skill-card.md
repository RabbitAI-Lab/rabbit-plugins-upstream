## Description:

Read angi.com from a shell with the fpx CLI to find home-service pros by trade and city, inspect pro profiles, ratings, reviews, and list trade or city taxonomy without running the angi-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Angi directory pages, parse provider and review records, and produce shell-based data extraction workflows for local analysis. Optional signed-in examples are limited to the user's own Angi account data.

### Deployment Geography for Use:

Global, with Angi directory data coverage focused on the United States.

## Known Risks and Mitigations:

Risk: Pairing fpx with an Angi browser tab can use the tab's current session, including optional signed-in my.angi.com pages.

Mitigation: Keep the profile limited to fetch capability, avoid adding cookie, storage, or header scopes, and use signed-in examples only when intentionally reading the user's own account data.

Risk: Wrong trade or city paths, duplicate sponsored/list rows, or unsupported zip filters can produce misleading provider results.

Mitigation: Resolve trade and city combinations from Angi sitemaps, deduplicate search results by id, and treat location as path-based rather than zip-based.

Risk: Cloudflare challenge pages or login redirects may return successful HTTP responses that are not the intended Angi data.

Mitigation: Confirm the response is the expected page content, refresh or re-pair the relevant tab when clearance is lost, and check signed-in state before parsing account pages.

## Reference(s):

- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC flight extractor](references/rsc.mjs)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi](https://angi.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JavaScript helper usage, and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflows; generated commands may fetch public Angi pages through a user-approved browser tab and parse results as JSON.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
