## Description: <br>
ByteRover helps agents retrieve, search, curate, review, and version project knowledge stored in `.brv/context-tree/` through the `brv` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent consult and maintain project memory, including knowledge queries, ranked local search, curated notes, pending change review, and context-tree version control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project knowledge, query text, and selected file contents may be processed by a configured LLM provider. <br>
Mitigation: Prefer local search when synthesis is unnecessary, avoid curating secrets or personal data, and review provider configuration before using query or curate workflows. <br>
Risk: Optional cloud sync and external memory-provider workflows can move project knowledge outside the local context tree. <br>
Mitigation: Require explicit user intent before running sync, swarm curate, or file-including curate commands. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and occasional JSON command output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to run local `brv` commands; query and curate workflows can process project knowledge, query text, and selected file contents with a configured LLM provider.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
