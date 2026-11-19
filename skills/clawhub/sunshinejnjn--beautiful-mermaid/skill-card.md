## Description:

Render Mermaid diagrams as beautiful SVG, PNG, or ASCII art. Supports 6 chart types (flowchart, sequence, state, class, ER, XY chart), 16 built-in themes, 5 style presets, CSS-level customization, interactive preview, and batch rendering. Works in terminal, chat, or web environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinejnjn](https://clawhub.ai/user/sunshinejnjn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical teams use the skill to turn Mermaid source into styled diagrams for documentation, presentations, applications, and terminal output. It supports interactive style previews and batch rendering for diagram collections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SVG from untrusted Mermaid input may be unsafe to embed.

Mitigation: Validate input and sanitize generated SVG before embedding it in a page or application.

Risk: The preview may make Google Fonts requests, and the security scan is incomplete with dependency advisories not independently verified.

Mitigation: Account for external font requests in privacy review, inspect files not fully covered by the scan, and verify dependency advisories before installation.

## Reference(s):

- [Project homepage](https://github.com/chouraycn/beautiful-mermaid)
- [Mermaid syntax documentation](https://mermaid.js.org/)
- [Online demo](https://agents.craft.do/mermaid)

## Skill Output:

**Output Type(s):** [SVG diagrams, PNG images, ASCII/Unicode diagrams, HTML pages]

**Output Format:** [SVG, PNG, ASCII/Unicode text, and HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports themed and customized output, interactive previews, and batch rendering.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
