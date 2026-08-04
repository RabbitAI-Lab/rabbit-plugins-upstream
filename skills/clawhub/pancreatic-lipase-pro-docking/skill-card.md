## Description: <br>
Professional virtual-screening stack for human pancreatic lipase PDB 1LPB with multi-site docking, high-exhaustiveness re-docking, reporting, environment checks, structured logging, reproducibility records, output validation, and tests. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, educators, and developers use this skill to run virtual screening workflows for human pancreatic lipase from molecule names or ligand CSV files, producing docking results and reports for authorized research and education. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may install sizable chemistry dependencies and use public chemistry or receptor services. <br>
Mitigation: Run it in a disposable conda environment, VM, or container and review network/data handling before using proprietary molecule sets. <br>
Risk: Docking outputs are research artifacts and can be misleading if dependencies, receptor files, or ligand inputs are wrong. <br>
Mitigation: Run the environment self-check, keep logs and versions.json, validate results, and review scores before using them for scientific decisions. <br>
Risk: The skill writes run outputs into the current working directory. <br>
Mitigation: Execute it from an intended project or scratch directory and review generated files before sharing or committing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/pancreatic-lipase-pro-docking) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local run artifacts such as docking result CSV files, logs, reports, validation output, and reproducibility records when executed.] <br>

## Skill Version(s): <br>
100.3.4 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
