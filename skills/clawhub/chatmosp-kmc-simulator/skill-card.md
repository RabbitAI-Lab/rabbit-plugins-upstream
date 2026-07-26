## Description: <br>
KMC simulation skill for chatMOSP that runs a Wine-backed kinetic Monte Carlo engine and produces coverage and TOF results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanyangye](https://clawhub.ai/user/sanyangye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers running chatMOSP workflows use this skill after KMC parameters are prepared and confirmed. It executes catalyst surface reaction kinetic simulations, checks completion, and returns coverage and TOF plots and data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs external mosp-for-chatMOSP code and a Windows engine through Wine. <br>
Mitigation: Confirm trust in the external code and engine before installation or execution, and run simulations in a controlled workspace. <br>
Risk: Wine installation commands may change system packages. <br>
Mitigation: Only run the Wine installation commands after user approval and when system package changes are acceptable. <br>
Risk: The submitted skill files contain confusing language-routing labels. <br>
Mitigation: Verify the intended language file before relying on instructions, and have the publisher correct the labels. <br>
Risk: Large KMC step counts can create long-running jobs. <br>
Mitigation: Warn and obtain confirmation before running simulations at or above 20M steps, using the documented time estimates. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, JSON configuration, CSV/raw data outputs, and image file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces four result plots for coverage and TOF versus time and steps, plus CSV and raw KMC data files when the simulation completes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
