## Description:

Finds matching AI-video tutorials, skills, options, and production steps for an agent’s video request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to find a relevant video-making workflow, compare visual options, and get the steps and install command before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests are sent to an external service without an explicit privacy warning in the skill.

Mitigation: Tell users before searching and avoid including confidential or personal details in queries.

Risk: Installation examples include unpinned commands.

Mitigation: Review the install command and pin versions where supported before running it.

Risk: The security scan was partial because some local references were unresolved.

Mitigation: Review the unresolved references and complete a full scan before relying on the security assessment.

## Reference(s):

- [varg how-to](https://varg.ai/how-to)
- [ClawHub release page](https://clawhub.ai/vargai/skills/how-to-make-ai-video)
- [Whole-video production prompt](artifact/references/whole-video-prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Matched tutorials, skill suggestions, visual options, and production steps; does not generate video.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
