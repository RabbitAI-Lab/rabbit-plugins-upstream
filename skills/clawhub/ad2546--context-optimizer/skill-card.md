## Description: <br>
Advanced context management with auto-compaction and dynamic context optimization for DeepSeek's 64k context window, including compaction, query-aware relevance scoring, hierarchical memory archive retrieval, and optimization event logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ad2546](https://clawhub.ai/user/ad2546) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to keep long DeepSeek conversations within context limits while preserving recent, high-priority, and query-relevant information. It can compact conversation history, retrieve archived snippets, report context health, and provide CLI or JavaScript integration paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation content may be retained locally or surfaced through optimization logs. <br>
Mitigation: For sensitive work, disable archive and chat logging or use a protected archive path with explicit retention and deletion rules. <br>
Risk: Cleanup or deletion commands may affect archived conversation data if paths are misconfigured. <br>
Mitigation: Review archive, uninstall, and cleanup paths before running commands that delete stored data. <br>


## Reference(s): <br>
- [Context Optimizer on ClawHub](https://clawhub.ai/ad2546/skills/context-optimizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Processed message arrays, archive snippets, status summaries, Markdown documentation, JavaScript examples, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can reflect configurable context limits, compaction thresholds, archive settings, and chat logging preferences.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
