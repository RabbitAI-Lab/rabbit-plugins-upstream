## Description:

This skill helps agents retrieve public Douyin search results, creator posts, video comments, and real-time hot topics as structured JSON for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for Douyin-focused content research, competitor monitoring, public comment analysis, and hot-topic tracking. It is suited to retrieving public platform data and turning natural-language research requests into the appropriate search, post, comment, or hot-list command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggering can send general short-video research prompts to the external Guaikei service even when the user did not explicitly intend Douyin research.

Mitigation: Use the skill only for explicit Douyin public-data retrieval tasks and confirm ambiguous research requests before running a command.

Risk: Queries, creator URLs, video URLs, and the GUAIKEI API token are sent to guaikei.com, with the token included in request parameters.

Mitigation: Treat the token and request URLs as sensitive, use a scoped token where possible, and avoid running the skill in environments where URL logs are broadly visible.

Risk: Returned public data is saved locally under the skill's logs directory and may include sensitive research topics or comment text.

Mitigation: Review retention needs before use and periodically delete logs that contain sensitive topics, URLs, or comments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-search-post-comment-hot)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei Service Page](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout, operational messages on stderr, and JSON log files under the skill logs directory.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN; each command returns one retrieval result stream.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
