## Description:

Bundles a directory of Markdown files into a self-contained offline HTML document browser with a directory tree, global search, cross-document links, and built-in rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and project teams use this skill to package multi-file Markdown documentation or research outputs into one portable HTML browser for offline reading, search, and sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generated HTML contains the full text of every bundled Markdown file and may disclose private notes, secrets, or internal material if shared.

Mitigation: Review the selected directory before bundling and exclude sensitive files before opening or sharing the generated HTML.

Risk: Untrusted Markdown content is packaged into a browser-viewed HTML document.

Mitigation: Bundle trusted Markdown sources or inspect the generated HTML before distributing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shiyan521/skills/markdown-bundle-browser)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated self-contained HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated HTML embeds the selected Markdown content and is intended for offline browser viewing.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
