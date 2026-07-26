## Description: <br>
Manage an Obsidian-based personal knowledge base with structured ingestion, querying, linting, reflection, merge, and question-tracking workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haima666](https://clawhub.ai/user/haima666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to have an agent maintain an Obsidian vault using defined protocols for source ingestion, wiki updates, search-backed answers, health checks, synthesis notes, deduplication, and question tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read private wiki content, write many files under wiki/, fetch URL content into raw/clippings/, and run qmd maintenance commands. <br>
Mitigation: Use explicit commands, review generated file changes, and keep backups or version control for the vault. <br>
Risk: Broad trigger phrases may start knowledge-base operations with too little user control. <br>
Mitigation: Confirm the intended operation and target vault or files before allowing ingest, query, lint, reflect, merge, or add-question workflows to proceed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haima666/obsidian-wiki-manager) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, markdown tables, Marp slides, Python matplotlib code blocks, structured bullet lists, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write source pages, concept pages, entity pages, synthesis notes, lint reports, gap reports, logs, and question entries inside the configured Obsidian wiki structure.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
