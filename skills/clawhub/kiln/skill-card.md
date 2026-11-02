## Description:

Design, check, slice, print, and monitor objects on real 3D printers through the Kiln MCP server and CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[codeofaxel](https://clawhub.ai/user/codeofaxel)

### License/Terms of Use:

AGPL-3.0-or-later

## Use Case:

Makers, designers, and developers use Kiln to turn an idea or existing model into a checked, sliced 3D print, and to monitor or recover an active printer job.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Printing or placing an outside order can cause physical or financial consequences.

Mitigation: Keep print and order approvals enabled; review and approve each action before it is carried out.

Risk: Printer API credentials and information sent to cloud services may be sensitive.

Mitigation: Protect stored printer keys, connect only intended printers, and review what cloud services receive before use.

Risk: The security assessment did not include external package runtime code.

Mitigation: Pin a reviewed package version and assess the installed package before deployment.

## Reference(s):

- [Kiln on ClawHub](https://clawhub.ai/codeofaxel/skills/kiln)
- [Installation guide](https://kiln3d.com/install)
- [Supported printers](https://kiln3d.com/printers)
- [Kiln3d on PyPI](https://pypi.org/project/kiln3d/)
- [Version 1.5.0 release notes](https://github.com/codeofaxel/Kiln/releases/tag/v1.5.0)

## Skill Output:

**Output Type(s):** [3D model files, Slicer outputs, Printer-control actions, Analysis, Guidance]

**Output Format:** [3D model and slicer files, plus structured tool results and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send approved jobs to a connected physical printer.]

## Skill Version(s):

1.5.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
