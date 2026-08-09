## Description: <br>
Transforms vague prompts into precise, structured AI instructions for prompt refinement, prompt engineering, system prompts, and more effective AI instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, prompt authors, and agent builders use this skill to turn vague requests into precise, structured prompts. It is especially relevant for instructions that another AI system will parse without a human back-channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A refined prompt can introduce incorrect or misleading instructions that downstream agents may follow. <br>
Mitigation: Review generated prompts before use, especially for system prompts or other machine-parsed instructions. <br>
Risk: Persisting prompt text can store sensitive or inappropriate content if the original prompt contains it. <br>
Mitigation: Use the skill's user-confirmed save behavior and review content before appending it to .ai/PROMPT.md. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown prompt text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May offer to append the refined prompt to .ai/PROMPT.md only after user confirmation.] <br>

## Skill Version(s): <br>
4.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
