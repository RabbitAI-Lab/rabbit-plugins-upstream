## Description: <br>
Short-form video market research via the Virlo API for viral niche research, trend tracking, creator vetting, hashtag intelligence, and sound intelligence across TikTok, YouTube Shorts, and Instagram Reels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virlo-ai](https://clawhub.ai/user/virlo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, creators, and research teams use this skill to ask an agent for short-form video market research, trend discovery, creator analysis, and recurring niche monitoring across TikTok, YouTube Shorts, and Instagram Reels through the Virlo API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Virlo API key and sends research topics, creator handles, video URLs, and related prompts to Virlo. <br>
Mitigation: Configure the key through the VIRLO_API_KEY environment variable and avoid pasting secrets into chat; use the skill only for data you are comfortable sending to Virlo. <br>
Risk: Virlo API calls can consume prepaid balance, especially one-shot searches, recurring monitor runs, tracking cycles, and data intelligence add-ons. <br>
Mitigation: Check account balance before paid requests, review estimated costs, and ask for confirmation before setting recurring cadence or optional paid add-ons. <br>
Risk: Recurring monitors and autopilot settings can continue changing or running after initial setup. <br>
Mitigation: Confirm before creating monitors, enabling autopilot, applying proposals, pausing, deleting, or changing tracked resources. <br>


## Reference(s): <br>
- [Virlo API Documentation](https://dev.virlo.ai/docs) <br>
- [Virlo API LLM Reference](https://dev.virlo.ai/llms-full.txt) <br>
- [Virlo Agent Playbook](https://dev.virlo.ai/agent-playbook.txt) <br>
- [Virlo Pricing](https://dev.virlo.ai/pricing) <br>
- [ClawHub Skill Page](https://clawhub.ai/virlo-ai/skills/short-form-market-research-brain) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown with curl examples, JSON API payloads, and concise research summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize Virlo API results and may guide setup of paid one-shot searches, recurring monitors, tracking, or autonomy settings.] <br>

## Skill Version(s): <br>
1.8.4 (source: server release metadata, artifact/SKILL.md frontmatter, artifact/clawhub.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
