## Description: <br>
Find, evaluate, and download common purchasable CAD parts from step.parts, including named off-the-shelf actuators, servos, motors, electronics boards, connectors, screws, bolts, nuts, washers, bearings, standoffs, and other catalog components. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liubuq-sys](https://clawhub.ai/user/liubuq-sys) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to search hosted step.parts catalog data, resolve fuzzy CAD part names or standards, select matching off-the-shelf components, and download canonical STEP files with checksum verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts step.parts and can save CAD STEP files locally. <br>
Mitigation: Use a dedicated output directory, review downloaded files before incorporating them into CAD assemblies, and verify checksums when provided. <br>
Risk: The downloader can replace existing files when overwrite behavior is requested. <br>
Mitigation: Avoid --overwrite unless replacement is intentional and the destination path has been checked. <br>
Risk: Alternate API origins can change the source and trust boundary for downloaded CAD assets. <br>
Mitigation: Use alternate API origins only when the user supplied them and they are trusted. <br>


## Reference(s): <br>
- [step.parts API Reference](references/step-parts-api.md) <br>
- [step.parts API](https://api.step.parts) <br>
- [step.parts Agent Guide](https://www.step.parts/llms.txt) <br>
- [ClawHub Skill Page](https://clawhub.ai/liubuq-sys/skills/step-parts) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional JSON output from bundled downloader commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save STEP files locally and report selected part IDs, source URLs, file paths, SHA-256 values, and checksum verification status.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
