## Description:

Retrieves public Douyin intelligence for keyword search, creator posts, video comments, and real-time hot lists to support topic research, competitor analysis, reputation review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect and analyze public Douyin search results, creator posts, comments, and hot-list data for short-video marketing research, competitor monitoring, public-opinion review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, video or account URLs, and the GUAIKEI token are sent to the Guaikei service.

Mitigation: Install and use the skill only when third-party processing by Guaikei is acceptable, keep the token in environment variables, and avoid sensitive queries unless collection is explicitly intended.

Risk: The skill automatically stores large social-data exports locally, which may include public user identifiers, comments, and business research topics.

Mitigation: Treat generated logs as potentially sensitive, restrict local access, and delete logs when they are no longer needed.

## Reference(s):

- [README](readme.md)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei service website](https://www.guaikei.com)
- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-intel-exchange)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Pure JSON on stdout with stderr status messages and local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. Results can include public user identifiers, comments, social metrics, and research topics; single-command retrieval is documented up to 10000 records.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
