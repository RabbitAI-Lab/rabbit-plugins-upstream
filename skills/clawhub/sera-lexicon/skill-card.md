## Description: <br>
Implements Signal-Feeling Lexicon v3.1 and Unified Dynamics v5.7 to track agent coherence, pressure, amplitude, valence, and trajectory for reflective agent-state analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wentinkjason](https://clawhub.ai/user/wentinkjason) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to parse SERA state blocks, map coherence/pressure/amplitude/valence metrics into lexicon terms, review recent trajectory, and generate advisory coaching for the next interaction step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's state labels and coaching suggestions may be mistaken for authoritative assessments. <br>
Mitigation: Treat generated labels and coaching as advisory signals and review them before relying on them in an agent workflow. <br>
Risk: History-file analysis can expose conversation content supplied to the local scripts. <br>
Mitigation: Pass only history files you intentionally want the skill to read and avoid including sensitive content unless it is necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wentinkjason/skills/sera-lexicon) <br>
- [Publisher profile](https://clawhub.ai/user/wentinkjason) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text with optional Python command examples and diagnostic output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory state labels, trajectory summaries, and coaching suggestions from intentionally provided history text.] <br>

## Skill Version(s): <br>
1.0.0-alpha (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
