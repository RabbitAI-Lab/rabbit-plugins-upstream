## Description: <br>
Audits the DSA problem bank for coverage gaps and proposes new YAML entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to review DSA problem-bank coverage, identify gaps against the manifest, and prepare proposed YAML entries for human approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated problem proposals can be incomplete, inaccurate, or misaligned with the existing DSA problem bank. <br>
Mitigation: Review the markdown report and validate proposed YAML entries before merging any changes. <br>
Risk: Repository or service actions may be privileged when the skill is used inside broader release or administration workflows. <br>
Mitigation: Use scoped access, review commands before execution, and avoid granting unrelated production credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-gauntlet-curate) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, YAML, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with YAML proposal snippets and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Proposal-only output; human review is required before modifying problem-bank YAML files.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
