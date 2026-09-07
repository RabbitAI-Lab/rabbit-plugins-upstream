## Description:

A UI design specification system based on off-the-shelf UI frameworks (Element Plus, Ant Design, Arco Design, TDesign, Semi Design). Suitable for projects using framework-built-in components, as opposed to headless component libraries (shadcn/ui, Radix UI). Use when: generating UI code with a specified framework, reviewing existing code for framework compliance, recommending between frameworks, or migrating code from one framework to another. Keywords: Element Plus, Ant Design, Arco Design, TDesign, Semi Design, framework components, Vue components, React components, framework migration, design tokens, theme variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select among supported UI frameworks, generate framework-compliant UI code, review existing code for component and token usage, and plan migrations between framework component systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated UI code may carry an unintended locale choice from framework examples.

Mitigation: Confirm the target application locale and framework locale imports before applying generated code.

Risk: Framework API details may drift as the referenced UI libraries release new versions.

Mitigation: Check the current official framework documentation when generating production code or planning migrations.

## Reference(s):

- [Framework Selection Guide](references/framework-selection.md)
- [Element Plus Reference](references/element-plus.md)
- [Ant Design Reference](references/ant-design.md)
- [Arco Design Reference](references/arco-design.md)
- [TDesign Reference](references/tdesign.md)
- [Semi Design Reference](references/semi-design.md)
- [Element Plus Documentation](https://element-plus.org)
- [Ant Design Documentation](https://ant.design)
- [Arco Design Documentation](https://arco.design)
- [TDesign Documentation](https://tdesign.tencent.com)
- [Semi Design Documentation](https://semi.design)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration]

**Output Format:** [Markdown with framework-specific code examples and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should follow the selected framework's official component names, props, layout system, and design token conventions.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
