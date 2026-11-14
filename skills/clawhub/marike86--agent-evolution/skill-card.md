## Description:

边做科研边保存可复用成果，用元认知复盘和后续验证改进智能体的工作方法。

This skill is ready for commercial/non-commercial use.

## Publisher:

[marike86](https://clawhub.ai/user/marike86)

### License/Terms of Use:

MIT-0

## Use Case:

科研人员与研究智能体使用此技能，在复杂研究任务中生成、验证并保存可复用成果，复盘工作过程，并在后续任务中检验和修订项目记忆。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan notes detected file read/write capabilities without a declared scope; runtime permissions were not verified.

Mitigation: Before enabling file-backed memory, review the host's actual read/write permissions and authorize only the intended project directory.

## Reference(s):

- [ClawHub release provenance](https://github.com/marike86/scientific-ideation_skill/tree/main/skills/agent-evolution)
- [ClawHub skill page](https://clawhub.ai/marike86/skills/agent-evolution)
- [创造性元认知框架](https://doi.org/10.1016/j.plrev.2023.07.002)
- [Creative Cognition: The Geneplore Model](https://mitpress.mit.edu/9780262061506/creative-cognition/)
- [Dual-Space Search](https://doi.org/10.1016/0364-0213%2888%2990007-9)
- [CoALA modular memory paper](https://openreview.net/pdf/07475727a2787df12052196b9f2624497ef3c3bd.pdf)
- [记忆与试验操作](references/operations.md)
- [产品机制与接入](references/product-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown guidance and JSON memory entries, with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels unverified ideas as candidates and captures only reusable content that is authorized to retain.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
