## Description: <br>
Chatmosp Msr Generator runs the ChatMOSP MSR workflow to generate metal cluster structures, validate outputs, create PNG and GIF visualizations, and send results through Feishu. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanyangye](https://clawhub.ai/user/sanyangye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers using ChatMOSP use this skill after parameter preparation to run MSR Wulff cluster generation, produce structure files and visual artifacts, and hand the generated cluster output to downstream workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow invokes local mosp-for-chatMOSP Python scripts. <br>
Mitigation: Confirm the local mosp-for-chatMOSP installation and review commands before execution. <br>
Risk: Generated PNG and GIF research artifacts are sent through Feishu. <br>
Mitigation: Verify the Feishu destination before sending outputs, especially for confidential work. <br>
Risk: Large cluster radii can create long-running calculations and large visualizations. <br>
Mitigation: Warn users before running R >= 50A jobs and consider skipping GIF generation above 20,000 atoms. <br>
Risk: Re-running a task may overwrite an existing output directory. <br>
Mitigation: Ask the user before overwriting existing ChatMOSP output files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanyangye/skills/chatmosp-msr-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell commands, JSON action payloads, and generated file descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces or references ini.xyz, cluster XYZ, faceinfo.txt, input.json, structure.png, and rotation.gif artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
