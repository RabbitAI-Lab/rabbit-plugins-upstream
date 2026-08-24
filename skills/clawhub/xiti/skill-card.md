## Description:

析题 helps agents generate heuristic competitive-programming solution writeups, code explanations, and problem analyses that emphasize how to think through a problem rather than only giving an answer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn programming contest statements, URLs, or reference solutions into readable Chinese teaching materials with reasoning paths, annotated code, complexity analysis, examples, and common pitfalls. It can produce single-file HTML explanations with visualizations or Typst sources intended to compile into PDF handouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read problem or code files supplied by the user and incorporate them into generated writeups.

Mitigation: Use it only with contest materials and code appropriate for that workflow, and review quoted or transformed code before sharing outputs.

Risk: Generated HTML may load public CDN libraries for math rendering, syntax highlighting, diagrams, and animation.

Mitigation: Review generated HTML before publishing and confirm that external CDN loading is acceptable for the target environment.

Risk: The skill may propose or run local build and preview commands such as Typst compilation.

Mitigation: Review generated commands and outputs before deployment or publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fslong520/skills/xiti)
- [AtCoder ABC457 Tasks](https://atcoder.jp/contests/abc457/tasks)
- [AtCoder ABC460 Tasks](https://atcoder.jp/contests/abc460/tasks)
- [KaTeX CDN Dependency](https://cdn.jsdelivr.net/npm/katex@0.16.21/dist/katex.min.css)
- [Mermaid CDN Dependency](https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js)
- [anime.js CDN Dependency](https://cdn.jsdelivr.net/npm/animejs@3.2.2/lib/anime.min.js)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance, annotated code, HTML files, Typst files, SVG/PNG-backed visual materials, and shell commands for local rendering or verification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read contest statements or code supplied by the user, write solution documents, run local build or preview commands, and generate HTML that loads public CDN libraries.]

## Skill Version(s):

1.7.0 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
