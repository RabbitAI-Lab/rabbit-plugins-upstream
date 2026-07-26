## Description: <br>
Drafts, revises, polishes, humanizes, and quality-checks Chinese official documents and government-style practical writing with correct document type, format, restrained tone, concrete facts, and reduced AI-flavored phrasing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuxiangjian-ai](https://clawhub.ai/user/liuxiangjian-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to generate, revise, or polish Chinese official documents, government-style practical writing, policy explanations, speeches, reports, notices, requests, and related institutional materials. It is intended to produce usable Chinese drafts while flagging missing facts with placeholders instead of inventing official details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may provide confidential or regulated government material to the agent environment. <br>
Mitigation: Use the skill only in an environment approved for that material, and avoid submitting sensitive government content when the environment is not appropriate. <br>
Risk: Official documents can become misleading if the model invents laws, approvals, names, dates, budgets, metrics, or outcomes. <br>
Mitigation: Require source facts from the user, preserve bracketed placeholders for missing facts, and review all factual claims before use. <br>
Risk: The wrong document type or official relationship can create an unusable or procedurally incorrect draft. <br>
Mitigation: Check the selected document type, issuer-recipient relationship, required closing formula, and format elements before final delivery. <br>


## Reference(s): <br>
- [Artifact README](artifact/README.md) <br>
- [Manual Regression Tests](artifact/tests.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/liuxiangjian-ai/skills/document-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Chinese prose or Markdown draft with optional short missing-information list] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses bracketed placeholders when key facts are missing; produces no executable output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
