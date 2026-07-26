## Description: <br>
Helps developers create, review, and refine agent skills by analyzing boundaries, extracting reusable constraint patterns, and proposing concrete revisions that make skills better scoped and harder to misuse. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[immmmmmortal1](https://clawhub.ai/user/immmmmmortal1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to audit existing skills, extract reusable boundary patterns, and revise skill instructions with clearer scope, fallback behavior, and output contracts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated skill revisions can introduce incorrect or overly broad instructions if applied without review. <br>
Mitigation: Review proposed changes against the target skill's intended scope before installing or publishing them. <br>
Risk: The skill references a hard-coded local pattern file path that may not exist in a user's environment. <br>
Mitigation: Update the pattern storage path before relying on the pattern harvesting step. <br>


## Reference(s): <br>
- [Source repository](https://github.com/Immmmmmortal1/shuxia_skill_library) <br>
- [ClawHub skill page](https://clawhub.ai/immmmmmortal1/skills/shuxia-skill-library) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with structured review sections and concrete rewrite suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PASS, WARNING, or ERROR review labels, reusable boundary patterns, and skill revision guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; provenance commit c8df0d1abab060279afc5850ce91728ef2c91c2e) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
