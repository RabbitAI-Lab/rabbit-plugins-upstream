## Description:

Make a site citable by AI engines through crawler allowlists, stable Schema.org @graph IDs, IndexNow, answer-first pages, and llms.txt guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO operators use this skill to audit and improve public site visibility in AI-generated answers. It guides crawler access checks, structured data cleanup, sitemap and IndexNow readiness, competitive benchmarking, content refresh planning, and answer-first page rewrites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide edits to public SEO files such as robots.txt, llms.txt, sitemaps, and structured data.

Mitigation: Review proposed edits before publishing, keep sensitive paths out of public robots.txt, and verify crawler rules against the intended domain.

Risk: The optional IndexNow script submits sitemap or CLI URLs to a public endpoint.

Mitigation: Use it only for URLs on the intended verified domain, set INDEXNOW_HOST and SITEMAP_PATH deliberately, and validate sitemap URLs before automation.

Risk: The IndexNow key file can become difficult to rotate if committed to source control.

Mitigation: Set INDEXNOW_KEY only for the intended run, serve the required key file from the site root, and keep the generated key file out of git.

Risk: Drafted page copy, author blocks, and public claims may be inaccurate or unsupported if published without review.

Mitigation: Require a named human author or reviewer to confirm sources, claims, dates, credentials, and compliance constraints before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/ai-search-visibility)
- [Playbooks: consoles, refresh, and multi-domain](artifact/references/playbooks.md)
- [robots.txt template](artifact/templates/robots.txt)
- [llms.txt template](artifact/templates/llms.txt)
- [Schema.org @graph template](artifact/templates/graph.json)
- [IndexNow ping script](artifact/scripts/indexnow-ping.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with audit tables, code and configuration snippets, file templates, and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce proposed edits for public SEO files, JSON-LD, page-copy drafts, audit scores, refresh plans, and IndexNow command usage.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
