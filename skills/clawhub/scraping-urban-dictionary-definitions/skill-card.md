## Description:

Extracts definitions, examples, and community votes from Urban Dictionary using apidojo's Urban Dictionary Scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, content teams, brand analysts, and developers use this skill to collect Urban Dictionary definitions, examples, author names, vote counts, timestamps, and source URLs for slang terms or Urban Dictionary pages. The resulting dataset supports downstream analysis of internet language, memes, and community voting patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected keywords or Urban Dictionary URLs are sent to Apify when the scraper runs.

Mitigation: Avoid submitting confidential search terms or sensitive URLs, and treat the Apify token as a secret.

Risk: Urban Dictionary contains explicit user-generated content.

Mitigation: Review or filter scraper output before sharing it or using it in downstream analysis.

Risk: Unbounded collection can increase runtime, cost, or dataset size.

Mitigation: Set maxItems to an appropriate cap before running the actor.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-urban-dictionary-definitions)
- [Apify actor run endpoint](https://api.apify.com/v2/acts/apidojo~urbandictionary-scraper/runs)

## Skill Output:

**Output Type(s):** [Text, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured Urban Dictionary records that can be saved as JSON or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include word, definition, example, author, id, createdAt, numberOfThumbsUp, numberOfThumbsDown, and url fields.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
