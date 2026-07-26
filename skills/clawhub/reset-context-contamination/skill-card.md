## Description: <br>
Discard the accumulated drafts and framings from this thread and re-derive the task from a clean problem statement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Agents use this skill when a conversation has drifted or become anchored on earlier drafts. It helps extract the facts worth keeping, then either continue from a clean brief or hand the task to a fresh context for higher-stakes work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reset pattern intentionally deprioritizes earlier drafts, which can drop useful context if the extracted brief is incomplete. <br>
Mitigation: Review the extracted brief before continuing on sensitive work. <br>
Risk: For deep contamination or high-stakes work, continuing in the same conversation can preserve unwanted anchoring. <br>
Mitigation: Move the clean brief to a fresh subagent or a new session when the skill identifies deep contamination. <br>


## Reference(s): <br>
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/reset-context-contamination) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text] <br>
**Output Format:** [Markdown or plain text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only; no files, shell commands, or configuration are produced.] <br>

## Skill Version(s): <br>
0.1.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
