## Description: <br>
Ai Kujiale Design guides an agent through Kujiale-based interior design, including floorplan search or upload, style selection, automatic layout, and render or panorama output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, interior designers, real-estate professionals, and renovation teams use this skill to turn a selected or uploaded floorplan into Kujiale layout proposals, render images, panorama links, and concise design highlights. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow relies on a persistent Kujiale account token stored in .kjlconfig.json. <br>
Mitigation: Use a dedicated Kujiale token where possible, keep .kjlconfig.json out of version control, and restrict local file permissions. <br>
Risk: Layout and rendering actions may consume paid or quota-limited Kujiale resources. <br>
Mitigation: Require explicit user confirmation before actions that spend layout or rendering quota, and stop when quota is unavailable. <br>
Risk: The skill can upload floorplan images and monitor a local inbound media folder. <br>
Mitigation: Use a dedicated workspace, verify the intended image before upload, and avoid shared or synced folders for sensitive floorplans. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-kujiale-design) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [Kujiale skills portal](https://www.kujiale.com/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command snippets, image links, panorama links, and design highlights] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final output is expected to include ordered render images, panorama links, design highlights, and a Kujiale design detail link.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
