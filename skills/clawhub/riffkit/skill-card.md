## Description: <br>
Riffkit helps an agent turn one source video, TikTok link, or analyzed template into a post-ready short-form or UGC-style ad video by reusing the source's emotion formula with optional character, product, language, and creative-direction settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[riffkit](https://clawhub.ai/user/riffkit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and agent users use Riffkit to plan, submit, monitor, and retrieve AI-generated riff videos based on a TikTok link, uploaded source video, or existing analyzed template. The skill guides source selection, optional product or character setup, user confirmation before paid submission, progress polling, and delivery of download links, captions, hashtags, and strategy recap. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The heartbeat can replace the installed SKILL.md from the vendor site without a signed or reviewed update channel. <br>
Mitigation: Disable or remove the heartbeat, or route updates through a reviewed install process before allowing the skill to overwrite local instructions. <br>
Risk: The skill can initiate paid video-generation requests through the Riffkit API. <br>
Mitigation: Require the documented pre-submit confirmation before calling generation endpoints and do not retry failed or insufficient-balance requests automatically. <br>
Risk: Generated videos may depend on third-party source URLs, uploaded media, product data, and account credentials. <br>
Mitigation: Use only trusted source links and uploads, keep session tokens out of task or content fields, and review generated output before publishing it outside the agent workflow. <br>


## Reference(s): <br>
- [Riffkit homepage](https://riffkit.ai) <br>
- [Riffkit skill source](https://riffkit.ai/SKILL.md) <br>
- [Riffkit ClawHub skill page](https://clawhub.ai/riffkit/skills/riffkit) <br>
- [Riffkit publisher profile](https://clawhub.ai/user/riffkit) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with API request instructions, shell commands, and user-facing status or delivery text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces plans, confirmation prompts, progress updates, video download links, captions, hashtags, strategy recaps, and heartbeat update guidance; paid generation requires explicit user confirmation.] <br>

## Skill Version(s): <br>
1.2.2 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
