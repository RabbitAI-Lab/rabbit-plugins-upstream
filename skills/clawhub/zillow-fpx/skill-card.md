## Description:

Query zillow.com from a shell with the fpx CLI to search listings, fetch property records, histories, photos, market reports, and signed-in saved Zillow data through the user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Zillow listing, property, market, photo, and saved-account data from shell workflows when the Zillow MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill routes Zillow requests through a paired browser extension and the user's active Zillow tab.

Mitigation: Pair fpx only on machines and browser profiles where this access is intended, and review the active Zillow session before running commands.

Risk: Saved searches, saved homes, and generated temporary HTML or JSON files may expose private housing preferences or account-derived Zillow data.

Mitigation: Fetch saved-account pages only when needed for the task, and inspect or remove generated files before sharing logs, workspaces, or outputs.

## Reference(s):

- [Zillow pages for fpx](artifact/references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce temporary HTML or JSON dumps that can contain personal Zillow account data when saved-data pages are fetched.]

## Skill Version(s):

0.13.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
