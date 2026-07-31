## Description: <br>
video-add-b-roll helps an agent add selective, transcript-timed B-roll cutaways to talking-head, interview, documentary, or explanatory video projects using validated local media or Pexels assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an already-understood video project needs a small number of concrete, evidence-backed B-roll shots that align with transcript words, preserve timeline and audio, and pass review before final delivery. <br>

### Deployment Geography for Use: <br>
Global, subject to the user's local media rights, Pexels license terms, and organization policies for video production. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read a local Pexels API key and contact Pexels to search and download media. <br>
Mitigation: Store the key only in the local environment or the skill's .env file, do not share it in chat or logs, and use the workflow only where Pexels network access is approved. <br>
Risk: The skill runs ffmpeg-based media commands and modifies files under the target video project. <br>
Mitigation: Run it on a project workspace where generated review, cache, render, and operation metadata are expected, and review the produced plan, receipts, and final video before relying on the result. <br>
Risk: Poorly matched or unlicensed B-roll can misrepresent the speaker's claims or introduce rights issues. <br>
Mitigation: Use only validated local or Pexels candidates with recorded provenance, skip weak matches, and complete the exact-candidate review and visual delivery checks before final registration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/video-add-b-roll) <br>
- [Publisher profile](https://clawhub.ai/user/whitetowerai) <br>
- [Pexels license](https://www.pexels.com/license/) <br>
- [Pexels terms of service](https://www.pexels.com/terms-of-service/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown] <br>
**Output Format:** [Structured workflow guidance, JSON plans and receipts, review HTML, media validation artifacts, shell commands, and project metadata updates.] <br>
**Output Parameters:** [Requires a video project root, outputs from video-understand, a verified upstream review video, Python with ffmpeg/ffprobe and Pillow, and a Pexels API key when using Pexels media.] <br>
**Other Properties Related to Output:** [Produces durable B-roll plans, interaction and visual-review receipts, normalized silent overlays, contact sheets, boundary reels, stills, summaries, and final project registration updates.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
