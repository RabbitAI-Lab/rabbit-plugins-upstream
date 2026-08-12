## Description:

Removes signs of AI-generated writing from text and rewrites content toward a more natural human writing style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to revise provided text so it reads less like AI-generated prose and more like ordinary human writing. It is suited to text, Markdown, JSON-style responses, and batch-oriented content rewriting workflows where disclosure and integrity requirements are already understood.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is framed as removing signs of AI authorship, which can conflict with disclosure, academic integrity, compliance, or platform authenticity rules.

Mitigation: Use it only in workflows where AI assistance may be used and disclosed according to the applicable policy; do not use it to bypass authorship or integrity requirements.

Risk: The artifact declares read, write, and command execution capabilities that are broader than needed for simple text rewriting.

Mitigation: Run it with the minimum available permissions, avoid granting command execution or broad filesystem access, and review any proposed file or shell actions before execution.

Risk: Content sent through the skill may include sensitive or confidential text.

Mitigation: Avoid submitting secrets, regulated data, or confidential material unless the agent platform and model path are approved for that data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/humanizer)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Homepage listed in artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text with optional JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten content, processing status, metadata such as word count and style, and operational guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
