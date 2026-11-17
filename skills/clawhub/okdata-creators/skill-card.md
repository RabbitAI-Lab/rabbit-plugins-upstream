## Description:

Searches selected social platforms for creators by keyword and presents names, bios, follower counts, and post counts in one cross-platform table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creator partnership staff use the skill to find and compare potential creators for a category across selected social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to the external okdata service, which the security assessment flagged for review.

Mitigation: Use the service only when trusted and appropriate for the query; avoid sending sensitive search terms.

Risk: Search calls can incur charges, including when a data-source request fails or returns no results.

Mitigation: State the selected calls and maximum cost before the first paid call, and get approval before going beyond six calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conn-ho/skills/okdata-creators)
- [okdata creator search guide (English)](https://okdata.online/skills/creators/?src=skill-okdata-creators)
- [okdata creator search guide (中文)](https://okdata.online/zh/skills/creators/?src=skill-okdata-creators)
- [okdata agent setup guide](https://okdata.online/agents.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table with platform, creator name, bio, follower and post counts, and link, followed by source and cost details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One results page per selected platform; unavailable figures are left blank.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
