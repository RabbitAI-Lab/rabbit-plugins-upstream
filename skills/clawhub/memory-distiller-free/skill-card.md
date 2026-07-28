## Description: <br>
Provides local log distillation that compresses a single Markdown log into a structured summary using keyword extraction and concise summary principles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to summarize daily Markdown logs into shorter structured memory notes before optionally appending them to long-term memory files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Compressed summaries may omit details, duplicate content, or introduce lossy interpretations before being added to long-term memory. <br>
Mitigation: Review the generated summary, especially /tmp/compressed.md, before appending it to MEMORY.md. <br>
Risk: The artifact references a Node.js script that is not present in the submitted package. <br>
Mitigation: Confirm the required script is available in the runtime environment before relying on the skill for log distillation. <br>
Risk: A callback URL could send processed results outside the local workspace if used. <br>
Mitigation: Avoid callback_url unless the destination is known and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/memory-distiller-free) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown summary with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a local compressed summary for review before appending to MEMORY.md.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
