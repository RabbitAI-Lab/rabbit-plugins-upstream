## Description:

Query etix.com event, venue, and performer discovery data from a shell with the fpx CLI instead of running the etix-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate fpx commands and parsing recipes for public Etix discovery data, including search suggestions, event detail, venue detail, and geolocation lookups. It is intended for anonymous discovery reads and explicitly excludes ticket purchasing or seller API workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pairing Fetchproxy/Transporter with an etix.com-scoped profile sends search terms and geolocation inputs to Etix through the user's browser session.

Mitigation: Install only when comfortable with that scoped pairing, keep the profile limited to etix.com, and treat search and location inputs as data sent to Etix.

Risk: Fetched event or venue pages may be saved to temporary files that remain on disk.

Mitigation: Remove temporary files when fetched event or venue content should not persist locally.

Risk: Etix HTML responses can be DataDome interstitial pages even when the fetch command exits successfully.

Mitigation: Check HTML responses for captcha-delivery or the DataDome enable-JS message before parsing them as event or venue content.

Risk: Ticket purchasing and seller API use could involve financial actions or venue credentials outside the skill's intended scope.

Mitigation: Use the skill only for anonymous public discovery reads and do not use it for purchases or OAuth-protected seller API workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [Etix consumer endpoints for fpx](artifact/references/etix-endpoints.md)
- [Etix dataLayer extractor](artifact/references/extract-datalayer.mjs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON extraction examples, and small JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fpx commands, jq filters, temporary file paths, endpoint paths, and troubleshooting guidance for DataDome or Fetchproxy bridge failures.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
