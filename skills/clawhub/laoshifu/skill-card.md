## Description: <br>
A Chinese-language fortune-telling consultation skill that role-plays an experienced practitioner, handles birth-chart and event-divination inputs, runs bundled charting and validation scripts, and returns unified conversational readings with standard hexagram tables when applicable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External users use this skill for Chinese fortune-telling style consultations about personal fate, relationships, career, wealth, timing, and concrete decisions. Agents use it to gather birth or divination inputs, run local charting and validation workflows, and produce concise Chinese guidance without exposing internal reasoning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an immersive fortune-teller persona that may not identify itself as AI. <br>
Mitigation: Deploy with clear surrounding disclosure and review the user experience for appropriate identity and expectation setting. <br>
Risk: The skill may give confident statements about sensitive medical, legal, financial, or relationship topics. <br>
Mitigation: Frame outputs as reflective or entertainment guidance and direct high-stakes decisions to qualified professionals. <br>
Risk: The workflow may persist birth details and generated local files during charting and validation. <br>
Mitigation: Collect only necessary personal details, avoid unnecessary retention, and clear generated local files after use. <br>
Risk: The skill depends on hard-coded external local skill paths. <br>
Mitigation: Review the referenced dependencies and paths before running the skill in a new environment. <br>


## Reference(s): <br>
- [consultation-method.md](references/consultation-method.md) <br>
- [consultation-plan-schema.md](references/consultation-plan-schema.md) <br>
- [interpretation-method.md](references/interpretation-method.md) <br>
- [liuyao-method.md](references/liuyao-method.md) <br>
- [liuyao-plan-schema.md](references/liuyao-plan-schema.md) <br>
- [master-identity.md](references/master-identity.md) <br>
- [voice-and-dialogue.md](references/voice-and-dialogue.md) <br>
- [ziwei.my charting and interpretation notes](https://www.ziwei.my/zi-wei-dou-shu-portfolio/zwds-guide-zi-wei-dou-shu-basics-9/) <br>
- [ziwei.my focus questions and interpretive structure](https://www.ziwei.my/zi-wei-dou-shu-portfolio/zwds-guide-zi-wei-dou-shu-basics-8/) <br>
- [Ling et al., CSCW 2026 GenAI fortune-telling study](https://arxiv.org/abs/2603.27784) <br>
- [Reading the Heart](https://doi.org/10.1177/10892680241269290) <br>
- [The Art of Fate Calculation review](https://www.cefc.com.hk/article/homola-stephanie-2023-the-art-of-fate-calculation-practicing-divination-in-taipei-beijing-and-kaifeng-new-york-berghahn-books/) <br>
- [NIDA OARS communication techniques](https://nida.nih.gov/sites/default/files/oarsessentialcommunicationtechniques.pdf) <br>
- [SPIKES protocol](https://academic.oup.com/oncolo/article/5/4/302/6386019) <br>
- [Dulwich Centre externalising conversations](https://dulwichcentre.com.au/courses/externalising-conversations/) <br>
- [APA Dictionary: Barnum effect](https://dictionary.apa.org/barnum-effect) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Chinese conversational text with optional Markdown hexagram tables and local JSON validation artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate local chart, fusion, plan, and response files during validation; user-facing output should hide internal reasoning and algorithmic details.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
