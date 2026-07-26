## Description: <br>
Write or rewrite a document in evidence-locked mode so every substantive claim cites an exact passage from user-provided sources or is explicitly marked as unsupported. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to draft or revise documents for review-sensitive audiences where factual claims need quote-level support from supplied sources. It is suited for legal, board, regulatory, enterprise buyer, and similar documents where unsupported claims should be visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may quote exact passages from user-provided sources in the generated source map. <br>
Mitigation: Provide only sources the user is authorized to use and share in the resulting document. <br>
Risk: The skill cannot produce evidence-locked output without supplied sources. <br>
Mitigation: Require source material before using the workflow, and keep unsupported claims flagged or moved to the unsupported-claims register. <br>


## Reference(s): <br>
- [Evidence Lock on ClawHub](https://clawhub.ai/mohitagw15856/skills/evidence-lock) <br>
- [Evidence Lock homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/evidence-lock.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown document with numbered citations, source map, unsupported-claims register, and coverage score] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided sources; substantive claims are cited, labelled as inference, or marked unsupported depending on strictness.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
