## Description: <br>
Submit and manage asynchronous batch AI inference jobs via Doubleword API supporting OpenAI-compatible endpoints, tool calling, and structured outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pjb157](https://clawhub.ai/user/pjb157) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create JSONL batch request files, submit them to Doubleword, monitor asynchronous jobs, and retrieve results for large-scale inference workloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch files are uploaded to Doubleword and can contain sensitive prompts, customer data, or regulated information. <br>
Mitigation: Review JSONL contents before upload and avoid secrets or regulated data unless the user has approved handling through Doubleword. <br>
Risk: Large batches may consume Doubleword account credits. <br>
Mitigation: Use the Doubleword Console cost estimator and confirm account credits before submitting large jobs. <br>
Risk: The optional autobatcher dependency changes API call behavior by batching requests. <br>
Mitigation: Verify the autobatcher package and test it in a controlled environment before using it in production workflows. <br>


## Reference(s): <br>
- [Doubleword Batch API Reference](references/api_reference.md) <br>
- [Getting Started with Doubleword Batch API](references/getting_started.md) <br>
- [Doubleword Batch API Pricing](references/pricing.md) <br>
- [Doubleword Console](https://app.doubleword.ai/) <br>
- [autobatcher](https://github.com/doublewordai/autobatcher) <br>
- [ClawHub Skill Page](https://clawhub.ai/pjb157/skills/doubleword) <br>
- [Publisher Profile](https://clawhub.ai/user/pjb157) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python helper code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce JSONL batch request files through the included helper script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
