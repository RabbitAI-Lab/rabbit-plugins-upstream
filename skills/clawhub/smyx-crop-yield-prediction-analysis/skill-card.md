## Description: <br>
Predicts expected yield of economic crops such as tomato, corn and potato by combining growth stage, nutrition status, environmental data and historical yield references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to estimate expected yield ranges, confidence, and yield factors for crops such as tomato, corn, potato, and peanut from field or plant images/videos plus optional environmental and historical yield context. It also supports querying prior yield-prediction reports for the current internally managed identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crop images, videos, URLs, and related context are sent to a cloud service for analysis. <br>
Mitigation: Use only media and business context that are acceptable to share with the service, and require publisher documentation for retention and handling before using sensitive farm, business, or personal data. <br>
Risk: The skill can create or reuse an internally managed identity and associate history with that identity. <br>
Mitigation: Review identity creation, account reuse, report access, and deletion controls before deployment, especially in shared workspaces. <br>
Risk: Service tokens may be stored locally after remote registration or login. <br>
Mitigation: Run the skill in an isolated workspace when evaluating it and define a process for locating, rotating, and deleting locally stored tokens. <br>
Risk: Yield predictions can be wrong because image/video evidence may cover only part of a field and actual yield depends on factors outside the media. <br>
Mitigation: Treat results as planning guidance and verify final yield accounting or insurance adjustment with field measurements and business rules. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown analysis reports and JSON-style structured results; historical report queries are formatted as Markdown tables.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can optionally write results to a user-specified output file; predictions are for business reference and should be checked against field measurements for final yield accounting or insurance adjustment.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; artifact frontmatter says 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
