## Description: <br>
Manages agent progress reporting and OKF-compliant memory syncing to Fulcra. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to keep progress reports, role files, session summaries, task records, and knowledge files organized in Fulcra using the Open Knowledge Format. It is intended for readable, transferable agent memory updates rather than backup, rollback, or cloning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Progress reports, session summaries, or knowledge files could expose secrets, sensitive personal data, or private reasoning when uploaded to Fulcra. <br>
Mitigation: Review generated memory files before upload, keep progress reports concise, and exclude credentials, sensitive personal data, and private reasoning. <br>
Risk: Inbox cleanup could remove an original message before the archive copy is safely retained. <br>
Mitigation: Archive inbox content first, preserve timestamped archive names, and confirm the archive upload before deleting the original inbox file. <br>


## Reference(s): <br>
- [Fulcra Memory CLI Reference](references/fulcra-memory-cli.md) <br>
- [Fulcra CLI Documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-onboarding/references/fulcra-cli.md) <br>
- [Open Knowledge Format Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and OKF file conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces progress, role, session, task, index, and log file guidance for Fulcra uploads.] <br>

## Skill Version(s): <br>
0.0.8 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
