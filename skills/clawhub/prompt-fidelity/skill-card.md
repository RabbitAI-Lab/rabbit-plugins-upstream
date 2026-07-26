## Description: <br>
Self-checks how much of a request is verifiable vs guesswork before answering it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[barneyjm](https://clawhub.ai/user/barneyjm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to separate mechanically verified criteria from subjective judgment in search, filtering, recommendation, and data-retrieval answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may add counting, checking, or reporting steps to retrieval and recommendation tasks. <br>
Mitigation: Use cheap system-returned counts, planner statistics, samples, or small local checks before considering exact counts, and avoid unbounded scans on large shared systems. <br>
Risk: The submitted artifact references a helper script that is not included. <br>
Mitigation: Treat the script-based computation path as unavailable unless the helper is supplied in the runtime environment; otherwise compute and report the fidelity breakdown manually. <br>
Risk: Subjective criteria or noisy proxies can be overstated as verified. <br>
Mitigation: Classify uncertain criteria as inferred, split rough proxies into verified query terms plus remaining semantic judgment, and disclose the distinction in the answer. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/barneyjm/skills/prompt-fidelity) <br>
- [Server-Resolved GitHub Provenance](https://github.com/Barneyjm/prompt-fidelity/tree/main/skills/prompt-fidelity) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with optional JSON constraint data and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports which answer constraints are verified, inferred, or injected, and may include a fidelity score.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
