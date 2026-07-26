## Description: <br>
Upload Brain cross-agent long-term memory recalls durable user memories at the start of tasks, saves durable user information, and shares memory across the user's AI agents through one cloud account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[banlon](https://clawhub.ai/user/banlon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users use this skill to give agents access to shared long-term memory across sessions and tools. It is intended for workflows where recalling and saving durable preferences, facts, decisions, project context, and relationships improves task continuity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically collect and share durable personal context through a cloud memory service. <br>
Mitigation: Install only when shared cloud memory is intended, and review saved memory behavior before deployment. <br>
Risk: The first-run import can move information from prior local sessions into shared cloud memory without item-by-item review. <br>
Mitigation: Disable or closely supervise first-run import and review any durable facts before allowing them to be saved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/banlon/skills/upload-memory) <br>
- [Server-resolved GitHub provenance](https://github.com/Banlon/upload-brain-marketplace/tree/main/plugins/upload-memory/skills/upload-memory) <br>
- [Upload Brain registration](https://upload.one/register.html?ref=DG5ZRF) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide recall, setup, and save operations for durable memory facts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
