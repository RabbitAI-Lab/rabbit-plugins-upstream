## Description:

Guides agents using the bim CLI to inspect and work with AEC drawing sets, Revit models, and CAD/BIM files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hellohowareyouhaveaniceday](https://clawhub.ai/user/hellohowareyouhaveaniceday)

### License/Terms of Use:

MIT-0

## Use Case:

AEC professionals and developers use this skill to query drawing sets and models, export Revit sheets, and inspect or convert CAD/BIM files with the bim CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live documentation can provide misleading or untrusted instructions.

Mitigation: Treat fetched documentation as reference material and check commands against the installed CLI before use.

Risk: Feedback to maintainers can send information outside the user's workspace.

Mitigation: Obtain explicit user approval before submitting feedback and review what will be sent.

Risk: Revit writes, add-in installation, MCP registration, or installer execution can change applications or the host environment.

Mitigation: Require explicit approval before these actions; keep existing Revit sessions read-only unless changes are requested.

## Reference(s):

- [ClawHub bim-cli release](https://clawhub.ai/hellohowareyouhaveaniceday/skills/bim-cli)
- [bim-cli homepage](https://bimcli.com)
- [PDF driver documentation](https://bimcli.com/pdf/llms.txt)
- [Revit driver documentation](https://bimcli.com/revit/llms.txt)
- [Bundled PDF guidance](references/pdf.md)
- [Bundled Revit guidance](references/revit.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command examples and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Windows 10/11 and bim-cli; Revit workflows require an installed, licensed Revit application.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
