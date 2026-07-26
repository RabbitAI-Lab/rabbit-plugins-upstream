## Description: <br>
Four-Layer Memory organizes agent memory into identity, working memory, short-term logs, and long-term storage so context can accumulate without overcrowding active prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lingmoon96-dev](https://clawhub.ai/user/lingmoon96-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to keep persistent memory organized by stability and recency, including identity anchors, current tasks, daily logs, and confirmed long-term preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory can retain secrets or sensitive personal details if users save them intentionally or accidentally. <br>
Mitigation: Avoid storing secrets or sensitive personal details unless intentional, and periodically review or archive saved memory. <br>
Risk: The skill recommends commands for a separate personal_ai_memory.py script whose contents are not included in the artifact evidence. <br>
Mitigation: Inspect the local personal_ai_memory.py script before running the recommended commands. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides directory-placement guidance for memory records and recommended maintenance commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
