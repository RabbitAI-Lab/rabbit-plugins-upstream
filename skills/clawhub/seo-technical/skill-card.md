## Description:

Technical SEO audit across nine categories: crawlability, indexability, security, URL structure, mobile, Core Web Vitals, structured data, JavaScript rendering, and IndexNow protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners, SEO practitioners, developers, and marketing teams use this skill to audit a provided URL for technical SEO issues and receive prioritized remediation guidance. It focuses on crawlability, indexability, security, URL structure, mobile experience, Core Web Vitals, structured data, JavaScript rendering, IndexNow, and agent-friendly page checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Google API and DataForSEO integrations can query account-linked SEO data.

Mitigation: Enable those integrations only for approved accounts and authorized properties, and review data access before running an audit.

Risk: IndexNow tooling can submit changed URLs to participating search engines.

Mitigation: Review the URL list and confirm host authorization before enabling or running IndexNow submission.

Risk: The skill can direct an agent to run checks against user-provided URLs.

Mitigation: Run audits only for URLs the user is authorized to test and apply URL-safety checks before fetching untrusted targets.

## Reference(s):

- [Agent-friendly pages audit reference](artifact/references/agent-friendly-pages.md)
- [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown audit report with score tables, prioritized findings, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-producing command suggestions and optional API-backed observations when tools are available.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata version 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
