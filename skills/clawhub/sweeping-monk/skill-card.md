## Description: <br>
Sweeping Monk helps researchers and academic writers diagnose methodology, research design, critical reasoning, writing, review-response, and communication problems, while handing literature search and citation verification to companion skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers, students, and academic writers use this skill to clarify research questions, select or critique methodology, diagnose study-design issues, structure academic writing, and respond to reviews. It is advisory-first and can provide concrete code, shell commands, or file edits only when the user explicitly asks for implementation help. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables persistent local usage logging and anonymous cloud upload by default. <br>
Mitigation: Review this behavior before installing, disable cloud upload immediately if outbound method-level metadata is not acceptable, and disable local logging if persistent local records are not acceptable. <br>
Risk: Bundled creator proposal tooling can use local creator tokens and affect files when approval or apply-style commands are invoked. <br>
Mitigation: Do not invoke proposal approval or application commands unless you are the skill creator and have reviewed the remote changes, token use, and resulting file modifications. <br>
Risk: Academic methodology advice can be incorrect, overconfident, or mismatched to the user's discipline and evidence base. <br>
Mitigation: Treat outputs as advisory, review important recommendations with domain experts, and use dedicated literature search or citation-checking skills for source retrieval and verification. <br>


## Reference(s): <br>
- [Research Playbook](references/research-playbook.md) <br>
- [Method Matrix](references/method-matrix.md) <br>
- [Cognitive Apprenticeship](references/cognitive-apprenticeship.md) <br>
- [Double-Loop Learning](references/double-loop.md) <br>
- [Researcher Reasoning Biases](references/reasoning-biases.md) <br>
- [Rapport Guidance](references/rapport.md) <br>
- [Signals Specification](references/signals.md) <br>
- [Methodology Reading List](references/methodology-reading-list.md) <br>
- [Core Literature Source Cards](references/sources/README.md) <br>
- [Coverage Dimensions](references/coverage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown conversational guidance with optional code, shell command, or configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May record local method-level usage signals and may send anonymous method-level usage metadata when cloud upload remains enabled.] <br>

## Skill Version(s): <br>
1.9.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
