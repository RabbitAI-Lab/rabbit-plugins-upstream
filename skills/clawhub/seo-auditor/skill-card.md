## Description:

SEO Auditor helps agents research keyword metrics, audit public webpages, compare a site's keyword gap with one competitor, and compile sourced findings and metrics into SEO audit reports using the ai-skills.open-idea.net service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, site owners, and agents use this skill to request keyword research, public page audits, competitor gap checks, and sourced SEO report summaries. It is intended for workflows that can send keywords, domains, public URLs, findings, and metrics to the external SEO Auditor service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested keywords, domains, public URLs, findings, and metrics to the external SEO Auditor service.

Mitigation: Install and use it only when that remote service use is acceptable for the SEO data being processed.

Risk: The skill requires SEO_AUDITOR_API_KEY for authorization.

Mitigation: Keep the key in the environment, do not paste it into chat, and do not write it into JSON, logs, evidence, or reports.

Risk: The documentation is Chinese-only, which may increase operator misunderstanding for non-Chinese readers.

Mitigation: Have a reader who understands the documentation review behavior, inputs, and limits before deployment.

Risk: SEO metrics, rankings, and page findings are source-specific time slices and can be incomplete or outdated.

Mitigation: Preserve source and observed_at values, distinguish evidence from analysis, and avoid presenting missing data as proof that no issue exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/seo-auditor)
- [Publisher Profile](https://clawhub.ai/user/youteacher)
- [SEO Auditor Service Homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Evidence, Safety, and Error Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text with JSON request examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source, observed_at, evidence_url, task status, and billing headers when returned by the service.]

## Skill Version(s):

1.0.0 (source: release evidence, package metadata, and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
