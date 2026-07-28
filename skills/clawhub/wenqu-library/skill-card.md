## Description: <br>
文曲·文库 guides agents through planning, search, download, indexing, and reusable library maintenance for evidence-driven Chinese writing research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, content creators, and agents use this skill to collect traceable similar articles and factual source material before drafting Chinese articles, reports, tutorials, project introductions, and explanatory documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A broad or ambiguous collection request can gather irrelevant or excessive source material. <br>
Mitigation: Review and confirm the collection plan, scope boundaries, keyword groups, and expected download count before search or download begins. <br>
Risk: The skill performs web searches and downloads selected pages, including optional browser-assisted retrieval. <br>
Mitigation: Use native search first, keep browser recovery bounded to documented recipes, record failed URLs, and do not bypass login, paywall, verification, or other access controls. <br>
Risk: Optional helper CLIs may change the user's local environment if installed. <br>
Mitigation: Request explicit approval before installing open-websearch or Crawl4AI tooling; if approval is denied or validation fails, fall back to native search and download. <br>
Risk: Collected materials may mix factual sources, similar writing examples, and unverified claims. <br>
Mitigation: Maintain an index with original URL or path:line, source type, retrieval channel, file path, tags, intended use, and failure notes for each material entry. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-library) <br>
- [Project homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-library) <br>
- [Collection playbook](references/collection-playbook.md) <br>
- [open-websearch search supplement](references/open-websearch/README.md) <br>
- [open-websearch CLI protocol](references/open-websearch/cli.md) <br>
- [Crawl4AI download enhancement](references/crawl4ai/README.md) <br>
- [Crawl4AI site recipes](references/crawl4ai/site-recipes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown collection plans, indexed source tables, local research files, shell commands for optional tools, and concise status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes indexed source material to local project and user library paths; optional CLI installation and browser setup require explicit user approval.] <br>

## Skill Version(s): <br>
0.1.12 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
