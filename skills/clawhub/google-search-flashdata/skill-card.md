## Description:

Searches Google through FlashData and returns structured results with titles, URLs, snippets and positions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find web sources, documents and site-specific results, with optional country and language settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to FlashData and may include confidential information.

Mitigation: Submit sensitive terms only when this fits your FlashData account and privacy expectations.

Risk: Search requests spend paid FlashData Credits.

Mitigation: Check pricing and obtain approval for the query budget before submitting requests.

Risk: Exposure of the FlashData API key could permit unauthorized use.

Mitigation: Keep the key in an environment variable or secret manager, never in prompts or skill files.

## Reference(s):

- [FlashData Google Search documentation](https://flashdata.dev/docs/sources/google_search?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task)
- [FlashData API keys](https://flashdata.dev/app/api-keys)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Search request schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured JSON results or Markdown summaries with source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include titles, URLs, snippets and positions; snippets are not full pages.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
