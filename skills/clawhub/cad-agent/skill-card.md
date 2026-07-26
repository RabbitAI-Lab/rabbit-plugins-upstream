## Description: <br>
Send build123d CAD commands via HTTP to render images, allowing visual iteration on 3D models entirely within a containerized CAD environment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawd-maf](https://clawhub.ai/user/clawd-maf) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI agents use this skill to create and refine build123d CAD models by sending commands to a local rendering service, reviewing rendered images, and iterating before export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CAD helper runs through a local Docker-backed rendering service with exposed ports and possible host directory mounts. <br>
Mitigation: Review the referenced repository and Docker configuration before installing, especially exposed ports and mounted host directories. <br>
Risk: The service and generated CAD outputs may remain on the machine after use. <br>
Mitigation: Stop and remove the container when finished if the service or generated outputs should not persist locally. <br>
Risk: Modeling commands execute inside the containerized CAD environment. <br>
Mitigation: Review build123d code before sending it to the service and keep the container isolated to the intended local workflow. <br>


## Reference(s): <br>
- [CAD Agent on ClawHub](https://clawhub.ai/clawd-maf/skills/cad-agent) <br>
- [build123d documentation](https://build123d.readthedocs.io/) <br>
- [VTK](https://vtk.org/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with HTTP command examples and build123d code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The local CAD service may return JSON statuses, rendered PNG images, and exported CAD files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
