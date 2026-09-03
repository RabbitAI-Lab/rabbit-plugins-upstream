## Description:

A highly customizable UI design specification system based on headless component libraries (shadcn/ui, Radix UI), integrating Apple HIG, Microsoft Fluent, and Google Material Design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to generate or review custom UI implementations against Apple HIG, Microsoft Fluent, and Google Material Design guidance while retaining control over component structure and styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The validator can read local UI source files explicitly passed to it.

Mitigation: Run validation only on files intended for UI review and inspect the report before applying changes.

Risk: Validation reports and generated UI guidance can still miss context-specific accessibility or design issues.

Mitigation: Pair automated validation with the included checklist and human review for accessibility, responsive behavior, and platform fit.

## Reference(s):

- [Apple Human Interface Guidelines](references/apple-hig.md)
- [Microsoft Fluent Design System](references/microsoft-fluent.md)
- [Google Material Design 3](references/google-material.md)
- [Component Unified Specification and Comparison](references/component-specs.md)
- [Interaction Guidelines Comparison](references/interaction-guidelines.md)
- [UI Design Specification Validation Checklist](references/checklist.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Markdown]

**Output Format:** [Markdown guidance, UI code, validation commands, and structured validation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Validation can be run with python3 scripts/validate_ui.py against file or text input; color checks are optional.]

## Skill Version(s):

0.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
