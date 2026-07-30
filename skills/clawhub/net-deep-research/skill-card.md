## Description: <br>
Net Deep Research performs current, multi-source public-web research with source reputation scoring, URL safety checks, evidence synthesis, and structured feedback to a remote backend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[h4444433333](https://clawhub.ai/user/h4444433333) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill for current public-web research, product or policy verification, implementation comparisons, and source-backed summaries. It is best suited to non-confidential questions where public evidence and visible uncertainty are more important than offline-only handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Online runs send research prompts, generated answers, cited-source details, and feedback signals to a third-party backend without a per-run consent control. <br>
Mitigation: Use the skill only for non-confidential public-web research unless the publisher provides clear consent, redaction, retention, and deletion controls. <br>
Risk: Generated research answers can still be incomplete, outdated, or misleading despite source scoring and cross-checking. <br>
Mitigation: Review the cited sources, uncertainty notes, and cross-source discussion before relying on the answer, especially for high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/h4444433333/skills/net-deep-research) <br>
- [Remote backend service](https://www.shoggoth.vip) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, API Calls, JSON] <br>
**Output Format:** [Markdown research answer with source notes, uncertainty sections, and internal structured JSON feedback.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Online runs may transmit research queries, cited source metadata, answer text, and feedback signals to https://www.shoggoth.vip.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
