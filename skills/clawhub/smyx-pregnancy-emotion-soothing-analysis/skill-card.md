## Description: <br>
Analyzes pregnancy-related camera/video inputs and optional microphone audio for emotion-related behavior signals, returns structured reports and report links, and can support soothing actions or caregiver alerts through LifeEmergence services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and care teams can use this skill to analyze consented home or clinic waiting-room media for pregnancy emotion fluctuation signals, receive structured event summaries, query cloud history, and coordinate non-diagnostic soothing or escalation recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes highly sensitive pregnancy-related home or clinic audio/video, including possible bystander data. <br>
Mitigation: Use only with explicit consent from the monitored person, clear notice to bystanders, and a practical opt-out path for clinic or waiting-room deployments. <br>
Risk: Files or URLs may be submitted to external LifeEmergence services and cloud history may be retrieved. <br>
Mitigation: Confirm cloud processing is acceptable before use, avoid submitting unnecessary media, and restrict access to generated history and report links. <br>
Risk: The skill silently creates or reuses a local/remote identity and stores tokens in a workspace SQLite database. <br>
Mitigation: Run only in an approved workspace, protect local data files and databases, and rotate or remove stored tokens when the deployment ends. <br>
Risk: Outputs concern emotional state and pregnancy-related wellbeing but are not medical diagnoses. <br>
Mitigation: Present outputs as behavior observations and support recommendations, and escalate repeated or urgent concerns to qualified prenatal care or mental-health resources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis) <br>
- [Pregnancy emotion soothing API reference](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Structured JSON or Markdown text with analysis summaries, history lists, recommendations, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write analysis output to a requested file and may include cloud report export URLs.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
