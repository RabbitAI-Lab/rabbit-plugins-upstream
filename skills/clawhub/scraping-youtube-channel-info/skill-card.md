## Description:

Extracts YouTube channel metadata, subscriber counts, video counts, descriptions, verification status, and keywords using apidojo's YouTube Channel Scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, marketers, and analysts use this skill to collect public YouTube channel metadata by URL, handle, or keyword for downstream influencer research, competitive analysis, and channel discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs are sent to Apify under the user's APIFY_TOKEN.

Mitigation: Use only appropriate public YouTube URLs, handles, keywords, and locale options, and avoid passing secrets in actor input.

Risk: Untrusted JavaScript in customMapFunction could transform results in unexpected ways.

Mitigation: Review customMapFunction before execution or omit it when a raw dataset is sufficient.

Risk: Large channel searches can increase scraping volume and cost.

Mitigation: Set maxItems and targeted filters such as gl, hl, keywords, or handles before running bulk jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-youtube-channel-info)
- [Apify actor REST API endpoint](https://api.apify.com/v2/acts/apidojo~youtube-channel-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with JSON, CSV, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return raw YouTube channel metadata in JSON or CSV, including channel names, URLs, descriptions, subscriber counts, video counts, verification status, keywords, countries, thumbnails, and tags.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
