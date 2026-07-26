## Description: <br>
Provides supportive mental health responses and mental health knowledge Q&A, with task selection for counseling or education modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integrators use this skill to pass a mental health question from CLI arguments, JSON/JSONL files, or stdin to a configured medical LLM for supportive counseling or educational Q&A. Outputs are model-assisted information and should not be treated as clinical decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mental health questions may be sent to the configured LLM API. <br>
Mitigation: Use only data approved for that API, avoid identifiable patient or crisis information unless allowed by the operator's process, and communicate this data flow to users. <br>
Risk: Model answers could be mistaken for diagnosis or emergency mental health support. <br>
Mitigation: Treat outputs as model-assisted information, keep professional review in the workflow, and direct crisis situations to appropriate professional or emergency help. <br>
Risk: Untrusted API URLs or output paths could expose sensitive prompts or responses. <br>
Mitigation: Restrict --api-url and --output to trusted destinations and review configuration before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-mental-health) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration] <br>
**Output Format:** [JSON response by default, optional plain text answer with --text-only, and NDJSON for batch input.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires task selection and an appkey unless running --dry-run; can write full results to an output path.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
