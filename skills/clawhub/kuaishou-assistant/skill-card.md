## Description:

Search public Kuaishou videos by keyword, review video comments, and retrieve creators’ public posts and profile data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts can research public Kuaishou content, creator activity, and video discussions to support topic planning and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords and video links are sent to GuaiKei to retrieve public data. ClawScan reports a privacy disclosure gap and medium confidence because some scripts were only partially inspected.

Mitigation: Review GuaiKei’s data handling terms and avoid sensitive research inputs unless you have authorization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-assistant)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [GuaiKei product site](https://www.guaikei.com)
- [Usage options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands]

**Output Format:** [Structured JSON results in an output envelope; the skill is invoked with Node.js command-line instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns public video, creator, or comment data. Result fields and count types vary by command and are documented in the included schemas.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
