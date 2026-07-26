## Description: <br>
Run parallel agents to debate multiple approaches to a question, then synthesize their positions to identify a recommended solution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cxbjames](https://clawhub.ai/user/cxbjames) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical teams use this skill to structure non-obvious decisions by assigning multiple agents to argue competing positions, write debate notes, and synthesize a verdict. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local debate files may expose sensitive topic names, prompts, or decision details if committed or shared. <br>
Mitigation: Use non-sensitive topic names, avoid secrets in debate prompts, and review generated markdown files before committing or sharing them. <br>
Risk: A synthesized verdict can be persuasive while still omitting evidence or recommending an unsuitable approach. <br>
Mitigation: Treat the verdict as decision support and validate important claims against project evidence before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cxbjames/skills/agent-debate) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance] <br>
**Output Format:** [Markdown debate notes and synthesis files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local files under plans/debate-{topic}/ for the question, agent positions, rebuttals, synthesis, and final decision.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
