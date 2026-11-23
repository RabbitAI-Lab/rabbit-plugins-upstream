## Description:

Design, build, refactor, or review terminal interfaces—full-screen TUIs, interactive prompts, and command-line tools. Use for terminal-app layout and UX, CLI behavior, ncurses-style tools, dashboards, REPLs, fzf-like pickers, and libraries such as Bubble Tea, Ratatui, Textual, or Ink, including requests that name a known TUI such as lazygit, k9s, btop, helix, or yazi instead of saying “TUI.” Do not use for browser or web UI, native GUI, editor or font configuration, or backend and shell work that has no terminal interface.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gfargo](https://clawhub.ai/user/gfargo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to design, build, refactor, and review command-line and full-screen terminal interfaces. It guides layout, interaction, accessibility, terminal behavior, and ecosystem-specific implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested free-text history may be retained without privacy safeguards.

Mitigation: Review whether history is stored, explain what it contains and how long it persists, and provide a clear way to disable or clear it.

Risk: The skill includes an unpinned package command.

Mitigation: Inspect the package and pin an approved version before running the command.

Risk: Three of eleven components were only partially inspected, so scan evidence is incomplete.

Mitigation: Review the affected components before relying on the skill in a sensitive workflow.

## Reference(s):

- [ClawHub release](https://clawhub.ai/gfargo/skills/tui-design)
- [Resolved GitHub source provenance](https://github.com/gfargo/tui-design-skill/tree/main/plugins/tui-design/skills/tui-design)
- [CLI basics](references/cli-basics.md)
- [Go ecosystem](references/ecosystem-go.md)
- [Python ecosystem](references/ecosystem-python.md)
- [Rust ecosystem](references/ecosystem-rust.md)
- [TypeScript ecosystem](references/ecosystem-typescript.md)
- [Exemplar apps](references/exemplar-apps.md)
- [Interaction patterns](references/interaction-patterns.md)
- [Terminal protocols](references/terminal-protocols.md)
- [Visual patterns](references/visual-patterns.md)
- [CLI Guidelines](https://clig.dev)
- [12-Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46)
- [Bubble Tea v2.1.0 source](https://github.com/charmbracelet/bubbletea/blob/v2.1.0/tea.go)
- [Bubbles v2 upgrade guide](https://github.com/charmbracelet/bubbles/blob/v2.2.1/UPGRADE_GUIDE_V2.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code]

**Output Format:** [Markdown with design recommendations, review findings, ASCII wireframes, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-dependent; focused references are selected for the interface type and ecosystem.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
