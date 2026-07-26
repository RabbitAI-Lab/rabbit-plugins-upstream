## Description: <br>
Checks paper drafts or AI-generated reference lists against SmartLib data, flags likely citation hallucinations or metadata mismatches, and produces an HTML verification report with corrected citation text, difference markers, statistics, and verification links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, researchers, editors, and reviewers use this skill to verify whether pasted references, BibTeX entries, or paper draft citations exist and to identify citation fields that may need correction before submission or review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send user email, references, and manuscript-derived citation text to SmartLib or gateway services. <br>
Mitigation: Use it only when that data sharing is acceptable; avoid confidential or sensitive unpublished drafts unless they are approved for third-party processing. <br>
Risk: Citation checks rely on quota-bearing SmartLib API calls and may be blocked or degraded when quota is low or exhausted. <br>
Mitigation: Confirm the user's email and quota posture before running checks, and disclose that citation verification consumes account quota. <br>
Risk: Generated verification links and gateway notices are third-party content. <br>
Mitigation: Treat external links and notices as untrusted until reviewed, especially before opening links or following account-upgrade guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/j-levee/skills/smartlib-citation-checker) <br>
- [Artifact README](artifact/README.md) <br>
- [Paper draft verification sample report](artifact/examples/citation_check_paper_draft_sample.html) <br>
- [AI hallucination citation-check sample report](artifact/examples/citation_check_ai_hallucination_sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Text, Guidance] <br>
**Output Format:** [HTML report with plain-text corrected citations, difference markers, statistics, quota status, and verification links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include downloadable text exports for all corrected references or individual citations.] <br>

## Skill Version(s): <br>
3.6.3 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
