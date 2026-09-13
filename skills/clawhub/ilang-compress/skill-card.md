## Description:

Compress natural language prompts into I-Lang — AI-native structured instructions. Output is text notation only — review before passing to execution agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsorgcn](https://clawhub.ai/user/adsorgcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, prompt engineers, and agent users use this skill to compress natural-language prompts into compact I-Lang notation while preserving the intended task semantics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compressed output can contain command-like verbs and resource references such as READ, WRIT, DEL, COPY, SYNC, @LOCAL, or cloud targets.

Mitigation: Review the generated notation before passing it to any agent or tool that can execute file, cloud, or deletion operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/adsorgcn/skills/ilang-compress)
- [I-Lang Homepage](https://ilang.ai)
- [I-Lang Specification](https://ilang.ai/spec/)
- [I-Lang Dictionary](https://github.com/ilang-ai/ilang-dict)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Plain text I-Lang notation followed by a brief explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command-like notation is text only and should be reviewed before use with execution agents.]

## Skill Version(s):

2.3.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
