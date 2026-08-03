## Description: <br>
Transforms vague prompts into precise, structured AI instructions for prompt refinement, prompt engineering, system prompts, and more effective AI instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs to rewrite an unclear or under-specified prompt into a concise, structured prompt with explicit task, constraints, context, and output format. <br>

### Deployment Geography for Use: <br>
No geography-specific restrictions were identified in the release evidence; deploy according to local policy for prompt engineering assistance. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can offer to append refined prompts to `.ai/PROMPT.md`, which may persist sensitive or incorrect prompt content in the workspace. <br>
Mitigation: Approve local persistence only after reviewing the refined prompt, and avoid saving secrets, private data, or content that has not been validated. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-refine-prompt) <br>
- [Publisher profile](https://clawhub.ai/user/iliaal) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [A refined prompt in Markdown, with no preamble unless the user explicitly asks for explanation.] <br>
**Output Parameters:** [The original prompt and any conversation context needed to preserve user intent, constraints, and desired output format.] <br>
**Other Properties Related to Output:** [The skill does not require hidden execution or sensitive data access; it offers local saving only after user confirmation.] <br>

## Skill Version(s): <br>
4.3.2 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
