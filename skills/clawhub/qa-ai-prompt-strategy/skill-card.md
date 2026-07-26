## Description: <br>
Selects structured prompt patterns that help agents generate deeper, more useful QA test cases from testing goals and context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, testers, and agent operators use this skill to choose prompt templates for functional, exception, boundary, concurrency, security, performance, multi-perspective, and adversarial test-case generation. It is especially useful when prior AI-generated test cases are too generic or shallow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad prompt-improvement requests outside a QA test-case workflow. <br>
Mitigation: Confirm the user's goal is QA test-case generation before applying these templates. <br>
Risk: Generated prompts can produce shallow or poorly targeted test cases when the input context is incomplete. <br>
Mitigation: Return to context engineering and add missing functional, risk, and constraint details before regenerating the prompt. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-ai-prompt-strategy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown prompt templates with role definitions, output-format specifications, and constraint lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces optimized prompts rather than executing tests or modifying files.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
