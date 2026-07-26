## Description: <br>
Adversarial implementation review based on Block's g3 dialectical autocoding research, used to validate implementation completeness against requirements with fresh objectivity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killerapp](https://clawhub.ai/user/killerapp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering reviewers use this skill to compare an implementation against stated requirements, identify missing functionality or security gaps, and decide whether the work is ready to approve. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The review can give misleading confidence if requirements, build status, tests, or runtime behavior are not actually checked. <br>
Mitigation: Use a clear requirements file or issue reference when possible, and verify compilation, tests, and important flows before accepting IMPLEMENTATION_APPROVED. <br>
Risk: Suggested build, test, or run commands may execute untrusted project code during review. <br>
Mitigation: Treat commands proposed in untrusted repositories as normal code-execution risk and approve or sandbox them deliberately. <br>


## Reference(s): <br>
- [Adversarial Cooperation in Code Synthesis](https://block.xyz/documents/adversarial-cooperation-in-code-synthesis.pdf) <br>
- [g3 research implementation](https://github.com/dhanji/g3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown review verdict with concise bullets and optional file or line references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include IMPLEMENTATION_APPROVED as a termination signal, or a requirements compliance summary with immediate actions.] <br>

## Skill Version(s): <br>
0.9.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
