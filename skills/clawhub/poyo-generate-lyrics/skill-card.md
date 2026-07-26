## Description: <br>
Generates lyric drafts with PoYo from a theme, mood, genre, or story prompt and guides result retrieval for follow-on music-generation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and music workflow builders use this skill to prepare PoYo generate-lyrics requests, submit reviewed payloads, and retrieve lyric results for drafting or downstream music-generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lyric prompts are sent to PoYo as part of the skill's normal operation. <br>
Mitigation: Use the skill only when sending the prompt content to PoYo is acceptable, and avoid confidential, personal, or unreleased material unless sharing it is approved. <br>
Risk: The skill depends on a PoYo API key and optional callback URLs. <br>
Mitigation: Keep POYO_API_KEY private, use only callback URLs you control, and review PoYo pricing and retention expectations before high-volume use. <br>
Risk: Generated lyrics may require rights, originality, or policy review before release. <br>
Mitigation: Treat generated lyrics as drafts and review them before publication or commercial use. <br>


## Reference(s): <br>
- [PoYo Generate Lyrics API Reference](references/api.md) <br>
- [PoYo Generate Lyrics Model Page](https://poyo.ai/models/generate-lyrics) <br>
- [PoYo Generate Lyrics API Docs](https://docs.poyo.ai/api-manual/music-series/generate-lyrics) <br>
- [PoYo Query Music Detail Docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo Music Webhook Docs](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-generate-lyrics) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload summaries and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a submitted task_id, result retrieval method, and whether the lyrics should feed a music-generation workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
