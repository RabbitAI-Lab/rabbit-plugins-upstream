## Description: <br>
Analyzes aquarium pet image or video files and URLs to produce aquatic pet health findings, possible disease warnings, care suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and aquarium caretakers use this skill to check videos or images of aquatic pets such as goldfish, koi, betta, shrimp, crab, and turtles for health indicators. The output is a health-reference report with observations and care suggestions, not a substitute for professional veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquatic pet media or media URLs are sent to the Lifeemergence analysis service. <br>
Mitigation: Submit only media that is acceptable to transmit to that service, and review the service and skill privacy expectations before use. <br>
Risk: The skill can create or reuse an internal identity and store account tokens locally. <br>
Mitigation: Review the workspace data directory, including the SQLite user database and `smyx-api-key.txt`, before and after use; isolate or clear that data when identity reuse is not desired. <br>
Risk: Historical report access is account-linked cloud data rather than a purely local report list. <br>
Mitigation: Confirm the expected account context before querying history and avoid sharing workspaces across users who should not see the same report history. <br>
Risk: Health findings may be incomplete or incorrect and are not veterinary diagnosis. <br>
Mitigation: Use reports as screening guidance only and consult a qualified aquatic veterinarian for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save output to a user-specified file; results depend on remote analysis service responses.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
