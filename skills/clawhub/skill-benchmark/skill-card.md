## Description: <br>
Benchmark ClawHub skills for performance, correctness, and documentation quality. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Skill authors, reviewers, and ClawHub users use this skill to score skill folders, inspect sub-scores and issues, and produce A-F quality grades with optional JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional CI verifier can execute repository test code while checking a product folder. <br>
Mitigation: Run ci/verify_product.py only on repositories whose tests you are willing to execute; use the benchmark itself on ordinary local skill folders for normal review. <br>
Risk: The README includes an unpinned curl command for fetching the tool script. <br>
Mitigation: Prefer the reviewed package copy when supply-chain reproducibility matters. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itspremkumar/skills/skill-benchmark) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [CLI text or JSON score output with markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.8+ and runs offline using the Python standard library.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
