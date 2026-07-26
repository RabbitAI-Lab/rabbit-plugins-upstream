## Description: <br>
Bump Doctor helps developers assess npm or PyPI dependency upgrades by fetching upstream release evidence, comparing it with symbols used in the target codebase, and returning a focused risk report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ckarnell](https://clawhub.ai/user/ckarnell) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before bumping an npm or PyPI dependency to identify likely breaking changes, migration work, and code-specific upgrade risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The analyzer fetches public npm, PyPI, and GitHub release data, so results depend on upstream availability and rate limits. <br>
Mitigation: Use the skill only when public network lookups are acceptable, and manually verify any inconclusive changelog or release-note result before advising an upgrade. <br>
Risk: When GITHUB_TOKEN is set, the analyzer reads it from the environment to raise GitHub rate limits. <br>
Mitigation: Use a low-scope token for this workflow or unset GITHUB_TOKEN when it is not needed. <br>
Risk: The raw headline, risk score, and symbol matches are heuristic and may over-count changes that do not actually affect the user's code. <br>
Mitigation: Review matched items against the user's source code and present only verified upgrade impacts. <br>


## Reference(s): <br>
- [Bump Doctor on ClawHub](https://clawhub.ai/ckarnell/skills/bump-doctor) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with analyzer JSON summarized for the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analyzer output includes a heuristic risk score, headline, risk items, migration steps, and notes; the agent is expected to verify matches before reporting conclusions.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
