## Description:

Guides agents in choosing varg video, image, voice, and music models, writing prompts, and checking generated clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and developers use this skill to plan varg media generations, select models, write reference-aware prompts, and review clips for visual and audio issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send user media to external generation services.

Mitigation: Check which files will be uploaded and to which service, and confirm authorization to share them before generation.

Risk: The installation example does not pin an exact version.

Mitigation: Pin the reviewed release version when installing the skill.

Risk: The security scan was partial because some referenced paths were missing.

Mitigation: Review the complete release contents and resolve missing paths before relying on the scan.

## Reference(s):

- [MCP tools and workflow](references/mcp-tools.md)
- [Prompt templates](references/prompt-templates.md)
- [Model guidance](references/models.md)
- [Generation examples](references/examples.md)
- [Look references](references/look-references.md)
- [Varg model catalog](https://varg.ai/models/llms.txt)
- [Seedance 2.5 model notes](https://varg.ai/models/seedance_2_5.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Model recommendations, media-generation prompts, and QA checklists in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include reference roles, timed shot instructions, and shell command examples.]

## Skill Version(s):

1.0.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
