## Description: <br>
Objective, source-traceable evaluation of HiFi gear, covering transducers such as IEMs, headphones, and TWS, and source gear such as DACs, amps, and DAPs, as a bilingual evidence-traced verdict. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentjiang06](https://clawhub.ai/user/vincentjiang06) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill for objective HiFi device evaluation and A/B comparison, including frequency-response-based transducer analysis and measured source-gear competence. It is not intended for buying recommendations, EQ tuning, speakers, or non-audio tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live source retrieval may return stale, unavailable, biased, or conflicting review and measurement evidence. <br>
Mitigation: Follow the retrieval and data-cleaning rules: record provenance, source tier, freshness, dissent, and unsupported gaps instead of filling missing evidence. <br>
Risk: Frequency-response comparisons can mislead when rigs, targets, or measurers are mixed. <br>
Mitigation: Use same-rig targets and comparison guards, and refuse false-precision verdicts when the evidence is not comparable. <br>
Risk: Subjective review consensus can be overstated as measurement evidence, especially in long-form prose. <br>
Mitigation: Keep every claim tagged as measured, consensus, or prior, and run validate_output.py or check_longform.py before delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincentjiang06/skills/hifi-review) <br>
- [Skill specification](SKILL.md) <br>
- [English README](README.en.md) <br>
- [Research bibliography](references/research-bibliography.md) <br>
- [Source registry](references/source-registry.json) <br>
- [Targets](references/targets.json) <br>
- [Accuracy guardrails](rules/accuracy-guardrails.md) <br>
- [Technicalities from reviews](rules/technicalities-from-reviews.md) <br>
- [Source gear evaluation](rules/source-gear-eval.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Bilingual Markdown with optional JSON analysis traces and inline shell command invocations for local validators.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports compact summaries or Chinese-primary long-form reviews; claims are tagged as measured, consensus, or prior with provenance and confidence.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
