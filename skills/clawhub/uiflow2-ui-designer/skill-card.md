## Description:

Design, generate, beautify, optimize, or review UIFlow2 interfaces, graphics, dashboards, gauges, animations, round-screen layouts, e-paper screens, and LED-matrix experiences for M5Stack devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuyun2000](https://clawhub.ai/user/yuyun2000)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, generate, review, and refine embedded UIFlow2 interfaces for M5Stack devices, including dashboards, gauges, animations, round screens, e-paper displays, and LED-matrix layouts. It helps select an appropriate UIFlow2 rendering approach and keeps visual quality, API boundaries, and device constraints visible during implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may produce UIFlow2 design or code guidance that depends on board, display, input, font, RAM, or adjacent API documentation context.

Mitigation: Confirm the target device profile and consult the referenced UIFlow2 API documentation before treating generated code or interface choices as deployable.

Risk: Visual quality can be overstated if the interface is reviewed only through code or serial output.

Mitigation: Require simulator screenshots, fresh device images, or human device observation before marking a new or redesigned visible UI as visually passed.

Risk: Mixing UIFlow2 rendering systems or using oversized buffers can cause inconsistent behavior, flicker, or memory pressure on embedded devices.

Mitigation: Use one primary rendering path per interface and apply the skill's rendering strategy, frame-rate, and buffer-budget checks during implementation.

## Reference(s):

- [Skill release page](https://clawhub.ai/yuyun2000/skills/uiflow2-ui-designer)
- [Design Directions](artifact/references/design-directions.md)
- [Visual Quality Gate](artifact/references/visual-quality-gate.md)
- [Visual System](artifact/references/visual-system.md)
- [Rendering Strategy](artifact/references/rendering-strategy.md)
- [UIFlow2 API Patterns](artifact/references/api-patterns.md)
- [Layout Recipes](artifact/references/layout-recipes.md)
- [Display Profiles](artifact/references/display-profiles.md)
- [Motion And Effects](artifact/references/motion-and-effects.md)
- [UI Review Checklist](artifact/references/review-checklist.md)
- [m5ui overview](artifact/../uiflow2-coder/docs/m5ui/_overview.md)
- [Display API](artifact/../uiflow2-coder/docs/hardware/display.md)
- [Widgets overview](artifact/../uiflow2-coder/docs/widgets/_overview.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown prose with optional MicroPython code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for board, display, input, and content context; visual results should be reported as NOT RUN or PARTIAL when render or device evidence is unavailable.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
