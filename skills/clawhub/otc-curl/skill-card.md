## Description:

Helps agents query public On the Cheap city sites for local event listings and free or low-cost deal articles using curl, jq, and small parsing recipes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when the On the Cheap MCP server is unavailable and they need shell-based retrieval of local event schedules, venue details, prices, and deal articles from public city sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may show expired deals if the per-site expired category is not excluded.

Mitigation: Resolve the expired category ID for the selected site before querying posts and apply it as a categories_exclude filter.

Risk: Event pages can return misleading results when dates are requested in ISO format.

Mitigation: Convert dates to the documented M-D-YYYY path format and confirm the rendered event heading matches the requested date.

Risk: Monthly calendar pages can undercount events because cells show only a limited number of listings.

Mitigation: Use month pages for overview counts only, then fetch day pages for complete event listings.

## Reference(s):

- [otc-curl on ClawHub](https://clawhub.ai/chrischall/skills/otc-curl)
- [Ready-to-run recipes](artifact/references/recipes.md)
- [Charlotte on the Cheap](https://www.charlotteonthecheap.com)
- [Mile High on the Cheap](https://www.milehighonthecheap.com)
- [Triangle on the Cheap](https://triangleonthecheap.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, guidance]

**Output Format:** [Markdown with inline bash, jq, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-only retrieval and parsing guidance for public web pages and WordPress REST responses.]

## Skill Version(s):

0.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
