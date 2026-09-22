## Description:

Automates Figma API workflows for browsing team projects and files, reading design structure, exporting images, managing comments, viewing version history, and retrieving design variables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and automation users can use this skill to inspect Figma files, export design assets, manage comments, review version history, and retrieve components, styles, and variables through an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command execution capabilities that are not clearly limited to Figma work.

Mitigation: Install and run it only in an environment where those capabilities are acceptable, and restrict agent access to the files and commands needed for the Figma task.

Risk: Figma credentials or linked account access could expose more teams, files, or comments than intended.

Mitigation: Use a Figma account or API key scoped to the specific teams and files required for the workflow, and avoid using broad personal or organization-wide credentials.

Risk: Image exports return temporary URLs and full file-tree reads can be slow for large Figma files.

Mitigation: Treat export URLs as time-limited outputs and use shallow file reads such as depth 1 or 2 for large files when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/figma-2)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [API Calls, Files, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance and JSON-style operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce exported image files or temporary Figma export URLs depending on the requested operation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
