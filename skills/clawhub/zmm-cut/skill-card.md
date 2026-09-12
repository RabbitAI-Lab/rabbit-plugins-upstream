## Description:

Guides an agent through Chinese talking-head video post-production: content-level deletion and reordering, speech cleanup, speed adjustment, captions, optional B-roll, export checks, and local transcription fallback while avoiding invented speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to turn recorded talking-head footage into a publishable cut by cleaning speech, deleting or reordering only recorded content, applying caption defaults, and checking the final timeline or export. It is tailored to a single account's editing defaults but includes guidance for changing account-specific parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide local vault-memory reads and writes, which may persist account-specific preferences or editing history beyond the immediate task.

Mitigation: Review memory paths before use, avoid storing sensitive source material or private client details, and confirm any new memory entry with the user before writing it.

Risk: The security summary flags destructive cleanup guidance, and the artifact includes advice to delete unmasked original media after use.

Mitigation: Require explicit approval before deleting original media, verify that exported or masked copies are usable, and retain source files according to the user's retention policy.

Risk: The security guidance flags platform-review evasion concerns and recommends overriding rules that leave financial amounts visible or reduce cross-channel review risk.

Mitigation: Do not use the skill to bypass platform review; manually review any financial, customer, or platform-sensitive footage and mask or remove sensitive elements before publication.

Risk: Timeline and caption tool metadata may be misleading, causing edits or captions to appear correct when the rendered frame or file differs.

Mitigation: Read back the timeline after edits and verify full-size rendered frames or the exported file itself before treating the cut as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-cut)
- [ChatCut 实操](artifact/references/ChatCut实操.md)
- [内容层重组](artifact/references/内容层重组.md)
- [规则卡](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checkpointed edit decisions, timeline instructions, and optional shell-command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local transcription commands, deletion/reorder rationales, caption settings, B-roll handling guidance, export checks, and vault-memory update guidance.]

## Skill Version(s):

0.2.6 (source: server release metadata; artifact frontmatter lists 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
