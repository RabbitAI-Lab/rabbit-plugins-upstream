## Description: <br>
Analyzes cat scratch-post area videos or video URLs through publisher-hosted APIs to identify scratching behavior, estimate frequency, duration, and relative intensity, and return structured observations about stress level and claw health without disease diagnosis or behavior-correction advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to process cat scratch-post footage for structured behavior observations, including scratch frequency, session duration, relative intensity, stress-level signals, claw-health observations, and cloud history lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos, video URLs, and derived analysis results are sent to publisher-operated remote services. <br>
Mitigation: Use only footage appropriate for third-party processing and confirm the publisher's retention and handling practices before use with sensitive home recordings. <br>
Risk: The skill may create or reuse an internal identity, query cloud history, and persist account or token data in the workspace. <br>
Mitigation: Run in an isolated workspace when evaluating the skill, review local workspace data before reuse or sharing, and avoid installation where silent account-linking or token persistence is unacceptable. <br>
Risk: The output includes behavioral and claw-health observations but is not a veterinary diagnosis or behavior-correction plan. <br>
Mitigation: Treat results as observational signals and route health, injury, or abnormal-behavior concerns to qualified professional review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text returned by command-line scripts and remote API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured analysis data, cloud report lists, and report export links.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter says 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
