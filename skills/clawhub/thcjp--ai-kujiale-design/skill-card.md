## Description: <br>
Ai Kujiale Design guides agents through Kujiale-based interior design workflows, including floorplan search or upload, style selection, automated layout, and rendered image or panorama output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, designers, and automation operators use this skill to create interior-design previews from a known community or uploaded floorplan, choose a style, generate a layout, and collect rendered images, panorama links, and design notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Floorplan or home-layout data may be uploaded to Kujiale during search, copy, layout, or rendering flows. <br>
Mitigation: Use the skill only when the user intends to send that data to Kujiale, and obtain explicit confirmation before uploads. <br>
Risk: The workflow depends on a Kujiale access token stored in local configuration. <br>
Mitigation: Keep the token in a local config controlled by the user, avoid committing it to version control, and rotate it if exposure is suspected. <br>
Risk: The skill proposes command execution and layout steps that may consume account quota. <br>
Mitigation: Require explicit user confirmation before command execution and before any quota-consuming layout operation. <br>
Risk: The artifact describes monitoring an inbound media directory for uploaded images. <br>
Mitigation: Remove unrelated images from the monitored directory before use so only the intended floorplan is processed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-kujiale-design) <br>
- [Kujiale skills token page](https://www.kujiale.com/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown result file with progress text, design highlights, rendered image links, panorama links, and Kujiale design-detail links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require a local Kujiale access token and user confirmation before upload, command execution, or quota-consuming layout steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
