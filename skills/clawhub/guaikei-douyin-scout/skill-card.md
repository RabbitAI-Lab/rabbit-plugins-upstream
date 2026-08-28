## Description:

Guides an agent to run Node.js CLI commands that collect public Douyin search results, creator posts, video comments, and hot-list data as structured JSON for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content researchers, and developers use this skill to investigate public Douyin trends, competitor accounts, creator output, and video comments through token-authenticated CLI calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin queries, creator or video URLs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install only when that data sharing is acceptable, keep the token private, and avoid using the skill for sensitive targets or personal-data profiling.

Risk: Search, post, and comment results are automatically saved under the skill's logs directory.

Mitigation: Review and periodically delete local logs, especially after investigations involving people, creators, or competitors.

Risk: Broad short-video research prompts can trigger Douyin collection even when the user did not explicitly request Douyin.

Mitigation: Confirm the platform and intent before running commands for ambiguous research prompts.

Risk: Runtime support messaging includes an unverified private contact path.

Mitigation: Treat that contact path as unverified and prefer documented organizational support channels when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-scout)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [README](artifact/readme.md)
- [Complete CLI options](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout, log files under logs/, and concise Markdown guidance with shell commands when explaining usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14 or newer and GUAIKEI_API_TOKEN; single-request limits are documented up to 10000 returned items.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
