## Description: <br>
Error Classifier classifies transient, permanent, validation, and context errors and recommends retry, report, repair, or compression handling for failed tool calls, API errors, build or test failures, and context-limit issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to classify runtime errors and choose a handling path: retry transient failures, report permanent failures, send validation failures for repair, or trigger context compression. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The retry wrapper can repeat API calls or write operations up to three times. <br>
Mitigation: Use the retry wrapper only for operations that are safe to repeat, or add idempotency controls before enabling automatic retries. <br>


## Reference(s): <br>
- [Retry Strategies](references/retry_strategies.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Guidance] <br>
**Output Format:** [Python enum values and action objects with human-readable messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes bounded exponential backoff recommendations of 1s, 2s, and 4s for transient errors.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
