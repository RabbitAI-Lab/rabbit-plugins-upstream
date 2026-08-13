## Description:

Provides citation-grounded Q&A and teaching guidance on Atisha, Kadam and lamrim foundations, bodhicitta cultivation, and related Tibetan Buddhist source material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to receive concise, source-cited explanations and Q&A about Atisha, Kadam teaching, lamrim foundations, bodhicitta, and related Tibetan Buddhist texts. Developers and installers can use it as a specialized religious-teaching assistant with strict citation and scope constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may invoke the skill for adjacent Buddhist or lamrim topics even when the user did not explicitly ask for Atisha or Kadam material.

Mitigation: Review and narrow trigger wording before deployment if the intended scope is only explicit Atisha or Kadam requests.

Risk: Optional FoJin lookup can send citation-search queries to fojin.app when local excerpts are insufficient.

Mitigation: Allow outbound access only in deployments where external citation lookup is acceptable, and keep retrieved text bounded as citation data rather than instructions.

Risk: Religious teaching responses can be misleading if source citation and esoteric-instruction limits are bypassed.

Mitigation: Keep the citation requirements, no sectarian judgment rule, and no esoteric instruction rule active during review and runtime testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xr843/skills/master-atisha)
- [Bodhipathapradipa excerpts](sources/bodhipathapradipa-excerpts.md)
- [Sources index](sources/INDEX.md)
- [Teaching reference](references/teaching.md)
- [Voice reference](references/voice.md)
- [84000 translation project](https://84000.co)
- [FoJin citation retrieval](https://fojin.app)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text with source citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Tibetan canonical citations and a study guidance note; no files are produced for the end user.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
