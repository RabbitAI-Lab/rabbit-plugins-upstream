## Description:

Monitors public Douyin content by searching keywords, collecting creator posts and comments, and fetching hot-list data for competitor and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Marketing analysts, content strategists, and agents use this skill to inspect public Douyin videos, creator activity, comments, and trending topics for competitor monitoring, campaign research, and issue tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, profile or video URLs, and the Guaikei API token to www.guaikei.com.

Mitigation: Use it only for non-sensitive public Douyin research, avoid private investigations or sensitive keywords, and confirm that the Guaikei service is approved for the intended workspace.

Risk: Collected results may be saved automatically under the skill's logs directory.

Mitigation: Review generated logs after each run and delete or retain them according to the user's data handling policy.

Risk: Broad auto-triggering can run the skill for short-video, creator, comment, or hot-topic requests even when the user does not explicitly name Douyin.

Mitigation: Confirm the target platform and intent before execution when the request is ambiguous or could involve another platform.

Risk: Invalid-token paths may show contact or marketing text instead of only neutral setup guidance.

Mitigation: Treat authentication failures as setup errors and avoid repeating promotional or contact text from command output to the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-competitor-watch)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei Service Website](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [JSON results from CLI commands, with Markdown guidance for command selection and parameter mapping.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save collected results under the skill logs directory.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
