## Description:

QGIS-Agent lets an AI agent drive a local QGIS Processing server over HTTP to discover and run GIS analysis, conversion, project, and rendering workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaojj662](https://clawhub.ai/user/zhaojj662)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GIS analysts, and agent builders use QGIS-Agent to let an agent search QGIS Processing algorithms, inspect parameters, run spatial analysis chains, manage QGIS projects, and render map outputs through a local HTTP service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated local HTTP controls can read and write GIS files.

Mitigation: Run the service only for trusted local callers, set QGIS_ALLOWED_PATHS before use, and keep outputs in a dedicated working directory.

Risk: Project save, render, and processing operations can write to user-selected paths.

Mitigation: Review every project save, render, and output path before allowing an agent to execute requests.

Risk: Optional PyQGIS execution can run arbitrary Python code when enabled.

Mitigation: Keep PYQGIS_ENABLE_EXEC disabled unless operating in a trusted, constrained environment.

## Reference(s):

- [QGIS Agent API detailed specification](configs/api.md)
- [QGIS Agent call examples](references/examples.md)
- [QGIS download page](https://qgis.org/download/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with HTTP/curl examples and JSON request/response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide local HTTP requests that produce GIS files such as GeoPackage, raster outputs, QGIS projects, and PNG renderings.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
