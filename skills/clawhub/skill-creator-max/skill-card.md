## Description: <br>
Builds a new agent skill end to end by dispatching role-specific subagents through specification, structure, implementation, compression, and independent review gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to create new agent skills from scratch with structured role packs, typed artifacts, validation gates, and an independent adversarial review step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run local harness scripts selected by generated evidence files. <br>
Mitigation: Use it only in a trusted disposable or sandboxed project directory and review any Evidence Dossier harness_path before validation. <br>
Risk: The skill can make broad project documentation changes, including root README, KB, or changelog updates. <br>
Mitigation: Require explicit confirmation before accepting root documentation, KB, or changelog changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/skill-creator-max) <br>
- [README.en.md](README.en.md) <br>
- [orchestration-anchors.md](references/orchestration-anchors.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with generated skill files, JSON artifacts, validation commands, and configuration schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can run generated local validation harnesses and may propose broad documentation updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
