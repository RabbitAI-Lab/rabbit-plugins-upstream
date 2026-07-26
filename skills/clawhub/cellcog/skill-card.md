## Description: <br>
Cellcog helps agents offload multimodal work to the CellCog service, including research, analysis, file-aware tasks, media generation, documents, dashboards, code, and other generated deliverables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitishgargiitd](https://clawhub.ai/user/nitishgargiitd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to invoke CellCog as a third-party AI sub-agent for multimodal research, analysis, generation, and file-producing workflows. It is especially relevant when an agent needs to submit prompts and selected local files to CellCog and receive text plus generated artifacts back. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tagged local files are uploaded to CellCog as attachments. <br>
Mitigation: Use SHOW_FILE only for files intended for the third-party service, and do not tag secrets, credentials, private keys, .env files, or other sensitive material. <br>
Risk: Generated files may be downloaded to paths requested by the user or selected by the SDK. <br>
Mitigation: Review requested output paths before generation and inspect downloaded artifacts before opening, executing, or sharing them. <br>
Risk: The integration depends on a CellCog API key and account credits. <br>
Mitigation: Configure CELLCOG_API_KEY only in the intended environment and monitor task cost or credit usage reported in completion messages. <br>


## Reference(s): <br>
- [CellCog homepage](https://cellcog.ai) <br>
- [CellCog Python SDK](https://github.com/CellCog/cellcog_python) <br>
- [CellCog Python package](https://pypi.org/project/cellcog/) <br>
- [DeepResearch Bench Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) <br>
- [ClawHub skill page](https://clawhub.ai/nitishgargiitd/skills/cellcog) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/nitishgargiitd) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with Python and shell examples, plus references to generated output files when CellCog produces artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include CellCog chat status, messages, downloaded file paths, and follow-up instructions from the third-party service.] <br>

## Skill Version(s): <br>
2.0.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
