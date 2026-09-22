## Description: <br>
Agent Knowledge helps agents capture and retrieve knowledge from URLs, videos, articles, papers, and social posts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to capture, structure, and retrieve knowledge from URLs, videos, articles, papers, and social posts within an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad command execution and file-writing authority for a generic knowledge workflow. <br>
Mitigation: Review proposed commands, file writes, and API calls before execution, and run the skill in a supervised or sandboxed agent environment. <br>
Risk: The security guidance cautions against giving the skill sensitive local data unless storage and handling are clear. <br>
Mitigation: Avoid sharing secrets or sensitive documents with the skill unless the data handling path is understood and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Structured text, Markdown, or JSON depending on the requested mode] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured processing results and metadata about the generated response.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
