## Description: <br>
Automatically retries HTTP requests with exponential backoff, timeout control, and connection pooling to handle network errors and rate limits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[2233admin](https://clawhub.ai/user/2233admin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill when they need an agent to propose JavaScript HTTP request code that retries transient failures, rate limits, and timeouts with exponential backoff and connection reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Retry logic can duplicate state-changing actions or contribute to retry storms when copied into production code without guardrails. <br>
Mitigation: Default retries to idempotent requests, use idempotency keys for operations that change data, respect service retry guidance such as Retry-After, and cap retry attempts and delays. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, guidance] <br>
**Output Format:** [Markdown with JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes trigger terms for HTTP timeout, connection reset, connection refusal, rate-limit, retry, HTTP error, and network timeout scenarios.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
