## Description:

Identifies and removes AI watermark and provenance signals in images, video, and text that the user generated or edited.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can inspect or remove supported AI marks and provenance signals in content they generated or edited. The skill directs users to avoid removing marks that protect third-party paid or copyrighted assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete, and it notes text-processing functions beyond the stated image and video scope, along with undeclared tool scope.

Mitigation: Review the requested operation and relevant local references before running commands; use the skill only on content the user generated or edited and is allowed to change.

## Reference(s):

- [Command reference](references/commands.md)
- [Installation guide](references/install.md)
- [Project site](https://raiw.cc)
- [Project repository](https://github.com/wiltodelta/remove-ai-watermarks)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Files]

**Output Format:** [Markdown guidance and shell commands; may create processed media or text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only results observed from commands run; does not treat missing local signals as proof of human origin or a clean file.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
