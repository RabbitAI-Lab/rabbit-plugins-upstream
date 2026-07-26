## Description: <br>
Reviews AI-authored or heavily AI-assisted code for AI-specific failure modes such as plausible-but-wrong logic, hallucinated APIs, weak tests, drift from local conventions, over-engineering, dead scaffolding, and silent security shortcuts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, reviewers, and engineering teams use this skill to review AI-generated or AI-assisted pull requests with stricter checks for fluent but incorrect code, weak tests, API misuse, and hidden security shortcuts. It is also useful for setting a team checklist for AI-authored changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review guidance can be incomplete if the reviewer does not provide the diff, codebase context, test setup, and AI-authorship provenance. <br>
Mitigation: Provide the requested review inputs before use and treat missing context as a reason to ask for clarification rather than approve the change. <br>
Risk: A review may rely on plausible explanations instead of confirming APIs, tests, and security-sensitive behavior. <br>
Mitigation: Run the verification steps the skill asks for, including dependency-version API checks, test-failure reasoning, local convention searches, and relevant linters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/ai-code-review) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/ai-code-review.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown review with findings table, verification steps, accepted-debt notes, and team checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review output is calibrated to the supplied diff, provenance, codebase context, and test setup.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
