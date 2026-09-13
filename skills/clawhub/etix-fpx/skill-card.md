## Description:

Query etix.com event discovery data from a shell with the fpx CLI, including event, venue, performer, geolocation, and detail lookups through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate shell commands and extraction guidance for public Etix event discovery workflows without running the Etix MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent Etix-scoped browser-extension pairing for fpx requests.

Mitigation: Pair only with the intended Etix profile, keep browser site access limited to etix.com, and revoke the pairing when it is no longer needed.

Risk: Setup examples install a global npm CLI without pinning a package version.

Mitigation: Use a pinned @fetchproxy/cli version where reproducibility matters and avoid running npm with administrator privileges.

Risk: Example commands write event and geolocation data to shared /tmp paths.

Mitigation: Use a private temporary directory such as one created by mktemp -d for real workflows.

Risk: HTML responses can still be DataDome interstitial pages even when the fetch command exits successfully.

Mitigation: Check responses for captcha-delivery or the documented interstitial text before parsing HTML as Etix event or venue data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)
- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes for fpx, jq, and Node-based extraction; it does not purchase tickets or require an Etix account.]

## Skill Version(s):

0.6.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
