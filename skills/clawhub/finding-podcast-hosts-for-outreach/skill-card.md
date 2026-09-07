## Description:

Finds podcast hosts for PR and guest outreach using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External PR teams, executives, authors, and founders use this skill to find and prioritize podcast hosts for guest outreach in a specific topic or industry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Podcast search terms, Twitter handles, URLs, and public social data requests are sent to Apify/Twitter scraping services.

Mitigation: Use only data that is appropriate to share with Apify, keep result limits reasonable, and verify that outreach workflows comply with applicable platform and privacy rules.

Risk: The workflow depends on an APIFY_TOKEN credential.

Mitigation: Store the token in the environment or a protected .env file, avoid placing it in prompts or exported results, and rotate it if exposure is suspected.

Risk: Podcast host classification can include false positives such as listeners, promotional accounts, inactive hosts, or large media brands unsuitable for routine outreach.

Mitigation: Review bios, recent episode activity, show names, and guest-format signals before using the outreach list.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/finding-podcast-hosts-for-outreach)
- [ClawHub Publisher Profile](https://clawhub.ai/user/apidojo-io)
- [Apify Actor: apidojo/twitter-user-scraper](https://apify.com/apidojo/twitter-user-scraper)
- [Apify Actor: apidojo/tweet-scraper](https://apify.com/apidojo/tweet-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, JSON examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CSV or JSON outreach lists when the workflow is run with file output options.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
