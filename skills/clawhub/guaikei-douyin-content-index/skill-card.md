## Description:

This skill helps agents collect and structure public Douyin content data for keyword search, creator post collection, comment analysis, and real-time hot-list tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content, marketing, and research teams use this skill to query public Douyin videos, creator posts, comments, and hot-list data for topic planning, competitor monitoring, public-comment analysis, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation rules may cause an agent to send ambiguous Douyin-related requests or URLs to the external guaikei.com service.

Mitigation: Confirm the user's intended Douyin data task and parameters before invoking the skill when the request is ambiguous.

Risk: Generated logs can contain public comments, account data, and business research results.

Mitigation: Review retention needs, restrict access to generated logs, and delete logs that are no longer needed.

Risk: The skill depends on GUAIKEI_API_TOKEN and server-side access to public Douyin data.

Mitigation: Provide the token only through the environment, avoid echoing it in prompts or logs, and stop execution on token or quota errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-content-index)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [README](readme.md)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei token and service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [JSON from CLI stdout, with operational logs on stderr and saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN; commands cover search, creator posts, comments, and hot-list retrieval.]

## Skill Version(s):

1.0.0 (source: package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
