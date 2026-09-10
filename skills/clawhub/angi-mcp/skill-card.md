## Description:

Read angi.com from a shell with the fpx CLI to find home-service pros by trade and city, inspect profiles, ratings, reviews, and list Angi taxonomy data without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve and parse Angi provider search results, profiles, ratings, reviews, and taxonomy data from shell workflows. It is useful when Angi data is needed in scripts or on machines where the MCP server is not installed.

### Deployment Geography for Use:

Global, for Angi's U.S. home-services directory.

## Known Risks and Mitigations:

Risk: Pairing fpx with a signed-in my.angi.com tab can allow the agent to read the user's own account data.

Mitigation: Use only a www.angi.com tab for public provider data, and pair my.angi.com only when signed-in account access is explicitly intended.

Risk: The setup installs @fetchproxy/cli globally without a pinned version.

Mitigation: Pin and review the @fetchproxy/cli version before installation, and install it without elevated privileges where possible.

Risk: Browser-tab access depends on the active tab state and Cloudflare clearance.

Mitigation: Keep the intended Angi host open in the browser, verify fpx health before fetching, and treat challenge or login pages as failed data fetches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)
- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC flight extractor](references/rsc.mjs)
- [Angi trade sitemap](https://www.angi.com/sitemap/statecat-sitemap.xml)
- [Angi geo sitemap example](https://www.angi.com/sitemap/angi-geocat-plumbing.xml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets, JavaScript helper code, and JSON-processing examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce fpx, curl, node, and jq command pipelines; the bundled extractor emits JSON arrays from Angi page HTML.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
