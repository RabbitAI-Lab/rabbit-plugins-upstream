## Description: <br>
Runs a one-command virtual screening workflow against human pancreatic lipase (PDB 1LPB), producing ranked docking energies, poses, and an HTML report from ligand CSV input. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, researchers, and educators use this command skill to run pancreatic-lipase ligand docking experiments and review ranked outputs for education, research, or screening analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The one-command path unpacks embedded code and may install or upgrade scientific packages. <br>
Mitigation: Review the artifact before execution and run it in a disposable virtual environment or container. <br>
Risk: The workflow may download public receptor data, run external docking tools, and write result or log directories. <br>
Mitigation: Run it from an isolated project directory with expected network and disk-write permissions. <br>
Risk: The security guidance warns against the zero-instruction path on shared HPC resources. <br>
Mitigation: Avoid running the zero-instruction path on shared HPC systems; use a non-shared machine or controlled job environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/pancreatic-lipase-pro-docking) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands; runtime outputs include CSV results, pose files, logs, and an HTML report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ligand CSV input and may write speed_runs result directories in the caller's working directory.] <br>

## Skill Version(s): <br>
100.0.8 (source: server release metadata; artifact frontmatter reports 100.1.3 and artifact _meta.json reports 100.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
