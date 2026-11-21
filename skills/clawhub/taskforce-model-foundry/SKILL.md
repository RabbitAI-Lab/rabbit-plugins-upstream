---
name: taskforce-model-foundry
description: Train, evaluate, resume, and export local models with Taskforce Model Foundry. Use for tmf CLI jobs, HF/PEFT fine-tuning, independent quality gates, and OpenClaw or Hermes model-customization workflows.
license: MIT
---

# Taskforce Model Foundry

1. Establish the job contract: dataset provenance, allowed compute host, backend,
   model path, resource/time budget, independent holdout, and quality thresholds.
   Default to synthetic data and local CPU. Obtain task-specific authorization
   before private data, paid compute, remote transfers, production changes, or
   publishing. Finish with a recorded scope and success criteria.

2. Locate a trusted installation using [the command reference](references/commands.md).
   Run version, doctor, and backends checks. Doctor can return success while a
   missing config is only a warning: validate the actual config separately.
   Finish with the executable, version, usable backend, and validated config known.

3. Prepare an isolated project directory. Use `init` only for a new synthetic
   project; for an existing project inspect its configuration before changing it.
   Keep data outside this skill directory. For HF/PEFT select an existing local
   model and a dedicated Python environment; inspect `docs/tutorial.md` in the
   installation for current config fields. Do not invent model download or GPU
   setup commands. Finish with licensed/provenanced data and disjoint splits.

4. Fix the evaluation policy before training. `eval.gates` replaces the default
   list in full; validate it, and preserve the approved thresholds. A tiny fixture
   with fixture-specific gates validates plumbing, not business quality. Finish
   with a recorded baseline, holdout policy, and explicit gate list or defaults.

5. Assign a stable job ID, inspect durable status, then train. After a timeout or
   disconnected session, query the execution host's durable state before retrying;
   resume the same job rather than submitting a duplicate. Cancellation uses
   SIGINT/SIGTERM and exit 130; resume an intentionally cancelled job only when
   authorized to continue. Finish with durable succeeded, cancelled, or failed
   state and the actual process exit code, not just a launched-process receipt.

6. Evaluate baseline and tuned model on the independent holdout. Check leakage,
   sample counts, actual parameter changes, and each declared gate. Treat failed
   evaluation as a failed deliverable; diagnose it instead of weakening gates
   after seeing results. Finish with the report path, metrics, and gate verdict.

7. Export only a passing job, preferably pinning its reviewed evaluation report.
   Verify `checksums.txt` from the bundle directory. HF/PEFT exports include adapter
   bytes but reference the local base model: record its identity and availability.
   Finish with bundle path, digest, lineage, checksum results, and base dependency.

8. Report measured results separately from unsupported or unverified capabilities.
   Read [capability and host boundaries](references/boundaries.md) before making
   GPU, remote execution, recovery, or production claims. Include test pass/fail/
   skip counts; a skipped test is not a pass. Publishing requires its own actual
   registry/release and installation verification. Finish with evidence paths,
   remaining limits, and whether the artifact is local, published, or deployed.
