## Description: <br>
Create and query BytePlus/MediaKit video highlight editing tasks with the video-highlights-llm tool, focused on preset-based football highlight reels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bpvnebot](https://clawhub.ai/user/bpvnebot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to submit BytePlus MediaKit football highlight jobs from one or more HTTP/HTTPS video URLs, then query asynchronous task results and report returned highlight outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill submits video URLs, prompts, callback data, task queries, and MediaKit credentials to the configured MediaKit endpoint. <br>
Mitigation: Configure API keys outside chat, use trusted endpoints and headers, and avoid sending sensitive media URLs or prompt content unless the MediaKit account and endpoint are approved for that data. <br>
Risk: Endpoint or header overrides can route requests to an unintended environment. <br>
Mitigation: Use the production endpoint by default, set internal environment headers only when explicitly required, and review BYTEPLUS_MEDIAKIT_ENDPOINT and BYTEPLUS_MEDIAKIT_HEADERS before submission. <br>
Risk: Unsupported payloads can fail or create misleading expectations for non-football edits. <br>
Mitigation: Validate requests before submission: use only HTTP/HTTPS video URLs, the football preset, up to five unique target durations, and omit unsupported story_prompt or background_music_urls fields. <br>


## Reference(s): <br>
- [video-highlights-llm API Notes](artifact/references/api.md) <br>
- [Request Templates](artifact/references/templates.md) <br>
- [BytePlus MediaKit endpoint](https://mediakit.ap-southeast-1.bytepluses.com/api/v1/tools/video-highlights-llm) <br>
- [ClawHub Skill Page](https://clawhub.ai/bpvnebot/skills/byteplus-mediakit-video-highlights) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON task results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports task IDs, status, duration, and per-output highlight URLs when the MediaKit task succeeds.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
