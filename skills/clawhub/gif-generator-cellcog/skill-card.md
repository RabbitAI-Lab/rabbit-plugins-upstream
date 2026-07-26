## Description: <br>
Gif Generator Cellcog helps agents request CellCog-generated GIFs such as reaction GIFs, product loops, cinemagraphs, and social media animations optimized for platforms like Discord, Twitter/X, Slack, and WhatsApp. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitishgargiitd](https://clawhub.ai/user/nitishgargiitd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to direct CellCog to create new GIFs for reactions, product showcases, cinemagraphs, social media content, animated art, and UI demos. The skill guides prompt structure, platform targeting, output constraints, and CellCog SDK usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, requested media, or local context may be sent to CellCog as an external paid AI service. <br>
Mitigation: Review requests before submission and avoid including sensitive files, private content, or confidential prompts unless they are intended for CellCog. <br>
Risk: The skill requires a CellCog API key. <br>
Mitigation: Store CELLCOG_API_KEY only in trusted environments and avoid exposing it in prompts, logs, examples, or shared configuration. <br>
Risk: Fire-and-forget mode can continue work asynchronously. <br>
Mitigation: Review the notification session key and task label before use, then monitor returned status and outputs before relying on generated GIFs. <br>


## Reference(s): <br>
- [CellCog homepage](https://cellcog.ai) <br>
- [ClawHub skill page](https://clawhub.ai/nitishgargiitd/skills/gif-generator-cellcog) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/nitishgargiitd) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, API Calls, Files] <br>
**Output Format:** [Markdown guidance with Python code snippets and generated GIF or MP4 outputs from CellCog.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; prompts and requested media are handled by the external CellCog service.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
