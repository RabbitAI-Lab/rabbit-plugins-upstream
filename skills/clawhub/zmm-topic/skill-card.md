## Description:

An interactive short-video topic selection skill that helps creators judge topic demand, benchmark signals, real user evidence, and content mix before choosing what to film.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to evaluate short-video topic ideas, generate a small set of evidence-backed candidates, diagnose weak topics, and turn flat themes into stronger angles without fabricating data or forcing one-click topic lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save interaction outcomes and modify shared guidance or memory files, which may affect other creator workflows without clear user consent.

Mitigation: Require explicit confirmation before automatic feedback writeback or memory updates, especially for shared framework files.

Risk: The skill may read sensitive creator strategy, client, or business material from the intended creator vault.

Mitigation: Use it only with vaults intended for this workflow, and avoid using it on sensitive material unless access scope and retention behavior are acceptable.

Risk: Topic recommendations can be misleading if benchmark or personal evidence is missing, stale, or overgeneralized.

Mitigation: Keep unsupported judgments labeled as inference and review evidence before filming or publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-topic)
- [常识缺口法](references/常识缺口法.md)
- [议程与合集](references/议程与合集.md)
- [选题三路](references/选题三路.md)
- [题感引擎](references/题感引擎.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with structured topic diagnostics, candidate options, evidence notes, and next-step choices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose shell commands only when the user's local creator vault and supporting scripts are available.]

## Skill Version(s):

0.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
