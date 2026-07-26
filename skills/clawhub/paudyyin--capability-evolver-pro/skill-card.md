## Description: <br>
Capability Evolver Pro analyzes runtime logs to detect error patterns, regressions, and inefficiencies, then generates structured improvement proposals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to analyze agent runtime logs, assess system health, and generate human-reviewed reliability improvement proposals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Runtime logs can contain secrets or sensitive operational details. <br>
Mitigation: Provide scoped or redacted log excerpts and avoid including unnecessary sensitive data. <br>
Risk: Evolution recommendations may be incorrect or incomplete when log data is sparse, noisy, or missing operational context. <br>
Mitigation: Treat recommendations as proposals for human review before changing code, configuration, or deployment behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/capability-evolver-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [Structured JSON objects containing detected patterns, health scores, summaries, recommendations, and evolution proposals.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Actions include analyze, evolve, and status; analyze and evolve use structured log entries with optional strategy or target_file inputs.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
