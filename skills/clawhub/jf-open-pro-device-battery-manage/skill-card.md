## Description: <br>
JFTech low-power device battery management skill for querying battery threshold ranges and setting the low-battery mode threshold. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to manage supported JFTech low-power, battery, or solar-powered devices. It helps an agent configure credentials, query supported low-battery threshold ranges, inspect the current threshold, and run the documented threshold update flow. <br>

### Deployment Geography for Use: <br>
China (CN), Asia (AS), Europe (EU), and North America (NA), based on the documented JFTech regional API endpoints. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles device credentials and device interface tokens, and token retrieval can print sensitive token material to terminal output. <br>
Mitigation: Use the skill only in a controlled environment, avoid logging token retrieval output, and keep JF_UUID, JF_APP_KEY, JF_APP_SECRET, and JF_DEVICE_TOKEN out of shared transcripts. <br>
Risk: The skill allows JF_ENDPOINT to choose the API host. <br>
Mitigation: Set JF_ENDPOINT only to documented JFTech hosts for the intended region before running any API command. <br>
Risk: The skill can change low-battery mode settings on a real device. <br>
Mitigation: Confirm the target device and requested threshold before any set-threshold action, and prefer the get-and-set flow so the threshold is checked against the device-supported range first. <br>


## Reference(s): <br>
- [JFTech open platform documentation](https://docs.jftech.com) <br>
- [Get low battery threshold range configuration](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=9bf993f3140ad9f9b4390fee750ba740&lang=zh) <br>
- [Set low battery threshold configuration](https://docs.jftech.com/docs?menusId=54582398fd8d4248962354e92ac2e47a&siderId=b246b44faa8c4d41a3f10e3de95b892a&lang=zh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, environment variable configuration, and API response interpretation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled scripts produce terminal output and JSON-derived device threshold values; token retrieval may print sensitive token material.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter metadata.version is 1.4.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
