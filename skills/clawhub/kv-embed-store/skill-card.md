## Description: <br>
Embedding-based key-value store with fuzzy embedding search, multi-alias deduplication, and optional memory indexing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaojun0](https://clawhub.ai/user/shaojun0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to store structured values under natural-language aliases, retrieve them by embedding similarity, and optionally expose selected entries through memory search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Embedding provider requests can disclose key names and search queries to the configured provider. <br>
Mitigation: Use a trusted HTTPS embedding provider, protect the API key, and avoid sensitive keys or regulated data. <br>
Risk: Enabling memoryIndex can make stored aliases and value previews discoverable through memory search. <br>
Mitigation: Enable memoryIndex only for entries that are acceptable to expose through workspace memory discovery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shaojun0/skills/kv-embed-store) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May emit JSON-formatted key-value store records and search results when used through the standalone CLI.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
