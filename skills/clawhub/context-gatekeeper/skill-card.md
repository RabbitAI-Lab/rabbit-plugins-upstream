## Description: <br>
Keeps the conversation token-friendly by summarizing recent exchanges, surfacing pending actions, and delivering a compact briefing for each turn before calling the model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davienzomq](https://clawhub.ai/user/davienzomq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Context Gatekeeper to compress long OpenClaw conversations into a compact Markdown briefing with summary bullets, pending actions, and recent turns before the next model call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected chat history may be stored in local context files and reused in later prompts, which can expose secrets, personal data, or regulated data if users log it. <br>
Mitigation: Keep history short, remove secrets and personal or regulated data before logging, inspect current-summary.md before reuse, and clear the context files when finished. <br>
Risk: The background monitor can continuously watch history.txt and refresh summaries, creating ongoing local retention and lifecycle risk if left running unintentionally. <br>
Mitigation: Run the monitor only when continuous updates are deliberately needed, review its output files, and stop or remove the local context files after the workflow ends. <br>
Risk: Compact summaries can omit nuance or carry stale pending-action signals into later prompts. <br>
Mitigation: Review current-summary.md before relying on it and add the latest concrete turns when the compressed briefing is not enough for the next response. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davienzomq/skills/context-gatekeeper) <br>
- [README.md](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary file with command-line usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a compact summary from a local ROLE: message history; an optional monitor refreshes the summary when the history changes.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata and README publication details) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
