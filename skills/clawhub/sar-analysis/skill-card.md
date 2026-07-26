## Description: <br>
Structure-activity relationship analysis workflows using SciMiner's MCS-based and scaffold-based SAR APIs for file or inline table inputs, plus an AlphaFold3-based binding-mode prediction workflow for target-aware SAR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sciminer](https://clawhub.ai/user/sciminer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Medicinal chemistry, cheminformatics, and computational drug discovery teams use this skill to compare compound series, identify shared cores or scaffolds, and relate activity trends to predicted binding modes when target context is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a local SciMiner API key. <br>
Mitigation: Use a low-privilege SciMiner key stored only in the documented credential file and avoid printing, logging, or persisting the key. <br>
Risk: The skill may upload analysis files and molecular data to SciMiner services. <br>
Mitigation: Use it only with data approved for SciMiner processing and run it in a constrained environment when handling sensitive compound series. <br>
Risk: The bundled RCSB helper can save raw API output to local paths when requested. <br>
Mitigation: Avoid raw-output saves to arbitrary paths and review any requested output path before execution. <br>
Risk: The workflow relies on live SciMiner documentation for request construction. <br>
Mitigation: Read the current tool documentation before each invocation and validate required parameters against the selected document section. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sciminer/skills/sar-analysis) <br>
- [SciMiner API key utility](https://sciminer.tech/utility) <br>
- [SciMiner tool API documentation](https://sciminer.tech/tool_api_files/) <br>
- [RCSB PDB Data API](https://data.rcsb.org/rest/v1) <br>
- [RCSB PDB Search API](https://search.rcsb.org/rcsbsearch/v2) <br>
- [RCSB PDB](https://www.rcsb.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON snippets, shell commands, API request code, and share URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SciMiner task IDs and share URLs, selected PDB IDs and chains, retained conformation scores, correlation coefficients, and concise RCSB summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
