## Description: <br>
Prove your AI agents actually did the work - catch fake-success, dry-run theater, and stub code before it ships. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therealmacsteel](https://clawhub.ai/user/therealmacsteel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use ProofKit to scan files for fake-success patterns and to guide proof-of-work review before trusting an agent's reported result. It is suited for AI-generated code, autonomous agent workflows, and multi-agent fleets where a false success can corrupt downstream decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A clean static scan can be mistaken for proof that code executed successfully. <br>
Mitigation: Require a live artifact such as real output, a non-zero message id, a created file with bytes, an HTTP 200 response, or a changed database row before marking work verified. <br>
Risk: Heuristic scanner results can include false positives or miss behavior outside its pattern list. <br>
Mitigation: Treat scanner output as a review aid and pair it with manual review, targeted tests, and the live-artifact verification method. <br>
Risk: The listing describes premium capabilities that are not included in the free artifact. <br>
Mitigation: Evaluate this release by the included free scanner and documented method unless separate premium artifacts are provided. <br>


## Reference(s): <br>
- [ProofKit ClawHub listing](https://clawhub.ai/therealmacsteel/skills/proofkit) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Artifact listing](artifact/CLAWHUB_LISTING.md) <br>
- [Static scanner script](artifact/verify_real_scan.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and scanner text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; reads user-specified local files and reports heuristic static findings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
