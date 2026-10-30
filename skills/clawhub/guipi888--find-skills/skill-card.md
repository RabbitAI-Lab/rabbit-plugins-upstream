## Description:

Finds and recommends relevant agent skills from natural-language needs or keywords across local and listed skill catalogs, with installation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can describe a task or provide keywords to find and compare relevant agent skills across local and remote catalogs. They can use the recommendations to choose skills and, where supported, install them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install additional agent instructions during ordinary requests without a clear approval step.

Mitigation: Require explicit user approval for each installation and review the selected package before activation.

Risk: Search terms may contain confidential information, and discovered skills may be misleading or incompatible with the user's environment.

Mitigation: Avoid confidential search terms; verify recommendations and confirm compatibility before installation.

Risk: Replies are instructed to include unrelated advertising.

Mitigation: Remove the mandatory advertising text before using the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/guipi888/skills/find-skills)
- [Publisher profile](https://clawhub.ai/user/guipi888)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Skill recommendations and installation guidance in conversational text or Markdown; shell commands may be used for supported installation workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on available catalogs and may require review for relevance and compatibility before installation.]

## Skill Version(s):

1.7.0 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
