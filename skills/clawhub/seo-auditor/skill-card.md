## Description:

SEO Auditor helps agents research keyword metrics, audit public web pages, compare a site against a competitor for keyword gaps, and assemble sourced SEO findings into an audit report using a dedicated API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and SEO practitioners use this skill to run API-backed keyword research, public page audits, competitor gap analysis, and report generation while preserving sources and observation timestamps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SEO queries, public URLs or domains, and billing activity to ai-skills.open-idea.net using SEO_AUDITOR_API_KEY.

Mitigation: Confirm the user trusts the service, keep the API key in the dedicated environment variable, do not paste or log full keys, and avoid overriding AI_SKILLS_API_URL unless the target service is controlled.

Risk: Page audit inputs could be unsafe or outside the user's intended scope.

Mitigation: Submit only user-specified public HTTP(S) URLs and rely on the platform checks that reject localhost, IP literals, unusual ports, private or reserved addresses, and DNS rebinding.

Risk: SEO metrics and audit findings are time-bound evidence snapshots and may be incomplete or stale.

Mitigation: Distinguish evidence from analysis, preserve source and observed_at fields, do not treat empty or partial results as proof that no issue exists, and obtain user confirmation before publishing reports or making SEO changes.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Operations Contract](references/OPERATIONS.md)
- [HTTP Requests and Task Polling](references/HTTP-REQUESTS.md)
- [Evidence, Security, and Error Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve metric and finding sources, observation timestamps, and task status boundaries.]

## Skill Version(s):

1.2.1 (source: server evidence release.version and metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
