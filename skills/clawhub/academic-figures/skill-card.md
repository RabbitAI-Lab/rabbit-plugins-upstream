## Description:

Helps agents generate publication-ready scientific charts and journal figures from local data using a command-line renderer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, clinicians, and developers use this skill to turn JSON, CSV, or Excel data into scientific charts and publication-ready figures, including survival curves, forest plots, and multi-panel layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: On shared machines, the MCP server's predictable temporary output paths can expose or overwrite rendered research or clinical data.

Mitigation: Prefer local single-user CLI rendering; avoid the MCP server with sensitive data until its output paths are private, randomized, and symlink-safe.

Risk: The documented unpinned git-based MCP installation can incorporate unexpected upstream changes.

Mitigation: Pin the installation to a reviewed version or commit.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and compatibility](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The suggested local commands can render PNG, PDF, SVG, TIFF, or EPS figures.]

## Skill Version(s):

4.8.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
