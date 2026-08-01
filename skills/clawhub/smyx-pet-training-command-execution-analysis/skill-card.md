## Description: <br>
Analyzes pet training videos or video URLs through remote APIs to judge whether a pet performed Sit, Down, or Stay commands, compare posture timing with command timestamps, and return structured training results without providing medical diagnosis or behavior therapy advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to evaluate pet command execution from training-area video, including posture match, response delay, and historical training report lookup. It is intended for smart pet-training devices, remote training workflows, and behavior-correction support, not clinical diagnosis or therapy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or video URLs are processed by remote Life Emergence services. <br>
Mitigation: Use the skill only when remote processing of the submitted media is acceptable, and avoid submitting sensitive video content. <br>
Risk: The skill can create or reuse an internal identity, query cloud report history, and retain account tokens in the workspace data directory. <br>
Mitigation: Review or clear the local data store when account linkage, retained tokens, or historical cloud report access are not acceptable. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-training-command-execution-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files] <br>
**Output Format:** [Structured Markdown or JSON analysis report with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command name, command timestamp, detected pet posture, posture match score, response delay, success judgment, recommendations, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.6 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
