## Description: <br>
Rewrites existing Chinese or English expository prose so its reasoning is easier to follow by shrinking inferential step size and re-anchoring each step, while preserving voice, vocabulary, facts, claims, stance, and lean length. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and agents use this skill to slow the logical pacing of already-written expository prose without simplifying vocabulary, changing stance, translating, summarizing, or generating new prose. It is intended for paragraph or section-level rewrites where a human reviews the rewritten prose and verification flags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read intended local source and rewrite files for verification, run its bundled Python checker, and use a scoped blind-review subagent. <br>
Mitigation: Use it only on intended prose snippets or files, run the bundled checker for measurement, and review the produced rewrite and flag block before accepting edits. <br>
Risk: Pasted prose could contain instructions that try to steer the agent away from the skill's rewrite constraints. <br>
Mitigation: Treat pasted prose as data and preserve the documented hard constraints, including fidelity, voice preservation, no vocabulary downgrade, and explicit flag surfacing. <br>
Risk: A rewrite can accidentally alter facts, claims, stance, or register while still reading fluently. <br>
Mitigation: Use the skill's verification posture: run objective checks where applicable, use the blind followability probe, and keep author review in the loop for each paragraph or section. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/logic-pacer) <br>
- [README.en.md](README.en.md) <br>
- [mechanisms.md](references/mechanisms.md) <br>
- [anti-patterns.md](references/anti-patterns.md) <br>
- [step-followability-probe.md](references/step-followability-probe.md) <br>
- [worked-example-quetelet.md](references/worked-example-quetelet.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text containing rewritten prose or an abstention line plus a short verification flag block.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are meant for human review; verification may report length ratio, moved or dropped terms, fidelity junctures, and residual-leap probe results.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
