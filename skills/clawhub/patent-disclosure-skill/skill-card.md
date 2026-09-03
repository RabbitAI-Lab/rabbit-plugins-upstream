## Description:

中国专利技能：挖掘专利点与编写交底书（发明/实用/外观），按著录字段检索公布公告，通俗解读专利，对照审查口径出政策简报，辅助审查答复。| China patents skill: mine patent points and draft disclosures, search CNIPA bibliographic records, explain patents, brief examination-policy changes for disclosures, and assist office-action responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

Patent practitioners, inventors, engineers, and agents use this skill to draft Chinese patent disclosure materials, run CNIPA bibliographic searches, explain published patents in plain language, prepare examination-policy briefs, and assist with office-action response drafts. Human review remains required for filing decisions, legal strategy, and submitted documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional OA playbook path can automatically install and execute externally sourced tooling with weak command scoping.

Mitigation: Avoid the auto-install path unless the third-party source is trusted; prefer a pinned, fixed install command reviewed before execution.

Risk: Patent-reader workflows can write into an Obsidian vault and may alter a user's working knowledge base.

Mitigation: Use a dedicated test Obsidian vault first, then promote outputs into a production vault after review.

Risk: Document-conversion and browser-based tooling may process untrusted documents or web content.

Mitigation: Update and pin document-conversion dependencies, and process untrusted files in a constrained workspace.

Risk: API keys or other credentials could be exposed if passed through shell commands.

Mitigation: Use environment configuration and avoid passing API keys directly on the command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill)
- [AgentSkills standard](https://agentskills.io)
- [Patent disclosure schema references](skills/patent-disclosure/references/schemas/README.md)
- [Formula paradigms reference](skills/patent-disclosure/references/formulas/README.md)
- [Patent search type reference](skills/patent-search/references/patent_type_search.yaml)
- [Patent reader domain rules](skills/patent-reader/references/patent_domain_rules.yaml)
- [Patent examination policy sources](skills/patent-exam-policy/references/sources.yaml)
- [CNIPA patent publication search](http://epub.cnipa.gov.cn/)
- [Playwright documentation](https://playwright.dev/)
- [Obsidian CLI documentation](https://help.obsidian.md/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, DOCX, JSON/YAML schemas, search reports, Obsidian notes/canvases, and shell command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing outputs default to Simplified Chinese; workflow artifacts are written under the user's workspace outputs directory.]

## Skill Version(s):

4.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
