## Description: <br>
Fetch handwritten notes, sketches, and drawings from a reMarkable tablet via Cloud API (rmapi). Process content by refining artwork with AI image generation, extracting handwritten text to memory/journal, or using sketches as input for other workflows. Use when working with reMarkable tablet content, syncing handwritten notes, processing sketches, or integrating tablet drawings into projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolmanns](https://clawhub.ai/user/coolmanns) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to fetch selected reMarkable tablet notes, sketches, and drawings, then extract handwritten text or refine visual content for journals, memory files, project docs, and illustration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent may access more reMarkable Cloud content than the user intended. <br>
Mitigation: Use a dedicated sharing folder, explicit share tag, or starred-item workflow and preview matches before downloading. <br>
Risk: The rmapi token stored in ~/.rmapi can allow automatic cloud access. <br>
Mitigation: Protect ~/.rmapi and remove it when automatic reMarkable Cloud access is no longer desired. <br>
Risk: Extracted handwriting can be incorrect or unsuitable for memory, journal, or project files. <br>
Mitigation: Review extracted handwriting before saving it to memory, journals, or project documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolmanns/skills/remarkable-tablet) <br>
- [reMarkable desktop connection](https://my.remarkable.com/connect/desktop) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown, Files] <br>
**Output Format:** [Markdown guidance with shell command examples and file workflow instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce downloaded PDF or PNG files, extracted handwritten text, journal or memory entries, project documentation updates, or refined images depending on the agent workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
