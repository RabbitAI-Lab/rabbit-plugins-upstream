## Description: <br>
WaitSpin helps agents guide sponsored developer wait-state ad workflows, including campaign creation, email OTP onboarding, earning-surface installation, wallet checks, and public API or trust-boundary questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nttylock](https://clawhub.ai/user/nttylock) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, advertisers, and publishers use WaitSpin to manage wait-state ad campaigns, onboard with email OTP credentials, install supported earning surfaces in developer tools, inspect market and wallet status, and consult public API, privacy, and trust-boundary guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys or OTP codes could be exposed in logs, shell history, screenshots, source files, or chat output. <br>
Mitigation: Keep credentials secret, use the host secret store or tool-scoped environment variables, and do not echo API keys or OTP codes back to the user. <br>
Risk: User-provided emails, OTP codes, URLs, campaign IDs, or ad text could be unsafe if interpolated into shell commands. <br>
Mitigation: Validate inputs before use and pass values through structured argv or tool-scoped environment variables rather than raw shell interpolation. <br>
Risk: Using broad control credentials for installed earning surfaces could exceed the privilege needed for publisher workflows. <br>
Mitigation: Use control keys for advertiser and payout actions, and publisher-extension keys for installs, serve polling, impressions, wallet status, and ledger reads. <br>
Risk: Installing earning surfaces changes visible status or hook behavior in selected developer tools. <br>
Mitigation: Run dry-run and status commands first, install only requested targets, and preserve existing local configuration when the CLI supports compose-existing behavior. <br>
Risk: Payout or account-credit behavior may be mistaken for live production capability when only test-mode evidence is available. <br>
Mitigation: Treat payout dry-runs and confirm-test-transfer flows as readiness or test-mode only unless fresh operator proof confirms live payouts. <br>


## Reference(s): <br>
- [WaitSpin Public Site](https://waitspin.com) <br>
- [WaitSpin API Docs](https://waitspin.com/docs) <br>
- [WaitSpin Agent Contract](https://waitspin.com/.well-known/agents.md) <br>
- [WaitSpin Trust Boundary](https://waitspin.com/waitspin/trust) <br>
- [WaitSpin Public Client Source](https://github.com/citedy/waitspin) <br>
- [WaitSpin OpenAPI Document](https://waitspin.com/openapi/waitspin-api.openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-oriented CLI/API instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend JSON-mode CLI output; API keys and OTP codes must remain secret.] <br>

## Skill Version(s): <br>
0.1.19 (source: server release evidence; SKILL.md states v0.1.19) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
