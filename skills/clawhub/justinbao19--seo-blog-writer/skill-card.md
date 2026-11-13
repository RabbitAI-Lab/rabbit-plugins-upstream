## Description:

Fully automated SEO article writer that takes a topic and domain, discovers product context, researches keywords, analyzes competitors, writes an article, verifies links, and produces a publication package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[justinbao19](https://clawhub.ai/user/justinbao19)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content teams, and website operators use this skill to produce SEO-focused blog articles and related publishing assets for a provided domain. It is intended for hands-off research, drafting, link checking, QA, schema markup, and promotion checklist generation after an initial confirmation gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may search the web, fetch many public pages, and write files locally.

Mitigation: Run it in a sandbox constrained to the intended output directory and public HTTP/HTTPS access.

Risk: The skill asks for broad subagent execution authority for file writes and link verification.

Mitigation: Avoid granting full subagent execution privileges when possible; run the workflow in the main session or another controlled environment with scoped file access.

Risk: The skill fetches arbitrary external links for SEO research and link validation without clear destination controls.

Mitigation: Review target domains and generated links before publication, and restrict network access where the host environment supports it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/justinbao19/skills/seo-blog-writer)
- [Publisher profile](https://clawhub.ai/user/justinbao19)
- [Schema.org](https://schema.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown article, QA report, JSON-LD schema markup, and promotion checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes article and supporting files to a user-configurable local output directory.]

## Skill Version(s):

3.2.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
