## Description: <br>
Analyzes pet video or image inputs through server-side APIs to produce a Pet Safety Guardian health report and, when requested, retrieve cloud report history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit cat, dog, bird, or other pet media for health-oriented analysis, receive structured findings and care suggestions, and list prior cloud reports. Results are health references and are not a substitute for professional veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos, images, or media URLs are sent to lifeemergence.com services for analysis. <br>
Mitigation: Use only when the user is comfortable sharing the media with that service, and avoid submitting sensitive or unrelated files. <br>
Risk: The skill automatically creates or reuses local identity records and stores service tokens in the workspace data directory. <br>
Mitigation: Use a private workspace for sensitive reports, review local workspace data handling, and clear stored state before sharing the workspace. <br>
Risk: Cloud report history retrieval may expose prior pet health reports associated with the local identity. <br>
Mitigation: Confirm the user intends to view report history and avoid running history queries in shared or untrusted sessions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown or JSON health analysis report, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links, status messages, care suggestions, and cloud history tables.] <br>

## Skill Version(s): <br>
999.999.1001 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
