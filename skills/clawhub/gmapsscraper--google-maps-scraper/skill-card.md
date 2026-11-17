## Description:

Scrape business data from Google Maps, including names, phones, emails, websites, ratings, and reviews, by keyword and location with no coding required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmapsscraper](https://clawhub.ai/user/gmapsscraper)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Google Maps by business category and location, then retrieve lead data such as addresses, phones, websites, emails, ratings, reviews, and map links. The workflow is intended to confirm search parameters before spending API credits and to summarize downloaded results for follow-up sales or market analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms may include raw user-supplied text in documented curl examples.

Mitigation: Serialize request JSON or otherwise treat user-provided keywords and locations strictly as data before making API calls.

Risk: The workflow collects business contact data, including emails and phone numbers.

Mitigation: Collect and use contact data only when there is a lawful, policy-compliant reason and apply appropriate privacy review before outreach or export.

Risk: The skill sends searches and the API key to gmapsscraper.io.

Mitigation: Use the skill only when the user trusts gmapsscraper.io with the API key and search data, and avoid exposing the key in logs or shared transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gmapsscraper/skills/google-maps-scraper)
- [gmapsscraper homepage](https://gmapsscraper.io)
- [gmapsscraper dashboard](https://gmapsscraper.io/dashboard)
- [gmapsscraper pricing](https://gmapsscraper.io/#pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and CSV-oriented result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and GMAPS_SCRAPER_API_KEY; API searches consume credits and may produce downloadable CSV results.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
