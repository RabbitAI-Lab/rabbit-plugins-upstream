## Description:

Enforces fresh verification evidence before any completion claim, especially before claiming tests pass, a bug is fixed, work is done, a branch is ready to merge, or scope is clear enough to edit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill before claiming work complete, committing, pushing, opening a PR, or handing off work. It guides them to identify claim-matched verification, run fresh proof, read the full result, and report only outcomes supported by evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause agents to spend additional time running and reading verification commands before reporting completion.

Mitigation: Apply it where stricter engineering handoff discipline is desired and report any skipped or failed checks concisely.

Risk: Verification commands may operate on repositories or environments outside the user's intended scope if the agent does not constrain them.

Mitigation: Keep verification limited to repositories and environments the user has authorized, and resolve materially ambiguous scope before editing or running broad checks.

## Reference(s):

- [Change Strategies](references/change-strategies.md)
- [Claims and Failures](references/claims-and-failures.md)
- [Isolated Verification](references/isolated-verification.md)
- [Proof Integrity](references/proof-integrity.md)
- [Scope and Sweeps](references/scope-and-sweeps.md)
- [System-Wide Test Check](references/system-wide-test-check.md)
- [Verification Oracles](references/verification-oracles.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell commands and concise completion reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Markdown-only discipline skill; no API calls, credentials, or generated files are required by the skill itself.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
