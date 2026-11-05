## Description:

Read your organization's Workvivo feeds, news, posts, spaces, events, people directory, notifications, and search results through your signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use the skill to find internal updates, company content, events, and colleague or team information in Workvivo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workvivo searches are recorded in the user's search history, and downloaded files remain on disk.

Mitigation: Account for these side effects when searching or downloading, and handle downloaded files under your organization's data practices.

Risk: Raw Workvivo responses can contain session tokens, personal information, or event passwords.

Mitigation: Use the named-field projections in the endpoint recipes and avoid printing raw responses.

Risk: The external fpx CLI and browser extension were outside the security review.

Mitigation: Review their source and permissions before installation, and pair only the intended signed-in browser.

## Reference(s):

- [Workvivo read endpoints](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workvivo-fpx)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Concise text answers or selected JSON fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workvivo data; fields are selected to avoid relaying unnecessary sensitive information.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
