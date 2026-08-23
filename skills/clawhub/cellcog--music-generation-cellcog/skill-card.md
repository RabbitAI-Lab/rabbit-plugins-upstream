## Description: <br>
AI music generation powered by CellCog. Original instrumental and vocal tracks, 5 seconds to 10 minutes. Cinematic scores, background tracks, podcast intros, game soundtracks, ambient soundscapes, jingles, lo-fi beats, orchestral compositions, songs with lyrics. Royalty-free. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cellcog](https://clawhub.ai/user/cellcog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to prompt CellCog to generate original instrumental or vocal music for videos, podcasts, games, apps, ads, streaming, and other creative workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends music-generation requests to CellCog as an external service and requires CELLCOG_API_KEY. <br>
Mitigation: Use approved CellCog accounts, store CELLCOG_API_KEY in a secret manager or local environment, and avoid placing secrets in prompts or shared files. <br>
Risk: Commercial use depends on CellCog's current licensing and terms. <br>
Mitigation: Confirm CellCog's terms before using generated music in commercial releases or client deliverables. <br>
Risk: Prompting with copyrighted song references can create intellectual-property review concerns. <br>
Mitigation: Use mood, genre, instrumentation, and arrangement descriptions instead of requesting imitation of specific copyrighted songs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cellcog/skills/music-generation-cellcog) <br>
- [CellCog publisher profile](https://clawhub.ai/user/cellcog) <br>
- [CellCog homepage](https://cellcog.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and CELLCOG_API_KEY; generated music is delivered by CellCog as MP3 when the service completes.] <br>

## Skill Version(s): <br>
1.0.13 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
