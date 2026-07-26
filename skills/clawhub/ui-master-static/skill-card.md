## Description: <br>
Guides agents in building production-grade static user interfaces with native CSS, BEM, design tokens, accessible layouts, and modern effects without Tailwind, CSS-in-JS, or utility frameworks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and UI engineers use this skill to guide agents through framework-free HTML/CSS interface work, including static sites, headers, dashboard shells, landing layouts, design-token architecture, BEM naming, accessibility checks, and modern CSS effects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated UI changes can introduce accessibility, keyboard navigation, focus, contrast, or responsive-layout regressions. <br>
Mitigation: Use the bundled accessibility and performance checklist before shipping, including tab navigation, visible focus, semantic markup, contrast checks, touch targets, and 360px, 768px, and 1024px viewport tests. <br>
Risk: Advanced CSS effects such as scroll-driven animation, parallax, Houdini Paint API, and backdrop filters may behave differently across browsers or affect motion-sensitive users. <br>
Mitigation: Apply the artifact's reduced-motion guards and @supports fallbacks, limit heavy effects to a small number of elements, and test non-Chromium behavior when using Paint API or scroll-timeline features. <br>
Risk: The skill may guide an agent to edit project UI files and add small browser-side scripts for navigation toggles, theme state, or visual effects. <br>
Mitigation: Review generated file changes before deployment and verify that added scripts are limited to UI behavior rather than credential access, network exfiltration, or privileged system changes. <br>


## Reference(s): <br>
- [CSS Architecture: Tokens + BEM](artifact/references/css-architecture-bem.md) <br>
- [Layout Patterns - Native CSS](artifact/references/layout-patterns.md) <br>
- [Modern Effects Catalogue - Native CSS](artifact/references/modern-effects.md) <br>
- [Accessibility & Performance - Production Floor](artifact/references/accessibility-performance-checklist.md) <br>
- [ClawHub skill page](https://clawhub.ai/anjasta-tarigan/skills/ui-master-static) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to create or edit static UI files and add small browser-side JavaScript for navigation, theme state, or visual effects.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
