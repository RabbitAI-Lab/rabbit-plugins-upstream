## Description:

Helps AI platform teams, relay operators, enterprise developers, content studios, and e-commerce technical teams organize authorized model APIs into an AI-HIVE workflow for key management, routing, quota control, auditing, media upload, image/video task polling, and result download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to design and test AI-HIVE model relay workflows that keep API keys authorized, isolated, rotated, and auditable. It can produce integration blueprints, shell commands, JSON task responses, and image/video connectivity test outputs for approved AI-HIVE accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles paid AI-HIVE API keys and can spend API credits.

Mitigation: Use only an authorized AI-HIVE key, keep it in environment variables or the local config file, rotate it regularly, and confirm credit-spending commands before execution.

Risk: Changing the API base URL could send prompts, media, or keys to an untrusted endpoint.

Mitigation: Keep the default AI-HIVE base URL unless the endpoint is independently trusted and approved.

Risk: Image and video commands may upload local media files.

Mitigation: Confirm file paths, rights, and sensitivity before running upload or generation commands that reference local media.

Risk: Broad search-trigger wording may invoke the skill for loosely related AI relay or content-generation requests.

Mitigation: Before using the skill, confirm the user intends to work with AI-HIVE and authorized model relay workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-ai-relay-search-alias)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE Homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON, API Calls, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON blueprints and API responses, local configuration, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write AI-HIVE configuration to ~/.ai-hive/config.json with 0600 permissions and may download generated image/video outputs to the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
