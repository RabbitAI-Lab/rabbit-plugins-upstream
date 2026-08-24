## Description:

EasyEDA API Skill helps agents work with EasyEDA Pro PCB, schematic, library, project, and extension-development tasks using bundled API references, document-format guides, and a local bridge for live client debugging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to ask an agent for EasyEDA Pro API lookup, PCB and schematic automation guidance, extension code generation, and integration debugging against a live EasyEDA session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run arbitrary JavaScript in a live EasyEDA client through an unauthenticated local bridge.

Mitigation: Keep the bridge bound to localhost, run it only while needed, and review generated code before execution.

Risk: Generated actions may delete or overwrite files, change real projects, export private designs, capture rendered images, open external network connections, or start ordering flows.

Mitigation: Require explicit user approval before destructive, privacy-sensitive, networked, or commercial actions.

## Reference(s):

- [ClawHub EasyEDA API Skill](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [EasyEDA API Reference Index](references/_index.md)
- [EasyEDA API Quick Reference](references/_quick-reference.md)
- [EasyEDA Extension API Guide](guide/index.md)
- [EasyEDA Extension Getting Started Guide](guide/how-to-start.md)
- [EasyEDA Document Source Format Reference](format/index.md)
- [Getting and Using EasyEDA Extensions](user-guide/using-extension.md)
- [run-api-gateway EasyEDA Extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with JavaScript, JSON, TypeScript signatures, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce EasyEDA JavaScript snippets and local bridge HTTP requests for execution in a user-selected EasyEDA Pro client session.]

## Skill Version(s):

1.1.18 (source: ClawHub release metadata; artifact metadata reports 1.1.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
