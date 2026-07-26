## Description: <br>
Memory Bank text-based update workflow following integrated-rules v6.12 for manually updating memory bank markdown files, including edit chunks, tasks.md, session_cache.md, session files, and task files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents maintaining classic text-based memory banks use this skill to document completed work through direct markdown edits. It guides discovery of undocumented changes and updates task, session, cache, implementation, and edit-history records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can lead an agent to create or update local memory-bank documentation, and weak change control could record incorrect or unintended project history. <br>
Mitigation: Use this only when local memory-bank markdown maintenance is intended, require review before creating session files or updating documentation, and inspect generated edits before relying on them. <br>


## Reference(s): <br>
- [Integrated Code Rules and Memory Bank System, v6.12](references/integrated-rules-v6.12.md) <br>
- [Memory Bank File Templates, v6.12](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with templates and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local documentation-update guidance for memory-bank markdown files; security evidence found no hidden execution, network use, or credential handling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
