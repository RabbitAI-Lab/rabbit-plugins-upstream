## Description:

Search Pinterest pins, pull one pin with its save/share counts, read a user's profile and boards, page through a board, and look up how often external URLs have been saved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and analysts use this skill to retrieve structured Pinterest search, pin, profile, board, and URL-save-count data through Scavio's API for content research, trend spotting, and creator analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls are sent to Scavio and may disclose Pinterest search terms, usernames, pins, boards, or URLs to that service.

Mitigation: Use the skill only with data that is appropriate to share with Scavio, and review requests before sending them.

Risk: Requests consume Scavio API credits, including empty results and URL-stat lookups.

Mitigation: Check credit costs before broad use, monitor credits_remaining, and page through cursor-based results deliberately.

Risk: The skill returns public Pinterest content that may include user-written descriptions or profiles.

Mitigation: Summarize user-authored content and avoid building profiles of individuals from returned data.

## Reference(s):

- [Scavio Pinterest API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=pinterest-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/pinterest-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell, Python, curl, and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; responses use a JSON envelope with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
