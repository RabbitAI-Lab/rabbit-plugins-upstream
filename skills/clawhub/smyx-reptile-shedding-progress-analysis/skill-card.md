## Description: <br>
Analyzes reptile enclosure images or video to classify shedding phase, identify stuck-shed risk signals, and produce care-oriented analysis reports and history views. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External keepers, breeders, and developers use this skill to analyze reptile enclosure media for shedding progress, stuck-shed warning signs, and care recommendations. It can also retrieve cloud-hosted historical shedding reports associated with the local skill identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reptile enclosure images or video may be sent to the publisher's remote services for analysis and history retrieval. <br>
Mitigation: Use only media appropriate for third-party processing, avoid private enclosure footage unless remote retention and deletion controls are acceptable, and restrict network URL inputs to trusted sources. <br>
Risk: The skill may create or reuse a local identity and store service tokens in the workspace data area. <br>
Mitigation: Run it in an isolated workspace, review and remove local identity or token files when no longer needed, and avoid sharing the workspace with users who should not access the reports. <br>
Risk: Visual shedding analysis can be wrong or incomplete, especially for poor angles, low resolution, abnormal lighting, injury, brumation, or species-specific shedding differences. <br>
Mitigation: Treat outputs as decision support, follow the skill's unreliable-signal handling, avoid invasive or medication guidance, and consult a reptile veterinarian for persistent or high-risk stuck-shed cases. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-like structured text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write an optional output file when requested; history listing is returned from the publisher's remote service.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
