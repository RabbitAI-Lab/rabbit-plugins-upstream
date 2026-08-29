## Description:

Turns Chinese batch short-video production requests into auditable production plans, prompts, runnable AI-HIVE commands, task records, and acceptance checklists for e-commerce and marketing teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, e-commerce operators, marketing teams, and content operations teams use this skill to turn SKU tables, brand rules, source assets, platform requirements, and delivery targets into batch short-video workflows. It can also provide scripts, prompts, runnable AI-HIVE commands, task tracking, retry guidance, and final acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation may be billable when users submit image or video jobs.

Mitigation: Review the final prompt, model mode, route, media inputs, and pricing snapshot before submission; run a small sample before launching batch work.

Risk: The workflow uses user-provided API credentials.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable or the script's restricted config file, and do not place API keys in prompts, logs, screenshots, or version control.

Risk: The helper can upload selected media and download generated results through AI-HIVE.

Mitigation: Upload only assets the user is authorized to use, and review generated media before publication for rights, likeness, brand, and claim issues.

Risk: Generated marketing content can include inaccurate product claims or misleading endorsements if unchecked.

Mitigation: Keep required product and brand facts explicit, require human review, and avoid unsupported claims, fake testimonials, or platform-rule evasion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-video-batch-production-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with JSON artifacts and inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local production blueprint JSON files and downloaded media when the bundled scripts are executed.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
