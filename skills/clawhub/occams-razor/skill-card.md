## Description: <br>
Occam's Razor helps an agent rank competing explanations, designs, or diagnoses by checking that each candidate fits the evidence and then preferring the one with the fewest unsupported assumptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to compare multiple plausible hypotheses or designs, run a parsimony audit, and identify what evidence would overturn the preferred option. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Runtime freshness checks can make agent behavior depend on remote, changeable instructions. <br>
Mitigation: Review, pin, or disable the remote update path when reproducible, locally reviewed behavior is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/occams-razor) <br>
- [Sources](references/sources.md) <br>
- [deciqAI current skill metadata](https://www.deciqai.com/s/occams-razor.json) <br>
- [Stanford Encyclopedia of Philosophy: William of Ockham](https://plato.stanford.edu/entries/ockham/) <br>
- [Encyclopaedia Britannica: Occam's razor](https://www.britannica.com/topic/Occams-razor) <br>
- [Anthropic: Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text] <br>
**Output Format:** [Markdown Parsimony Audit with candidates, fit check, assumption load, preferred option, over-shave check, and overturning evidence.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask follow-up questions in coach mode and pause at explicit wait points when guiding a novice.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
