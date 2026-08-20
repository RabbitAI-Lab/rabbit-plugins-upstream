## Description:

Helps agents create, upload, submit, inspect, and cancel Amazon Selling Partner API Feeds for a selected LinkFox Amazon store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage Amazon SP-API Feeds workflows, including feed document creation, content upload, feed submission, polling, result lookup, and cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API keys and account onboarding data.

Mitigation: Treat generated API keys and payment QR data as secrets, and configure credentials only through trusted environment variables.

Risk: The skill can upload local feed content to a provided URL.

Mitigation: Use only trusted upload URLs and confirm local file paths before running upload commands with real seller data.

Risk: The skill can cancel Amazon feed processing.

Mitigation: Confirm the target feed ID and user intent before running cancellation commands.

Risk: The skill persists full API responses to local session files.

Mitigation: Review saved response files for sensitive seller or feed data and store them according to the user's data handling requirements.

## Reference(s):

- [Skill API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [Amazon createFeedDocument](https://developer-docs.amazon.com/sp-api/reference/createfeeddocument)
- [Amazon getFeedDocument](https://developer-docs.amazon.com/sp-api/reference/getfeeddocument)
- [Amazon createFeed](https://developer-docs.amazon.com/sp-api/reference/createfeed)
- [Amazon getFeed](https://developer-docs.amazon.com/sp-api/reference/getfeed)
- [Amazon getFeeds](https://developer-docs.amazon.com/sp-api/reference/getfeeds)
- [Amazon cancelFeed](https://developer-docs.amazon.com/sp-api/reference/cancelfeed)
- [Amazon Feed Type Values](https://developer-docs.amazon.com/sp-api/docs/feed-type-values)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance, shell command examples, and JSON API/script responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are summarized in stdout when large and full responses are persisted under a linkfox session directory.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
