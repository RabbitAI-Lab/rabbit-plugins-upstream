## Description: <br>
Compress JSON data to TOON format for ~40% context savings when fetching APIs, reading JSON files, or handling structured command output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bonk-moltbot](https://clawhub.ai/user/bonk-moltbot) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to pipe trusted JSON API responses, JSON files, or structured command output through TOON for more compact context use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed bundle does not include the helper script or CLI implementation. <br>
Mitigation: Verify the installed toon executable or @toon-format/cli package before use. <br>
Risk: Piping sensitive or exact-fidelity data through a formatter can expose or alter content that should remain unchanged. <br>
Mitigation: Use the skill only with trusted JSON and avoid secrets, credentials, personal data, or workflows that require exact raw JSON preservation. <br>


## Reference(s): <br>
- [TOON Format Specification](https://toonformat.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Text] <br>
**Output Format:** [Markdown with inline bash commands and TOON or pass-through text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npx and an available toon executable or @toon-format/cli package; JSON is transformed to TOON and non-JSON passes through unchanged.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
