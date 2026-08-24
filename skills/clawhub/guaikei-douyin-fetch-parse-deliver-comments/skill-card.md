## Description:

This skill helps agents search Douyin, fetch public creator posts and video comments, and retrieve real-time trending topics as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content analysts, and developers use this skill for public Douyin content research, competitor monitoring, comment analysis, and trend tracking. It is intended for structured collection and downstream analysis of public search, creator, post, comment, and hot-list data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger rules may cause the agent to use this Douyin data-collection skill for ambiguous general web-search requests.

Mitigation: Narrow operational use to explicit Douyin or short-video research contexts, and ask for confirmation when the requested source is ambiguous.

Risk: The configured GUAIKEI_API_TOKEN is sent to guaikei.com when API-backed commands run.

Mitigation: Use a scoped token intended for this service, keep it in the environment rather than prompts or files, and rotate it if exposure is suspected.

Risk: Search, post, and comment results can be saved locally in logs, including public profile, post, comment, and engagement data.

Mitigation: Treat generated logs as sensitive operational data, control workspace access, and remove logs when retention is not needed.

Risk: Security evidence flags misleading token/auth error behavior and says the documented no-contact-runtime claim is unreliable until those paths are fixed.

Mitigation: Review token validation and authentication error paths before deployment, and avoid relying on documentation claims that conflict with the security summary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-fetch-parse-deliver-comments)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Structured JSON on stdout with status, request, metadata, and result fields; local JSON logs may also be written for completed search, post, and comment tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a GUAIKEI_API_TOKEN environment variable and Node.js 16.14.0 or newer; individual commands accept keyword, URL, sorting, time range, content type, duration, and limit parameters depending on task.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
