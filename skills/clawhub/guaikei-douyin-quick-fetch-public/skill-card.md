## Description:

Collects structured public Douyin data for keyword search, creator posts, video comments, and real-time trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, operators, marketers, and analysts use this skill to collect public Douyin search results, creator posts, comments, and hot-list data for content research, competitor analysis, sentiment review, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger scope is broad enough to run on generic research prompts when Douyin was not explicitly intended.

Mitigation: Use the skill only when Douyin public-data collection is the intended platform task, and confirm platform intent before running it from generic research requests.

Risk: Successful search, creator-post, and comment fetches are saved locally and may include profile or comment data.

Mitigation: Treat saved logs as potentially personal data, restrict access to the logs/ directory, and delete outputs when they are no longer needed.

Risk: The skill sends requests through the third-party guaikei.com service and requires an API token.

Mitigation: Review before installing, provide GUAIKEI_API_TOKEN only through the environment, and avoid exposing token values in prompts, logs, or shared outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-quick-fetch-public)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Complete Options](references/options.md)
- [Input and Output JSON Schemas](assets/*.schema.json)
- [Changelog](references/changelog.md)
- [Guaikei Service Site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON on stdout with stderr logs and optional local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and saves successful search, creator-post, and comment fetches under logs/.]

## Skill Version(s):

1.0.0 (source: package.json, artifact constants, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
