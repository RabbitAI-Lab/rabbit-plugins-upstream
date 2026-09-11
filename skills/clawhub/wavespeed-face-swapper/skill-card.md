## Description:

Swap faces in images and videos using WaveSpeed AI with multi-face targeting, automatic lighting and skin tone adaptation, and consent-focused refusal guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to perform consented, lawful image or video face swaps through WaveSpeed AI while refusing impersonation, deception, sexual content, and other prohibited likeness edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media is processed by WaveSpeed and a WaveSpeed login may be stored locally.

Mitigation: Use only consented, lawful, non-deceptive media and rely on local login or environment credentials without sharing keys in chat.

Risk: Global npm installs can add ordinary third-party package and local privilege risk.

Mitigation: Avoid running npm commands as administrator and prefer pinned or reviewed package versions where feasible.

Risk: Face swapping can create misleading likeness edits if consent, rights, or disclosure are unclear.

Mitigation: Confirm consent, media rights, non-deceptive purpose, no sexual or intimate content, no minors, and recommend labeling shared outputs as AI-edited.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wavespeed/skills/wavespeed-face-swapper)
- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces WaveSpeed output URLs or downloaded media files when commands are executed.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
