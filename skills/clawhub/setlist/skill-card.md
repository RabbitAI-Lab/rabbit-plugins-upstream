## Description:

Look up concert setlists and live-music history via setlist.fm for questions about songs performed at shows, tour setlists, venue histories, dates, artists, cities, and years.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to configure and operate a setlist.fm MCP workflow for finding concert setlists, artist histories, venue activity, and related live-music information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs mutable external code through setlist-mcp, which should be reviewed before installation.

Mitigation: Pin setlist-mcp to a reviewed version or commit and install it in a restricted environment.

Risk: The skill requires a SETLIST_API_KEY and uses account-writing attendance tools.

Mitigation: Protect and rotate the API key as needed, and allow attendance changes only with explicit confirmation.

Risk: The skill's read-only claims conflict with account-writing attendance tools.

Mitigation: Treat setlist_mark_attended and setlist_unmark_attended as write actions that require review and confirmation.

Risk: setlist.fm API access may have non-commercial or permission requirements depending on the user's intended use.

Mitigation: Review setlist.fm API terms and obtain any required permission before commercial use of API data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include followable setlist.fm source links when presenting setlist results.]

## Skill Version(s):

0.11.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
