## Description:

Design and implement intentional web motion with GSAP, React, Next.js, ScrollTrigger, Flip, SplitText, accessibility, performance, and responsive behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cbbathaglini](https://clawhub.ai/user/cbbathaglini)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and frontend engineers use this skill to design and implement purposeful GSAP motion in React and Next.js interfaces, including scroll interactions, layout transitions, reduced-motion alternatives, and performance-conscious animation patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated animation code can create accessibility regressions if reduced-motion preferences, keyboard flow, or screen-reader semantics are missed.

Mitigation: Review generated code for prefers-reduced-motion handling, visible focus behavior, semantic DOM structure, and usable screen-reader flows.

Risk: Scroll-linked or layout-heavy animations can cause jank, delayed interaction, or obscured content on small screens and lower-powered devices.

Mitigation: Prefer transform and opacity animations, simplify mobile scroll scenes, avoid unnecessary pinning, and test timing and trigger behavior across viewport sizes.

Risk: React and Next.js integrations can duplicate animations or leak triggers when component lifecycle cleanup is incomplete.

Mitigation: Scope GSAP work to component refs or contexts and clean up timelines, ScrollTriggers, matchMedia registrations, and event listeners on unmount or route change.

## Reference(s):

- [Accessibility](artifact/references/accessibility.md)
- [Anti-Patterns](artifact/references/anti-patterns.md)
- [Decision Guide](artifact/references/decision-guide.md)
- [GSAP Core](artifact/references/gsap-core.md)
- [Motion Design](artifact/references/motion-design.md)
- [Next.js](artifact/references/nextjs.md)
- [Performance](artifact/references/performance.md)
- [React](artifact/references/react.md)
- [Responsive Motion](artifact/references/responsive-motion.md)
- [ScrollTrigger](artifact/references/scrolltrigger.md)
- [Timelines](artifact/references/timelines.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration]

**Output Format:** [Markdown guidance with TypeScript, TSX, CSS, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs should be reviewed for accessibility, reduced-motion behavior, lifecycle cleanup, and animation performance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
