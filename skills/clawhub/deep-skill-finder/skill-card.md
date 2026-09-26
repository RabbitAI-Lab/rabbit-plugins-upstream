## Description:

Deep Skill Finder helps an agent search, rank, recommend, install, and collect reviewed feedback for skills based on a user's task and real usage signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lintong123](https://clawhub.ai/user/lintong123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external agent users use this skill when they need an agent to find relevant skills, compare recommendations using real usage feedback, install a selected skill, or submit reviewed performance feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted skill name could cause downloaded content to be written outside the intended skills directory.

Mitigation: Avoid installing results whose names contain slashes, dots, path-like text, or unusual characters; prefer manual inspection or a sandboxed skills directory until installer name validation is added.

Risk: The skill searches a remote registry and can download and write skill files into the local skills directory.

Mitigation: Use it only with trusted registries and review recommended skills before approving installation.

Risk: Feedback submission can keep an anonymous local client ID and upload reviewed feedback plus optional image or video attachments.

Mitigation: Submit feedback only after reviewing the redacted fields and ensuring attachments contain no sensitive information.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/lintong123/skills/deep-skill-finder)
- [DeepSkill Market skill directory](https://www.deepskill.market/skill)
- [Skill evaluation workflow](artifact/references/skill-evaluation.md)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown recommendations with inline shell commands and JSON status or error payloads from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces up to five ranked skill recommendations and can guide installation and reviewed feedback submission.]

## Skill Version(s):

1.3.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
