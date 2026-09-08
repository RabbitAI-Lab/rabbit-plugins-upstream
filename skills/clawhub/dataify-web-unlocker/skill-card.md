## Description:

Fetch HTML or a screenshot from a known blocked or JavaScript-rendered webpage with Dataify Web Unlocker.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve HTML or screenshots for a specific public webpage that may be blocked, CAPTCHA-protected, or JavaScript-rendered.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied URLs, fetched page content, and optional headers or cookies are sent to Dataify.

Mitigation: Use only public URLs or data intended for Dataify; do not provide browser cookies, authorization headers, internal URLs, or long-lived secrets.

Risk: The package contains broader search and business-scraping helpers beyond the main web-unlocker purpose.

Mitigation: Review the included scripts before deployment and restrict agent use to the web-unlocker wrapper unless the broader helpers are explicitly needed.

Risk: Credential handling mistakes could expose the Dataify API token.

Mitigation: Configure DATAIFY_API_TOKEN through the environment, verify only whether it is present, and never paste or print the token in chat or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-web-unlocker)
- [Dataify Web Unlocker API endpoint](https://webunlocker.dataify.com/request)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command snippets and returned API response bodies, typically HTML, JSON, or screenshot data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and sends the target URL plus optional headers or cookies to Dataify.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
