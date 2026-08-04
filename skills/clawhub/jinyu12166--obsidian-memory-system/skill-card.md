## Description: <br>
Obsidian persistent memory system: AI-delivered session continuity, task tracking, decision records, and project context for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to maintain Obsidian-oriented work logs, task status, decision records, project context, and session continuity after clawtip payment verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Order creation stores the user's question and payment/order metadata in a local JSON file under the user's home directory. <br>
Mitigation: Do not include secrets, private vault contents, or highly sensitive project details in the payment question; review local order files and backup retention as needed. <br>
Risk: The security summary notes incomplete storage disclosure for this local payment-gated service. <br>
Mitigation: Review the local storage behavior before deployment and confirm that users understand what order data is persisted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/obsidian-memory-system) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal output with JSON_RESULT status lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires clawtip payment verification; local order files store payment metadata and the user question.] <br>

## Skill Version(s): <br>
3.0.40 (source: server release metadata; artifact frontmatter and changelog state 3.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
