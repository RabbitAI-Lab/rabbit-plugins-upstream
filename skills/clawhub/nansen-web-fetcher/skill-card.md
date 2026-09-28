## Description:

Fetches content from supplied URLs and answers questions about it using Gemini 2.5 Flash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can retrieve and compare up to 20 specified web pages to answer a question or summarize their content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Page content and questions may be sent to Nansen/Gemini for processing.

Mitigation: Review URLs and questions before use and avoid sharing sensitive content without authorization.

Risk: Paywalled or bot-blocked pages may not be retrieved.

Mitigation: Check failed_urls and verify that the answer is based on the intended pages.

## Reference(s):

- [Nansen Web Fetcher skill listing](https://clawhub.ai/nansen-devops/skills/nansen-web-fetcher)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes analysis, retrieved_urls and failed_urls; optional human-readable JSON with --pretty. Requests time out after 30 seconds.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
