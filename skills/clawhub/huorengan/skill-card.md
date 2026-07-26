## Description: <br>
Huorengan audits and rewrites Chinese or English text to reduce AI-like tone while preserving protected facts, quotes, commands, paths, and technical wording. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fendouai](https://clawhub.ai/user/fendouai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and editors use this skill to detect AI-like phrasing, rewrite drafts, or make minimal in-place edits in Chinese or English. It is most useful when a user asks for less template-like writing while preserving factual and technical spans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rewrite or edit mode can unintentionally alter facts, quotes, commands, paths, or technical wording. <br>
Mitigation: Review changes before sending or committing them, and preserve protected spans when fidelity conflicts with style. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fendouai/skills/huorengan) <br>
- [Server-resolved GitHub provenance](https://github.com/fendouai/huorengan) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>
- [Protected spans reference](artifact/references/protected-spans.md) <br>
- [Voice contract reference](artifact/references/voice-contract.md) <br>
- [Detector category map](artifact/detector/CATEGORIES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text with audit findings, rewrites, edit summaries, and voice drift notes depending on mode] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No external tools or APIs are required; edit mode may propose minimal changes to user-provided files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
