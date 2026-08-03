## Description: <br>
Jina AI (jina.ai). Use this skill for ANY Jina AI request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run Jina AI embedding and document reranking actions through an OOMOL-connected account with live schema inspection and CLI execution guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and documents sent for embeddings or reranking pass through the OOMOL Jina AI connector and may consume service credits. <br>
Mitigation: Confirm the payload and expected service usage before running actions, and avoid sending sensitive content unless the user approves that handling. <br>
Risk: The create_embeddings action is write-tagged and may create service-side artifacts or billable work. <br>
Mitigation: Confirm the exact JSON payload and intended effect with the user before executing write-tagged actions. <br>
Risk: First-time installer, login, and connection commands can change local or account state if run unnecessarily. <br>
Mitigation: Run setup, authentication, or connection steps only after a command fails with the matching missing-tool, auth, scope, credential, app, or billing error. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-jina-ai) <br>
- [Jina AI Homepage](https://jina.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
