## Description:

Audit text, transcripts, audio, or video for bogus proof tactics, handwaving, bad citations, and weak argument moves.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stanestane](https://clawhub.ai/user/stanestane)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, analysts, and reviewers use this skill to audit text, transcripts, audio, video, or mixed media for unsupported claims, citation theater, technical fog, and weak argument moves. It helps produce a verdict, prioritized findings, a claim map, and concrete repair steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio or video audits can miss or mislocate claims when no reliable transcript is available.

Mitigation: Use an available transcription path and preserve timestamps; if transcription is unavailable, limit the audit to visible text and user-provided context.

Risk: The audit could overstate an unsupported claim as false or imply dishonesty without sufficient evidence.

Mitigation: Separate absence of proof from falsity, classify issues as unsupported, contradicted, ambiguous, or overclaimed, and avoid claiming deception unless the artifact supports it.

Risk: Citation findings can be misleading if references are judged without inspection.

Mitigation: Inspect accessible references before flagging citation defects and distinguish missing support from material that is merely unexplained for the current audience.

## Reference(s):

- [Korpi Proof Technique Map](references/korpi-proof-technique-map.md)
- [Korpi's World: 63 Methods of Mathematical Proof](https://www.korpisworld.com/Mathematics/math%20leftovers/methods_of_mathematical_proof.htm)
- [ClawHub Skill Page](https://clawhub.ai/stanestane/skills/bullshit-argument-audit)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown audit report with verdict, findings, claim map, and repair plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include short quoted snippets, paraphrased locations, timestamps when available, and severity ratings.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
