## Description:

Helps AI agents work with EasyEDA by providing API references, extension-development guidance, document-format docs, and a local bridge for live client debugging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to look up EasyEDA APIs, generate or debug extension code, inspect PCB, schematic, and project formats, and optionally execute code in a connected EasyEDA Pro client through the bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can execute broad EasyEDA code without authentication.

Mitigation: Run the bridge only while actively debugging, keep it stopped otherwise, and review code before sending it to /execute.

Risk: A running localhost bridge may be exposed to unwanted browser or local process interaction.

Mitigation: Avoid browsing untrusted sites while the bridge is running and confirm the connected EasyEDA client before executing actions.

Risk: Mutable setup commands can change the installed toolchain over time.

Mitigation: Prefer pinned or otherwise verified installation and publishing commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [EasyEDA API Skill README](artifact/README.md)
- [Skill Instructions](artifact/SKILL.md)
- [API Reference Index](artifact/references/_index.md)
- [Quick API Reference](artifact/references/_quick-reference.md)
- [AI Integration Guide](artifact/guide/how-to-start-for-ai.md)
- [Extension Development Guide](artifact/guide/how-to-start.md)
- [EasyEDA Extension Gateway](https://jlcext.com/item/oshwhub-official/run-api-gateway)
- [Agent Skills Standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks, commands, and API-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JavaScript snippets and localhost bridge commands for use with an EasyEDA Pro client.]

## Skill Version(s):

1.1.24 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
