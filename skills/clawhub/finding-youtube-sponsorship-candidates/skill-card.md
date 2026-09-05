## Description:

Finds YouTube channels suitable for brand sponsorships using apidojo's YouTube scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External brand partnerships managers, sponsorship agencies, and SaaS marketing teams use this skill to discover, score, and rank YouTube channels for sponsorship outreach in a target niche.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube search terms and target-channel URLs are sent to Apify under the user's Apify account.

Mitigation: Avoid submitting sensitive campaign strategy details unless Apify is an acceptable processor for that data.

Risk: An Apify token is required for intended operation.

Mitigation: Prefer MCP or a wrapper that keeps APIFY_TOKEN out of command URLs and stores credentials in the environment or an approved secret store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-youtube-sponsorship-candidates)
- [Apify YouTube Scraper actor](https://apify.com/apidojo/youtube-scraper)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with ranked tables and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional CSV or JSON file outputs when the actor wrapper is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
