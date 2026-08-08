## Description: <br>
AI video generation powered by CellCog via Seedance for cinematic 1080p videos with smooth motion, multi-shot narratives, lipsync, voice synthesis, and scoring from a single prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cellcog](https://clawhub.ai/user/cellcog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to ask an agent to create Seedance-powered videos through CellCog, including marketing, explainer, cinematic, and spokesperson-style productions from natural-language prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video prompts or attached content may be sent to CellCog and its model pipeline. <br>
Mitigation: Avoid submitting secrets, confidential business material, regulated data, or personal information unless the relevant data-sharing terms have been approved. <br>
Risk: The skill depends on cloud/API access and a CELLCOG_API_KEY, so it may fail when credentials are missing or service access is unavailable. <br>
Mitigation: Install the CellCog dependency, set CELLCOG_API_KEY in the runtime environment, and verify service access before relying on the workflow. <br>


## Reference(s): <br>
- [CellCog homepage](https://cellcog.ai) <br>
- [ClawHub skill page](https://clawhub.ai/cellcog/skills/seedance-video-generation-cellcog) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for invoking CellCog; generated video assets are created by the external CellCog service.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
