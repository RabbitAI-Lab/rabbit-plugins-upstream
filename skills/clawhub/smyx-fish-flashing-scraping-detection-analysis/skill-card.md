## Description: <br>
Analyzes fixed aquarium camera video to detect fish flashing and scraping behavior, count abnormal friction events, and produce ectoparasite risk warnings without diagnosing a specific disease. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze aquarium, quarantine tank, or aquaculture video for flashing and scraping events, warning levels, and structured follow-up guidance. It is intended for behavior-based risk screening and report retrieval, not veterinary diagnosis or treatment selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends aquarium videos or camera URLs to a cloud service and can query cloud report history. <br>
Mitigation: Use only media and URLs that are acceptable for cloud processing, and review cloud upload, retention, and account-linking expectations before installation. <br>
Risk: The skill silently creates or reuses local identity state and stores authentication tokens in workspace data. <br>
Mitigation: Install and run it only in workspaces where local identity and token storage are acceptable, and review stored workspace data as part of operational controls. <br>
Risk: Behavioral signals can be mistaken for parasitic disease or treatment advice. <br>
Mitigation: Treat outputs as behavior-based risk warnings only; require close observation and professional veterinary microscopy for diagnosis and treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON structured reports with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save analysis output to a file and can return cloud report history when requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
