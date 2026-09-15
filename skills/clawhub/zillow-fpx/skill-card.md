## Description:

Query Zillow from a shell with the fpx CLI to search listings, retrieve property records, histories, photos, market reports, and signed-in saved searches or homes through a browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide one-shot shell retrieval of Zillow listing, property, market, photo, and saved-account data when they want fpx-based access instead of running the Zillow MCP server.

### Deployment Geography for Use:

Global, for Zillow U.S. real-estate data

## Known Risks and Mitigations:

Risk: The paired browser bridge can reuse a signed-in Zillow session and expose saved searches, saved homes, or other account data.

Mitigation: Use a dedicated browser profile or a signed-out Zillow tab unless saved data is required, and revoke the pairing when finished.

Risk: Fetched Zillow page data, including account-backed data, may be written to temporary files during command examples.

Mitigation: Store outputs in a private workspace, avoid shared /tmp files for account data, and delete fetched pages when they are no longer needed.

Risk: Signed-out redirects, captcha pages, or bot-wall responses can appear as successful fetches.

Mitigation: Check the final response body or URL for login and captcha markers before trusting empty or unexpected results.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with shell, Python, and jq snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands fetch Zillow HTML through a paired browser session and parse page-state JSON from the response.]

## Skill Version(s):

0.13.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
