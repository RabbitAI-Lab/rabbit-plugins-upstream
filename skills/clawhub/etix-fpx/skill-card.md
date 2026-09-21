## Description:

Query public etix.com event discovery data from a shell with the @fetchproxy/cli fpx tool through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users use this skill to retrieve public Etix event, venue, performer, and geolocation discovery data from shell scripts without running the etix-mcp server. The documented scope is anonymous discovery reads only, not ticket purchasing or account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a persistent paired browser fetch profile and Transporter extension access for etix.com.

Mitigation: Install and pair fpx only in an environment where that browser-extension access is acceptable, and keep the profile scoped to etix.com fetch use.

Risk: Etix HTML responses can still be a DataDome interstitial even when the fetch command exits successfully.

Mitigation: Check fetched HTML for DataDome challenge text before parsing or trusting event and venue detail output.

Risk: Ticket purchasing and account actions are financial or account workflows outside the documented skill scope.

Mitigation: Use the skill only for anonymous public discovery reads and avoid purchase, login, or account-management actions.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON extraction examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the fpx CLI, the Transporter browser extension, and a paired etix.com browser profile for live fetches.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
