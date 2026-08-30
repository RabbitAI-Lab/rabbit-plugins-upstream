## Description:

Helps agriculture companies plan AI-assisted image, short-video, and content marketing workflows around verified production sites, farming processes, products, traceability, and channel-specific campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams and agricultural businesses use this skill to create audience strategy, 30-day content calendars, image and video prompts, platform rewrites, AI-HIVE task records, and review checklists for agriculture content marketing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The init flow may store an API key locally while the skill text prefers environment-only secrets.

Mitigation: Prefer supplying AI_HIVE_API_KEY as an environment variable and review any local configuration before installation.

Risk: Selected prompts or media may be sent to AI-HIVE during image or video generation.

Mitigation: Upload only authorized material and avoid sensitive customer, farm, financial, or compliance content unless AI-HIVE handling is acceptable for the organization.

Risk: Agriculture marketing content can misstate origin, variety, production year, process, testing, nutrition, efficacy, or traceability.

Mitigation: Require human review of facts and rights before paid generation or publication, and mark unverified claims as pending verification.

## Reference(s):

- [农业企业图片视频内容营销行业手册](references/industry-playbook.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/industry-agriculture-company-marketing-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON files and inline bash/Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs for image or video generation after user confirmation; task IDs, price snapshots, input hashes, and downloaded outputs may be recorded.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
