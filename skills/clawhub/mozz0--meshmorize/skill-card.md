## Description: <br>
Multi-layer memory system for LLM agents with a fresh daily layer, mesh graph indexing, auto-logging, cross-layer search, and compliance checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mozz0](https://clawhub.ai/user/mozz0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Meshmorize to give an LLM agent persistent local memory across sessions, including daily notes, graph-indexed memory, interaction logging, search, and compliance checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to retain interaction logs and memory files across sessions, which can preserve sensitive or regulated data if an agent logs it. <br>
Mitigation: Review what is logged before use, avoid secrets and regulated data, and clear workspace memory files when retention is no longer intended. <br>
Risk: Installation guidance involves local command symlinks, so stale or unwanted commands can remain available after removing the workspace files. <br>
Mitigation: Track created symlinks and remove the related ~/.local/bin entries during uninstall. <br>


## Reference(s): <br>
- [Meshmorize release page](https://clawhub.ai/mozz0/meshmorize) <br>
- [mozz0 publisher profile](https://clawhub.ai/user/mozz0) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe persistent local memory files and command symlinks used by the agent workspace.] <br>

## Skill Version(s): <br>
3.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
