## Description:

Helps solo knowledge-video creators choose short-video topics through interactive supply-demand checks, benchmark signals, real evidence, conflict framing, and feasibility filters rather than one-click topic list generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill as a topic-selection adviser for short-form knowledge videos. It helps evaluate candidate topics, turn broad topics into stronger angles, surface evidence and risks, and prepare next-step guidance without deciding the final topic for the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the agent to execute local commands or persist changes to topic pipeline, published index, vault, and memory folders.

Mitigation: Use it only in a trusted, scoped workspace and require explicit confirmation before command execution or persistent writes.

Risk: User-provided keywords or topics could be passed into shell commands during candidate surfacing or index rebuilding.

Mitigation: Review command text before execution and avoid passing untrusted or unsanitized input to shell commands.

Risk: Topic recommendations can overstate confidence when benchmark data, personal evidence, or publication history is incomplete.

Mitigation: Keep evidence labels explicit, distinguish inferred judgments from verified data, and require the creator to choose and review topics before publication.

Risk: Automatic feedback or memory updates may preserve incorrect preferences or private context.

Mitigation: Review the exact paths and content before memory writes, and keep changes scoped to the intended creator workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-topic)
- [常识缺口法](references/常识缺口法.md)
- [选题三路](references/选题三路.md)
- [题感引擎](references/题感引擎.md)
- [议程与合集](references/议程与合集.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with candidate topic sections, diagnostics, evidence notes, short hook drafts, and occasional shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose topic-pipeline, published-index, vault, and memory updates when used in a trusted, scoped workspace.]

## Skill Version(s):

0.2.6 (source: server release evidence; artifact frontmatter says 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
