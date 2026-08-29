## Description:

This skill helps advertisers, campaign optimizers, and content teams turn A/B ad creative needs into testable creative matrices, generation tasks, naming rules, and reviewable delivery plans using AI-HIVE workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers, merchants, marketing teams, and content producers use this skill to plan Chinese-language A/B ad creative matrices, generate or edit AI-HIVE media tasks, and track routing, cost, status, and acceptance criteria. It is intended for authorized product, brand, and campaign materials where claims and test conclusions remain human-reviewed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit billable remote AI-HIVE image or video generation tasks and poll for downloaded outputs.

Mitigation: Review prompts, model routing, batch size, and cost or speed priority before running generation; start with a small sample batch.

Risk: The skill may upload selected images, videos, or audio to AI-HIVE as reference media.

Mitigation: Use only assets the user is authorized to upload and avoid sensitive, private, or regulated media unless appropriate review has been completed.

Risk: Ad claims, performance expectations, and A/B conclusions can be misleading if generated content is treated as verified evidence.

Mitigation: Keep factual claims tied to user-provided evidence, mark uncertain claims for verification, and have campaign owners validate test results and statistical conclusions.

Risk: Creative adaptation requests may drift into unauthorized copying or impersonation.

Mitigation: Use references only for abstract structure and create new scenes, wording, visual style, and identity elements unless rights are confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ad-ab-creative-matrix-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with runnable Python and shell command examples plus JSON task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local files such as blueprint JSON, generated media downloads, and edited video outputs when the user runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
