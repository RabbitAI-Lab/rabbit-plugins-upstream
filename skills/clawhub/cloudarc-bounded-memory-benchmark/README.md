# CloudArc Bounded-Memory Benchmark

A repeatable workflow skill for validating **bounded-memory streaming pack/unpack**,
**high-cardinality multi-file `.vibo` packages**, **deduplication**, **remote-search
range telemetry**, and **CI/manual benchmark gates** in CloudArc.

Use it when changing benchmarks, SLOs, manifest/index cardinality, remote metadata
reads, GitHub Actions checks, or when reviewing a large-package MVP before cloud
provider integration.

**Five entry points:** `doctor` (environment + repository readiness, no checkout
required), `selfcheck` (2 MiB pack/unpack with real RSS - the fastest proof),
`badge` (flat SVG SLO badge from a result artifact), `smoke` (tests + small
profiles), `manual` (1/5/10 GiB behind `--yes`).

> **Honest status:** the limits below are the **CloudArc SLO contract** (documented
> target values), not measurements produced by this package on this machine.
> Reproduce real numbers by running `smoke` / `manual` inside a CloudArc checkout
> (`benchmarks/large_package.py` must be present). Until then, treat the table as
> the contract the workflow enforces, not as a measured result.

## What it protects

| Limit | Value |
|---|---|
| Peak RSS (pack & unpack) | <= 256 MiB |
| 1/5/10 GiB peak-RSS spread | <= 64 MiB |
| Pack staging | <= 2.10 * payload + 64 MiB |
| Unpack staging | <= 1.10 * payload + 64 MiB |

The data section is never read by remote metadata or search operations. Provider
errors stay visible; only a missing capability may trigger the validated sidecar
fallback. The portable reference backend stays authoritative and the native
semantic backend remains optional.

## Bundled helper

Three safe entry points, no shell-specific glue:

    python -B scripts/cloudarc_benchmark.py smoke --repo .
    python -B scripts/cloudarc_benchmark.py manual --repo . --yes
    python -B scripts/cloudarc_benchmark.py check-telemetry --input remote-response.json --expected range

`manual` requires `--yes` because it can consume hours and tens of GiB of temporary
disk. `check-telemetry` accepts a response object containing `telemetry` or a
telemetry object directly, and returns non-zero on invariant violations.

Both benchmark commands verify that the JSON artifact reports a passing evaluation,
that multi-file manifest/index counts match the requested file count, and that the
paired Markdown report exists and contains `PASS`.

## Install

- Clone this repository into your agent's skills directory, or
- Install from the ClawHub registry by slug `cloudarc-bounded-memory-benchmark`.

The skill runs entirely locally. It requires no cloud credentials and does not
enable any cloud provider or native backend.

## Contents

    SKILL.md                            workflow instructions
    VERSION                             package version
    agents/skywork.yaml                 registry interface metadata
    references/contract.md              detailed SLO, telemetry, resume, CI contracts
    references/release-notes.md         upgrade notes
    scripts/cloudarc_benchmark.py       safe benchmark/telemetry helper
