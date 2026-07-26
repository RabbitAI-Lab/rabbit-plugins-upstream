## Description: <br>
Hanlon's Razor helps an agent analyze conflicts by testing whether mistake, miscommunication, incompetence, or asymmetric information explains hostile-seeming behavior before escalating to malice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill when a person or team is tempted to read harmful or frustrating behavior as intentional malice. It structures a clarifying analysis that states the action and harm, tests non-malice explanations, identifies what malice would additionally require, and sets override signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be misapplied when concrete evidence of malice already exists. <br>
Mitigation: Treat Hanlon's Razor as a starting prior only and override it when documented malicious intent or credible intent evidence appears. <br>
Risk: The skill may underreact in safety-critical, abusive, or serious power-imbalance contexts where assuming non-malice could increase harm. <br>
Mitigation: Do not use this lens as the primary response in catastrophic-risk or abuse-enabling settings; shift to a protective posture before intent is proven. <br>
Risk: The analysis can be used to excuse harmful behavior once incompetence is identified. <br>
Mitigation: Keep attribution separate from accountability: incompetence-caused harm still requires response, remediation, and follow-up. <br>


## Reference(s): <br>
- [Sources - hanlons-razor](references/sources.md) <br>
- [Hanlon's Submission 1980; Heinlein's 1941 Articulation](examples/hanlons-submission-1980-heinleins-1941-articulation.md) <br>
- [AI Incidents - Incompetence and Emergent Error as a Prior Over Malice (2024-2026)](examples/ai-incidents-malice-vs-emergent-error-2024-2026.md) <br>
- [Hanlon's Razor - Quote Investigator](https://quoteinvestigator.com/2016/12/30/not-malice/) <br>
- [Gemini image generation got it wrong. We'll do better.](https://blog.google/products/gemini/gemini-image-generation-issue/) <br>
- [deciqAI Hanlon's Razor page](https://www.deciqai.com/c/hanlons-razor) <br>
- [deciqAI Hanlon's Razor machine-readable metadata](https://www.deciqai.com/s/hanlons-razor.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis with concise structured fields and optional step-by-step coaching questions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May pause at explicit wait points when coaching a novice through the analysis.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
