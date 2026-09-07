## Description:

yotta-secret is a local, zero-dependency secret and credential leak scanner that checks source code, configuration, .env files, and git history for suspected API keys, private keys, credential assignments, URL-embedded credentials, and high-entropy tokens, with text, JSON, or CSV output masked by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent operators use this skill to scan authorized local repositories, configuration files, text input, or git history for suspected hardcoded secrets before committing, releasing, or sharing material. Results support human triage and remediation decisions such as rotation, removal from source, and follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive source files, configuration, logs, or git history.

Mitigation: Run it only on authorized, owned, or educational assets and define the scan scope before execution.

Risk: Scanner findings are suspected secrets and can include false positives or context-dependent results.

Mitigation: Require human verification before rotating, revoking, escalating, or treating a finding as confirmed exposure.

Risk: Displaying raw secrets can create secondary exposure.

Mitigation: Keep the default masked output unless raw values are specifically needed in a controlled environment.

Risk: Broad or global installation can place the skill in an unintended agent environment.

Mitigation: Install only into the intended agent skill directory, prefer explicit --agent or --dir installation, and pin the npm version when reproducible supply-chain provenance matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-secret)
- [Rule catalog and matching behavior](references/rules.md)
- [Entropy and verification specification](references/entropy-and-verification.md)
- [Integration guidance](references/integration.md)

## Skill Output:

**Output Type(s):** [text, JSON, CSV, shell commands, guidance]

**Output Format:** [Text, JSON, or CSV scanner results, often accompanied by Markdown guidance and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Secrets are masked by default; explicit raw-secret display is available only when requested.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
