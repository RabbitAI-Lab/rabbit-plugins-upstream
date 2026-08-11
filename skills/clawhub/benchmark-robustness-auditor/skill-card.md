## Description:

Red-team auditor for LLM benchmarks that produces robustness reports with severity scoring, contamination checks, evaluator-injection tests, proof-of-concept exploit descriptions, mitigations, and detection tests for defensive research use.

This skill is for research and development only.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, benchmark maintainers, and evaluation teams use this skill to audit benchmarks they own or are authorized to test, identify contamination and leaderboard-gaming risks, and produce a robustness report with mitigations and CI detection tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The submitted artifact documents executable audit scripts that are not present in the artifact bundle.

Mitigation: Inspect the installed package before running commands and confirm referenced scripts, paths, and exit codes match the documentation.

Risk: Proof-of-concept exploit workflows can affect benchmark harnesses or generate misleading conclusions if used outside an authorized audit.

Mitigation: Run the skill only on benchmarks you own or are authorized to test, preferably in an isolated environment with reviewed inputs and outputs.

Risk: Optional GitHub-token and external helper-script workflows can expose credentials or run unreviewed local code.

Mitigation: Use least-privilege tokens, avoid logging secrets, and review any external self-heal or cache scripts before sourcing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/benchmark-robustness-auditor)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with JSON severity outputs and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proof-of-concept prompts, mitigation recommendations, and detection-test guidance for authorized benchmark audits.]

## Skill Version(s):

1.1.6 (source: server release metadata; artifact frontmatter reports 1.2.0 and artifact _meta.json reports 1.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
