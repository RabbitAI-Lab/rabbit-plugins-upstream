## Description:

Uses the GuaiKei-backed Douyin public-data service to search content, fetch creator posts, retrieve video comments, and query real-time hot topics, while excluding publishing, editing, downloading, or private data access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and analysts use this skill to run Douyin public-data lookups for content research, competitor monitoring, comment analysis, and trend tracking. It is intended for public Douyin data and requires a configured GUAIKEI_API_TOKEN.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends lookup requests to a GuaiKei-backed remote API and requires an access token.

Mitigation: Provide only the required GUAIKEI_API_TOKEN and use the skill only for intended Douyin public-data lookups.

Risk: Ambiguous requests about short-video trends or competitors could be routed to Douyin unintentionally.

Mitigation: Confirm that ambiguous trend, search, or competitor-monitoring requests should target Douyin before running the CLI.

Risk: Returned public-data results may be retained in local JSON logs.

Mitigation: Clear the logs directory when retained local copies are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-disclosure-data)
- [Skill README](readme.md)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [JSON schemas](assets/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples; CLI execution returns JSON on stdout and logs on stderr.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; supports up to 10000 records per request; saves JSON result logs locally.]

## Skill Version(s):

1.0.0 (source: package.json, constants.js, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
