## Description: <br>
Audits and rewrites Chinese or English content to remove AI tone and pull drafts toward a target human voice, with detect-only and edit-in-place modes, scene packs, protected spans, and voice profiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fendouai](https://clawhub.ai/user/fendouai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, writers, and content teams use this skill to review and rewrite drafts that sound overly templated, promotional, or AI-shaped while preserving facts, commands, paths, quotes, and other protected spans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The submitted package includes unrelated local runtime logs and state files. <br>
Mitigation: Review before installing and republish without .omx logs or state files. <br>
Risk: Ambiguous review requests could lead to unintended rewrites instead of detection-only feedback. <br>
Mitigation: Use explicit modes such as detect, rewrite, or edit, and ask for clarification before changing user text when intent is unclear. <br>
Risk: Custom voice samples could be misused to imitate an identifiable person without permission. <br>
Mitigation: Use custom voice calibration only with authorized samples and avoid copying factual content, opinions, or identity-specific traits from the sample. <br>
Risk: AI-tone findings are writing-quality signals, not proof that text was AI-generated. <br>
Mitigation: Treat findings as editorial guidance and require human review before making claims about authorship. <br>


## Reference(s): <br>
- [Humanize Text Skill on ClawHub](https://clawhub.ai/fendouai/skills/humanize-text-skill) <br>
- [Project Homepage](https://github.com/fendouai/humanize-text-skill) <br>
- [Lynote.ai](https://lynote.ai) <br>
- [Reference Index](references/README.md) <br>
- [Operation Manual](references/operation-manual.md) <br>
- [Protected Spans](references/protected-spans.md) <br>
- [Voice Contract](references/voice-contract.md) <br>
- [Scene Packs](references/scene-packs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or plain text with issue notes, rewritten passages, and optional edit guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May preserve protected spans and may return detect-only findings instead of rewrites when requested.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata; artifact frontmatter, package.json, and CHANGELOG show 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
