## Description: <br>
CellCog helps agents send multimodal research, analysis, generation, and coding tasks to the CellCog cloud service through its Python SDK, including optional local file inputs and generated file outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cellcog](https://clawhub.ai/user/cellcog) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to configure the CellCog SDK, authenticate with CELLCOG_API_KEY, and delegate multimodal tasks that can return text, code, analysis, dashboards, documents, media, or generated files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and SHOW_FILE-tagged files are sent to CellCog's cloud service. <br>
Mitigation: Only tag files intended for sharing with CellCog, and do not tag secrets, private keys, .env files, or other credential-adjacent files. <br>
Risk: The CELLCOG_API_KEY environment variable can expose access to the connected CellCog account if mishandled. <br>
Mitigation: Store the API key as a protected environment secret, avoid including it in prompts or tagged files, and rotate it if exposure is suspected. <br>
Risk: GENERATE_FILE and notify-mode workflows can download generated outputs to local paths. <br>
Mitigation: Review requested output paths and task instructions before allowing generated files to be written. <br>


## Reference(s): <br>
- [CellCog](https://cellcog.ai) <br>
- [CellCog Python SDK](https://github.com/CellCog/cellcog_python) <br>
- [cellcog PyPI package](https://pypi.org/project/cellcog/) <br>
- [DeepResearch Bench Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Text, Files] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to print CellCog responses in full and to download generated files to requested local paths.] <br>

## Skill Version(s): <br>
2.0.18 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
