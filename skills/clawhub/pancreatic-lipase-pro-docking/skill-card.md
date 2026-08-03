## Description: <br>
Provides a virtual-screening workflow for human pancreatic lipase (PDB 1LPB) that ranks ligand CSV inputs with docking-energy results, poses, filters, and an executive HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, computational chemists, and research teams use this skill to screen ligand CSVs against human pancreatic lipase and review ranked docking results, poses, descriptors, PAINS/druglike filters, and GI-fluid-aware reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The runnable stack is stored in an encoded archive and can make persistent user-level package or environment changes. <br>
Mitigation: Review the decoded payload before execution and install only inside an isolated VM, container, or dedicated conda or micromamba environment. <br>
Risk: The workflow may download dependencies or data and run package installation steps on the user's machine. <br>
Mitigation: Approve network access explicitly, avoid shared or HPC login nodes unless permitted, and run from a disposable or dedicated environment. <br>
Risk: Docking scores and filters are screening signals rather than biological proof. <br>
Mitigation: Treat results as decision-support outputs, review poses and controls, and confirm promising candidates with appropriate experimental or higher-fidelity computational validation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/pancreatic-lipase-pro-docking) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Artifact restore helper](artifact/restore_and_run.sh) <br>
- [Artifact payload archive](artifact/payload_universal_upload.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Analysis, Files, Markdown] <br>
**Output Format:** [Markdown guidance with bash commands and generated CSV, HTML, log, metadata, and pose files when executed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates run directories with ranked docking results, reports, descriptors, logs, and prepared molecular artifacts.] <br>

## Skill Version(s): <br>
100.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
