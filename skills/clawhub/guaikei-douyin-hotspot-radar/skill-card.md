## Description:

This skill helps agents query public Douyin data for keyword search, creator posts, video comments, and real-time hot lists for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content analysts use this skill to collect structured JSON from public Douyin search results, creator pages, comments, and hot lists for marketing research, competitor monitoring, public-content analysis, and trend tracking.

### Deployment Geography for Use:

Global, with documentation noting a Chinese-language interface and domestic-server availability.

## Known Risks and Mitigations:

Risk: The skill can trigger on vague short-video research requests and send Douyin queries through a third-party API.

Mitigation: Confirm the user's intent, target platform, and query before running commands, especially when Douyin is not named explicitly.

Risk: The GUAIKEI_API_TOKEN controls API access and could be exposed if mishandled.

Mitigation: Provide the token only through the environment variable, avoid printing it, and rotate it if exposure is suspected.

Risk: Collected public-platform data, account URLs, creator data, keywords, and comments may be saved locally.

Mitigation: Review or delete the logs directory regularly and share exported data only when authorized.

Risk: Third-party API requests may disclose query terms, account identifiers, and video URLs outside the local environment.

Mitigation: Use the skill only for data approved for third-party processing.

## Reference(s):

- [Skill README](artifact/readme.md)
- [Options Reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Command JSON Schemas](artifact/assets/)
- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-hotspot-radar)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance for command selection and parseable JSON from CLI stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save collected public-platform data to local logs.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
