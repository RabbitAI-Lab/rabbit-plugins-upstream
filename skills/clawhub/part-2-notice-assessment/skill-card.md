## Description: <br>
Assesses a publicly posted Part 2 patient notice for SUD treatment programs against 42 CFR §2.22(b) and reports face-of-document content gaps with citations and quoted notice language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dangsllc](https://clawhub.ai/user/dangsllc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Healthcare compliance practitioners, auditors, and developers use this skill to review a SUD program's posted Part 2 patient notice against the required §2.22 content elements. It produces document-review findings only and does not assess the organization's actual privacy practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat notice-content findings as legal conclusions about a program's real-world privacy practices. <br>
Mitigation: Use the output as a public-document review aid and have qualified legal or compliance reviewers decide operational significance and remediation. <br>
Risk: Untrusted or incomplete notice text could lead to inaccurate absent or insufficient-information findings. <br>
Mitigation: Prefer pasted notice text or trusted public http/https URLs, and verify that retrieved text is complete before relying on final findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dangsllc/skills/part-2-notice-assessment) <br>
- [Rote Compliance Skills](https://github.com/Rote-Compliance/rote-compliance-skills) <br>
- [Rote Compliance](https://rotecompliance.com) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON coverage map or Markdown summary with cited notice excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include shell commands for fetching public notice text; findings are limited to public notice content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
