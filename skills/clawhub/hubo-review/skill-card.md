## Description: <br>
Reviews without editing, then has a critic challenge every finding and missed risk until the review is reconciled. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[h0ngcha0](https://clawhub.ai/user/h0ngcha0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical reviewers use this skill to perform read-only reviews of code, diffs, pull requests, tests, designs, or technical claims. It coordinates a reviewer and critic so each finding is challenged and reconciled before the final review is returned. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may spawn and reuse two review-related agent sessions when explicitly invoked. <br>
Mitigation: Invoke it intentionally for a review target and keep the reviewer and critic lineages read-only. <br>
Risk: The host may be unable to mechanically verify the read-only boundary for the specified target. <br>
Mitigation: Compare before-and-after evidence around role turns when possible and report when the boundary cannot be verified. <br>
Risk: Review findings can be incorrect, overstated, duplicated, or incomplete. <br>
Mitigation: Use the critic loop to challenge correctness, severity, scope, required outcomes, duplicates, false positives, and omissions before returning the final canonical review. <br>


## Reference(s): <br>
- [Hubo Review Skill Page](https://clawhub.ai/h0ngcha0/skills/hubo-review) <br>
- [Karpathy-inspired discipline](https://github.com/multica-ai/andrej-karpathy-skills) <br>
- [Ponytail](https://github.com/DietrichGebert/ponytail) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown review report and chronological reviewer/critic exchange transcript] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns findings in the conversation and does not write the review to a file.] <br>

## Skill Version(s): <br>
0.4.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
