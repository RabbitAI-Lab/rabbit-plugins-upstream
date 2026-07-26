## Description: <br>
Helps agents coach users through concrete continue, pivot, or quit decisions by separating unrecoverable prior investment from marginal future costs and benefits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and agents use this skill as decision support when prior spending, time, effort, reputation, or project momentum may be distorting a continue-or-quit choice. It guides the user through fresh-start testing, marginal future NPV comparison, mechanism diagnosis, and structural countermeasures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may influence business, career, investment, or relationship decisions. <br>
Mitigation: Treat outputs as decision support and independently verify important assumptions before acting. <br>
Risk: A user may apply sunk-cost reasoning when prior investment genuinely lowers future marginal costs or switching costs exceed continuing costs. <br>
Mitigation: Run the skill's fit check first and exclude cases where real synergies, short-term variance, or switching costs explain continued investment. <br>
Risk: Marginal future NPV can be misleading when costs, benefits, or alternatives are poorly estimated. <br>
Mitigation: Quantify future continue and quit scenarios explicitly, document assumptions, and use fresh-eyes review or stage-gate criteria for consequential decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/sunk-cost-fallacy) <br>
- [deciqAI Sunk-Cost Fallacy Skill Page](https://www.deciqai.com/c/sunk-cost-fallacy) <br>
- [deciqAI Machine-Readable Skill Metadata](https://www.deciqai.com/s/sunk-cost-fallacy.json) <br>
- [Primary Sources](references/sources.md) <br>
- [Arkes & Blumer's 1985 Studies](examples/arkes-blumers-1985-studies.md) <br>
- [The Concorde Program](examples/concorde-program.md) <br>
- [AI Build-Out Sunk Costs (2023-2026)](examples/ai-buildout-sunk-costs-2023-2026.md) <br>
- [Dawkins & Carlisle (1976), Nature DOI](https://doi.org/10.1038/262131a0) <br>
- [Stanford HAI AI Index Report 2025](https://aiindex.stanford.edu) <br>
- [Menlo Ventures State of Generative AI in the Enterprise](https://menlovc.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown coaching response with a structured decision template] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Interactive coach mode may pause at WAIT prompts; no executable code, privileged access, persistence, or hidden behavior is present in the artifact.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
