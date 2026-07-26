## Description: <br>
Guides an agent to read AIOS ontology, construct request payloads, invoke AIOS/OpenClaw/Forguncy business-system commands through the approved CLI, and summarize live results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kadbbz](https://clawhub.ai/user/kadbbz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query or operate AIOS, OpenClaw, and Forguncy business systems after reading the current ontology, preparing request JSON, invoking the approved CLI, and summarizing live results. It is suited to workflows that need real-time business data, binding lookups, or confirmed system actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent live access to business systems with high-impact read/write authority that may not be scoped clearly enough for automatic use. <br>
Mitigation: Install only for agents intended to access those systems, limit the connected account permissions, prefer read-only access where possible, and require explicit confirmation before changes, workflow triggers, or sensitive payloads. <br>
Risk: Incorrect session or workspace identifiers could expose or mix user data during file-backed requests, downloads, or intermediate processing. <br>
Mitigation: Use only the current session topic_id for CLI calls and the current senderId for workspace isolation; stop if either required value is missing. <br>
Risk: Calling a business command with guessed application names, command names, parameters, or enum mappings could produce incorrect results or unintended system actions. <br>
Mitigation: Read the current ontology before each call, treat it as the source of truth, and stop for user review when required fields or unique command matches are unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kadbbz/skills/aios-call-app-service) <br>
- [Artifact README](artifact/readme.md) <br>
- [Artifact skill instructions](artifact/SKILL.md) <br>
- [AIOS application invocation rules](artifact/references/invoke-rules.md) <br>
- [AIOS data processing rules](artifact/references/data-processing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command examples when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite the ontology files or entries used, identify servercommand versus binding calls, and disclose assumptions, missing fields, skipped data, and uncertainty.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
