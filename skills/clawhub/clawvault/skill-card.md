## Description: <br>
Agent memory system with memory graph, context profiles, checkpoint and recovery support, structured storage, semantic search, observational memory, task tracking, and canvas workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g9pedro](https://clawhub.ai/user/g9pedro) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use ClawVault to preserve and retrieve local agent memory, recover session context, checkpoint ongoing work, search prior decisions, and inject relevant context into OpenClaw sessions after explicit hook installation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can automatically reuse prior vault and session context, which may surface unrelated or sensitive history during future work. <br>
Mitigation: Choose CLAWVAULT_PATH deliberately, review stored memories regularly, and avoid storing secrets or unrelated private history in the vault. <br>
Risk: The opt-in hook reads and writes local vault files and can inspect or modify OpenClaw session transcripts for recovery workflows. <br>
Mitigation: Review the bundled hook before enabling it, install and enable hooks explicitly, and rely on the documented backup behavior for session repair. <br>
Risk: Observation compression can send transcript-derived content to Gemini when GEMINI_API_KEY is configured. <br>
Mitigation: Leave GEMINI_API_KEY unset unless sending that content to the configured LLM provider is acceptable for the environment. <br>


## Reference(s): <br>
- [ClawVault ClawHub page](https://clawhub.ai/g9pedro/skills/clawvault) <br>
- [ClawVault homepage](https://clawvault.dev) <br>
- [ClawVault npm package](https://www.npmjs.com/package/clawvault) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [qmd dependency](https://github.com/tobi/qmd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and hook-injected text context] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local vault Markdown files, create session checkpoints, and inject concise memory context into enabled OpenClaw sessions.] <br>

## Skill Version(s): <br>
2.5.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
