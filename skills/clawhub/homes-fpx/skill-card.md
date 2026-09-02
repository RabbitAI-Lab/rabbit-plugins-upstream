## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property details, photos, and history, and read saved homes through the user's signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate shell-based homes.com data queries through fpx when MCP tooling is unavailable or unsuitable. It supports real-estate lookup workflows for public listing data and signed-in saved-home or saved-search pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access saved homes and saved searches through the user's signed-in homes.com browser session.

Mitigation: Use a dedicated browser session when possible, treat saved-home and saved-search output as private account data, and avoid retaining temporary files longer than needed.

Risk: Automated querying may conflict with homes.com's terms or trigger access controls.

Mitigation: Review homes.com's terms before use and keep query volume within acceptable manual-use expectations.

Risk: Address resolution can return a closest result instead of a confirmed property match.

Mitigation: Verify resolved candidate URLs and addresses against the requested street address before relying on detail-page data.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell, JavaScript, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on a paired fpx profile, the Transporter extension, and the user's active homes.com browser session.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
