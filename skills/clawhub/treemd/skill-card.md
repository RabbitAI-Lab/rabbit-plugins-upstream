## Description:

Markdown document analysis and navigation using the treemd CLI for exploring heading trees, extracting sections, querying markdown elements with tql, and surveying large markdown files before reading or editing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wei840222](https://clawhub.ai/user/wei840222)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Markdown document structure, locate relevant headings, extract sections, and run tql queries without loading entire documents into context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or relying on the skill requires adding the upstream treemd CLI to the environment.

Mitigation: Confirm the upstream treemd CLI is acceptable for the environment before installation, then verify availability and version with command -v treemd and treemd --version.

Risk: Invoking treemd without a non-interactive action flag can launch the interactive TUI or file picker and block an agent session.

Mitigation: Use only documented non-interactive flags such as --tree, --list, --count, --section, --query, --help, or --version for agent tasks.

Risk: Section extraction can fail when the requested heading does not exactly match the full heading text.

Mitigation: List or query headings first, then pass the exact heading text to section extraction and handle non-zero exit codes.

## Reference(s):

- [treemd project homepage](https://github.com/Epistates/treemd)
- [treemd releases](https://github.com/Epistates/treemd/releases)
- [treemd Query Language Reference](references/query-language.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses treemd CLI modes that can emit plain text, JSON, JSONL, markdown, or tree output depending on the selected command flags.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
