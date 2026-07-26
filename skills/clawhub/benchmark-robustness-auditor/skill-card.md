## Description: <br>
Red-team auditor for LLM benchmarks that detects contamination, exploit patterns, and evaluation fragility and produces robustness reports with severity scores, proof-of-concept exploits, and mitigations. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, benchmark authors, and evaluation teams use this skill to audit LLM benchmarks and eval pipelines they are authorized to test. It helps identify contamination, scoring artifacts, judge injection, benchmark-specific fine-tuning, and related robustness risks before relying on leaderboard results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate or discuss adversarial benchmark prompts and proof-of-concept exploits. <br>
Mitigation: Use it only for defensive audits of benchmarks or eval pipelines you are authorized to test, and do not use the outputs to inflate public leaderboard scores. <br>
Risk: Generated audit reports may include incorrect or misleading robustness judgments if the benchmark, corpus, model endpoint, or scorer is misconfigured. <br>
Mitigation: Review findings before acting on them, reproduce high-severity results, and validate proposed mitigations against the target evaluation pipeline. <br>
Risk: Local reports and exploit artifacts may contain sensitive benchmark details, canary strings, or model-evaluation data. <br>
Mitigation: Store generated reports in approved locations, restrict sharing to the audit team, and remove sensitive test items before publishing summaries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/benchmark-robustness-auditor) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Moltchurch Tenets](https://molt.church) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report with inline shell commands, JSON/CSV report artifacts, and proof-of-concept code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include severity scores, estimated score-inflation deltas, exploit proof-of-concepts, detection tests, and mitigations.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence; skill frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
