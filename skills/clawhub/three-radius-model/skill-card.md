## Description: <br>
Guides agents through a Three-Radius Diagnostic that separates what a person or team understands, can do, and actually does so they can identify cognition-capability and capability-action gaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, coaches, operators, and teams use this skill to diagnose why understanding or capability is not translating into action, then define 30-day interventions with observable validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated diagnostics may include sensitive individual or team performance examples. <br>
Mitigation: Review diagnostics before sharing and avoid persisting real user or team failure examples into reusable notes unless explicitly approved. <br>
Risk: The skill can misclassify a gap if it relies on self-report instead of observable evidence. <br>
Mitigation: Apply the skill's gate rule by requiring dated behaviors, demonstrated outputs, external evaluation, and named validation mechanisms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/three-radius-model) <br>
- [deciqAI Three-Radius Model page](https://www.deciqai.com/c/three-radius-model) <br>
- [Agent metadata](https://www.deciqai.com/s/three-radius-model.json) <br>
- [Primary sources](references/sources.md) <br>
- [Nikola Tesla method-in-action example](examples/nikola-tesla-three-radius-divergence-1880-1943.md) <br>
- [Berkshire Hathaway 1996 letter](https://www.berkshirehathaway.com/letters/1996.html) <br>
- [Project Gutenberg: My Inventions](https://www.gutenberg.org/ebooks/13576) <br>
- [Project Gutenberg: Critique of Pure Reason](https://www.gutenberg.org/ebooks/4280) <br>
- [Dunning-Kruger study DOI](https://doi.org/10.1037/0022-3514.77.6.1121) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown diagnostic with structured lists, tables, questions, and 30-day action recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should pause at explicit WAIT gates when coaching novices and should rely on observable evidence rather than self-report.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
