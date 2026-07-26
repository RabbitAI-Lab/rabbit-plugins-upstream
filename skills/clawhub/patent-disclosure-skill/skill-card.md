## Description: <br>
Drafts Chinese patent technical disclosures from project materials, including novelty search, redacted drafting, self-checks, and iteration, or turns existing patents into plain-language notes and Obsidian knowledge graphs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[handsomestwei](https://clawhub.ai/user/handsomestwei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, inventors, patent engineers, and technical teams use this skill to identify patentable points from project materials, draft Chinese patent disclosure packages, convert Word or PowerPoint inputs for review, and iterate disclosure files. They can also use it to read existing patent publications or PDFs into plain-language Markdown notes, claim trees, public-clue summaries, and Obsidian knowledge graph artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist sensitive patent drafts, PDFs, public clues, Canvas graphs, Obsidian notes, and revision summaries. <br>
Mitigation: Use a test or backed-up vault first, confirm output paths before writes, and avoid saving real contact details unless they are required. <br>
Risk: The skill can modify an Obsidian vault and its settings. <br>
Mitigation: Disable Obsidian output or write to a local outputs directory when vault changes are not desired. <br>
Risk: The skill can perform network requests for public-clue fetching or CNIPA browser automation. <br>
Mitigation: Enable those flows only when those external requests are acceptable for the patent matter being handled. <br>
Risk: On Windows, Mermaid rendering may use an npx shell fallback. <br>
Mitigation: Prefer a locally installed mmdc path before rendering diagrams. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/patent-disclosure-skill) <br>
- [README](README.md) <br>
- [Installation guide](INSTALL.md) <br>
- [Patent PDF sources](references/patent_pdf_sources.yaml) <br>
- [Patent Obsidian format](references/patent_obsidian_format.md) <br>
- [IPC application hints](references/ipc_application_hints.yaml) <br>
- [Patent domain rules](references/patent_domain_rules.yaml) <br>
- [Tooling guide](tools/README.md) <br>
- [Patent reader tooling guide](tools/patent_reader/README.md) <br>
- [CNIPA patent publication search](http://epub.cnipa.gov.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documents, Word documents, JSON Canvas files, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can persist disclosure drafts, revision logs, patent-reader outputs, public-clue files, Obsidian notes, Canvas graphs, CSS, and Bases configuration depending on the selected workflow.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
