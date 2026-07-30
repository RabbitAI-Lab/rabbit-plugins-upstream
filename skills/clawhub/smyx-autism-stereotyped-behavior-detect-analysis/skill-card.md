## Description: <br>
Analyzes fixed-camera child behavior videos to identify repetitive stereotyped behaviors such as spinning, hand flapping, and body rocking, then returns structured behavior statistics and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Therapists, parents, rehabilitation teams, and developers use this skill to submit clear fixed-camera child behavior videos or video URLs and receive objective event-level statistics, summaries, and report links for professional review. It is descriptive support for behavior tracking, not a diagnostic tool or rehabilitation prescription. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child-behavior videos and reports may be uploaded to or retrieved from a remote service. <br>
Mitigation: Use only with explicit guardian consent, a trusted backend, defined retention policies, and account isolation; avoid unnecessary uploads and prefer privacy-preserving inputs where available. <br>
Risk: The skill can silently create or reuse an internal identity and query cloud history for reports tied to that identity. <br>
Mitigation: Run it in an isolated workspace and account context, restrict access to history-list workflows, and review or clear local identity files before sharing the workspace. <br>
Risk: Service tokens may be stored in a local workspace database. <br>
Mitigation: Protect the workspace data directory, do not publish workspace archives containing runtime data, and rotate or revoke tokens after testing or transfer. <br>
Risk: Visual behavior classification can misidentify everyday activity as stereotyped behavior and is not a diagnosis. <br>
Mitigation: Require professional review of sampled outputs and do not use reports as the sole basis for diagnosis, treatment, or rehabilitation planning. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage introduction](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-formatted structured report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include behavior event statistics, summary metrics, history-list output, report export links, and optional saved output files.] <br>

## Skill Version(s): <br>
1.0.6 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
