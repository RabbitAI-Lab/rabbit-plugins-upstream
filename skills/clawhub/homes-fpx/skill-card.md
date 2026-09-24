## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property details, photos, history, and read the signed-in user's saved homes through their own signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data workflows use this skill to generate shell commands and extraction recipes for querying homes.com listing, property, history, photo, nearby, saved-home, and saved-search pages through fpx.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an active homes.com browser session to access saved homes and saved searches, which may expose private account data.

Mitigation: Install only when comfortable using the active session, keep the fpx profile scoped to homes.com, and remove the pairing when it is no longer needed.

Risk: Address resolution and page scraping can return an unconfirmed or closest-match property result.

Mitigation: Verify candidate detail URLs and matched addresses against the requested address before relying on the result.

Risk: A missing sign-in session or uncleared AWS WAF challenge can return a sign-in redirect or challenge page instead of homes.com data.

Mitigation: Check response bodies and fpx exit codes, confirm a signed-in homes.com tab is open, and clear the WAF challenge before retrying.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, JavaScript, and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes and extraction guidance; runtime outputs may include HTML, JSON, and tabular text from homes.com responses.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
