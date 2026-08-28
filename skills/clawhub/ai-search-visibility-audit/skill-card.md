## Description:

Audits whether a public website can be found, crawled, and cited by AI answer engines, producing a citation baseline, crawler-access check, citability review, and ranked fix list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxaeo](https://clawhub.ai/user/maxaeo)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, content, SEO, and growth teams use this skill to audit public websites for visibility in AI answer engines. It helps identify citation gaps, crawler-access blockers, weakly citable content, and third-party pages that affect how answer engines describe a brand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be used to probe private, logged-in, paywalled, or unauthorized pages.

Mitigation: Use it only for publicly accessible pages, respect robots.txt and terms of service, confirm the domain and competitors before continuing, and stop when a page requires login or access controls.

Risk: A single audit run can overstate or understate AI-search visibility because answer engines vary by engine, prompt, and time.

Mitigation: Present measured rates as one sampled snapshot, state what was sampled, avoid trend claims, and record unavailable checks in the audit limits.

Risk: Crawler access conclusions can become stale as answer-engine operators add or rename crawlers.

Mitigation: Check each operator's published crawler documentation before concluding and state which crawler list was used.

## Reference(s):

- [MaxAEO homepage](https://maxaeo.ai/)
- [ClawHub skill listing](https://clawhub.ai/maxaeo/skills/ai-search-visibility-audit)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown audit report with tables, measured rates, ranked recommendations, and configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Every run should include Verdict, Citation baseline, Blockers, Fix list, and Limits of this audit sections.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
