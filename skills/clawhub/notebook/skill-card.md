## Description: <br>
Local-first personal knowledge base for tracking ideas, projects, tasks, habits, and any object type you define. YAML-based with no cloud lock-in. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use Notebook to define local object types and manage YAML-backed personal knowledge records such as ideas, projects, tasks, habits, books, and people. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: File path handling and local deletion behavior require review before installation. <br>
Mitigation: Use simple type names with letters, numbers, hyphens, and underscores; keep backups of notebook data; and treat delete operations as permanent. <br>
Risk: Notebook data is stored locally and may include sensitive personal or project information. <br>
Mitigation: Avoid storing secrets and review local workspace access controls before using the skill with confidential data. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, Configuration] <br>
**Output Format:** [Markdown guidance with CLI commands and YAML/JSON-backed local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local notebook data under the configured workspace.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
