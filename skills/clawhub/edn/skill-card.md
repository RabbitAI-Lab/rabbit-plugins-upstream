## Description:

Use before and after meaningful implementation work to keep a local engineering notebook synchronized with the repository, including current versus proposed architecture, ownership, dependencies, flows, tradeoffs, failure modes, verification evidence, security boundaries, and major technical decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skcache](https://clawhub.ai/user/skcache)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to keep a local architecture notebook synchronized with repository changes and to surface architectural tradeoffs before material implementation work proceeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local notebook can summarize private architecture, security boundaries, and implementation details.

Mitigation: Keep the notebook gitignored by default and review it before sharing or committing repository-visible documentation.

Risk: The skill may modify local repository files by creating or updating engineering-notebook.html and .gitignore.

Mitigation: Review the working tree changes before committing and confirm that notebook paths remain ignored unless public documentation is explicitly intended.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/skcache/edn)
- [ClawHub skill page](https://clawhub.ai/skcache/skills/edn)
- [skills.sh edn page](https://skills.sh/skcache/edn)
- [Architecture Check reference](references/ARCHITECTURE-CHECK.md)
- [Notebook Sections reference](references/NOTEBOOK-SECTIONS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code blocks and local HTML notebook file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a local engineering-notebook.html file and may add notebook paths to .gitignore.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
