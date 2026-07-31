## Description: <br>
AI通识课资深专家 V3 combines a full AI literacy curriculum across cognition, tools, methodology, practice, and professional application with p5.js 2.x creative coding support for generating interactive classroom courseware. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gqliang2026](https://clawhub.ai/user/gqliang2026) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, students, and course designers use this skill to explain AI literacy concepts, prepare lessons, create assignments and rubrics, and generate p5.js single-file HTML interactive courseware for classroom demonstrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML courseware commonly loads p5.js from external CDNs and may include browser capabilities such as camera, microphone, or network access. <br>
Mitigation: Review external CDN use and browser permissions before using generated courseware with students; prefer synthetic or public data and provide no-permission alternatives for classroom use. <br>
Risk: The skill teaches automation and Hooks concepts, and copied hook configurations can execute commands with the user's project permissions. <br>
Mitigation: Only copy hook or automation configurations that are understood, trusted, and manually reviewed, and keep human review for high-impact actions. <br>
Risk: AI-generated educational examples, references, code, and p5.js APIs can be inaccurate or unsupported. <br>
Mitigation: Apply the skill's verification discipline: check cited sources, run syntax or browser validation for generated HTML, and avoid claiming courseware is tested unless the documented checks have passed. <br>


## Reference(s): <br>
- [Skill definition](SKILL.md) <br>
- [p5.js interactive courseware guide](references/p5js-courseware-guide.md) <br>
- [p5.js system prompt](references/p5js-system-prompt.md) <br>
- [p5.js task template](references/p5js-task-template.md) <br>
- [AI literacy asset index](references/kb-asset-index.md) <br>
- [Lesson preparation workflow](references/lesson-prep-workflow.md) <br>
- [Module A cognition reference](references/module-a-cognition.md) <br>
- [Module B tools reference](references/module-b-tools.md) <br>
- [Module C methodology reference](references/module-c-methodology.md) <br>
- [Module D practice reference](references/module-d-practice.md) <br>
- [Module E professional application reference](references/module-e-professional.md) <br>
- [Professional orientation lecture script](references/lecture-script-professional-orientation.md) <br>
- [IMA AI literacy course knowledge base](https://ima.qq.com/wiki/?shareId=8beb984ebb359e372653e0c32376ee62aa2320088c3571954e2c3c844c41d552) <br>
- [TRAE IDE knowledge base](https://lcnziv86vkx6.feishu.cn/wiki/GEEnwlfTQi8qZrkFsPycfkUKnul) <br>
- [p5.js](https://p5js.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown responses, often including complete single-file HTML code blocks for p5.js courseware plus lesson-use guidance and validation notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are normally in Chinese and may include browser-runnable p5.js HTML that uses external CDN dependencies.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
