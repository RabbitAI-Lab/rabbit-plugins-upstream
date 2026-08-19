## Description:

EasyEDA API Skill helps agents work with EasyEDA by using API references, document format guidance, and a local WebSocket bridge for live debugging and extension development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect EasyEDA APIs, generate extension or automation code, debug against a running EasyEDA client, and understand project, schematic, and PCB source formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can expose unauthenticated code execution into a live EasyEDA design session.

Mitigation: Install only in a trusted local development environment, keep the bridge bound to localhost, stop it when not actively used, and require explicit human review before code changes projects or design data.

Risk: Bridge-driven actions may modify projects, delete data, capture design content, fetch remote libraries, or open manufacturing and order flows.

Mitigation: Review generated code and commands before execution, especially when they affect project state, external content, or manufacturing workflows.

Risk: The security evidence recommends updating the ws dependency before regular use.

Mitigation: Update ws to a patched version and rescan the package before routine installation.

## Reference(s):

- [EasyEDA API reference index](artifact/references/_index.md)
- [EasyEDA API quick reference](artifact/references/_quick-reference.md)
- [EasyEDA document source format overview](artifact/format/index.md)
- [EasyEDA extension development guide](artifact/guide/index.md)
- [EasyEDA extension user guide](artifact/user-guide/using-extension.md)
- [run-api-gateway extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands, JavaScript snippets, API request examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include EasyEDA API calls and local bridge commands that require human review before execution]

## Skill Version(s):

1.1.7 (source: server release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
