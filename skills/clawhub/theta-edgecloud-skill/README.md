# Theta EdgeCloud skill

Release: **0.1.28**. Security review: 2026-09-13.
See [security scope](references/security.md) for controls and residual risks.

Read [SKILL.md](SKILL.md) for the operating procedure and
[capabilities](references/capabilities.md) for supported commands, credentials,
current API gaps and primary sources.

## Validate

```bash
npm ci --ignore-scripts
npm run check
npm test
```

The package includes source, generated runtime, tests and references. Four former
placeholder tests now exercise real contracts/safety gates. Offline mocked tests
are not a substitute for live provider proof.

## Invoke

```js
import { executeThetaRuntimeCommand, listThetaRuntimeCommands } from './dist/index.js';
console.log(listThetaRuntimeCommands());
const result = await executeThetaRuntimeCommand(
  {command:'list_services'}, {env:process.env}
);
```

Supply credentials through protected environment or on-demand `ctx.getSecret`;
never paste keys into commands or chat. Discovery is read-only. Set
`THETA_DRY_RUN=1` before rehearsing mutations; GET requests can still run.

## Improvements

- GLM-5.3/Flash direct chat, structured tools, streaming parallel arguments and
  correlated tool-result continuation; reasoning retained separately.
- Discovery includes full prediction/input schemas and current GLM/image catalog entries.
- Training/custom templates and stopped GPU restart by base ID.
- Existing video/stream/ingestor operations exposed through runtime dispatch.
- Twelve game-key AI Characters/session API adapters with dry-run and contract tests.
- HTTPS origin allowlists, redirect refusal, path encoding, full secret redaction,
  no automatic mutation/inference retries, and fail-closed cleanup verification.
- Obsolete wallet/RPC modules and unsafe setup/live-smoke scripts are not shipped.

Installing this package does not change Gateway or model configuration.
GPU provisioning, live Video/Characters tests and expanded controller logs/usage APIs
remain subject to the credentials, API contracts and authority described in the skill.

Credit: [Theta Communications](https://www.thetacommunications.com).
Support: https://www.thetacommunications.com/donations
