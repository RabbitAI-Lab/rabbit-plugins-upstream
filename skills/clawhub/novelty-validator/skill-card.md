## Description: <br>
Validates whether a meeting or brainstorm idea appears novel by extracting a structured claim, comparing it against literature and patent evidence, and returning a confidence-scored novelty assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and technical teams use this skill during or after academic meetings, seminars, and brainstorms to check whether a proposed idea, method, or research direction is already covered by prior work. It supports Tencent Meeting transcripts, intelligent minutes, or directly stated ideas and returns evidence-backed novelty judgments plus next-step innovation paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting transcripts and research ideas may include confidential or pre-publication information that could be processed through external literature or embedding services. <br>
Mitigation: Use only with participant and data-owner consent, avoid confidential discussions unless remote embeddings are disabled or approved, and disclose any external processing before use. <br>
Risk: The skill requests broad meeting, identity, recording, attendee-report, and contact-lookup authority through Tencent Meeting workflows. <br>
Mitigation: Review Tencent Meeting permissions before use, authorize only meetings the user is allowed to access, and avoid collecting attendee or recording data that is not needed for the novelty check. <br>
Risk: Novelty judgments can be misleading when retrieval is incomplete, candidates lack verifiable evidence, or all candidates have low similarity. <br>
Mitigation: Downgrade conclusions when evidence is weak, require verifiable prior-work citations for similar or duplicate findings, and treat the report as rapid research guidance rather than a legal novelty determination. <br>


## Reference(s): <br>
- [Idea Extraction](artifact/references/idea-extraction.md) <br>
- [Novelty Rubric](artifact/references/novelty-rubric.md) <br>
- [Innovation Path](artifact/references/innovation_path.md) <br>
- [Vector Recall](artifact/references/vector_recall.md) <br>
- [Vector Recall Implementation](artifact/references/vector_recall_impl.py) <br>
- [Case Library](artifact/references/case_library.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/j-levee/skills/novelty-validator) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown report with structured claims, evidence lists, confidence notes, and optional shell or API command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should include cited prior-work evidence, overlap dimensions, confidence, and explicit uncertainty when retrieval is sparse or degraded.] <br>

## Skill Version(s): <br>
1.7.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
