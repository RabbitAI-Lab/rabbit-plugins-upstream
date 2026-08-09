## Description:

Helps agents create, upload, submit, query, and cancel Amazon SP-API Feeds through LinkFox gateway scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce operators use this skill to manage Amazon store feed documents and feed submissions, including creating feed documents, uploading feed content, submitting feeds, polling status, retrieving result-document metadata, and cancelling feeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Amazon SP-API Feeds workflows through LinkFox gateway endpoints and uses LinkFox API keys.

Mitigation: Run it only with trusted LinkFox endpoint environment variables and credentials intended for this workflow.

Risk: Full responses and payment QR artifacts can be saved locally under the linkfox session directory.

Mitigation: Review saved files for sensitive data and delete response or QR files when they are no longer needed.

Risk: The onboarding flow can request phone/SMS codes and create payment orders.

Mitigation: Share phone or SMS codes and initiate payment only when intentionally creating or accessing a LinkFox account.

## Reference(s):

- [API reference](references/api.md)
- [Onboarding and billing guidance](references/onboarding.md)
- [Amazon SP-API createFeedDocument](https://developer-docs.amazon.com/sp-api/reference/createfeeddocument)
- [Amazon SP-API getFeedDocument](https://developer-docs.amazon.com/sp-api/reference/getfeeddocument)
- [Amazon SP-API createFeed](https://developer-docs.amazon.com/sp-api/reference/createfeed)
- [Amazon SP-API getFeed](https://developer-docs.amazon.com/sp-api/reference/getfeed)
- [Amazon SP-API getFeeds](https://developer-docs.amazon.com/sp-api/reference/getfeeds)
- [Amazon SP-API cancelFeed](https://developer-docs.amazon.com/sp-api/reference/cancelfeed)
- [Amazon SP-API Feed Type Values](https://developer-docs.amazon.com/sp-api/docs/feed-type-values)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-feeds)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox agent portal](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [API Calls, Files, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses, saved JSON files, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally under a linkfox session directory; small responses or --inline output print full JSON, while larger responses print summaries.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
