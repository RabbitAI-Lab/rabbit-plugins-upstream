## Description:

Guides an agent through a Chinese-language workflow for re-explaining a familiar concept by locking the core question, definition, theory target, and analogies before drafting a short-form concept script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to turn a familiar business or cognition concept into a concise Chinese口播 draft with explicit concept gates, theory checks, analogies, revision discipline, and post-publication follow-up steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate from broad concept-explanation phrasing and may read or update AI KEY/vault content files.

Mitigation: Invoke it explicitly when possible and review proposed file reads or edits before allowing workspace changes.

Risk: Drafting guidance may carry incorrect theory citations, mismatched analogies, or outdated workspace rules into public content.

Mitigation: Use the skill's required four-lock checkpoint, citation verification level, red-line scan, and final human口述 review before publication.

## Reference(s):

- [规则卡](references/规则卡.md)
- [锁四样](references/锁四样.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-concept)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance and structured drafting checkpoints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily Chinese-language output; may propose edits to vault notes, draft files, metadata fields, checklists, and calendar follow-up items when the host workspace provides those paths.]

## Skill Version(s):

0.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
