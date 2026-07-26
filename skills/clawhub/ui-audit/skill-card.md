## Description: <br>
AI skill for automated UI audits. Evaluate interfaces against proven UX principles for visual hierarchy, accessibility, cognitive load, navigation, and more. Based on Making UX Decisions by Tommy Geoco. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tommygeoco](https://clawhub.ai/user/tommygeoco) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Designers, product teams, and developers use this skill to review interfaces, choose UI patterns, and produce structured audit reports covering hierarchy, visual style, accessibility, navigation, usability, onboarding, social proof, and forms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Npm installation runs a postinstall script. <br>
Mitigation: Evidence.security reports the reviewed postinstall command only prints setup instructions; review package scripts before installing in locked-down environments. <br>
Risk: UI audit recommendations can be subjective or incomplete without product context, user research, or accessibility testing. <br>
Mitigation: Use the skill output as review guidance and validate proposed fixes with product constraints, user evidence, and accessibility checks before implementation. <br>


## Reference(s): <br>
- [UI Audit ClawHub Page](https://clawhub.ai/tommygeoco/skills/ui-audit) <br>
- [UI Audit Guidelines](https://audit.uxtools.co) <br>
- [Making UX Decisions](https://uxdecisions.com) <br>
- [UI Audit npm Package](https://npmjs.com/package/ui-audit) <br>
- [Core Framework: Warp-Speed Decisioning](references/00-core-framework.md) <br>
- [The 7 Anchors: Foundational Mindsets](references/01-anchors.md) <br>
- [Information Scaffold: Psychology, Economics, Accessibility, Defaults](references/02-information-scaffold.md) <br>
- [Checklist: Designing New Interfaces](references/10-checklist-new-interfaces.md) <br>
- [Checklist: Improving Fidelity](references/11-checklist-fidelity.md) <br>
- [Checklist: Improving Visual Style](references/12-checklist-visual-style.md) <br>
- [Checklist: Innovation & Originality](references/13-checklist-innovation.md) <br>
- [Patterns: Visual Hierarchy](references/23-patterns-visual-hierarchy.md) <br>
- [Patterns: Social Proof](references/24-patterns-social-proof.md) <br>
- [Patterns: System Feedback](references/25-patterns-feedback.md) <br>
- [Patterns: Error Prevention & Handling](references/26-patterns-error-handling.md) <br>
- [Patterns: Accessibility](references/27-patterns-accessibility.md) <br>
- [Patterns: Navigation & Wayfinding](references/31-patterns-navigation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown guidance and structured JSON audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit reports may include pass, warn, fail, or not-applicable checks and prioritized fixes with framework references.] <br>

## Skill Version(s): <br>
1.0.1 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
