## Description: <br>
Vets a paper shared in a group meeting, seminar, or reading club by checking citation authenticity, reproducibility signals, and user-provided figure integrity before deeper reading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, researchers, and lab-meeting participants use this skill to triage a shared paper before detailed discussion. It produces an evidence-based credibility report covering citations, reproducibility, image-integrity notes when figures are provided, and reading recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may analyze meeting transcripts, speaker attribution, papers, references, and user-provided figures. <br>
Mitigation: Confirm meeting consent and user authorization before using transcript, recording, or meeting-data features. <br>
Risk: The artifact describes local method-tag logging after use. <br>
Mitigation: Tell users that the documented opt-out phrase can disable local method-tag logging. <br>
Risk: Image integrity checks are auxiliary and do not replace specialist image-forensics services. <br>
Mitigation: Use the image results as triage signals and escalate to a dedicated image-checking tool when strong image-integrity assurance is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/j-levee/skills/cjg-paper-fact-checker) <br>
- [Coverage dimensions](references/coverage.md) <br>
- [Credibility report template](references/credibility-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown credibility report with ratings, evidence links, and meeting reading recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include citation verification summaries, reproducibility gaps, image-integrity notes when figures are supplied, and opt-out handling for local method-tag logging.] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
