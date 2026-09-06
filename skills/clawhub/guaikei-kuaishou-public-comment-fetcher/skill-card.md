## Description:

Fetches public Kuaishou/Kwai search results, creator posts, and video comments as structured JSON for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, marketers, and analysts use this skill to collect public Kuaishou/Kwai video, creator, and comment data for topic research, competitor monitoring, KOL screening, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API token can be exposed if users print or share their environment value.

Mitigation: Configure GUAIKEI_API_TOKEN securely and avoid running, logging, or sharing commands that reveal the token value.

Risk: Fetched results are automatically saved locally and may include sensitive research targets or personal identifiers from public data.

Mitigation: Treat generated logs as retained data; delete, restrict, or protect log files according to the user's data handling requirements.

Risk: Requests are sent through Guaikei to collect Kuaishou public data.

Mitigation: Use the skill only for public Kuaishou data the user is allowed to collect, and confirm third-party request routing is acceptable before use.

## Reference(s):

- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei](https://www.guaikei.com)
- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-public-comment-fetcher)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [Structured JSON with status, request metadata, skill metadata, and results; successful runs may also write JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword, URL, sort, time, duration, and limit parameters.]

## Skill Version(s):

1.0.0 (source: SKILL.md metadata, package.json, changelog, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
