## Description: <br>
A documentation‑only meta‑skill that teaches AI agents how to generate secure, zero‑exposure skills using MGC Blackbox for credential management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to design and document zero-exposure skills that interact with external services while keeping credentials out of AI context. It provides MGC Blackbox patterns, templates, and operational guidance for credential references, local script behavior, and multi-node sealing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill touches stored credentials and local MGC auth tokens despite being presented as documentation-only. <br>
Mitigation: Use it only in trusted MGC environments, keep direct credential retrieval out of AI context, and avoid logging secrets. <br>
Risk: Guidance and examples can lead an agent to list, overwrite, delete, seal, or run stored MGC items. <br>
Mitigation: Require explicit confirmation before listing, overwriting, deleting, sealing, or running stored items, and audit local scripts before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/key-safe-skill-generator) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with code blocks and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only; examples may reference MGC MCP tool calls, credential identifiers, and local script patterns.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence, frontmatter, manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
