## Description: <br>
Turn a published TierVibe tier list into a narrated video by fetching public tier-list data and card images, capturing the board image, preparing reviewable narration, generating TTS audio and subtitles, and composing a scrolling tier-list video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill to turn published TierVibe tier-list posts into narrated videos with card-by-card explanations, subtitles, and generated media assets. Agents use it to guide data fetching, card identification, narration drafting, user review, TTS generation, and final video composition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Runtime dependency installation can modify the active Python environment. <br>
Mitigation: Install and run the skill scripts inside a virtual environment, as recommended by the release security guidance. <br>
Risk: TTS generation uses an online service and may process narration derived from the TierVibe post. <br>
Mitigation: Use only public TierVibe posts that the user is comfortable sending through online TTS. <br>
Risk: Card recognition or generated narration may mislabel items or misrepresent the author's tier-list rationale. <br>
Mitigation: Review the generated card manifest and narration script before creating the final video. <br>
Risk: Draft or unpublished TierVibe posts are not publicly readable and cannot provide the required board and card images. <br>
Mitigation: Ask the user to publish the TierVibe post first, then rerun the workflow with the public URL or slug. <br>


## Reference(s): <br>
- [TierVibe API reference](references/tiervibe-api.md) <br>
- [TierList Video Maker homepage](https://github.com/edison7009/TierList-Video-Maker) <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-video-maker) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Markdown, Files] <br>
**Output Format:** [Markdown workflow guidance with shell commands plus generated JSON manifests, a review table, TTS audio, subtitles, and MP4 video files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow expects a published TierVibe URL or slug and may require multimodal image recognition for image cards without detail text.] <br>

## Skill Version(s): <br>
1.0.11 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
