## Description: <br>
Compares two or more materials on the same topic or event before publication, flagging mismatched numbers, product names, fact wording, terminology, source attributions, structural promises, and cross-platform expression drift. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Editorial, PR, product marketing, and localization teams use this skill to compare related publication materials and produce a read-only consistency audit with severity-rated differences and unified wording recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-provided publication materials that may contain sensitive or pre-release content. <br>
Mitigation: Use a dedicated output directory and provide sensitive documents only to audit agents trusted for that content. <br>
Risk: Unified wording recommendations can affect public claims if accepted without review. <br>
Mitigation: Require human confirmation for P0 and P1 differences before any writer or editor applies changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/cross-material-consistency-auditor-skill) <br>
- [Consistency Checklist Reference](artifact/references/consistency-checklist.md) <br>
- [Replay References](artifact/references/replay-references.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown reports and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces extracted claims JSON, a diff matrix, an audit report, and unified wording JSON; original materials are not modified.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
