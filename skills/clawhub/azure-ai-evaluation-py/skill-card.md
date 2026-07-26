## Description: <br>
Azure AI Evaluation SDK for Python helps evaluate generative AI applications with quality, safety, and custom evaluators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to configure and run Azure AI Evaluation workflows for generative AI quality, safety, retrieval, and custom evaluation scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Evaluation content and results may be processed or stored by Azure services when users run AI-assisted evaluators, safety evaluators, prompt-based evaluators, or Foundry logging. <br>
Mitigation: Review and redact datasets before evaluation, use least-privilege Azure credentials, and confirm Azure service data-handling requirements for the target environment. <br>
Risk: The batch CLI depends on Azure credentials and environment variables, so careless setup can expose secrets or run against the wrong Azure resource. <br>
Mitigation: Use a virtual environment, keep secrets in environment variables or a secret manager, avoid committing credentials, and verify endpoint, deployment, and project settings before running. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thegovind/skills/azure-ai-evaluation-py) <br>
- [Built-in Evaluators Reference](references/built-in-evaluators.md) <br>
- [Custom Evaluators Reference](references/custom-evaluators.md) <br>
- [Batch Evaluation CLI](scripts/run_batch_evaluation.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Python and bash code blocks; optional JSON result files when the batch script is run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The batch script reads JSONL datasets, prints evaluation metrics, and can write JSON results including metrics, rows, and a Foundry URL.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
