## Description: <br>
Multilingual Learning Sprint is an adaptive language-learning coach that assesses ability, personalizes short sprint plans, runs practice and review quizzes, and supports documented Alipay AI Pay and JD ClawTip payment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners use this skill to choose a target language, take a lightweight placement diagnostic, and follow a 7, 14, or 30 day learning sprint with interest-based lessons and spaced review. Developers can also use its guidance and scripts to connect paid placement, lesson, or quiz fulfillment through Alipay AI Pay or JD ClawTip. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid fulfillment scripts handle learner profile data and ClawTip payment credentials through local order files and remote service calls. <br>
Mitigation: Use only trusted order files and trusted backend URLs, and review the skill before installation or paid fulfillment. <br>
Risk: Custom API base URLs or untrusted order files could direct learner data or payment credentials to an unintended service. <br>
Mitigation: Avoid untrusted custom API base URLs and only run payment scripts against a backend whose operator and payment configuration you trust. <br>
Risk: An instruction-only ClawHub skill does not itself enforce Alipay payment. <br>
Mitigation: Use a reviewed Restful service wrapper with merchant authorization, payment proof validation, and fulfillment confirmation before any production paid launch. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/multilingual-learning-sprint) <br>
- [Alipay AI Pay Integration Notes](references/alipay-aipay.md) <br>
- [Language Skill Research](references/research.md) <br>
- [Alipay AI Pay overview](https://aipay.alipay.com/docs/overview.html) <br>
- [Alipay AI Pay call-pay flow](https://aipay.alipay.com/callpay) <br>
- [Language Sprint ClawTip backend](https://language-sprint-clawtip.pages.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline YAML, JSON, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local ClawTip order JSON files and may call a remote language-sprint service when the paid fulfillment scripts are used.] <br>

## Skill Version(s): <br>
1.0.8 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
