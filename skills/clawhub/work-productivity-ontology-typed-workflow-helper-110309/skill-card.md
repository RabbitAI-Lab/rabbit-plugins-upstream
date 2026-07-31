## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create ontology-style productivity workflows, checklists, analysis, code changes, and decision support for bug fixing, setup hardening, reliability improvements, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External AI-agent users, skill authors, maintainers, and teams use this skill to turn ontology-style productivity needs into practical workflows, templates, checklists, code changes, or decision support. It is intended for local-friendly planning and implementation tasks where assumptions, constraints, validation, and follow-up risks should be visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill allows broad implicit invocation wording, which may cause it to activate for loosely related ontology or workflow requests. <br>
Mitigation: Before installing, narrow or disable implicit invocation if the helper should only run for explicit ontology or typed-workflow requests. <br>
Risk: Workflow proposals may be incomplete or unsuitable for a user's local environment, constraints, or safety requirements. <br>
Mitigation: Review generated artifacts against the stated success criteria, local hardware limits, and any setup or safety constraints before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Self-Improving + Proactive Agent demand signal](https://clawhub.ai/skills/self-improving) <br>
- [Ontology demand signal](https://clawhub.ai/skills/ontology) <br>
- [Multi Search Engine demand signal](https://clawhub.ai/skills/multi-search-engine) <br>
- [AdMapix demand signal](https://clawhub.ai/skills/admapix) <br>
- [Sentrup AI Customer Support Platform discussion](https://news.ycombinator.com/item?id=48662350) <br>
- [LiteLLM issue summary](https://github.com/arielb1-sun-security/copilot-studio-test/issues/2209) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include assumptions, validation notes, and remaining risks when useful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
